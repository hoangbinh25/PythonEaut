import numpy as np

path = 'D:/Documents/DHCNDA/Python/Class/TH04/TH04VD_BinhHP/Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int64)

print(diem_2a)
print("Kiểu dữ liệu của phẩn tử trong mảng diem_2a: ", diem_2a.dtype)
print("Kích thước của mảng diem_2a: ", diem_2a.shape)
print("Số phần tử của mảng diem_2a: ",diem_2a.size)
print("Số chiều của mảng diem_2a: ", diem_2a.ndim)