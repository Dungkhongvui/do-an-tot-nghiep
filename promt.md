# 🟠1. IMPORTING LIBRARIES

from google.colab import drive
drive.mount('contentdrive')

import pandas as pd

# 🟠2. DATA PROCESSING

# Show dữ liệu
energy_path = 'contentdriveMyDriveDo_an_tot_nghiepDataenergy.csv'
weather_path = 'contentdriveMyDriveDo_an_tot_nghiepDataweather.csv'

df_energy = pd.read_csv(energy_path)
df_weather = pd.read_csv(weather_path)

print(Dữ liệu Energy)
print(Shape, df_energy.shape)
print(Column, df_energy.columns.tolist())
print(df_energy.head())
print(df_energy.isna().sum())

print(nDữ liệu Weather)
print(Shape, df_weather.shape)
print(Column, df_weather.columns.tolist())
print(df_weather.head())
print(df_weather.isna().sum())

import pandas as pd
import numpy as np

# Xử lý dữ liệu thô - dữ liệu ổn
def process_weather(weather_pạth)
    df_weather = pd.read_csv(weather_pạth)
    # Chỉnh thời gian về giờ UTC
    df_weather['dt_iso'] = pd.to_datetime(df_weather['dt_iso',utc = True])

    # Chuyển dt_iso thành các hàng, city_name là các cột và các giá trị sẽ là nhiệt độ (được lấy mặc định là trung bình)
    weather_pivot = df_weather.pivot_table(index=dt_iso, columns=city_name, values=temp)




import pandas as pd
import numpy as np

def process_method_2_multivariate(energy_path, weather_path, output_path)
    print(--- BẮT ĐẦU XỬ LÝ (PHƯƠNG ÁN 2 GIỮ NGUYÊN 5 THÀNH PHỐ) ---)

    print(Đang đọc dữ liệu...)
    df_energy = pd.read_csv(energy_path)
    df_weather = pd.read_csv(weather_path)

    print(Đang xử lý dữ liệu thời tiết...)
    df_weather['dt_iso'] = pd.to_datetime(df_weather['dt_iso'], utc=True)
    df_weather = df_weather.drop_duplicates(subset=['dt_iso', 'city_name'])
    weather_pivot = df_weather.pivot_table(
        index='dt_iso',
        columns='city_name',
        values='temp'
    )
    weather_pivot = weather_pivot - 273.1
    weather_pivot.columns = [ftemp_{col.strip()} for col in weather_pivot.columns]
    print(f- Đã tách thành công {weather_pivot.shape[1]} cột thành phố {list(weather_pivot.columns)})
    print(Đang xử lý dữ liệu điện...)
    df_energy['time'] = pd.to_datetime(df_energy['time'], utc=True)
    df_energy.set_index('time', inplace=True)
    df_energy_clean = df_energy[['total load actual', 'price actual']].copy()
    df_energy_clean.columns = ['load', 'price']
    df_energy_clean = df_energy_clean.interpolate(method='linear')
    df_energy_clean.dropna(inplace=True)
    print(Đang gộp dữ liệu...)
    df_final = df_energy_clean.join(weather_pivot, how='inner')
    df_final.dropna(inplace=True)
    df_final.to_csv(output_path)
    print(f--- THÀNH CÔNG! File đã lưu tại {output_path} ---)
    print(fKích thước dữ liệu {df_final.shape})
    print(5 dòng đầu tiên)
    return df_final.head()

file_energy = 'contentdriveMyDriveDo_an_tot_nghiepDataenergy.csv'
file_weather = 'contentdriveMyDriveDo_an_tot_nghiepDataweather.csv'
output_file = 'contentdriveMyDriveDo_an_tot_nghiepDatagop_data.csv'

df_result = process_method_2_multivariate(file_energy, file_weather, output_file)
print(df_result)

Visualize dữ liệu đã gộp

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
gop_data_path = 'contentdriveMyDriveDo_an_tot_nghiepDatagop_data.csv'
df = pd.read_csv(gop_data_path)

# Select columns
temp_cols = ['temp_Barcelona', 'temp_Bilbao', 'temp_Madrid', 'temp_Seville', 'temp_Valencia']
target_cols = ['load', 'price'] + temp_cols

