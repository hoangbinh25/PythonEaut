import numpy as np

# Khởi tạo ma trận a
a = np.array([[9, 4, 19, 1, 18],
              [15, 11, 1, 9, 14],
              [17, 8, 4, 10, 13]])

# Khởi tạo ma trận b
b = np.array([[6, 4, 9, 12, 4],
              [3, 6, 11, 14, 10],
              [1, 6, 5, 12, 2]])

# So sánh hai ma trận
equal_ab = np.equal(a, b)
# hoặc equal_ab = a == b

print(equal_ab)
