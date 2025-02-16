import numpy as np

a = np.array([[ 1,  3,  1,  4],
              [ 3,  9,  5, 15],
              [ 0,  2,  1,  1],
              [ 0,  4,  2,  3]])

print('Ma trận a:\n', a)
det_a = np.linalg.det(a)
print('det(a) = ', det_a)

b = np.array([[ 1,  2,  3,  4],
              [-2, -1,  4,  1],
              [ 3, -4, -5,  6],
              [ 1,  2,  3,  4]])

print('Ma trận b:\n', b)
det_b = np.linalg.det(b)
print('det(b) = ', det_b)
