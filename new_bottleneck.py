import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange, reduce

# ============================================================================
# ECA Attention Module (Efficient Channel Attention)
# ============================================================================
class ECA(nn.Module):
    """ECA attention mechanism"""
    def __init__(self, channels, gamma=2, b=1):
        super().__init__()
        t = int(abs((np.log2(channels) + b) / gamma))
        k_size = t if t % 2 else t + 1
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # Global average pooling: [B, C, H, W] -> [B, C, 1, 1]
        y = self.avg_pool(x)
        # Squeeze and transpose: [B, C, 1, 1] -> [B, 1, C]
        y = y.squeeze(-1).transpose(-1, -2)
        # 1D convolution
        y = self.conv(y)
        # Transpose back: [B, 1, C] -> [B, C, 1, 1]
        y = y.transpose(-1, -2).unsqueeze(-1)
        # Multiply with input
        return x * self.sigmoid(y)


# ============================================================================
# SE Attention Module (Squeeze-and-Excitation)
# ============================================================================
class SE(nn.Module):
    """SE attention mechanism"""
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channels, channels // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channels // reduction, channels, bias=False),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        b, c, _, _ = x.size()
        # Squeeze
        y = self.avg_pool(x).view(b, c)
        # Excitation
        y = self.fc(y).view(b, c, 1, 1)
        # Scale
        return x * y.expand_as(x)


# ============================================================================
# ASPP-lite Module (Branch B in diagram)
# ============================================================================
class ASPPLite(nn.Module):
    """
    ASPP-lite: 3×3 dilated DWConv với dilation rates {1,2,4,8} song song + 1×1 fuse
    """
    def __init__(self, in_channels):
        super().__init__()
        
        # 4 nhánh dilated depthwise convolution song song
        self.dw_conv1 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=1, dilation=1, groups=in_channels, bias=False)
        self.dw_conv2 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=2, dilation=2, groups=in_channels, bias=False)
        self.dw_conv4 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=4, dilation=4, groups=in_channels, bias=False)
        self.dw_conv8 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=8, dilation=8, groups=in_channels, bias=False)
        
        # 1×1 fuse layer (pointwise convolution)
        self.fuse = nn.Conv2d(in_channels * 4, in_channels, kernel_size=1, bias=False)
        self.bn = nn.InstanceNorm2d(in_channels)
        self.act = nn.ReLU(inplace=True)
    
    def forward(self, x):
        # 4 nhánh song song
        x1 = self.dw_conv1(x)
        x2 = self.dw_conv2(x)
        x4 = self.dw_conv4(x)
        x8 = self.dw_conv8(x)
        
        # Concat các nhánh
        out = torch.cat([x1, x2, x4, x8], dim=1)  # [B, 4*C, H, W]
        
        # 1×1 fuse
        out = self.fuse(out)  # [B, C, H, W]
        out = self.bn(out)
        out = self.act(out)
        
        return out


