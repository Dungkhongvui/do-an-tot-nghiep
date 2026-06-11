import pandas as pd

def load_data(energy_path, weather_path):
    df_energy = pd.read_csv(energy_path)
    df_weather = pd.read_csv(weather_path)

    print("Energy infomation: ...")
    print("Shape:", df_energy.shape)
    print("Column:", df_energy.columns.to_list())
    print(df_energy.head())
    print(df_energy.isna().sum())

    print("\nWeather infomation: ...")
    print("Shape:", df_weather.shape)
    print("Column:", df_weather.columns.to_list())
    print(df_weather.head())
    print(df_weather.isna().sum())

def process_energy(energy_path):
    df_energy = pd.read_csv(energy_path)
    df_energy['time'] = pd.to_datetime(df_energy["time"], utc=True)
    df_energy.set_index('time',inplace=True)
    df_energy_copy = df_energy[['total load actual', 'price actual']].copy()
    df_energy_copy.columns = ['load', 'price']

    # Nội suy các giá trị thiếu
    df_energy_copy = df_energy_copy.interpolate(method='linear')
    df_energy_copy.dropna(inplace=True)
    # print('Energy sau xử lý:', df_energy_copy)
    return df_energy_copy

def process_weather(weather_path):
    df_weather = pd.read_csv(weather_path)
    df_weather['dt_iso'] = pd.to_datetime(df_weather['dt_iso'], utc=True)
    df_weather = df_weather.drop_duplicates(subset=['dt_iso', 'city_name'])
    weather_pivot = df_weather.pivot_table(values='temp', index='dt_iso', columns='city_name')
    weather_pivot = weather_pivot - 273.1
    weather_pivot.columns = [f"temp_{col.strip()}" for col in weather_pivot.columns]
    # print(weather_pivot.columns)
    return weather_pivot

def merge_data(energy_path, weather_path, output_path):
    df_energy_copy = process_energy(energy_path)
    weather_pivot = process_weather(weather_path)
    # Hợp nhất cột thời gian, các cột khác lấy luôn
    df_final = df_energy_copy.join(weather_pivot, how='inner')
    df_final.dropna(inplace=True)
    df_final.to_csv(output_path)
    return df_final

# Check
energy_path = 'C:\\Users\\LAPTOP\\Documents\\Careers\\HUST\\Do-an-tot-nghiep\\short_term_electricity_load_forecasting\\src\\data\\energy.csv'
weather_path = 'C:\\Users\\LAPTOP\\Documents\\Careers\\HUST\\Do-an-tot-nghiep\\short_term_electricity_load_forecasting\\src\\data\\weather.csv'
output_path = 'C:\\Users\\LAPTOP\\Documents\\Careers\\HUST\\Do-an-tot-nghiep\\short_term_electricity_load_forecasting\\src\\data\\gop_data.csv'


df_final = merge_data(energy_path, weather_path, output_path)