# Danh sách điểm trung bình cho từng môn học
diem_trung_binh = [4.73, 4.43, 5.5, 4.83, 4.97, 5.6, 6.23, 7.3, 6.13, 7.97]

# Tính điểm trung bình cho từng môn học
print("Điểm trung bình cho từng môn học:")
for i, diem in enumerate(diem_trung_binh):
    print(f"Môn học {i+1}: {diem}")

# Tìm môn học có điểm trung bình cao nhất
diem_cao_nhat = max(diem_trung_binh)
mon_cao_nhat = diem_trung_binh.index(diem_cao_nhat) + 1
print(f"\nĐiểm trung bình cao nhất: {diem_cao_nhat} (Môn học {mon_cao_nhat})")

# Tìm môn học có điểm trung bình thấp nhất
diem_thap_nhat = min(diem_trung_binh)
mon_thap_nhat = diem_trung_binh.index(diem_thap_nhat) + 1
print(f"\nĐiểm trung bình thấp nhất: {diem_thap_nhat} (Môn học {mon_thap_nhat})")
