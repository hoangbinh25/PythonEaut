import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào mảng numpy
data_diamond = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH4.2/TH04-2BT-BinhHP/data.txt')

diamond_size = data_diamond[:, 0]  # Cột 0: Trọng lượng
diamond_price = data_diamond[:, 1]  # Cột 1: Giá bán

print(diamond_size)
print(diamond_price)
