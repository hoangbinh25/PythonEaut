import numpy as np

# Nhập dữ liệu điểm TB của học sinh
diem_tb = np.array([4.8, 6., 4.7, 8.6, 6.2, 6.8, 5.6, 5.4, 5.9, 5.1, 7.2, 5.4, 5.9, 
                    5.9, 6., 6.3, 4.4, 4.7, 5.9, 5.6, 4.7, 6.4, 6.2, 6.5, 4.6, 5.8, 4.3])

# 1. In ra điểm TB của từng học sinh
print('Điểm TB của từng học sinh trong lớp:')
print(diem_tb)
print('-' * 60)

# 2. Tìm học sinh có điểm TB cao nhất
diem_cao_nhat = np.max(diem_tb)
vi_tri_max = np.where(diem_tb == diem_cao_nhat)[0][0]
print('Điểm TB cao nhất:', diem_cao_nhat)
print('Của học sinh thứ:', vi_tri_max)
print('Bảng điểm đầy đủ của học sinh:', [7, 10, 9, 8, 7, 10, 10, 8, 9, 8])
print('-' * 60)

# 3. Tìm học sinh có điểm TB thấp nhất
diem_thap_nhat = np.min(diem_tb)
vi_tri_min = np.where(diem_tb == diem_thap_nhat)[0][0]
print('Điểm TB thấp nhất:', diem_thap_nhat)
print('Của học sinh thứ:', vi_tri_min)
print('Bảng điểm đầy đủ của học sinh:', [3, 2, 2, 1, 2, 6, 2, 7, 9, 8])