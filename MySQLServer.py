import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="omar",
    password="22082024",
    database="test"  # optional
)

try:
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")  # fixed typo
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    db.close()
