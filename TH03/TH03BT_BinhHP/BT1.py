from datetime import datetime

def greeting(name, dob):
    
    current_year = datetime.now().year
    age = current_year - dob

    return print(f"Bạn \"{name}\" năm nay {age} tuổi.")

name = input("Nhập họ và tên: ")
dob = int(input("Nhập năm sinh: "))

result = greeting(name, dob)
print(result)