import numpy as np

# Giả sử bạn đã có ma trận weight
weight = np.array([[  0,  87, 110, 104,  61, 104,  92, 111,  90, 103],
                   [  0,   0, 101,  51,  79, 107, 112, 129, 145, 139],
                   [  0,   0,   0,  91,  96, 110, 124, 149, 153,   0],
                   [  0,   0,   0,   0, 153, 132, 114,  85,  82,   0],
                   [  0,   0,   0,   0,   0,  92, 127,  78,  94,   0],
                   [  0,   0,   0,   0,   0,   0,  72, 140,  61,   0],
                   [  0,   0,   0,   0,   0,   0,   0, 127,  70,   0],
                   [  0,   0,   0,   0,   0,   0,   0,   0, 140,   0],
                   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]])

# Tìm giá trị lớn nhất của ma trận đường chéo trên (không bao gồm đường chéo chính)
upper_triangular = np.triu(weight, k=1)
max_upper = np.max(upper_triangular)

# Tìm giá trị lớn nhất của ma trận đường chéo dưới (không bao gồm đường chéo chính)
lower_triangular = np.tril(weight, k=-1)
max_lower = np.max(lower_triangular)

print("Giá trị lớn nhất của ma trận đường chéo trên (không bao gồm đường chéo chính):", max_upper)
print("Giá trị lớn nhất của ma trận đường chéo dưới (không bao gồm đường chéo chính):", max_lower)
