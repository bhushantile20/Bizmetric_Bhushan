import pyodbc

SERVER = r"BT\\SQLEXPRESS"  # Change to your server name
DATABASE = "BillingDB"

def get_db():
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"Trusted_Connection=yes;"
    )