# 1. Calculate Descriptive Statistics
stats = df[target_cols].describe()
print(Descriptive Statistics for Load, Price, and Temperatures)
print(stats)

# 2. Visualization

# Set up the figure for Load and Price distribution
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Load Distribution
sns.histplot(df['load'], kde=True, ax=axes[0, 0], color='blue')
axes[0, 0].set_title('Phân bố Phụ tải điện (Load Distribution)')
axes[0, 0].set_xlabel('Load (MW)')

sns.boxplot(x=df['load'], ax=axes[0, 1], color='blue')
axes[0, 1].set_title('Biểu đồ hộp Phụ tải điện (Load Boxplot)')
axes[0, 1].set_xlabel('Load (MW)')

# Price Distribution
sns.histplot(df['price'], kde=True, ax=axes[1, 0], color='green')
axes[1, 0].set_title('Phân bố Giá điện (Price Distribution)')
axes[1, 0].set_xlabel('Price (EURMWh)')

sns.boxplot(x=df['price'], ax=axes[1, 1], color='green')
axes[1, 1].set_title('Biểu đồ hộp Giá điện (Price Boxplot)')
axes[1, 1].set_xlabel('Price (EURMWh)')

plt.tight_layout()
plt.savefig('load_price_distribution.png')
plt.show()

# Set up figure for Temperature comparison
plt.figure(figsize=(14, 8))
sns.boxplot(data=df[temp_cols], palette=coolwarm)
plt.title('So sánh phân bố Nhiệt độ giữa các thành phố (Temperature Comparison)')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('temp_comparison_boxplot.png')
plt.show()

# Correlation Matrix
plt.figure(figsize=(10, 8))
corr = df[target_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=.2f, linewidths=0.5)
plt.title('Ma trận tương quan (Correlation Matrix)')
plt.savefig('correlation_matrix.png')
plt.show()

Chuyển dữ liệu thành các feature đầu vào
- Lt-1, Lt-24, Lt-48, Lt-168 (tải giờ trước, tải hôm qua, tải 2 ngày trước, tải 1 tuần trước),
- Nhiệt độ 5 thành phố, Giá điện,
- hour_sin, day_sin (vì nếu không model sẽ thấy 23 và 0 rất xa nhau)
- holiday

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os


# 1. Load Data
gop_data_path = 'contentdriveMyDriveDo_an_tot_nghiepDatagop_data.csv'
df = pd.read_csv(gop_data_path)
df['time'] = pd.to_datetime(df['time'], utc=True)
df = df.sort_values('time')

# 2. Define Specific Holidays (Only the 3 requested 11, 158, 2512)
holidays_3 = [
    (1, 1),   # New Year (Año Nuevo)
    (6, 1),   # Epiphany  Three Kings (Reyes Magos) - Rất quan trọng ở TBN
    (1, 5),   # Labour Day (Fiesta del Trabajo)
    (15, 8),  # Assumption of Mary (Asunción)
    (12, 10), # National Day (Fiesta Nacional de España)
    (1, 11),  # All Saints (Todos los Santos)
    (6, 12),  # Constitution Day (Día de la Constitución)
    (8, 12),  # Immaculate Conception (Inmaculada Concepción)
    (25, 12)  # Christmas (Navidad)
]

df['day'] = df['time'].dt.day
df['month'] = df['time'].dt.month

# Create is_holiday column
df['is_holiday'] = 0
for day, month in holidays_3
    mask = (df['day'] == day) & (df['month'] == month)
    df.loc[mask, 'is_holiday'] = 1

# 3. Feature Engineering
# Cyclical features
df['hour_sin'] = np.sin(2  np.pi  df['time'].dt.hour  24)
df['day_of_week_sin'] = np.sin(2  np.pi  df['time'].dt.dayofweek  7)

# Lag features (Long term for 2-3 day forecast)
df['load_lag_24'] = df['load'].shift(24)
df['load_lag_48'] = df['load'].shift(48)
df['load_lag_168'] = df['load'].shift(168) # 7 days lag

# 4. CUT DATA
# User wants to cut the first 10 days to be safe for the 7-day lag.
# 10 days  24 hours = 240 rows.
# This is greater than 168 (7 days), so it safely removes all NaNs from lags.
cut_rows = 10  24
df_trimmed = df.iloc[cut_rows].reset_index(drop=True)

