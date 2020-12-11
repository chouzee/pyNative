import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor()
    alter_column = """ALTER TABLE Laptop DROP COLUMN Purchase_date"""
    cursor.execute(alter_column)
    connection.commit()
    print("Column deleted successfully")

except mysql.connector.Error as error:
    print(f"Failed to delete column: {error}")
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
