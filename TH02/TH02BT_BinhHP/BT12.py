# Nhập vào số N
try:
    N = int(input("Nhập vào số N: "))

    if N < 2:
        print("Không có số nguyên tố nào trong khoảng từ 2 tới N.")
    else:
        print(f"Các số nguyên tố từ 2 tới {N} là:")
        for num in range(2, N + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):  # Kiểm tra số nguyên tố
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
        print()  # In dòng mới sau khi hiển thị tất cả số nguyên tố
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
