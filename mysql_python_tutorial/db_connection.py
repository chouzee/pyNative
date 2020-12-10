import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29',
                                         connection_timeout=180)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL server version ", db_Info)
        cursor = connection.cursor()

        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)

        connection.commit()

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
