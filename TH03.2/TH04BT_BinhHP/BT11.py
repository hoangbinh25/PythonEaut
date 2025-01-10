f1 = open('Ghifile.txt', 'a+')

st = 'This is new line ...'

f1.write(st)
f1.close()

f = open('Ghifile.txt', "r")
print(f.read())