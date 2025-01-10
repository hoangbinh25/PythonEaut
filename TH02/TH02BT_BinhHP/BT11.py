# Nhập N
try:
    N = int(input("Nhập vào số tự nhiên N: "))

    # Kiểm tra N
    if N <= 1:
        print(f"{N} không phải là số nguyên tố (số nguyên tố phải lớn hơn 1).")
    else:
        # Kiểm tra số nguyên tố
        is_prime = True
        for i in range(2, int(N**0.5) + 1):  # Lặp qua các số từ 2 đến căn bậc hai của N
            if N % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{N} là số nguyên tố.")
        else:
            print(f"{N} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")
