import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (not to a specific database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bunny@9999"  # 🔁 Replace with your real password
    )

    cursor = connection.cursor()

    # Try to create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    # Close cursor and connection if they exist
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

