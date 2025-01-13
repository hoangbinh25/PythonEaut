import numpy as np
from scipy import stats as sp

# Tạo và phân tích dữ liệu giờ học và điểm thi
a_giohoc = np.array([4,7,1,2,8,0,3,8,6])  # Số giờ học
b_diem = np.array([7,9,3,4,9,0,5,10,8])   # Điểm thi

# Tính ma trận hệ số tương quan
co = np.corrcoef(a_giohoc, b_diem)
print('Hệ số tương quan:\n', co)
print(type(co))