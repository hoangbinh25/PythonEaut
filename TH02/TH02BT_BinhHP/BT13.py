# Nhập vào số tự nhiên N
try:
    N = int(input("Nhập vào số tự nhiên N (N > 0): "))

    # Kiểm tra điều kiện N > 0
    if N <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        # Chuyển đổi số N sang hệ nhị phân
        binary_representation = bin(N)[2:]  # Sử dụng hàm bin() và loại bỏ "0b" ở đầu
        print(f"Số {N} trong hệ nhị phân là: {binary_representation}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
