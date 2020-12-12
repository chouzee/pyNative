import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_query = """select * from Doctor where Speciality = %s and Salary > %s"""
        cursor.execute(sql_query, (speciality, salary))
        record = cursor.fetchall()
        for row in record:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Speciality:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except mysql.connector.Error as error:
        print(f"Failed to get recotd from table: {error}")

get_specialist_doctors_list("Garnacologist", 30000)
