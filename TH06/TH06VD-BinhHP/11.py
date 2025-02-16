import pandas as pd

# Đường dẫn file CSV
path = "D:/Documents/DHCNDA/Python/Class/TH06/TH06VD-BinhHP/data.csv" 

# Đọc dữ liệu từ file CSV
data = pd.read_csv(path)

# Hiển thị thông tin về dữ liệu
data.info()

