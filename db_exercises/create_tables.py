import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')

    mysql_create_table_hospital = """CREATE TABLE Hospital (
                                         Hospital_Id INT UNSIGNED NOT NULL,
                                         Hospital_Name TEXT NOT NULL,
                                         Bed_count INT,
                                         PRIMARY KEY (Hospital_Id)
                                         );"""

    mysql_create_table_doctor = """CREATE TABLE Doctor (
                                         Doctor_Id INT UNSIGNED NOT NULL,
                                         Doctor_Name TEXT NOT NULL, 
                                         Hospital_Id INT NOT NULL, 
                                         Joining_Date DATE NOT NULL, 
                                         Speciality TEXT NULL, 
                                         Salary INT NULL, 
                                         Experience INT NULL, 
                                         PRIMARY KEY (Doctor_Id)
                                         );"""

    cursor = connection.cursor()
    hospital = cursor.execute(mysql_create_table_hospital)
    doctor = cursor.execute(mysql_create_table_doctor)
    print("Hospital and Doctor tables created succsessfully")

except mysql.conector.Error as error:
    print(f"Failed to create tables in MySQL: {error}")
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
