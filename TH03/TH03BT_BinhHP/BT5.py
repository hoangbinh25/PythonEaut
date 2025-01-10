def cal_point(diem_he_10):
    # Hàm chuyển đổi điểm hệ 10 sang hệ chữ
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

    # Hàm chuyển đổi điểm hệ 10 sang hệ 4
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

    # Chuyển đổi điểm hệ 10 sang hệ chữ và hệ 4
    diem_chu = [chuyen_doi_diem(diem) for diem in diem_he_10]
    diem_he_4 = [chuyen_doi_he_4(diem) for diem in diem_he_10]

    # Tính điểm trung bình
    diem_tb_he_10 = sum(diem_he_10) / len(diem_he_10)
    diem_tb_he_4 = sum(diem_he_4) / len(diem_he_4)

    # Trả về kết quả
    return {
        "diem_chu": diem_chu,
        "diem_tb_he_10": round(diem_tb_he_10, 2),
        "diem_tb_he_4": round(diem_tb_he_4, 2)
    }


# Khởi tạo danh sách điểm hệ 10
diem_he_10 = [9, 8.5, 7, 5.5, 6]  # Bạn có thể thay đổi danh sách này

# Gọi hàm và in kết quả
result = cal_point(diem_he_10)
print("Danh sách điểm hệ 10:", diem_he_10)
print("Danh sách điểm chữ tương ứng:", result["diem_chu"])
print("Điểm trung bình hệ 10:", result["diem_tb_he_10"])
print("Điểm trung bình hệ 4:", result["diem_tb_he_4"])
