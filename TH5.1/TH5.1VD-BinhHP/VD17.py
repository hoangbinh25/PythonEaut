import numpy as np

x = np.array([-2, -1, 0, 1, 2])
print(x)
print('------------------')
print(np.abs(x))
print(np.absolute(x))

print('################################')

theta = np.linspace(0, np.pi, 3)
print("theta =", theta)
print('------------------')
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
