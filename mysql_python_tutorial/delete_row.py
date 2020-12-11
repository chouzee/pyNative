import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor()
    print("Displaying laptop record Before Deleting it")
    sql_select_query = """select * from Laptop where id = 7"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_delete_query = """Delete from Laptop where id = 7"""
    cursor.execute(sql_delete_query)
    connection.commit()

    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nRecord Deleted successfully ")

except mysql.connector.Error as Error:
    print(f"Failed to delete record from table: {error}")
finally:
    if (connection.is_connected()):
        cursor.close()
        print("MySQL connection is closed")
