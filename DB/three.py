import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="shop"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS user (uid INT AUTO_INCREMENT PRIMARY KEY, mobile VARCHAR(10), passkey VARCHAR(50), date DATE)")
mycursor.execute("CREATE TABLE IF NOT EXISTS product (pid INT AUTO_INCREMENT PRIMARY KEY, pname VARCHAR(50))")
mycursor.execute("CREATE TABLE IF NOT EXISTS orders (oid INT AUTO_INCREMENT PRIMARY KEY, uid INT, pid INT)")

class User:
    def __init__(self, uid=None):
        self.uid = uid
    
    def signup(self):
        mobile = input("Mobile: ")
        password = input("Password: ")
        mycursor.execute("INSERT INTO user (mobile, passkey, date) VALUES (%s, %s, CURDATE())", (mobile, password))
        mydb.commit()
        print("Signup done!")
    
    def signin(self):
        mobile = input("Mobile: ")
        password = input("Password: ")
        mycursor.execute("SELECT uid FROM user WHERE mobile=%s AND passkey=%s", (mobile, password))
        result = mycursor.fetchone()
        if result:
            self.uid = result[0]
            print("Login OK!")
            return True
        print("Wrong details!")
        return False
    
    def view_products(self):
        mycursor.execute("SELECT * FROM product")
        print("Products:", mycursor.fetchall())
    
    def view_orders(self):
        if not self.uid:
            print("Login first!")
            return
        mycursor.execute("SELECT o.oid, p.pname FROM orders o JOIN product p ON o.pid=p.pid WHERE uid=%s", (self.uid,))
        print("Your orders:", mycursor.fetchall())
    
    def place_order(self):
        if not self.uid:
            print("Login first!")
            return
        self.view_products()
        pid = int(input("Product ID: "))
        mycursor.execute("INSERT INTO orders (uid, pid) VALUES (%s, %s)", (self.uid, pid))
        mydb.commit()
        print("Order placed!")

# use
user = User()
print("1. Signup")
print("2. Signin")
print("3. View products") 
print("4. View orders")
print("5. Place order")

while True:
    choice = input("Choose: ")
    if choice == '1':
        user.signup()
    elif choice == '2':
        user.signin()
    elif choice == '3':
        user.view_products()
    elif choice == '4':
        user.view_orders()
    elif choice == '5':
        user.place_order()
    else:
        break

mydb.close()
