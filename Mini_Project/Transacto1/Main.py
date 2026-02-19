import mysql.connector
import uuid
from config import *
from account import Account


class BankApp:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.current = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB,
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print("Database connection failed:", e)

    def create_table(self):
        try:
            self.cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS accounts (
                id VARCHAR(8) PRIMARY KEY,
                balance DECIMAL(10,2) DEFAULT 0,
                name VARCHAR(30)
            )
            """
            )
            self.conn.commit()
        except mysql.connector.Error as e:
            print("Table creation error:", e)

    def list_accounts(self):
        try:
            self.cursor.execute("SELECT * FROM accounts")
            rows = self.cursor.fetchall()
            if not rows:
                print("No accounts found")
                return
            for r in rows:
                print(f"{r[0]} | ₹{float(r[1]):.2f} | {r[2]}")
        except mysql.connector.Error as e:
            print("List error:", e)

    def create_account(self):
        try:
            name = input("Enter name: ").strip()
            if not name:
                print("Name cannot be empty")
                return

            acc_id = str(uuid.uuid4())[:8]
            self.cursor.execute(
                "INSERT INTO accounts VALUES (%s,%s,%s)", (acc_id, 0, name)
            )
            self.conn.commit()
            print("Account created:", acc_id)

        except mysql.connector.Error as e:
            print("Create error:", e)

    def select_account(self):
        try:
            acc_id = input("Enter ID: ").strip()
            self.cursor.execute("SELECT * FROM accounts WHERE id=%s", (acc_id,))
            r = self.cursor.fetchone()

            if r:
                self.current = Account(r[0], r[1], r[2])
                print("Selected:", self.current.id)
            else:
                print("Account not found")

        except mysql.connector.Error as e:
            print("Select error:", e)

    def deposit_money(self):
        if not self.current:
            print("Select account first")
            return

        try:
            amt = input("Enter amount: ")
            msg = self.current.deposit(amt)
            print(msg)

            if "Deposited" in msg:
                self.cursor.execute(
                    "UPDATE accounts SET balance=%s WHERE id=%s",
                    (self.current.balance, self.current.id),
                )
                self.conn.commit()

        except mysql.connector.Error as e:
            print("Deposit DB error:", e)

    def withdraw_money(self):
        if not self.current:
            print("Select account first")
            return

        try:
            amt = input("Enter amount: ")
            msg = self.current.withdraw(amt)
            print(msg)

            if "Withdrew" in msg:
                self.cursor.execute(
                    "UPDATE accounts SET balance=%s WHERE id=%s",
                    (self.current.balance, self.current.id),
                )
                self.conn.commit()

        except mysql.connector.Error as e:
            print("Withdraw DB error:", e)

    def delete_account(self):
        if not self.current:
            print("Select account first")
            return

        try:
            confirm = input(f"Delete {self.current.id}? (y/n): ")
            if confirm.lower() != "y":
                return

            self.cursor.execute("DELETE FROM accounts WHERE id=%s", (self.current.id,))
            self.conn.commit()

            if self.cursor.rowcount:
                print("Account deleted")
                self.current = None
            else:
                print("Delete failed")

        except mysql.connector.Error as e:
            print("Delete error:", e)

    def menu(self):
        print("\n1 List")
        print("2 Create")
        print("3 Select")
        print("4 Deposit")
        print("5 Withdraw")
        print("6 Delete")
        print("0 Exit")
        return input("Choice: ")

    def run(self):
        while True:
            ch = self.menu()

            if ch == "1":
                self.list_accounts()

            elif ch == "2":
                self.create_account()

            elif ch == "3":
                self.select_account()

            elif ch == "4":
                self.deposit_money()

            elif ch == "5":
                self.withdraw_money()

            elif ch == "6":
                self.delete_account()

            elif ch == "0":
                break

            else:
                print("Invalid choice")

        self.close()

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except:
            pass


if __name__ == "__main__":
    app = BankApp()
    app.run()
