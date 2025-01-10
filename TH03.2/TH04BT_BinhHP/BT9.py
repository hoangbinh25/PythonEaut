f = open('D:/Documents/DHCNDA/Python/Class/TH04/test.txt', "r")

st = f.read()
st1 = f.read(15)

print(st)
print(st1, ' Số ký tự là: ', len(st1))

