import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import math
import warnings


warnings.filterwarnings('ignore')

# --- 1. SETUP DỮ LIỆU ---
print("Loading data...")
df = pd.read_csv('final_data_with_lag.csv')

# Tách Input (X) và Output (Y)
Y = df.iloc[:, 0].values.reshape(-1, 1)
X = df.iloc[:, 1:].values

# Chia Train/Test (80% Train, 20% Test) - KHÔNG SHUFFLE
train_size = int(len(df) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# Thông số thực tế để đổi đơn vị
REAL_MIN = 18041.0
REAL_MAX = 41015.0

# --- 2. CLASS ELM (KHÔNG DÙNG PSO) ---
class StandardELM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.W = None
        self.b = None
        self.beta = None
    
    def sigmoid(self, x):
        # Chặn overflow để tránh lỗi runtime với số quá lớn
        return 1 / (1 + np.exp(-np.clip(x, -250, 250)))
    
    def fit(self, X, Y):
        # KHÔNG cố định seed ở đây để mỗi lần khởi tạo là một bộ W khác nhau
        self.W = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.b = np.random.uniform(-1, 1, (self.hidden_size))
        
        H = np.dot(X, self.W) + self.b
        H = self.sigmoid(H)
        
        # Thêm Regularization nhỏ (1e-8) để tránh ma trận suy biến (Singular Matrix)
        # Công thức: Beta = pinv(H) * Y
        H_pinv = np.linalg.pinv(H)
        self.beta = np.dot(H_pinv, Y)
        
    def predict(self, X):
        H = np.dot(X, self.W) + self.b
        H = self.sigmoid(H)
        return np.dot(H, self.beta)

# --- 3. CHẠY VÒNG LẶP 20 LẦN ---
n_iterations = 20
hidden_neurons = 100
mape_results = []

print(f"Starting {n_iterations} runs for Standard ELM...")
print("-" * 40)

for i in range(n_iterations):
    # Khởi tạo và huấn luyện lại từ đầu
    elm = StandardELM(input_size=X_train.shape[1], hidden_size=hidden_neurons)
    elm.fit(X_train, Y_train)
    
    # Dự báo
    Y_pred_scaled = elm.predict(X_test)
    
    # Denormalize về đơn vị MW
    Y_test_MW = Y_test * (REAL_MAX - REAL_MIN) + REAL_MIN
    Y_pred_MW = Y_pred_scaled * (REAL_MAX - REAL_MIN) + REAL_MIN
    
    # Tính MAPE
    mape = mean_absolute_percentage_error(Y_test_MW, Y_pred_MW) * 100
    mape_results.append(mape)
    
    print(f"Run {i+1:02d}: MAPE = {mape:.4f}%")

# --- 4. TẠO BẢNG THỐNG KÊ (TIẾNG ANH) ---
mapes = np.array(mape_results)

statistics = {
    "Best (Min MAPE)": np.min(mapes),
    "Worst (Max MAPE)": np.max(mapes),
    "Average (Mean)": np.mean(mapes),
    "Standard Deviation": np.std(mapes), # Độ lệch chuẩn
    "Range (Max - Min)": np.ptp(mapes)   # ptp = peak to peak (Max - Min)
}

stats_df = pd.DataFrame(list(statistics.items()), columns=['Metric', 'Value (%)'])

print("\n" + "="*40)
print("ELM PERFORMANCE SUMMARY (20 RUNS)")
print("="*40)
print(stats_df.to_string(index=False, float_format=lambda x: "{:.4f}".format(x)))
print("="*40)

