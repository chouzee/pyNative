import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor()
    delete_table_query = """DROP TABLE Laptop"""
    cursor.execute(delete_table_query)

    delete_database_query = """DROP DATABASE Electronics"""
    cursor.execute(delete_database_query)
    connection.commit()
    print("Table and Database deleted successfully")

except mysql.connector.Error as error:
    print(f"Failed to delete table and database: {error}")
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
