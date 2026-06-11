import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('gop_data.csv')

# Select columns
temp_cols = ['temp_Barcelona', 'temp_Bilbao', 'temp_Madrid', 'temp_Seville', 'temp_Valencia']
target_cols = ['load', 'price'] + temp_cols

# 1. Calculate Descriptive Statistics
stats = df[target_cols].describe()
print("Descriptive Statistics for Load, Price, and Temperatures:")
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
axes[1, 0].set_xlabel('Price (EUR/MWh)')

sns.boxplot(x=df['price'], ax=axes[1, 1], color='green')
axes[1, 1].set_title('Biểu đồ hộp Giá điện (Price Boxplot)')
axes[1, 1].set_xlabel('Price (EUR/MWh)')

plt.tight_layout()
plt.savefig('load_price_distribution.png')
plt.show()

# Set up figure for Temperature comparison
plt.figure(figsize=(14, 8))
sns.boxplot(data=df[temp_cols], palette="coolwarm")
plt.title('So sánh phân bố Nhiệt độ giữa các thành phố (Temperature Comparison)')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('temp_comparison_boxplot.png')
plt.show()

# Correlation Matrix 
plt.figure(figsize=(10, 8))
corr = df[target_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Ma trận tương quan (Correlation Matrix)')
plt.savefig('correlation_matrix.png')
plt.show()