import numpy as np

# Dữ liệu mẫu
diem_2a = np.array([[9, 8, 7],  # Điểm môn 1
                    [10, 5, 6],  # Điểm môn 2
                    [3, 10, 0]]) # Điểm môn 3

for i in range(0, diem_2a.shape[0]):
    print('Độ chênh điểm của học sinh', i, ':', 
          diem_2a[i,:].max() - diem_2a[i,:].min())