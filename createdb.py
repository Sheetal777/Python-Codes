import mysql.connector 

# Connecting
connect = mysql.connector.connect(user = 'username', 
                               host = 'localhost', 
                              database = 'databse_name')   
print(connect) 
  
# Disconnecting
connect.close() 
