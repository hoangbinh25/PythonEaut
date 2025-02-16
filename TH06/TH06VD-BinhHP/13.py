import pandas as pd

# Đường dẫn file CSV
file_path = "D:/Documents/DHCNDA/Python/Class/TH06/TH06VD-BinhHP/data.csv"  
# Đọc dữ liệu từ file CSV với cột đầu tiên làm index
data = pd.read_csv(file_path, index_col=0)

# Hiển thị thông tin về dữ liệu
data.info()

# Hiển thị 5 dòng đầu tiên
data.head()
