def list_prime(n):
    # Kiểm tra nếu n nhỏ hơn 2, không có số nguyên tố
    if n < 2:
        return []

    # Hàm kiểm tra số nguyên tố
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Duyệt qua các số từ 2 đến n và kiểm tra số nguyên tố
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes


# Nhập vào số N từ người dùng
while True:
    user_input = input("Nhập vào số N: ")
    if user_input.isdigit():  # Kiểm tra xem người dùng nhập có phải là số dương không
        N = int(user_input)
        break
    else:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")

# Gọi hàm và in danh sách số nguyên tố
primes = list_prime(N)
if primes:
    print(f"Các số nguyên tố từ 2 tới {N} là: {primes}")
else:
    print("Không có số nguyên tố nào trong khoảng từ 2 tới N.")
