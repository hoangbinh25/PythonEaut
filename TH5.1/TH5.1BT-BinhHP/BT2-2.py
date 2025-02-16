import numpy as np

# Vector chiều cao ban đầu (đơn vị: cm)
v_height = np.array([174, 189, 157, 149, 189, 147, 154, 174, 169, 159])

# Chuyển đổi đơn vị từ cm sang m
v_height_m = v_height / 100

# Tính bình phương giá trị các phần tử (đơn vị: m^2)
v_height_m2 = np.square(v_height_m)

print('Vector v_height:', v_height)
print('Vector v_height_m2:', v_height_m2)
