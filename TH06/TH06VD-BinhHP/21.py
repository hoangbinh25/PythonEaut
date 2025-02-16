import pandas as pd

# Đường dẫn tới file Excel
file_path = "D:/Documents/DHCNDA/Python/Class/TH06/TH06VD-BinhHP/Data_Exercise/Data_Exercise/Data_Excel.xlsx"  

# Đọc dữ liệu từ file Excel
data = pd.read_excel(file_path)

# Hiển thị 5 dòng đầu tiên
print(data.head())
