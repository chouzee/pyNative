import mysql.connector
from mysql.connector import Error

def getLaptopDetail(id):
    try:
        mySQLConnection = mysql.connector.connect(host='localhost',
                                                  database='Electronics',
                                                  user='pynative',
                                                  password='pynative@#29')

        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """select * from Laptop where id = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary = ", row[3], "\n")

    except mysql.connector.Error as error:
        print(f"Failed to get record from MySQL table {error}")

    finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()
            print("MySQL connection is closed")

id1 = 2
id2 = 3

getLaptopDetail(id1)
getLaptopDetail(id2)
