def giai_thua(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

# n = int(input('Nhập vào một số nguyên N: '))
# print(n, '! =', giai_thua(n))

print('12! =', giai_thua(12))

# Lỗi khi không truyền tham số
# print('12! =', giai_thua())
