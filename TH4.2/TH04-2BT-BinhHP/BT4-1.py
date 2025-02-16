import numpy as np

file_path = 'D:/Documents/DHCNDA/Python/Class/TH4.2/TH04-2BT-BinhHP/temp.txt'

try:
    # Đọc dữ liệu với dấu cách làm dấu phân cách
    data_numpy = np.loadtxt(file_path, delimiter=' ')

    # Lấy thông tin về kích thước, số chiều, kiểu dữ liệu và số phần tử
    shape = data_numpy.shape
    ndim = data_numpy.ndim
    dtype = data_numpy.dtype
    size = data_numpy.size

    # In các thông tin
    print(f"Kích thước của data_numpy: {shape}")
    print(f"Số chiều của data_numpy: {ndim}")
    print(f"Kiểu dữ liệu của data_numpy: {dtype}")
    print(f"Số phần tử trong data_numpy: {size}")

except OSError:
    print("Không thể mở file Temp.txt. Vui lòng kiểm tra lại đường dẫn hoặc file.")
except ValueError:
    print(f"Dữ liệu trong file không hợp lệ hoặc không thể phân tích: {ValueError}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
