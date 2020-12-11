import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Price = %s where id = %s"""
    records_to_update = [(3000, 3), (2750, 4)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()

    print(cursor.rowcount, "Records of a Laptop table updated successfully")

except mysql.connector.Error as error:
    print(f"Failed to update records to database: {error}")
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
