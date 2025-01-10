import numpy as np

b = np.array([(1, 2, 5.0),(7, 0, 8)])

print(b)
print("Loại dữ liệu của biến a: ", type(b))
print("Kiểu dữ liệu của phẩn tử trong mảng a: ", b.dtype)
print("Kích thước của mảng a: ", b.shape)
print("Số phần tử của mảng a: ", b.size)
print("Số chiều của mảng a: ", b.ndim)
