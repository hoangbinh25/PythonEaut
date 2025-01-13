import numpy as np

diem_2a = np.array([
    [9, 8, 7, 10],  # Học sinh 0
    [10, 8, 9, 7],  # Học sinh 1
    [8, 7, 10, 9],  # Học sinh 2
])

print('Tổng tất các điểm trong của lớp 2A: ', diem_2a.sum())
print('-----------------------------------------------------')

for i in range(0, diem_2a.shape[1]):
    print('Tổng điểm các môn của học sinh ', i, ' : ', diem_2a[:,i].sum())