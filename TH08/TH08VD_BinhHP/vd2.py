import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "123456") 
    
# in đối tượng connection ra màn hình 
print(myconn) 