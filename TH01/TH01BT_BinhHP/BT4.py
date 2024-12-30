
doan_van = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

# số ký tự có trong đoạn văn trên
so_ky_tu = len(doan_van)
print(f"Số ký tự trong đoạn văn: {so_ky_tu}")

# kiểm tra từ "hồ chí minh" và "non sông" có trong đoạn văn không (không phân biệt hoa thường)
tu_1 = "hồ chí minh"
tu_2 = "non sông"
co_tu_1 = tu_1.lower() in doan_van.lower()
co_tu_2 = tu_2.lower() in doan_van.lower()
print(f"Đoạn văn có chứa từ '{tu_1}': {co_tu_1}")
print(f"Đoạn văn có chứa từ '{tu_2}': {co_tu_2}")

# tách đoạn văn thành các câu bởi dấu .
cau = doan_van.split('.')
cau = [c.strip() for c in cau if c.strip()] # loại bỏ khoảng trắng
print("Các câu trong đoạn văn:")
for i, c in enumerate(cau, 1):
    print(f"Câu {i}: {c}")

# kiểm tra trong đoạn có ký tự nào khác ký tự chữ và số không
co_ky_tu_khac = any(not char.isalnum() and not char.isspace() for char in doan_van)
print(f"Đoạn văn có chứa ký tự khác chữ và số: {co_ky_tu_khac}")

# "Việt Nam" bằng "VIỆTNAM"
doan_van_thay_the = doan_van.replace("Việt Nam", "VIỆT NAM")
print("Đoạn văn sau khi thay thế:")
print(doan_van_thay_the)
