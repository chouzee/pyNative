import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def insert_vars_into_table(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='pynative',
                                             password='pynative@#29')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                                VALUES
                                (%s, %s, %s, %s)"""

        recordTuple = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print(f"Failed to insert record into Laptop table {error}")

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insert_vars_into_table(2, 'Area 51M', 6999, '2019-04-14')
insert_vars_into_table(3, 'MacBook Pro', 2499, '2019-06-20')
