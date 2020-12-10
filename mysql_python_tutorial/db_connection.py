import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL server version ", db_Info)
        cursor = connection.cursor()
        # cursor.execute()  SQL queries from Python
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        # close cursor object
        cursor.close()
        # close db connection
        connection.close()
        print("MySQL connection is closed")
