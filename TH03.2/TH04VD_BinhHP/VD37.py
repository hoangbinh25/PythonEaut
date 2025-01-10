f = open('test.txt', "r")

st = f.read()
st1 = f.read(5)

print(st)
print(st1, ' Số ký tự là: ', len(st1))

