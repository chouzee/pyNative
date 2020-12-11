import mysql.connector
from mysql.connector import Error

def updateLaptopPrice(id, price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='pynative',
                                             password='pynative@#29')

        cursor = connection.cursor()
        sql_update_query = """Update Laptop set price = %s where id = %s"""
        inputData = (price, id)
        cursor.execute(sql_update_query, inputData)
        connection.commit()
        print("record Updated successfully")


    except mysql.connector.Error as error:
        print(f"Failed to update record to database: {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


updateLaptopPrice(7500, 2)
updateLaptopPrice(5000, 3)
