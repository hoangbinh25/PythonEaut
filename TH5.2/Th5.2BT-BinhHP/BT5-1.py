import numpy as np

# Khởi tạo ma trận Height và Weight
height = np.array([[174, 195, 157, 153, 175, 168, 191, 153, 164, 178],
                   [189, 159, 153, 178, 149, 176, 141, 178, 166, 183],
                   [185, 129, 160, 174, 179, 176, 145, 176, 166, 193],
                   [195, 155, 159, 160, 161, 170, 161, 153, 165, 177],
                   [189, 153, 151, 181, 163, 168, 153, 168, 164, 179],
                   [147, 157, 153, 178, 149, 176, 141, 178, 166, 183],
                   [185, 129, 160, 174, 179, 176, 145, 176, 166, 193],
                   [174, 144, 163, 171, 161, 164, 164, 159, 195, 0],
                   [169, 172, 179, 185, 194, 193, 181, 185, 190, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

weight = np.array([[ 96,  87, 110, 121, 120, 135, 54, 51, 75, 154],
                   [ 81,  80, 149,  52, 108,  54, 143, 117, 140,  96],
                   [110, 101,  97, 156, 111, 108, 105, 111, 105,  74],
                   [104,  51, 139, 131, 115,  83,  75, 118,  61,   0],
                   [ 92, 115,  94, 122,  96, 104, 154, 150, 145, 139],
                   [ 91,  94, 125,  72,  78, 120, 124,  69,   0,   0],
                   [103, 139, 152,  81, 152, 140,  50,   0,   0,   0],
                   [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   1],
                   [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   1],
                   [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   1]])

# Tính ma trận nghịch đảo và hạng của ma trận Height
if np.linalg.det(height) != 0:
    height_inv = np.linalg.inv(height)
    height_rank = np.linalg.matrix_rank(height)
    print("Ma trận nghịch đảo Height:\n", height_inv)
    print("Hạng của ma trận Height:", height_rank)
else:
    print("Ma trận Height không có ma trận nghịch đảo.")

# Tính ma trận nghịch đảo và hạng của ma trận Weight
if np.linalg.det(weight) != 0:
    weight_inv = np.linalg.inv(weight)
    weight_rank = np.linalg.matrix_rank(weight)
    print("Ma trận nghịch đảo Weight:\n", weight_inv)
    print("Hạng của ma trận Weight:", weight_rank)
else:
    print("Ma trận Weight không có ma trận nghịch đảo.")
