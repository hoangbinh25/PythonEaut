n = int(input("Nhập số kẹo của cô: "))
m = int(input("Nhấp số học sinh trong lớp: "))

if m == 0:
    print("Lỗi. Không có học sinh nào để chia kẹo")
else:
    candyForStudent = n // m
    candy = n % m

if candyForStudent == 0:
    print(f"Số kẹo ({n}) ít hơn số học sinh ({m}), mỗi học sinh không nhận được kẹo.")
    print(f"Số kẹo còn dư: {candy}")
else:
    print(f"Mỗi học sinh nhận được {candyForStudent} kẹo.")
    print(f"Cô còn lại {candy} cái kẹo.")
