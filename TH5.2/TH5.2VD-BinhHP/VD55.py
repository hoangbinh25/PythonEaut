import numpy as np

# Tạo ma trận a
a = np.array([[ 9,  4,  9,  1, 18],
              [15, 11,  9,  9, 14]])

# Tạo ma trận c
c = np.array([[17,  2,  4],
              [12,  1,  3],
              [ 1,  2,  3],
              [ 1,  6,  4],
              [13,  6,  4]])

# Nhân hai ma trận a và c
multi_ac = np.dot(a, c)
# Hoặc sử dụng toán tử @
# multi_ac1 = a @ c

print('Kết quả của tích hai ma trận a và c:')
print(multi_ac)

# Tạo hai vector ngẫu nhiên
vector_a = np.random.randint(1, 20, 10)
vector_b = np.random.randint(1, 20, 10)

# Tích của hai vector
vector_ab = np.dot(vector_a, vector_b)
# Hoặc sử dụng toán tử @
# vector_ab = vector_a @ vector_b

print('\nVector a:')
print(vector_a)
print('Vector b:')
print(vector_b)
print('Tích của hai vector:')
print(vector_ab)
