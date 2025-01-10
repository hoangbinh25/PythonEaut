import numpy as np

a_float = np.linspace(0, 15, 11)

print(a_float)
print('Kiểu dữ liệu: ', a_float.dtype)
print('----------------------------------------------------------------')

a_int = a_float.astype(int)
print(a_int)
print('Dữ liệu sau khi chuyển: ', a_int.dtype)

a_str = a_int.astype(np.str_)
print(a_str)
print('Dữ liệu sau khi chuyển: ', a_str.dtype)
print('----------------------------------------------------------------')

a_bol = a_int.astype(np.bool)
print(a_bol)
print('Dữ liệu sau khi chuyển: ', a_bol.dtype)
