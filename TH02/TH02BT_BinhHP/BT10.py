        # Khởi tạo danh sách điểm hệ 10
diem_he_10 = [9, 8.5, 7, 5.5, 6]  # Bạn có thể thay đổi danh sách này

# 1) Chuyển đổi điểm hệ 10 sang điểm chữ
def chuyen_doi_diem(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

diem_chu = [chuyen_doi_diem(diem) for diem in diem_he_10]

# 2) Tính điểm trung bình Hệ 10 và Hệ 4
def chuyen_doi_he_4(diem):
    if diem >= 8.5:
        return 4.0
    elif diem >= 7.0:
        return 3.0
    elif diem >= 5.5:
        return 2.0
    elif diem >= 4.0:
        return 1.0
    else:
        return 0.0

diem_he_4 = [chuyen_doi_he_4(diem) for diem in diem_he_10]

diem_tb_he_10 = sum(diem_he_10) / len(diem_he_10)
diem_tb_he_4 = sum(diem_he_4) / len(diem_he_4)

# Kết quả
print("Danh sách điểm hệ 10:", diem_he_10)
print("Danh sách điểm chữ tương ứng:", diem_chu)
print("Điểm trung bình hệ 10:", round(diem_tb_he_10, 2))
print("Điểm trung bình hệ 4:", round(diem_tb_he_4, 2))
