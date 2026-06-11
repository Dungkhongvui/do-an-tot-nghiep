import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
import math

# --- 1. SETUP DỮ LIỆU ---
print("Đang nạp dữ liệu...")
df = pd.read_csv('final_data_with_lag.csv')

# Tách Input (X) và Output (Y)
# Cột đầu tiên là 'load' -> Y, các cột còn lại -> X
Y = df.iloc[:, 0].values.reshape(-1, 1)
X = df.iloc[:, 1:].values

# Chia Train/Test (80% Train, 20% Test) - KHÔNG SHUFFLE
train_size = int(len(df) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

print(f"Dữ liệu Train: {X_train.shape}, Dữ liệu Test: {X_test.shape}")

# Thông số thực tế để đổi đơn vị (Denormalize)
REAL_MIN = 18041.0
REAL_MAX = 41015.0

# --- 2. XÂY DỰNG MÔ HÌNH ELM ---
class ELM_Model:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.beta = None
    
    def predict(self, X, W, b):
        # Tính H = sigmoid(X.W + b)
        H = np.dot(X, W) + b
        H = 1 / (1 + np.exp(-H)) # Sigmoid activation
        
        # Nếu đang training (có Y_train), ta tính Beta
        # Ở đây ta chỉ trả về H để dùng bên ngoài hoặc predict
        return H

# --- 3. THUẬT TOÁN PSO ---
def pso_optimize_elm(X_train, Y_train, hidden_size, pop_size=50, iterations=50):
    input_size = X_train.shape[1]
    dim = input_size * hidden_size + hidden_size # Số lượng trọng số cần tìm (W + b)
    
    # Khởi tạo bầy ong
    X_pop = np.random.uniform(-1, 1, (pop_size, dim)) # Vị trí
    V_pop = np.zeros((pop_size, dim))                 # Vận tốc
    
    P_best = X_pop.copy() # Ký ức cá nhân tốt nhất
    P_best_fitness = np.array([float('inf')] * pop_size)
    
    G_best = np.zeros(dim) # Ký ức toàn bầy tốt nhất
    G_best_fitness = float('inf')
    
    loss_history = []
    
    print(f"Bắt đầu PSO với {iterations} vòng lặp...")
    for i in range(iterations):
        for j in range(pop_size):
            # Tách vector thành W và b
            w_vec = X_pop[j, :input_size * hidden_size]
            b_vec = X_pop[j, input_size * hidden_size:]
            W = w_vec.reshape(input_size, hidden_size)
            b = b_vec
            
            # ELM Step 1: Tính H
            H = np.dot(X_train, W) + b
            H = 1 / (1 + np.exp(-H))
            
            # ELM Step 2: Tính Beta (Moore-Penrose Inverse)
            # Beta = pinv(H) * Y
            # Thêm I*C để ổn định (Regularization)
            H_pinv = np.linalg.pinv(H)
            beta = np.dot(H_pinv, Y_train)
            
            # Tính sai số (MSE) trên tập Train
            Y_pred = np.dot(H, beta)
            fitness = np.mean((Y_train - Y_pred) ** 2)
            
            # Cập nhật P_best
            if fitness < P_best_fitness[j]:
                P_best_fitness[j] = fitness
                P_best[j] = X_pop[j]
                
            # Cập nhật G_best
            if fitness < G_best_fitness:
                G_best_fitness = fitness
                G_best = X_pop[j]
        
        # Di chuyển bầy ong
        # w=0.7 (quán tính), c1=1.5 (cá nhân), c2=1.5 (xã hội)
        r1, r2 = np.random.rand(pop_size, dim), np.random.rand(pop_size, dim)
        V_pop = 0.7 * V_pop + 1.5 * r1 * (P_best - X_pop) + 1.5 * r2 * (G_best - X_pop)
        X_pop = X_pop + V_pop
        
        loss_history.append(G_best_fitness)
        if i % 5 == 0:
            print(f"Vòng {i}: MSE = {G_best_fitness:.5f}")
            
    return G_best, loss_history

# --- 4. CHẠY THỰC TẾ ---
hidden_neurons = 50
best_weights, loss_history = pso_optimize_elm(X_train, Y_train, hidden_neurons, pop_size=50, iterations=50)

# --- 5. ĐÁNH GIÁ TRÊN TẬP TEST (Chưa từng nhìn thấy) ---
# Giải mã bộ trọng số tốt nhất
input_dim = X_train.shape[1]
W_best = best_weights[:input_dim * hidden_neurons].reshape(input_dim, hidden_neurons)
b_best = best_weights[input_dim * hidden_neurons:]

# Tính H cho tập Test
H_test = np.dot(X_test, W_best) + b_best
H_test = 1 / (1 + np.exp(-H_test))

# Tính lại Beta từ tập Train (Dùng trọng số W_best để tính beta chuẩn)
H_train = np.dot(X_train, W_best) + b_best
H_train = 1 / (1 + np.exp(-H_train))
beta_final = np.dot(np.linalg.pinv(H_train), Y_train)

# Dự báo cuối cùng
Y_pred_scaled = np.dot(H_test, beta_final)

# Đổi đơn vị về MW
Y_test_MW = Y_test * (REAL_MAX - REAL_MIN) + REAL_MIN
Y_pred_MW = Y_pred_scaled * (REAL_MAX - REAL_MIN) + REAL_MIN

# Tính độ chính xác
mae = mean_absolute_error(Y_test_MW, Y_pred_MW) 
mape = mean_absolute_percentage_error(Y_test_MW, Y_pred_MW) * 100
rmse = math.sqrt(mean_squared_error(Y_test_MW, Y_pred_MW))

print("\n" + "="*30)
print(f"KẾT QUẢ DỰ BÁO (TEST SET)")
print("="*30)
print(f"Sai số trung bình (MAPE): {mape:.4f}%")
print(f"Độ lệch chuẩn (RMSE): {rmse:.2f} MW")
print(f"Sai số tuyệt đối trung bình (MAE): {mae:.2f} MW")
# --- 6. VẼ BIỂU ĐỒ ---
plt.figure(figsize=(15, 6))
# Vẽ 200 giờ cuối cùng
start_plot = 0
end_plot = 300
plt.plot(Y_test_MW[start_plot:end_plot], label='Thực tế (Actual)', color='blue', linewidth=2)
plt.plot(Y_pred_MW[start_plot:end_plot], label='Dự báo (PSO-ELM)', color='red', linestyle='--', linewidth=2)
plt.title(f'Dự báo Phụ tải điện (PSO-ELM) - {end_plot} giờ đầu tiên của tập Test')
plt.xlabel('Thời gian (Giờ)')
plt.ylabel('Công suất (MW)')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ biểu đồ hội tụ PSO
plt.figure(figsize=(10, 4))
plt.plot(loss_history, marker='o')
plt.title('Biểu đồ Hội tụ của PSO (Sai số giảm dần)')
plt.xlabel('Vòng lặp')
plt.ylabel('MSE (Loss)')
plt.grid(True)
plt.show()