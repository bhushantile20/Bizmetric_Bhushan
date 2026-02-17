from config import get_db
from datetime import datetime
def input_number(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Invalid number")

def input_text(msg):
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Value required")

def query(sql, params=(), fetch=False, one=False):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, params)

    data = None
    if fetch:
        data = cur.fetchone() if one else cur.fetchall()

    conn.commit()
    conn.close()
    return data

def add_customer():
    name = input_text("Name: ")
    mobile = input_text("Mobile: ")
    query("INSERT INTO customer(name, mobile) VALUES (?, ?)", (name, mobile))
    print("Customer added")

def add_product():
    name = input_text("Product: ")
    price = input_number("Price: ")
    query("INSERT INTO product_details(product_name, price) VALUES (?, ?)", (name, price))
    print("Product added")

def show_customers():
    rows = query("SELECT * FROM customer", fetch=True)
    if not rows:
        print("No customers")
        return
    for r in rows:
        print(r.customer_id, r.name, r.mobile)

def show_products():
    rows = query("SELECT * FROM product_details", fetch=True)
    if not rows:
        print("No products")
        return
    for r in rows:
        print(r.product_id, r.product_name, r.price)

def place_order():
    show_customers()
    cid = input_number("Customer ID: ")

    show_products()
    pid = input_number("Product ID: ")

    qty = input_number("Quantity: ")

    query("INSERT INTO order_details(customer_id, product_id, quantity) VALUES (?, ?, ?)", (cid, pid, qty))
    print("Order placed")

def print_bill():
    oid = input_number("Order ID: ")

    row = query("""
        SELECT c.name, p.product_name, p.price, o.quantity
        FROM order_details o
        JOIN customer c ON o.customer_id = c.customer_id
        JOIN product_details p ON o.product_id = p.product_id
        WHERE o.order_id = ?
    """, (oid,), fetch=True, one=True)

    if not row:
        print("Order not found")
        return

    total = row.price * row.quantity

    print("\n--- BILL ---")
    print("Customer :", row.name)
    print("Product  :", row.product_name)
    print("Qty      :", row.quantity)
    print("Price    :", row.price)
    print("Total    :", total)

    if input_text("Complete transaction (yes/no): ").lower() == "yes":
        query("INSERT INTO transaction_details(order_id, total_amount, transaction_date) VALUES (?, ?, ?)",(oid, total, datetime.now()))
        print("Transaction saved")
    else:
        print("Cancelled")
