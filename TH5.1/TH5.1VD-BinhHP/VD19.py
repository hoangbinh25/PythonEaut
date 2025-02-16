import numpy as np

x = np.array([1, 2, 3])

print("x =", x)
print('---------------------')
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))


x = np.array([1, 2, 4, 100])

print("x =", x)
print('---------------------')
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))
