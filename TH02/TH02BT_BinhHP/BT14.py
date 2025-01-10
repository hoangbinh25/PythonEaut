# Khởi tạo dãy số chiều cao của sinh viên
heights = [170, 160, 175, 180, 165, 155, 172, 168, 178, 185] 

# 1) Hiển thị chiều cao của sinh viên cao nhất và thấp nhất trong lớp
max_height = max(heights)
min_height = min(heights)
print(f"Chiều cao cao nhất trong lớp là: {max_height} cm")
print(f"Chiều cao thấp nhất trong lớp là: {min_height} cm")

# 2) Tính chiều cao trung bình của sinh viên trong lớp
average_height = sum(heights) / len(heights)
print(f"Chiều cao trung bình của sinh viên trong lớp là: {average_height:.2f} cm")

# 3) Số lượng sinh viên có chiều cao lớn hơn hoặc bằng chiều cao trung bình
count_above_average = len([height for height in heights if height >= average_height])
print(f"Số lượng sinh viên có chiều cao lớn hơn hoặc bằng chiều cao trung bình là: {count_above_average}")
