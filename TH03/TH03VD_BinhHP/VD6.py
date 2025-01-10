def giai_thua(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

n = int(input('Nhập vào một số nguyên N: '))
print(n, '!=', giai_thua(n))