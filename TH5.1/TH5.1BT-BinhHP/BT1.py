import numpy as np

# Tạo vector a gồm 30 phần tử, giá trị tăng dần từ 1 đến 30
a = np.arange(1, 31)
print('Vector a:\n', a)

# Chia vector a thành 3 vector con
# a_le: chứa các phần tử là số lẻ
a_le = a[a % 2 != 0]
# a_chan: chứa các phần tử là số chẵn
a_chan = a[a % 2 == 0]
# a_3: chứa các phần tử chia hết cho 3
a_3 = a[a % 3 == 0]

print('Vector a_le:', a_le)
print('Vector a_chan:', a_chan)
print('Vector a_3:', a_3)
