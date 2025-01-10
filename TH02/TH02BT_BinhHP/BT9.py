# Yêu cầu người dùng nhập bảng cửu chương muốn hiển thị
try:
    n = int(input("Nhập vào bảng cửu chương muốn hiển thị [1-10]: "))

    # Kiểm tra nếu giá trị nằm trong khoảng hợp lệ
    if 1 <= n <= 10:
        print(f"\nBảng cửu chương {n}:")
        for i in range(1, 11):  # Lặp qua các số từ 1 đến 10
            print(f"{n} x {i} = {n * i}")
    else:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số trong khoảng từ 1 đến 10.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