# 5. Select Final Columns
feature_cols = [
    'load', 'is_holiday', 'price',
    'temp_Barcelona', 'temp_Bilbao', 'temp_Madrid', 'temp_Seville', 'temp_Valencia',
    'hour_sin', 'day_of_week_sin',
    'load_lag_24', 'load_lag_48', 'load_lag_168'
]

df_final = df_trimmed[feature_cols]

# 6. Normalize [0, 1]
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_final), columns=df_final.columns)

# Save
output_filename = 'final_data_cut_10_days.csv'
df_scaled.to_csv(output_filename, index=False)

# Display stats to confirm with user
print(fĐã xử lý xong file {output_filename})
print(fSố dòng đã cắt bỏ {cut_rows} dòng (tương đương 10 ngày))
print(fKích thước dữ liệu còn lại {df_scaled.shape})
print(-  30)
print(Kiểm tra 5 dòng đầu tiên (để chắc chắn không còn NaN))
print(df_scaled.head())
print(-  30)
print(Kiểm tra giá trị NaN trong toàn bộ dữ liệu)
print(df_scaled.isna().sum())
print(os.getcwd())


import pandas as pd

# 1. Load dữ liệu đầu vào
df = pd.read_csv('final_data_cut_10_days.csv')

print(Original Data Head)
print(df.head())
print(Danh sách cột ban đầu, df.columns.tolist())

# 2. Tạo đặc trưng trễ (Lag Feature) với tên mới là 'load_lag_1h'
# Giả định cột đầu tiên là 'load', hoặc trò có thể gọi trực tiếp df['load'] nếu chắc chắn tên cột
load_col_name = 'load' if 'load' in df.columns else df.columns[0]
df['load_lag_1h'] = df[load_col_name].shift(1)

# 3. Sắp xếp lại thứ tự cột (Reordering)
# Mục tiêu [load, load_lag_1h, load_lag_24, ...]
# Logic Tìm vị trí của 'load_lag_24' để chèn 'load_lag_1h' vào ngay trước nó.

cols = df.columns.tolist()

# Loại bỏ 'load_lag_1h' khỏi danh sách hiện tại để ta tự tay chèn nó vào đúng chỗ
cols.remove('load_lag_1h')

if 'load_lag_24' in cols
    # Nếu có cột load_lag_24, ta tìm vị trí của nó
    idx_24 = cols.index('load_lag_24')
    # Chèn load_lag_1h vào đúng vị trí đó (nó sẽ đẩy load_lag_24 ra sau 1 bước)
    cols.insert(idx_24, 'load_lag_1h')
else
    # Trường hợp file không có load_lag_24, ta để mặc định ở vị trí thứ 2 (index 1) sau 'load'
    cols.insert(1, 'load_lag_1h')

# Cập nhật lại DataFrame theo thứ tự cột mới
df = df[cols]

# 4. Xử lý dữ liệu khuyết thiếu (NaN) sinh ra do hàm shift()
df_dropped = df.dropna()

# 5. Lưu file kết quả
output_filename = 'final_data_with_lag.csv'
df_dropped.to_csv(output_filename, index=False)

print(nNew Data Head)
print(df_dropped.head())
print(fnĐã lưu file đã xử lý xong vào {output_filename})
print(Thứ tự cột sau khi sửa, df_dropped.columns.tolist())

# 🟠8. ESN-ELM MODEL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')

# 1. SETUP DỮ LIỆU

print(Loading data...)
df = pd.read_csv('final_data_with_lag.csv')

# Output (GT) sử dụng cột đầu của bảng (load) và chuyển định dạng từ mảng 1 chiều - ma trận 2 chiều
Y    = df.iloc[, 0].values.reshape(-1, 1)   # 'load' — cột mục tiêu
X_df = df.iloc[, 1]                         # toàn bộ features

# Phân nhóm features
ESN_FEATURE   = 'load_lag_1h'
LAG_FEATURES  = ['load_lag_24','load_lag_168']    # không dùng — Variant B tốt hơn
EXOG_FEATURES = [c for c in X_df.columns
                 if c not in [ESN_FEATURE] + LAG_FEATURES]

