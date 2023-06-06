import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        return mysql.connector.connect(
            host=host_name, 
            user=user_name, 
            password=user_password,
            database=db_name
        )
    except Error as e:
        print(f"The error '{e}' occurred")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = str(cursor.fetchall())
        fb = open("database.json", "w")
        fb.write(result)
        fb.close()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    connect = create_connection("127.0.0.1", "root", "ytevt.ghblevsdfnmgfhjkb", "zavod")
    query = str(input("Enter query: "))
    print(create_database(connect, query))

if __name__ == "__main__":
    main()