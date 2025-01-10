import random

# Kích thước ma trận
n = 12

# Tạo ma trận vuông cấp n
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

# Tạo vector v_chinh: phần tử trên đường chéo chính
v_chinh = [matrix[i][i] for i in range(n)]

# Tạo vector v_phu: phần tử trên đường chéo phụ
v_phu = [matrix[i][n - 1 - i] for i in range(n)]

# Hiển thị ma trận
print("Ma trận vuông cấp {}:".format(n))
for row in matrix:
    print(row)

# Hiển thị kết quả
print("\nVector v_chinh (đường chéo chính):", v_chinh)
print("Vector v_phu (đường chéo phụ):", v_phu)
