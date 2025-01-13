import numpy as np

# Đọc dữ liệu từ file và lưu vào numpy array
data = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH4.2/TH04-2BT-BinhHP/temp.txt')

# Yêu cầu 2: Tính Max, Min, và Nhiệt độ trung bình của cả 6 thành phố
max_temp_all = np.max(data)
min_temp_all = np.min(data)
mean_temp_all = np.mean(data)

print(data)

print("Yêu cầu 2:")
print(f"Nhiệt độ cao nhất (Max) của cả 6 thành phố: {max_temp_all:.2f}")
print(f"Nhiệt độ thấp nhất (Min) của cả 6 thành phố: {min_temp_all:.2f}")
print(f"Nhiệt độ trung bình của cả 6 thành phố: {mean_temp_all:.2f}")
