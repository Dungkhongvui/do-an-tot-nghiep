# HƯỚNG DẪN THAY ĐỔI BOTTLENECK

## 1. Code Bottleneck Cũ (trong promt.pdf)

```python
class BottleneckPCAPSA(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.pca = PCA(dim)
        self.psa = PSA(dim)
    
    def forward(self, x):
        pca_out = self.pca(x)
        psa_out = self.psa(pca_out)
        return psa_out
```

## 2. Code Bottleneck Mới (theo hình vẽ)

```python
class BottleneckNew(nn.Module):
    """
    Kiến trúc mới:
    - Input: B×256×16×16
    - LN/IN normalization
    - Nhánh A: VSS × L (L∈{1,2})
    - Nhánh B: ASPP-lite (3×3 dilated DWConv với rates {1,2,4,8} + 1×1 fuse)
    - Concat (A,B) -> B×512×16×16
    - 1×1 PWConv -> 256 channels
    - ECA/SE attention (tùy chọn)
    - Residual connection
    - Output: B×256×16×16
    """
    def __init__(self, dim=256, num_vss_layers=2, use_attention='ECA'):
        super().__init__()
        
        # Normalization
        self.norm = nn.InstanceNorm2d(dim, affine=True)
        
        # NHÁNH A: VSS × L
        self.vss_layers = nn.ModuleList([
            VSSBlock(hidden_dim=dim, drop_path=0.0, d_state=16)
            for _ in range(num_vss_layers)
        ])
        
        # NHÁNH B: ASPP-lite
        self.aspp = ASPPLite(in_channels=dim)
        
        # 1×1 PWConv sau concat (512 -> 256)
        self.pw_conv = nn.Conv2d(dim * 2, dim, kernel_size=1, bias=False)
        self.bn = nn.InstanceNorm2d(dim)
        self.act = nn.ReLU(inplace=True)
        
        # Attention (ECA hoặc SE)
        if use_attention == 'ECA':
            self.attention = ECA(channels=dim)
        elif use_attention == 'SE':
            self.attention = SE(channels=dim, reduction=16)
        else:
            self.attention = None
    
    def forward(self, x):
        identity = x  # Residual
        
        # Normalization
        x = self.norm(x)
        
        # NHÁNH A: VSS
        branch_a = x.permute(0, 2, 3, 1)  # [B,C,H,W] -> [B,H,W,C]
        for vss_layer in self.vss_layers:
            branch_a = vss_layer(branch_a)
        branch_a = branch_a.permute(0, 3, 1, 2)  # [B,H,W,C] -> [B,C,H,W]
        
        # NHÁNH B: ASPP-lite
        branch_b = self.aspp(x)
        
        # CONCAT
        concat_out = torch.cat([branch_a, branch_b], dim=1)  # [B, 512, H, W]
        
        # 1×1 PWConv
        out = self.pw_conv(concat_out)
        out = self.bn(out)
        out = self.act(out)
        
        # Attention (optional)
        if self.attention is not None:
            out = self.attention(out)
        
        # Residual
        out = out + identity
        
        return out
```

## 3. Các Module Phụ Trợ

### 3.1. ASPP-Lite (Nhánh B)

```python
class ASPPLite(nn.Module):
    """3×3 dilated DWConv với rates {1,2,4,8} + 1×1 fuse"""
    def __init__(self, in_channels):
        super().__init__()
        
        # 4 nhánh dilated depthwise conv song song
        self.dw_conv1 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=1, dilation=1, groups=in_channels, bias=False)
        self.dw_conv2 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=2, dilation=2, groups=in_channels, bias=False)
        self.dw_conv4 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=4, dilation=4, groups=in_channels, bias=False)
        self.dw_conv8 = nn.Conv2d(in_channels, in_channels, kernel_size=3, 
                                   padding=8, dilation=8, groups=in_channels, bias=False)
        
        # 1×1 fuse
        self.fuse = nn.Conv2d(in_channels * 4, in_channels, kernel_size=1, bias=False)
        self.bn = nn.InstanceNorm2d(in_channels)
        self.act = nn.ReLU(inplace=True)
    
    def forward(self, x):
        x1 = self.dw_conv1(x)
        x2 = self.dw_conv2(x)
        x4 = self.dw_conv4(x)
        x8 = self.dw_conv8(x)
        
        out = torch.cat([x1, x2, x4, x8], dim=1)
        out = self.fuse(out)
        out = self.bn(out)
        out = self.act(out)
        return out
```

### 3.2. ECA Attention

```python
class ECA(nn.Module):
    """Efficient Channel Attention"""
    def __init__(self, channels, gamma=2, b=1):
        super().__init__()
        import numpy as np
        t = int(abs((np.log2(channels) + b) / gamma))
        k_size = t if t % 2 else t + 1
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        y = self.avg_pool(x)
        y = y.squeeze(-1).transpose(-1, -2)
        y = self.conv(y)
        y = y.transpose(-1, -2).unsqueeze(-1)
        return x * self.sigmoid(y)
```

### 3.3. SE Attention (Alternative)

```python
class SE(nn.Module):
    """Squeeze-and-Excitation"""
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
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)
```

## 4. CÁCH THAY ĐỔI TRONG CODE CHÍNH

### Bước 1: Xóa/Comment code cũ

Tìm và comment các dòng sau trong code:

```python
# class PSA(nn.Module):
#     ...
# 
# class PCA(nn.Module):
#     ...
# 
# class BottleneckPCAPSA(nn.Module):
#     ...
```

### Bước 2: Thêm code mới

Copy toàn bộ code từ file `new_bottleneck.py` (ECA, SE, ASPPLite, BottleneckNew) vào đúng vị trí cũ (section 4.2. Bottleneck).

### Bước 3: Sửa trong class ULite

Tìm dòng:
```python
"""Bottle Neck"""
self.b5 = BottleneckPCAPSA(256)
```

Thay bằng:
```python
"""Bottle Neck"""
self.b5 = BottleneckNew(dim=256, num_vss_layers=2, use_attention='ECA')
# Hoặc dùng SE:
# self.b5 = BottleneckNew(dim=256, num_vss_layers=2, use_attention='SE')
# Hoặc không dùng attention:
# self.b5 = BottleneckNew(dim=256, num_vss_layers=1, use_attention=None)
```

## 5. THAM SỐ CÓ THỂ CHỈNH

- `dim=256`: Số channels (mặc định 256 theo hình vẽ)
- `num_vss_layers=2`: Số VSS layers trong nhánh A (1 hoặc 2)
- `use_attention='ECA'`: Loại attention ('ECA', 'SE', hoặc None)

## 6. KẾT QUẢ

- **Input**: `[B, 256, 16, 16]`
- **Output**: `[B, 256, 16, 16]`
- Kiến trúc mới phức tạp hơn với:
  - Multi-scale features từ ASPP-lite
  - Long-range dependencies từ VSS
  - Residual connection để stable training
  - Optional attention mechanism

## 7. TEST

Sau khi thay đổi, test bằng:

```python
# Test shape
x = torch.randn(2, 256, 16, 16).to(device)
bottleneck = BottleneckNew(dim=256, num_vss_layers=2, use_attention='ECA').to(device)
out = bottleneck(x)
print(f"Input: {x.shape}, Output: {out.shape}")
# Expected: Input: torch.Size([2, 256, 16, 16]), Output: torch.Size([2, 256, 16, 16])
```
