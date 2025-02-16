

import numpy as np

# Tạo một vector ngẫu nhiên với các số nguyên từ 1 đến 32 và có độ dài 15
a = np.random.randint(1, 33, 15)

print('Vector ban đầu:\n', a)
print('------------------------------')
# Sắp xếp vector a tăng dần
a_sort = np.sort(a)

# Sắp xếp vector a giảm dần:
# 1) Lật vector a_sort để sắp xếp giảm dần
b_sort = np.flip(a_sort)
# 2) Sử dụng -np.sort(-x)
b_sort = -np.sort(-a)

print('Vector sắp xếp tăng dần:\n', a_sort)
print('Vector sắp xếp giảm dần:\n', b_sort)
