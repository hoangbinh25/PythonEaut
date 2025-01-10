import numpy as np

array_zeros = np.zeros((5, 2))

array_one = np.ones((5, 2), dtype=np.int32) 

print(array_zeros)
print("Kiểu dữ liệu của phẩn tử trong mảng array_zeros: ", array_zeros.dtype)
print("Kích thước của mảng array_zeros: ", array_zeros.shape)
print("Số phần tử của mảng array_zeros: ",array_zeros.size)
print("Số chiều của mảng array_zeros: ", array_zeros.ndim)
print("----------------------------------------------------------------")
print(array_one)
print("Kiểu dữ liệu của phẩn tử trong mảng array_one: ", array_one.dtype)
print("Kích thước của mảng array_one: ", array_one.shape)
print("Số phần tử của mảng array_one: ",array_one.size)
print("Số chiều của mảng array_one: ", array_one.ndim)