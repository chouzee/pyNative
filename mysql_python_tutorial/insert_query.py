import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                            VALUES
                            (10, 'Lenovo ThinkPad P71', 6459, '2019-08-14')"""

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print(f"Failed to insert record into Laptop table {error}")

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
