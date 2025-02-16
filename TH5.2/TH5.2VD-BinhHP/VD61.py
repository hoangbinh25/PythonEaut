import numpy as np

# Tạo ma trận A
A = np.array([[1, 2, 0, 4, 5, -3],
              [3, -7, 2, 6, 1, 4],
              [2, -5, 2, 4, 3, 6],
              [4, -9, 2, -4, -4, 7]])

# Tìm ma trận chuyển vị của A
A_T = A.T
print('Ma trận A:\n', A)
print('Ma trận chuyển vị của A:\n', A_T)

# Tạo ma trận B
B = np.array([[1, 3, 1, 4],
              [3, 9, 5, 15],
              [0, 2, 1, 4],
              [2, 4, 2, 3]])

# Tìm ma trận chuyển vị của B
B_T = B.T
print('Ma trận B:\n', B)
print('Ma trận chuyển vị của B:\n', B_T)
