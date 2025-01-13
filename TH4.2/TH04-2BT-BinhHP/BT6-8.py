import numpy as np
import matplotlib.pyplot as plt

data_diamond = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH4.2/TH04-2BT-BinhHP/data.txt')

diamond_size = data_diamond[:, 0]  # Cột 0: Trọng lượng
diamond_price = data_diamond[:, 1]  # Cột 1: Giá bán

plt.figure(figsize=(8, 6))
plt.scatter(diamond_size, diamond_price, color='blue', alpha=0.7, label='Dữ liệu')
plt.title("Mối quan hệ giữa kích thước và giá bán kim cương")
plt.xlabel("Kích thước (carat)")
plt.ylabel("Giá bán ($)")
plt.grid(True)
plt.legend()
plt.show()

# Tính hệ số tương quan giữa kích thước và giá bán
correlation_coefficient = np.corrcoef(diamond_size, diamond_price)[0, 1]
print(f"Hệ số tương quan giữa kích thước và giá bán kim cương: {correlation_coefficient:.2f}")