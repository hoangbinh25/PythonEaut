# Nhập ký tự từ người dùng
char = input("Nhập vào một ký tự chữ cái bất kỳ: ").lower()

# Kiểm tra ký tự có phải là chữ cái không
if char.isalpha() and len(char) == 1:
    if char in 'aeiou':  # Kiểm tra nguyên âm
        print(f"'{char}' là nguyên âm.")
    else:  # Nếu không phải nguyên âm, thì là phụ âm
        print(f"'{char}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự chữ cái hợp lệ.")
