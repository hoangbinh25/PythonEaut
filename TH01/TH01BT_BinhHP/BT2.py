from datetime import datetime

current_year = datetime.now().year

name = input("Nhập họ và tên: ")
dob = int(input("Nhập năm sinh: "))

age = current_year - dob

nameConvert = name.strip().upper()

print(f"Bạn \"{nameConvert}\" năm nay {age} tuổi.")