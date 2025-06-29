import os
import mysql.connector

try:
    mysql_password = os.getenv('MYSQL_PASSWORD')
    
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=mysql_password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")