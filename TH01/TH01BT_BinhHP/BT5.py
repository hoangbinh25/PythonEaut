# Bảng điểm lớp AIV_EVNICT
diem_thi = ['C', 'B', 'D', 'A', 'F', 'A', 'B', 'F', 'B', 'C', 'A', 'D', 'F', 'B', 'F']

# 1) Tổng số sinh viên trong lớp
so_sinh_vien = len(diem_thi)

# 2) Số sinh viên phải học lại môn này (điểm F)
so_hoc_lai = diem_thi.count('F')

# 3) Số sinh viên có điểm từ B trở lên
diem_tot = ['A', 'B']
so_diem_tot = sum(diem in diem_tot for diem in diem_thi)

# 4) Sinh viên đầu tiên và cuối cùng đã nghỉ học, tạo bảng điểm mới
diem_thi_moi = diem_thi[1:-1]

# In kết quả
print("Bảng điểm lớp AIV_EVNICT:")
print(diem_thi)
print("\n------------THỐNG KÊ------------")
print(f"1. Tổng số sinh viên trong lớp: {so_sinh_vien}")
print(f"2. Số sinh viên phải học lại môn này (điểm F): {so_hoc_lai}")
print(f"3. Số sinh viên có điểm từ B trở lên: {so_diem_tot}")
print(f"4. Bảng điểm mới (loại bỏ sinh viên đầu và cuối): {diem_thi_moi}")
