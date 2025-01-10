import random

# Kích thước ma trận
n = 12

# Tạo ma trận vuông cấp n
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

# Hiển thị ma trận
print("Ma trận vuông cấp {}:".format(n))
for row in matrix:
    print(row)
