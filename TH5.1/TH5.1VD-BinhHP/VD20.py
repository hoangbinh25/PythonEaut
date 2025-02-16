import numpy as np

arr = np.array([20.8999, 67.89899, 54.43409])

print(arr)
print('-----------------------------')
# 1) Làm tròn tới 1 số sau dấu phẩy
print(np.around(arr, 1))

# 2) Làm tròn tới 2 số sau dấu phẩy
print(np.around(arr, 2))

# 3) Làm tròn xuống số nguyên gần nhất
print(np.floor(arr))

# 4) Làm tròn lên số nguyên gần nhất
print(np.ceil(arr))
