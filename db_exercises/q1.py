# First step is to create db CREATE database and user
# Check db connection
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')

    if (connection.is_connected()):
        db_Info = connection.get_server_info()
        print("Connected to MySQL server ", db_Info)

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
