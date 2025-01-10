import numpy as np

a = np.array([1,9, 7, 2, 5, 3, 4])

print('Các phần tử của Vector a: \n', a)
print('----------------------------------------------------------------')
print('Phần tử đầu tiên: ', a[0])
print('Phần tử thứ 3: ', a[3])
print('Phần tử cuối cùng: ', a[-1])

print('----------------------------------------------------------------')
print('3 phần tử đầu tiên: ', a[:3])
print('Phần tử thứ 5 đến hết: ', a[5:])
print('Từ phần tử 2 đến phần tử 6 của vector: ', a[2:6])
