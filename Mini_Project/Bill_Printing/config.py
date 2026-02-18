import mysql.connector

server = "localhost"
database = "BillingDB"
username = "root"
password = "root"

def get_db():
    return mysql.connector.connect(
        host=server, database=database, user=username, password=password
    )
