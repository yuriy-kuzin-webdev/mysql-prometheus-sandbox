import mysql.connector
from mysql.connector import Error
import time

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='mysql',
            database='test',
            user='sample',
            password='password',
            port=3306
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def insert_data(connection, cursor):
    query = "INSERT INTO sample_table (name, age) VALUES (%s, %s)"
    values = ("John", 30)
    cursor.execute(query, values)
    connection.commit()
    print(f"Inserted: {cursor.rowcount} row(s)")

def read_data(cursor):
    query = "SELECT * FROM sample_table"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Reading data from database:")
    for row in rows:
        print(row)

def update_data(connection, cursor):
    query = "UPDATE sample_table SET age = %s WHERE name = %s"
    values = (35, "John")
    cursor.execute(query, values)
    connection.commit()
    print(f"Updated: {cursor.rowcount} row(s)")

def delete_data(connection, cursor):
    query = "DELETE FROM sample_table WHERE name = %s"
    values = ("John",)
    cursor.execute(query, values)
    connection.commit()
    print(f"Deleted: {cursor.rowcount} row(s)")

def simulate_operations():
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sample_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT
    );
    """)

    try:
        while True:
            print("\n----- Loop Start -----")
            insert_data(connection, cursor)   
            read_data(cursor)                 
            update_data(connection, cursor)   
            read_data(cursor)                
            delete_data(connection, cursor)   
            read_data(cursor)             
            print("----- Loop End -----\n")
            
            # time.sleep(5)
    except KeyboardInterrupt:
        print("Stopped the simulation.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    simulate_operations()
