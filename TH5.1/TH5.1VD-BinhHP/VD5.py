import numpy as np

# Tạo một vector
vector_a = np.array([5, 7, 2, 9, 10, 15, 2, 9, 2, 17, 28, 16], dtype=np.int16)

# In ra vector và số phần tử của vector
print(vector_a)
print('Số phần tử của vector:', vector_a.size)

# Chuyển đổi vector thành ma trận 3x4
matrix_a = vector_a.reshape(3, 4)
print('Reshape về matrix: 3 x 4')
print(matrix_a)
print('Số phần tử của matrix_a:', matrix_a.size)

# Chuyển đổi vector thành ma trận 2x6
matrix_b = vector_a.reshape(2, 6)
print('Reshape về matrix: 2 x 6')
print(matrix_b)
print('Số phần tử của matrix_b:', matrix_b.size)