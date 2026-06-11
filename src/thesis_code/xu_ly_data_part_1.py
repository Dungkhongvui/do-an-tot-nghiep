import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os


# 1. Load Data
df = pd.read_csv('gop_data.csv')
df['time'] = pd.to_datetime(df['time'], utc=True)
df = df.sort_values('time')

# 2. Define Specific Holidays (Only the 3 requested: 1/1, 15/8, 25/12)
holidays_3 = [
    (1, 1),   # New Year (Año Nuevo)
    (6, 1),   # Epiphany / Three Kings (Reyes Magos) - Rất quan trọng ở TBN
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
for day, month in holidays_3:
    mask = (df['day'] == day) & (df['month'] == month)
    df.loc[mask, 'is_holiday'] = 1

# 3. Feature Engineering
# Cyclical features
df['hour_sin'] = np.sin(2 * np.pi * df['time'].dt.hour / 24)
df['day_of_week_sin'] = np.sin(2 * np.pi * df['time'].dt.dayofweek / 7)

# Lag features (Long term for 2-3 day forecast)
df['load_lag_24'] = df['load'].shift(24)
df['load_lag_48'] = df['load'].shift(48)
df['load_lag_168'] = df['load'].shift(168) # 7 days lag

# 4. CUT DATA
# User wants to cut the first 10 days to be safe for the 7-day lag.
# 10 days * 24 hours = 240 rows.
# This is greater than 168 (7 days), so it safely removes all NaNs from lags.
cut_rows = 10 * 24 
df_trimmed = df.iloc[cut_rows:].reset_index(drop=True)

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
print(f"Đã xử lý xong file: {output_filename}")
print(f"Số dòng đã cắt bỏ: {cut_rows} dòng (tương đương 10 ngày)")
print(f"Kích thước dữ liệu còn lại: {df_scaled.shape}")
print("-" * 30)
print("Kiểm tra 5 dòng đầu tiên (để chắc chắn không còn NaN):")
print(df_scaled.head())
print("-" * 30)
print("Kiểm tra giá trị NaN trong toàn bộ dữ liệu:")
print(df_scaled.isna().sum())
print(os.getcwd())
