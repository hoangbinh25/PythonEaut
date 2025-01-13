import numpy as np

diem_2a = np.array([
    [9, 8, 7, 10],
    [10, 8, 9, 7],
    [8, 7, 10, 9],
])

a = diem_2a[1, :15]

print('Mảng a ban đầu: \n', a)
print('Số phần tử trong mảng a: \n', a.size)
print('Mảng a đã sắp xếp: \n', np.sort(a,))
print('Giá trị trung bình mean: ', np.mean(a))
print('Giá trị trung vị mean: ', np.mean(a))
