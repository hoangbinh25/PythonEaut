import numpy as np

# Vector BMI giả định (bạn nên sử dụng vector BMI từ dữ liệu thực của bạn)
v_bmi = np.array([31.7, 24.4, 22.1, 27.4, 25.7, 25.4, 29.5, 26.4, 29.8, 25.6, 
                  12.8, 13.9, 14.8, 15.6, 16.4, 17.1, 17.4, 17.7, 18.1, 19.5])

# Xác định các nhóm BMI
underweight = v_bmi[v_bmi < 18.5]
normal = v_bmi[(v_bmi >= 18.5) & (v_bmi < 25)]
overweight = v_bmi[(v_bmi >= 25) & (v_bmi < 30)]
obese = v_bmi[(v_bmi >= 30) & (v_bmi < 35)]
extremely_obese = v_bmi[v_bmi >= 35]

# Tính số lượng người trong mỗi nhóm
num_underweight = underweight.size
num_normal = normal.size
num_overweight = overweight.size
num_obese = obese.size
num_extremely_obese = extremely_obese.size

# Tổng số lượng người
total_people = v_bmi.size

print('Tổng số người:', total_people)
print('1. Underweight:', num_underweight)
print('2. Normal:', num_normal)
print('3. Overweight:', num_overweight)
print('4. Obese:', num_obese)
print('5. Extremely Obese:', num_extremely_obese)
