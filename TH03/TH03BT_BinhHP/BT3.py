def count_mark(diem_thi):
    
    # 1) Tổng số sinh viên trong lớp
    so_sinh_vien = len(diem_thi)

    # 2) Số sinh viên phải học lại môn này (điểm F)
    so_hoc_lai = diem_thi.count('F')

    return print(f"1. Tổng số sinh viên trong lớp: {so_sinh_vien}"), print(f"2. Số sinh viên phải học lại môn này (điểm F): {so_hoc_lai}")

diem_thi = ['C', 'B', 'D', 'A', 'F', 'A', 'B', 'F', 'B', 'C', 'A', 'D', 'F', 'B', 'F']
result = count_mark(diem_thi)