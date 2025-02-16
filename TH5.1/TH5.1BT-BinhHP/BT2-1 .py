import numpy as np

# Đọc dữ liệu từ tệp "Data_BMI.txt"
data = np.loadtxt('D:/Documents/DHCNDA/Python/Class/TH5.1/TH5.1BT-BinhHP/Data_BMI.txt', delimiter=',')
height = data[:, 0]
weight = data[:, 1]

# Tính chỉ số BMI
BMI = weight / (height / 100) ** 2

# Phân loại theo chỉ số BMI
categories = np.empty(BMI.shape, dtype=object)
categories[BMI < 18.5] = 'Underweight'
categories[(BMI >= 18.5) & (BMI < 25)] = 'Normal'
categories[(BMI >= 25) & (BMI < 30)] = 'Overweight'
categories[(BMI >= 30) & (BMI < 35)] = 'Obese'
categories[BMI >= 35] = 'Extremely Obese'

# In kết quả
for i in range(len(BMI)):
    print(f'Person {i+1}: Height = {height[i]} cm, Weight = {weight[i]} kg, BMI = {BMI[i]:.2f}, Category = {categories[i]}')
