import numpy as np

diem_2a = np.array([
    [9, 8, 7, 10],  # Học sinh 0
    [10, 8, 9, 7],  # Học sinh 1
    [8, 7, 10, 9],  # Học sinh 2
])

print('Điểm trung bình của cả lớp 2A: ', diem_2a.mean())
print('--------------------------------------------------------')

# Cách 1
for i in range(0, diem_2a.shape[1]):
    print('Điểm trung bình của học sinh ', i, ' : ', diem_2a[:,i].mean())

#Cách 2:
mean_2a = diem_2a.mean(axis=0)
#axis = 0: theo hàng
#axis = 1: theo cột

for i in range(0, mean_2a.size):
    print('Điểm trung bình của học sinh ', i, ' : ', mean_2a[i])
    