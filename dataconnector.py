import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='your_host',         # e.g., 'localhost' or an IP address
            user='your_username',     # e.g., 'root'
            password='your_password', # e.g., 'password123'
            database='your_database'  # e.g., 'mydatabase'
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database:", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_mysql()