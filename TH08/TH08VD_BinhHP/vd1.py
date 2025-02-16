import mysql.connector 
   #Create the connection object 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "123456") 
    
#printing the connection object 
print(myconn) 