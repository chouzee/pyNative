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


def get_hospital_name(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


def get_doctors(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_query = """select * from Doctor where Hospital_id = %s"""
        cursor.execute(sql_query, (hospital_id,))
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

get_doctors(2)
