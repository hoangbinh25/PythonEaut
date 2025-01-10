def rabbit_count(n):
    so_tho = 2 * (2 ** n)
    return print(f"Trong rừng có: {so_tho} con thỏ.")
 
n = int(input("Nhập vào số tháng n: "))
result = rabbit_count(n)
