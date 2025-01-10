import numpy as np

diem_2a =  [[6, 7, 9, 5, 10],
    [7, 8, 6, 9, 8],
    [9, 5, 8, 10, 7],
    [6, 8, 7, 9, 9],
    [7, 9, 8, 7, 9],
    [8, 7, 8, 9, 7]]

print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0][0])  # Phần tử (0,0)
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[1][1])       # Phần tử (1,1)
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1][-1]) # Phần tử (-1,-1)
print('----------------------------------------------------------------')
print('Bảng điểm lớp 2A \n', diem_2a)