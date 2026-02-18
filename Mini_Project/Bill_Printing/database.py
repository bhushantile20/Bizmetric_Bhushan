#i done with it using the classes 

from config import get_db

def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("enter number!")

def get_text(msg):
    while True:
        val = input(msg).strip()
        if val: return val
        print("enter value!")

def db_query(sql, params=(), get_data=False):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(sql, params)

        if get_data:
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        else:
            conn.commit()
            cur.close()
            conn.close()
            
    except Exception as e:
        print(f"datnase error: {e}")

def add_cust():
    try:
        name = input("name: ")
        mobile = input("mobile: ")
        db_query("insert into customer(name, mobile) values (%s, %s)", (name, mobile))
        print("customer added!")
    except:
        print("customer add failed!")

def add_prod():
    try:
        name = input("product: ")
        price = float(input("price: "))
        db_query(
            "insert into product_details(product_name, price) values (%s, %s)",
            (name, price),
        )
        print("product added!")
    except:
        print("product add failed!")

def show_cust():
    try:
        rows = db_query("select * from customer", get_data=True)
        if not rows:
            print("no customers")
            return
        print("id  name      mobile")
        print("-" * 20)
        for r in rows:
            print(f"{r[0]}  {r[1]:<8} {r[2]}")
    except:
        print("show customers failed!")


def show_prod():
    try:
        rows = db_query("select * from product_details", get_data=True)
        if not rows:
            print("no products")
            return
        print("id  product   price")
        print("-" * 20)
        for r in rows:
            print(f"{r[0]}  {r[1]:<8} rs{r[2]}")
    except:
        print("show products failed!")

def order():
    try:
        print("\n customers:")    
        show_cust()
        cid = get_int("cid: ")

        print("\nproducts:")     
        show_prod()
        pid = get_int("pid: ")
        qty = get_int("qty: ")

        db_query("insert into order_details(customer_id, product_id, quantity) values (%s,%s,%s)", (cid,pid,qty))
        print("order ok!")
    except:
        print("order failed!")

def bill():
    try:
        oid = get_int("order id: ")
        row = db_query("""
            select c.name, p.product_name, p.price, o.quantity 
            from order_details o 
            join customer c on o.customer_id=c.customer_id 
            join product_details p on o.product_id=p.product_id 
            where o.order_id=%s
        """, (oid,), get_data=True)

        if not row:
            print("no order!")
            return

        r = row[0]
        total = r[2] * r[3]
        
        print("\n" + "="*25)
        print(" curry leave's")
        print("="*25)
        print(f"sr  menu  qty  price")
        print("-"*25)
        print(f"1  {r[1]:<6} {r[3]:<3} {int(r[2])}")
        print("-"*25)
        print(f"total{'':<15} {int(total)}")
        print("="*25)
        

        f = open(f"bill_{oid}.txt", "w")
        f.write("="*25 + "\n")
        f.write("welcome to curryleaves \n")
        f.write("="*25 + "\n")
        f.write("sr  menu  qty  price\n")
        f.write("-"*25 + "\n")
        f.write(f"1  {r[1]:<6} {r[3]:<3} {int(r[2])}\n")
        f.write("-"*25 + "\n")
        f.write(f"total{'':<15} {int(total)}\n")
        f.write("="*25 + "\n")
        f.close()
        print(f"saved to bill_{oid}.txt")

        if get_text("save to db? y/n: ") == "y":
            db_query("insert into transaction_details(order_id, total_amount) values (%s, %s)", (oid, total))
            print("saved to db!")
            
    except:
        print("bill failed!")

