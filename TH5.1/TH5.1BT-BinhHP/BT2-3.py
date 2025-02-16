import numpy as np

# Đọc dữ liệu từ tệp "Data_BMI.txt"
data = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH5.1/TH5.1BT-BinhHP/Data_BMI.txt', delimiter=',')
v_height = data[:, 0]
v_weight = data[:, 1]

# Chuyển đổi đơn vị chiều cao từ cm sang m
v_height_m = v_height / 100

# Tính chỉ số BMI và làm tròn đến 1 chữ số thập phân
v_bmi = np.round(v_weight / (v_height_m ** 2), 1)

print('Chỉ số BMI:', v_bmi)
