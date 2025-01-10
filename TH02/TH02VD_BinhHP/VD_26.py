while True:
    n = int(input( 'Em sinh tháng mấy: '))
    if (1 <= n <= 12):
        break
    print( 'Tháng không đúng, vui lòng nhập lại' )

print( 'Chào em cô gái tháng ', n)