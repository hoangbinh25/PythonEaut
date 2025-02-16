import pandas as pd

# Đường dẫn file CSV
file_path = "D:/Documents/DHCNDA/Python/Class/TH06/TH06VD-BinhHP/data.csv" 

# Đọc dữ liệu từ file CSV với cột đầu tiên làm index
data3 = pd.read_csv(file_path,
                    names=['ID','Sex','H(cm)','W(kg)'],
                    skiprows=5)

# Hiển thị thông tin về dữ liệu
data3.info()

# Hiển thị 5 dòng đầu tiên
data3.head()
