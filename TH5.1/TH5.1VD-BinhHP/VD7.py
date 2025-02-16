import numpy as np

# Tạo một ma trận 2D
a1_2d = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])

# In ma trận
print('Matrix:\n', a1_2d)   

print('a) ravel by row (default order=\'C\')')
print(a1_2d.ravel())

print('\n b) ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))