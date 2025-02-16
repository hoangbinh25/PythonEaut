import random

n = 12

# Tạo ma trận vuông cấp n
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

# Hiển thị ma trận
print("Ma trận vuông cấp {}:".format(n))
for row in matrix:
    print(row)

# Nhập giá trị x từ người dùng
x = int(input("\nNhập một số nguyên x trong khoảng (0-100): "))
if x < 0 or x > 100:
    print("Giá trị x phải trong khoảng 0-100!")
else:
    # Đếm số phần tử bằng, lớn hơn và nhỏ hơn x
    count_equal = sum(1 for row in matrix for elem in row if elem == x)
    count_greater = sum(1 for row in matrix for elem in row if elem > x)
    count_smaller = sum(1 for row in matrix for elem in row if elem < x)

    # Hiển thị kết quả
    print("\nKết quả:")
    print(f"Số phần tử bằng {x}: {count_equal}")
    print(f"Số phần tử lớn hơn {x}: {count_greater}")
    print(f"Số phần tử nhỏ hơn {x}: {count_smaller}")
