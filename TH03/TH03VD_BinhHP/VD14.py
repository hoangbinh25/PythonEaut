x = 300
y = 800
def myfunc():
    x = 200
    total = x + y
    print('(Local) x :', x)
    print('Total :', total)

myfunc()

print('---------------------')
print('(global) x:', x)

def myfunc2():
    global k
    k = 200
    print('Inside func: k = ', k)

myfunc2()

print('---------------------')
print('Outside func: k =', k)
