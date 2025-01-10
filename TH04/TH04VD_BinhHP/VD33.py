# Tạo ma trận điểm của học sinh (ví dụ)
diem_2a = [
    [6, 7, 9, 5, 10],
    [7, 8, 6, 9, 8],
    [9, 5, 8, 10, 7],
    [6, 8, 7, 9, 9],
    [7, 9, 8, 7, 9],
    [8, 7, 8, 9, 7],
    [6, 5, 9, 7, 8],
    [7, 6, 8, 9, 8],
    [8, 8, 7, 7, 9],
    [7, 9, 6, 9, 10]
]

# Lấy điểm tất cả các môn của học sinh thứ 5
diem_hs5 = diem_2a[4][:5]
print("Điểm các môn của học sinh 5:", diem_hs5)

# Lấy điểm môn học cuối cùng của tất cả học sinh (cột cuối)
diem_mon = [row[-1] for row in diem_2a]
print("Điểm môn học cuối cùng của tất cả học sinh:\n", diem_mon)

# Lấy điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = [row[:5] for row in diem_2a[:10]]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp:\n", diem5_hs10)
