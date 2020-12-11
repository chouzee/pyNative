import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')


    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Name = %s, Price = %s where id = %s"""

    name = "HP Pavilion"
    price = 2200
    id = 4
    input = (name, price, id)

    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Multiple column updated successfully ")

except mysql.connector.Error as error:
    print(f"Failed to update record to database: {error}")

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