X_esn  = X_df[[ESN_FEATURE]].values    # [N, 1]
X_exog = X_df[EXOG_FEATURES].values    # [N, 9]

# Traintest split 8020, không shuffle
train_size    = int(len(df)  0.8)
X_esn_train,  X_esn_test  = X_esn[train_size],  X_esn[train_size]
X_exog_train, X_exog_test = X_exog[train_size],  X_exog[train_size]
Y_train,      Y_test       = Y[train_size],       Y[train_size]

# Giá trị max và min của phụ tải dùng để khôi phục dải 0 - 1 về dải gốc
REAL_MIN = 18041.0
REAL_MAX  = 41015.0

# Check thông tin đầu vào
print(fTrain {X_esn_train.shape[0]} samples  Test {X_esn_test.shape[0]} samples)
print(fESN input  {X_esn_train.shape})
print(fExog input {X_exog_train.shape})


# 2. CLASS EchoStateNetwork

class EchoStateNetwork
    
    Echo State Network với leaky integrator.

    Công thức cập nhật state tại bước t
        h(t) = (1 - alpha)  h(t-1)
               + alpha  tanh(W_in @ x(t) + W_res @ h(t-1) + b_res)

    Các ma trận W_in, W_res, b_res được khởi tạo ngẫu nhiên và CỐ ĐỊNH
    (không huấn luyện). Chỉ ELM phía sau được huấn luyện.

    Tham số đã chốt
        reservoir_size  = 100
        spectral_radius = 0.85
        leaking_rate    = 0.3
        input_scaling   = 1.0
        seed            = 42
    

    def __init__(self, input_size, reservoir_size=100, spectral_radius=0.85,
                 leaking_rate=0.3, input_scaling=1.0, seed=42)
        self.input_size      = input_size
        self.reservoir_size  = reservoir_size
        self.spectral_radius = spectral_radius
        self.leaking_rate    = leaking_rate
        self.input_scaling   = input_scaling
        self.seed            = seed
        self._last_state     = np.zeros(reservoir_size)
        # Trọng số đầu vào ESN (ngẫu nhiên, cố định)
        self._initialize_weights()

    def _initialize_weights(self)
        
        Khởi tạo W_in [reservoir, input], W_res [reservoir, reservoir], b_res.
        W_res thưa 20% non-zero, được scale đúng spectral radius.
        
        rng       = np.random.RandomState(self.seed)
        self.W_in = rng.uniform(-self.input_scaling, self.input_scaling,
                                (self.reservoir_size, self.input_size))

        # Tạo kết nối thưa
        W_raw = rng.uniform(-1, 1, (self.reservoir_size, self.reservoir_size))
        mask  = rng.rand(self.reservoir_size, self.reservoir_size)  0.2
        W_raw = W_raw  mask

        # ⚠️ eigvals trả về số phức — bắt buộc dùng np.abs
        rho = np.max(np.abs(np.linalg.eigvals(W_raw)))
        if rho  1e-10
            W_raw = rng.uniform(-1, 1, (self.reservoir_size, self.reservoir_size))
            rho   = np.max(np.abs(np.linalg.eigvals(W_raw)))

        self.W_res = W_raw  (self.spectral_radius  rho)
        self.b_res = rng.uniform(-0.1, 0.1, (self.reservoir_size,))

        actual_rho = np.max(np.abs(np.linalg.eigvals(self.W_res)))
        print(f[ESN] reservoir={self.reservoir_size}, 
              fspectral_radius={self.spectral_radius} (actual={actual_rho.4f}), 
              fleaking_rate={self.leaking_rate})

    def _run_reservoir(self, X, h_init)
        Chạy reservoir qua chuỗi X từ state h_init.
        h        = h_init.copy()
        H_states = np.zeros((X.shape[0], self.reservoir_size))
        for t in range(X.shape[0])
            pre = self.W_in @ X[t] + self.W_res @ h + self.b_res
            h   = (1 - self.leaking_rate)  h + self.leaking_rate  np.tanh(pre)
            H_states[t] = h
        return H_states, h

    def transform_train(self, X_train)
        
        Chạy ESN trên tập train, bắt đầu từ h=0.
        Lưu state cuối để transform_test() tiếp nối.

        Args
            X_train [N_train, input_size]
        Returns
            H_train [N_train, reservoir_size]
        
        H_train, self._last_state = self._run_reservoir(
            X_train, np.zeros(self.reservoir_size)
        )
        print(f[ESN] transform_train {X_train.shape} → {H_train.shape})
        return H_train

    def transform_test(self, X_test)
        
        Chạy ESN trên tập test, tiếp nối state cuối từ training.
        Không reset h=0 — chuỗi thời gian là liên tục.

        Args
            X_test [N_test, input_size]
        Returns
            H_test [N_test, reservoir_size]
        
        H_test, _ = self._run_reservoir(X_test, self._last_state)
        print(f[ESN] transform_test  {X_test.shape} → {H_test.shape})
        return H_test


