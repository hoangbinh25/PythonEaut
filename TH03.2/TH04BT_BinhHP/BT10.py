# Mở file để đọc dữ liệu
f = open('test.txt')

# Đọc từng dòng dữ liệu của file
# print(f.readline())
# print(f.readline())

for x in f:
    print(x)

# Đóng file dữ liệu
f.close()