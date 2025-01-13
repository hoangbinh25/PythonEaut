import numpy as np

diem_2a = np.array([
    [9, 8, 7, 10],  # Học sinh 0
    [10, 8, 9, 7],  # Học sinh 1
    [8, 7, 10, 9],  # Học sinh 2
])

# 1) Xác định điểm cao nhất và thấp nhất của cả lớp
print('Điểm cao nhất của lớp:', diem_2a.max())
print('Điểm thấp nhất của lớp:', diem_2a.min())
print()

# 2) Liệt kê điểm cao nhất và thấp nhất theo môn học
for i in range(diem_2a.shape[1]):
    print('Môn', i, ': Điểm Max:', diem_2a[:,i].max(), 
          '-- Điểm Min:', diem_2a[:,i].min())
print()

# 3) Liệt kê điểm cao nhất và thấp nhất của mỗi học sinh
for i in range(diem_2a.shape[0]):
    print('Học sinh', i, ': Điểm Max:', diem_2a[i,:].max(),
          '-- Điểm Min:', diem_2a[i,:].min())