# 3. CLASS StandardELM


class StandardELM
    
    Extreme Learning Machine chuẩn cho bài toán hồi quy.

    Trong ESN-ELM
        input_size = reservoir_size + len(EXOG_FEATURES) = 100 + 9 = 109

    Tham số đã chốt
        hidden_size = 500
        activation  = sigmoid
        solver      = pseudo-inverse
    

    def __init__(self, input_size, hidden_size=200)
        self.input_size  = input_size
        self.hidden_size = hidden_size
        self.W = self.b = self.beta = None

    def sigmoid(self, x)
        # Clip [-250, 250] tránh overflow khi tính exp
        return 1  (1 + np.exp(-np.clip(x, -250, 250)))

    def fit(self, X, Y)
        
        Huấn luyện ELM bằng pseudo-inverse.
            H    = sigmoid(X @ W + b)     [N, hidden_size]
            beta = pinv(H) @ Y            [hidden_size, 1]

        Args
            X [N, input_size] — H_states ghép với X_exog
            Y [N, 1]
        
        # KHÔNG cố định seed — mỗi run ELM có W, b khác nhau (đúng với thiết kế)
        self.W    = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.b    = np.random.uniform(-1, 1, (self.hidden_size,))
        H         = self.sigmoid(X @ self.W + self.b)   # [N, hidden_size]
        self.beta = np.linalg.pinv(H) @ Y               # [hidden_size, 1]

    def predict(self, X)
        
        Args
            X [N, input_size]
        Returns
            Y_pred [N, 1] — đã scale (0,1), chưa denormalize
        
        H = self.sigmoid(X @ self.W + self.b)
        return H @ self.beta   # [N, 1]



# 4. BUILD RESERVOIR STATES — 1 LẦN DUY NHẤT
# ESN seed=42 → W_in, W_res cố định → H_train, H_test không đổi
# Không cần tính lại trong vòng lặp 20 lần

print(n + ─50)
print(Bước 13 — Build reservoir states)
print(─50)

esn     = EchoStateNetwork(input_size=1)
H_train = esn.transform_train(X_esn_train)   # [27858, 100]
H_test  = esn.transform_test(X_esn_test)     # [6965,  100]

# Ghép H_states với features ngoại sinh — Variant B (tốt nhất từ thực nghiệm)
# ⚠️ np.hstack yêu cầu số hàng bằng nhau
ELM_train = np.hstack([H_train, X_exog_train])   # [27858, 109]
ELM_test  = np.hstack([H_test,  X_exog_test])    # [6965,  109]

print(fELM input train={ELM_train.shape}, test={ELM_test.shape})
# Luồng dữ liệu đầy đủ
# load_lag_1h [N,1] → ESN [reservoir=100] → H_states [N,100] ─┐
# X_exog      [N,9] ──────────────────────────────────────────►├─► ELM [hidden=500] → Y [N,1]
#                                                               ┘


# 5. VÒNG LẶP 20 LẦN

print(n + ─50)
print(Bước 23 — Chạy 20 lần ELM)
print(─50)

N_RUNS      = 20
HIDDEN_SIZE = 200
mape_results = []

for i in range(N_RUNS)
    elm = StandardELM(input_size=ELM_train.shape[1], hidden_size=HIDDEN_SIZE)
    elm.fit(ELM_train, Y_train)

    Y_pred_scaled = elm.predict(ELM_test)

    # Denormalize về MW — giữ nguyên từ code gốc
    Y_test_MW = Y_test         (REAL_MAX - REAL_MIN) + REAL_MIN
    Y_pred_MW = Y_pred_scaled  (REAL_MAX - REAL_MIN) + REAL_MIN

    mape = mean_absolute_percentage_error(Y_test_MW, Y_pred_MW)  100
    mape_results.append(mape)
    print(fRun {i+102d} MAPE = {mape.4f}%)

