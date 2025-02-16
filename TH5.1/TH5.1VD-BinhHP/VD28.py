import numpy as np

x = np.array([17, 2, 11, 1, 9, 15, 1, 3, 8, 1, 12, 13, 5])

# 1) Tìm kiếm các phần tử có giá trị == 1
t1 = np.where(x == 1)
print(t1)
print('1. Số phần tử thỏa mãn điều kiện = 1: ', t1[0].size)
print('---------------------------------------------')

# 2) Tìm kiếm các phần tử có giá trị > 10
t2 = np.where(x > 10)
print(t2)
print('2. Số phần tử thỏa mãn điều kiện > 10: ', t2[0].size)
print('---------------------------------------------')

# 3) Tìm kiếm các phần tử có giá trị trong khoảng [5, 12]
t3 = np.where((x >= 5) & (x <= 12))
print(t3)
print('3. Số phần tử thỏa mãn điều kiện [5, 10]: ', t3[0].size)
