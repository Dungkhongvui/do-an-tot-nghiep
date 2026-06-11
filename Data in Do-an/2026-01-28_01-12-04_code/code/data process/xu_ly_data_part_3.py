import pandas as pd

# 1. Load dữ liệu đầu vào
df = pd.read_csv('final_data_cut_10_days.csv')

print("Original Data Head:")
print(df.head())
print("Danh sách cột ban đầu:", df.columns.tolist())

# 2. Tạo đặc trưng trễ (Lag Feature) với tên mới là 'load_lag_1h'
# Giả định cột đầu tiên là 'load', hoặc trò có thể gọi trực tiếp df['load'] nếu chắc chắn tên cột
load_col_name = 'load' if 'load' in df.columns else df.columns[0]
df['load_lag_1h'] = df[load_col_name].shift(1)

# 3. Sắp xếp lại thứ tự cột (Reordering)
# Mục tiêu: [load, load_lag_1h, load_lag_24, ...]
# Logic: Tìm vị trí của 'load_lag_24' để chèn 'load_lag_1h' vào ngay trước nó.

cols = df.columns.tolist()

# Loại bỏ 'load_lag_1h' khỏi danh sách hiện tại để ta tự tay chèn nó vào đúng chỗ
cols.remove('load_lag_1h')

if 'load_lag_24' in cols:
    # Nếu có cột load_lag_24, ta tìm vị trí của nó
    idx_24 = cols.index('load_lag_24')
    # Chèn load_lag_1h vào đúng vị trí đó (nó sẽ đẩy load_lag_24 ra sau 1 bước)
    cols.insert(idx_24, 'load_lag_1h')
else:
    # Trường hợp file không có load_lag_24, ta để mặc định ở vị trí thứ 2 (index 1) sau 'load'
    cols.insert(1, 'load_lag_1h')

# Cập nhật lại DataFrame theo thứ tự cột mới
df = df[cols]

# 4. Xử lý dữ liệu khuyết thiếu (NaN) sinh ra do hàm shift()
df_dropped = df.dropna()

# 5. Lưu file kết quả
output_filename = 'final_data_with_lag.csv'
df_dropped.to_csv(output_filename, index=False)

print("\nNew Data Head:")
print(df_dropped.head())
print(f"\nĐã lưu file đã xử lý xong vào: {output_filename}")
print("Thứ tự cột sau khi sửa:", df_dropped.columns.tolist())