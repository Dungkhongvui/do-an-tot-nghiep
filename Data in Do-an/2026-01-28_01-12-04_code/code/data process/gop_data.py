import pandas as pd
import numpy as np

def process_method_2_multivariate(energy_path, weather_path, output_path):
    print("--- BẮT ĐẦU XỬ LÝ (PHƯƠNG ÁN 2: GIỮ NGUYÊN 5 THÀNH PHỐ) ---")

    # 1. ĐỌC DỮ LIỆU
    print("Đang đọc dữ liệu...")
    df_energy = pd.read_csv(energy_path)
    df_weather = pd.read_csv(weather_path)

    # 2. XỬ LÝ DỮ LIỆU THỜI TIẾT (PIVOT TABLE)
    print("Đang xử lý dữ liệu thời tiết...")
    
    # Chuẩn hóa thời gian về UTC
    df_weather['dt_iso'] = pd.to_datetime(df_weather['dt_iso'], utc=True)
    
    # Loại bỏ dữ liệu trùng lặp (nếu có)
    df_weather = df_weather.drop_duplicates(subset=['dt_iso', 'city_name'])

    # PIVOT: Chuyển 'city_name' thành các cột riêng biệt
    # Chúng ta sẽ lấy feature quan trọng nhất là 'temp' (Nhiệt độ)
    # Nếu bạn muốn thêm humidity, có thể làm tương tự
    weather_pivot = df_weather.pivot_table(
        index='dt_iso', 
        columns='city_name', 
        values='temp'
    )
    
    # Chuyển đổi Kelvin sang Celsius
    weather_pivot = weather_pivot - 273.15
    
    # Đổi tên cột cho sạch đẹp (Xóa khoảng trắng thừa, thêm tiền tố temp_)
    # Ví dụ: ' Barcelona' -> 'temp_Barcelona'
    weather_pivot.columns = [f"temp_{col.strip()}" for col in weather_pivot.columns]
    
    print(f"-> Đã tách thành công {weather_pivot.shape[1]} cột thành phố: {list(weather_pivot.columns)}")

    # 3. XỬ LÝ DỮ LIỆU ĐIỆN
    print("Đang xử lý dữ liệu điện...")
    df_energy['time'] = pd.to_datetime(df_energy['time'], utc=True)
    df_energy.set_index('time', inplace=True)

    # Chọn cột Load và Price
    df_energy_clean = df_energy[['total load actual', 'price actual']].copy()
    df_energy_clean.columns = ['load', 'price']

    # Nội suy giá trị thiếu
    df_energy_clean = df_energy_clean.interpolate(method='linear')
    df_energy_clean.dropna(inplace=True)

    # 4. GỘP DỮ LIỆU (MERGE)
    print("Đang gộp dữ liệu...")
    # Merge Inner Join theo index thời gian
    df_final = df_energy_clean.join(weather_pivot, how='inner')

    # Kiểm tra dữ liệu sau khi gộp (có thể còn sót NaN do lệch giờ ở đầu/cuối file weather)
    df_final.dropna(inplace=True)

    # 5. LƯU FILE
    df_final.to_csv(output_path)
    print(f"--- THÀNH CÔNG! File đã lưu tại: {output_path} ---")
    print(f"Kích thước dữ liệu: {df_final.shape}")
    print("5 dòng đầu tiên:")
    return df_final.head()

# --- CHẠY CODE ---
file_energy = r'C:\Users\PC\Desktop\python\data\energy.csv'
file_weather = r'C:\Users\PC\Desktop\python\data\weather.csv'
output_file = r'C:\Users\PC\Desktop\python\data\ex.csv'

df_result = process_method_2_multivariate(file_energy, file_weather, output_file)
print(df_result)