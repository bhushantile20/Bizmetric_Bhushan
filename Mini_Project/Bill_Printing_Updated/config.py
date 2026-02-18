import mysql.connector

server = "localhost"
database = "BillingDB"
username = "root"
password = "root"

def get_db():
    try:
        return mysql.connector.connect(
            host=server,
            database=database,
            user=username,
            password=password
        )
    except mysql.connector.Error as e:
        print("Database connection failed:", e)
        return None
