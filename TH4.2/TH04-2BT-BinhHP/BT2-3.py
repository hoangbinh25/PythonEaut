import numpy as np

# Bảng điểm của học sinh trong lớp
scores = np.array([
    [7, 10, 9, 8, 7, 10, 10, 8, 9, 8],
    [5, 1, 0, 10, 4, 7, 1, 8, 1, 7],
    # Thêm các học sinh khác vào đây
])

# Tính độ lệch chuẩn của mỗi học sinh
student_std = np.std(scores, axis=1)

# Sinh viên có điểm đồng đều nhất và lệch nhất
most_consistent_student = np.argmin(student_std)
most_varied_student = np.argmax(student_std)

print(f"Sinh viên có điểm đồng đều nhất: {most_consistent_student}")
print(f"Sinh viên có điểm lệch nhất: {most_varied_student}")

# Tính độ lệch chuẩn của mỗi môn học
subject_std = np.std(scores, axis=0)

# Môn học có điểm đồng đều nhất và chênh lệch nhất
most_consistent_subject = np.argmin(subject_std)
most_varied_subject = np.argmax(subject_std)

print(f"Môn học có điểm đồng đều nhất: {most_consistent_subject}")
print(f"Môn học có điểm chênh lệch nhất: {most_varied_subject}")