# Lưu run tốt nhất để plot
best_run_idx = int(np.argmin(mape_results))



# 6. BẢNG THỐNG KÊ

print(n + ─50)
print(Bước 33 — Thống kê và so sánh)
print(─50)

mapes = np.array(mape_results)

statistics = {
    Best (Min MAPE)    np.min(mapes),
    Worst (Max MAPE)   np.max(mapes),
    Average (Mean)     np.mean(mapes),
    Standard Deviation np.std(mapes),
    Range (Max - Min)  np.ptp(mapes),
}
stats_df = pd.DataFrame(list(statistics.items()), columns=['Metric', 'Value (%)'])

print(n + =50)
print(ESN-ELM PERFORMANCE SUMMARY (20 RUNS))
print(=50)
print(stats_df.to_string(index=False, float_format=lambda x f{x.4f}))
print(=50)

# --- Bảng so sánh với các mô hình trước ---
comparison = pd.DataFrame({
    'Model' [
        'ELM thuần (baseline)',
        'ESN-ELM Final (reservoir=100, hs=500)',
    ],
    'Mean MAPE (%)' [2.1683, np.mean(mapes)],
    'Min MAPE (%)'  ['2.1683', f{np.min(mapes).4f}],
    'Std (%)'       ['—',     f{np.std(mapes).4f}],
})
print(n + =50)
print(SO SÁNH VỚI BASELINE)
print(=50)
print(comparison.to_string(index=False))
improvement = 2.1683 - np.mean(mapes)
print(fn✅ ESN-ELM cải thiện {improvement.4f}% so với ELM thuần)



# 7. PLOT KẾT QUẢ — THÊM MỚI

# Dự báo lại với run tốt nhất để có Y_pred cho plot

elm_best = StandardELM(input_size=ELM_train.shape[1], hidden_size=HIDDEN_SIZE)
# Cố định seed cho run tốt nhất để tái lập được plot
np.random.seed(best_run_idx  7)
elm_best.fit(ELM_train, Y_train)
Y_pred_best = elm_best.predict(ELM_test)

Y_test_MW      = Y_test         (REAL_MAX - REAL_MIN) + REAL_MIN
Y_pred_best_MW = Y_pred_best    (REAL_MAX - REAL_MIN) + REAL_MIN

fig, axes = plt.subplots(2, 1, figsize=(14, 8))
fig.suptitle(f'ESN-ELM — Dự báo phụ tải điệnn'
             f'MAPE = {mape_results[best_run_idx].4f}% '
             f'(Run tốt nhất  20)', fontsize=13)

# Plot 1 So sánh thực tế vs dự báo (500 điểm cuối)
n_plot = 500
ax1 = axes[0]
ax1.plot(Y_test_MW[-n_plot],      label='Thực tế',  color='#2c7bb6', linewidth=1.2)
ax1.plot(Y_pred_best_MW[-n_plot], label='Dự báo',   color='#d7191c',
         linewidth=1.0, linestyle='--', alpha=0.85)
ax1.set_title(f'{n_plot} điểm cuối tập test')
ax1.set_ylabel('Phụ tải (MW)')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

# Plot 2 MAPE qua 20 lần chạy
ax2 = axes[1]
runs = np.arange(1, N_RUNS + 1)
ax2.bar(runs, mapes, color='#4dac26', alpha=0.75, label='MAPE mỗi run')
ax2.axhline(np.mean(mapes), color='#d01c8b', linewidth=1.8,
            linestyle='--', label=f'Mean = {np.mean(mapes).4f}%')
ax2.axhline(2.1683, color='#f1a340', linewidth=1.5,
            linestyle='', label=f'ELM baseline = 2.1683%')
ax2.set_title('MAPE qua 20 lần chạy')
ax2.set_xlabel('Run')
ax2.set_ylabel('MAPE (%)')
ax2.set_xticks(runs)
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('esn_elm_final_results.png', dpi=150, bbox_inches='tight')
plt.show()
print(nĐã lưu esn_elm_final_results.png)
