def all_ab(a, b):
    add = a + b
    sub = a - b
    multi = a * b
    div = a / b
    return add, sub, multi, div

a = 10
b = 6
add, sub, multi, div = all_ab(a, b)

print('Tong ', a, '+', b, '=', add)
print('Hieu ', a, '-', b, '=', sub)
print('Tich ', a, '*', b, '=', multi)
print('Thuong ', a, '/', b, '=', div)
