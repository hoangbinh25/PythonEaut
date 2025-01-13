from scipy import stats as sp
import numpy as np

diem_2a = np.array([
    [9, 8, 7, 10],
    [10, 8, 9, 7],
    [8, 7, 10, 9],
])

for i in range(0, diem_2a.shape[1]):
    a = sp.mode(diem_2a[:,i])
    print('Môn', i, ': Điểm xuất hiện nhiều nhất:', a[0],
          'số lần:', a[1])

print(type(a))