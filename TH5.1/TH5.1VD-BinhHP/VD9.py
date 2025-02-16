import numpy as np
x = np.arange(0, 6)
xy = np.arange(1, 10)

print(x)
print(xy)

x1, x2 = np.split(x, 2)
xy1, xy2, xy3 = np.split(xy, [2, 6])

print(x1, x2)
print('--------------------------------')
print(xy1, xy2, xy3)