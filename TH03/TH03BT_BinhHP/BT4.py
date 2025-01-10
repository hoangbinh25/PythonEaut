def bmi_show(height, weight):
    if height > 0 and weight > 0:
        # Tính chỉ số BMI
        bmi = weight / (height ** 2)

        # Hiển thị chỉ số BMI
        print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

        # Đưa ra nhận xét dựa trên BMI
        if bmi < 18.5:
            print("Nhận xét: Bạn gầy.")
        elif 18.5 <= bmi < 24.9:
            print("Nhận xét: Bạn bình thường.")
        elif 25 <= bmi < 29.9:
            print("Nhận xét: Bạn thừa cân.")
        else:
            print("Nhận xét: Bạn béo phì.")
    else:
        print("Chiều cao và cân nặng phải lớn hơn 0.")

try:
    height = float(input("Nhập chiều cao (m): "))
    weight = float(input("Nhập cân nặng (kg): "))
    bmi_show(height, weight)
except ValueError:
    print("Vui lòng nhập số hợp lệ cho chiều cao và cân nặng.")

