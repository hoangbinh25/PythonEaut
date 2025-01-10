fo = open('data.txt', 'w')

fo.write('Tobe or not tobe. \n Nghi lon de thanh cong ! \n')

fo.close()
print("Ghi file thanh cong")

obj = open('test.txt', 'w')
obj.write('Chao mung cac ban den voi khoa CNTT')
obj.close()
obj1 = open('test.txt', 'r')
s = obj1.read()
print(s)
obj1.close()
obj2 = open('test.txt', 'r')
s1 = obj2.read(20)
print(s1)
obj2.close()