import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào mảng numpy
data_diamond = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH4.2/TH04-2BT-BinhHP/data.txt')
# Thông tin về mảng data_diamond
print(data_diamond)
print(f"Kích thước biến data_diamond: {data_diamond.shape}")
print(f"Số chiều của biến data_diamond: {data_diamond.ndim}")
print(f"Kiểu dữ liệu của các phần tử: {data_diamond.dtype}")
print(f"Số phần tử: {data_diamond.size}")