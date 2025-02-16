import numpy as np

A = np.array([[8, 27, 2, 8, 3, 26],
              [7, 16, 19, 23, 19, 21],
              [14, 10, 3, 9, 5, 9],
              [29, 27, 19, 27, 29, 29],
              [4, 14, 10, 4, 23, 4]])

print('Ma trận A:\n', A)

#a) 
a_sort1 = np.sort(A, axis=0)
print('Ma trận 1:\n', a_sort1)


a_sort2 = np.sort(A, axis=1)
print('Ma trận 2:\n', a_sort2)

a_sort3 = np.sort(A, axis=None)
print('Vector:\n', a_sort3)

a_sort3_reshaped = np.sort(A, axis=None).reshape(A.shape[0], A.shape[1])
print('Ma trận 3:\n', a_sort3_reshaped)
