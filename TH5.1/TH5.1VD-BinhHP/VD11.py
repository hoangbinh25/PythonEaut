

import numpy as np

# Tạo ma trận ban đầu
A = np.array([[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]])

# Lật ngược ma trận theo cột
A1 = np.flip(A, axis=1)  # Tương đương với np.fliplr(A)
print("Lật ma trận theo cột:\n", A1)

# Lật ngược ma trận theo hàng
A2 = np.flip(A, axis=0)  # Tương đương với np.flipud(A)
print("\nLật ma trận theo hàng:\n", A2)