import numpy as np

# Tạo ma trận a
a = np.array([[ 9,  4, 19,  1, 18],
              [11,  9,  4, 14, 19],
              [17,  8, 14, 10, 13]])

# Tạo ma trận b
b = np.array([[ 6,  4,  9, 12,  4],
              [18, 17, 20,  2,  4],
              [ 1,  6,  9, 12,  2]])

# Phép cộng 2 ma trận
sum_ab = np.add(a, b)
# Hoặc sum_ab = a + b
print('Kết quả của phép cộng 2 ma trận:')
print(sum_ab)

# Phép trừ 2 ma trận
sub_ab = np.subtract(a, b)
# Hoặc sub_ab = a - b
print('Kết quả của phép trừ 2 ma trận:')
print(sub_ab)