# ============================================================================
# NEW BOTTLENECK (theo hình vẽ)
# ============================================================================
class BottleneckNew(nn.Module):
    """
    Bottleneck mới theo kiến trúc trong hình vẽ:
    - Input: B×256×16×16
    - LN/IN normalization
    - Nhánh A: VSS × L (L∈{1,2})
    - Nhánh B: ASPP-lite
    - Concat (A,B) -> B×512×16×16
    - 1×1 PWConv -> 256 channels
    - ECA hoặc SE attention (tùy chọn)
    - Residual connection
    - Output: B×256×16×16
    """
    def __init__(self, dim=256, num_vss_layers=2, use_attention='ECA'):
        """
        Args:
            dim: Number of input/output channels (default: 256)
            num_vss_layers: Number of VSS layers in branch A (1 or 2)
            use_attention: 'ECA', 'SE', or None
        """
        super().__init__()
        
        # Layer Normalization / Instance Normalization
        self.norm = nn.InstanceNorm2d(dim, affine=True)
        
        # ========== NHÁNH A: VSS × L ==========
        # Assuming VSSBlock is already defined in your code
        # VSSBlock expects input shape [B, H, W, C]
        self.vss_layers = nn.ModuleList([
            VSSBlock(hidden_dim=dim, drop_path=0.0, d_state=16)
            for _ in range(num_vss_layers)
        ])
        
        # ========== NHÁNH B: ASPP-lite ==========
        self.aspp = ASPPLite(in_channels=dim)
        
        # ========== 1×1 PWConv after concat ==========
        # Input: 512 channels (256 from A + 256 from B)
        # Output: 256 channels
        self.pw_conv = nn.Conv2d(dim * 2, dim, kernel_size=1, bias=False)
        self.bn = nn.InstanceNorm2d(dim)
        self.act = nn.ReLU(inplace=True)
        
        # ========== ECA hoặc SE Attention ==========
        if use_attention == 'ECA':
            self.attention = ECA(channels=dim)
        elif use_attention == 'SE':
            self.attention = SE(channels=dim, reduction=16)
        else:
            self.attention = None
    
    def forward(self, x):
        """
        Args:
            x: Input tensor [B, 256, H, W]
        Returns:
            Output tensor [B, 256, H, W]
        """
        # Residual connection
        identity = x
        
        # Layer Normalization / Instance Normalization
        x = self.norm(x)
        
        # ========== NHÁNH A: VSS × L ==========
        # VSSBlock expects [B, H, W, C], so we need to permute
        branch_a = x.permute(0, 2, 3, 1)  # [B, C, H, W] -> [B, H, W, C]
        
        for vss_layer in self.vss_layers:
            branch_a = vss_layer(branch_a)
        
        # Permute back to [B, C, H, W]
        branch_a = branch_a.permute(0, 3, 1, 2)  # [B, H, W, C] -> [B, C, H, W]
        
        # ========== NHÁNH B: ASPP-lite ==========
        branch_b = self.aspp(x)
        
        # ========== CONCAT (A, B) ==========
        concat_out = torch.cat([branch_a, branch_b], dim=1)  # [B, 512, H, W]
        
        # ========== 1×1 PWConv -> 256 channels ==========
        out = self.pw_conv(concat_out)
        out = self.bn(out)
        out = self.act(out)
        
        # ========== ECA hoặc SE Attention (optional) ==========
        if self.attention is not None:
            out = self.attention(out)
        
        # ========== Residual Add ==========
        out = out + identity
        
        return out


# ============================================================================
# TEST CODE
# ============================================================================
if __name__ == "__main__":
    print("="*80)
    print("Testing NEW Bottleneck Implementation")
    print("="*80)
    
    # Test input
    B, C, H, W = 2, 256, 16, 16
    x = torch.randn(B, C, H, W)
    
    print(f"\nInput shape: {x.shape}")
    
    # Test Bottleneck with ECA
    print("\n--- Testing with ECA attention ---")
    bottleneck_eca = BottleneckNew(dim=256, num_vss_layers=2, use_attention='ECA')
    out_eca = bottleneck_eca(x)
    print(f"Output shape: {out_eca.shape}")
    print(f"Expected: torch.Size([{B}, {C}, {H}, {W}])")
    
    # Test Bottleneck with SE
    print("\n--- Testing with SE attention ---")
    bottleneck_se = BottleneckNew(dim=256, num_vss_layers=2, use_attention='SE')
    out_se = bottleneck_se(x)
    print(f"Output shape: {out_se.shape}")
    
    # Test Bottleneck without attention
    print("\n--- Testing without attention ---")
    bottleneck_none = BottleneckNew(dim=256, num_vss_layers=1, use_attention=None)
    out_none = bottleneck_none(x)
    print(f"Output shape: {out_none.shape}")
    
    print("\n" + "="*80)
    print("All tests passed! ✓")
    print("="*80)
