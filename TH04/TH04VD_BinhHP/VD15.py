import numpy as np

c = np.array([[(1, 2, 5, 8),(7, 0, 8, 9)],
             [(2, 6, 5, 4),(1, 7, 0, 8)],
             [(1, 4, 2, 3),(9, 7, 0, 8)]])

print(c)
print("Loại dữ liệu của biến c: ", type(c))
print("Kiểu dữ liệu của phẩn tử trong mảng c: ", c.dtype)
print("Kích thước của mảng c: ", c.shape)
print("Số phần tử của mảng c: ", c.size)
print("Số chiều của mảng c: ", c.ndim)
