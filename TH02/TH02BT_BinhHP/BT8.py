# Nhập tháng sinh từ người dùng
try:
    month = int(input("Nhập vào tháng sinh của bạn (1-12): "))

    # Xác định mùa sinh
    if 1 <= month <= 3:
        print("Bạn sinh vào Mùa xuân.")
    elif 4 <= month <= 6:
        print("Bạn sinh vào Mùa hạ.")
    elif 7 <= month <= 9:
        print("Bạn sinh vào Mùa thu.")
    elif 10 <= month <= 12:
        print("Bạn sinh vào Mùa đông.")
    else:
        print("Tháng sinh nhập vào không đúng.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ từ 1 đến 12.")
