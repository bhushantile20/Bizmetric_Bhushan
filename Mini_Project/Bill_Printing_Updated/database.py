from config import get_db

class InputHelper:

    @staticmethod
    def get_int(msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("enter number!")

    @staticmethod
    def get_float(msg):
        while True:
            try:
                return float(input(msg))
            except:
                print("enter valid price!")

    @staticmethod
    def get_text(msg):
        while True:
            val = input(msg).strip()
            if val:
                return val
            print("enter value!")


class DatabaseManager:

    @staticmethod
    def execute(sql, params=(), fetch=False):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute(sql, params)

            if fetch:
                data = cur.fetchall()
                cur.close()
                conn.close()
                return data
            else:
                conn.commit()
                cur.close()
                conn.close()

        except Exception as e:
            print("database error:", e)


class CustomerService:
    @staticmethod
    def add_customer():
        name = InputHelper.get_text("name: ")
        mobile = InputHelper.get_text("mobile: ")

        DatabaseManager.execute(
            "insert into customer(name, mobile) values (%s, %s)",
            (name, mobile),
        )
        print("customer added!")

    @staticmethod
    def show_customers():
        rows = DatabaseManager.execute("select * from customer", fetch=True)

        if not rows:
            print("no customers")
            return

        print("id  name      mobile")
        print("-" * 25)
        for r in rows:
            print(f"{r[0]}  {r[1]:<8} {r[2]}")


class ProductService:
    @staticmethod
    def add_product():
        name = InputHelper.get_text("product: ")
        price = InputHelper.get_float("price: ")

        DatabaseManager.execute(
            "insert into product_details(product_name, price) values (%s, %s)",
            (name, price),
        )
        print("product added!")

    @staticmethod
    def show_products():
        rows = DatabaseManager.execute("select * from product_details", fetch=True)

        if not rows:
            print("no products")
            return

        print("id  product   price")
        print("-" * 25)
        for r in rows:
            print(f"{r[0]}  {r[1]:<8} rs{r[2]}")


class OrderService:
    
    @staticmethod
    def place_order():
        print("\ncustomers:")
        CustomerService.show_customers()
        cid = InputHelper.get_int("cid: ")

        print("\nproducts:")
        ProductService.show_products()
        pid = InputHelper.get_int("pid: ")

        qty = InputHelper.get_int("qty: ")

        DatabaseManager.execute(
            "insert into order_details(customer_id, product_id, quantity) values (%s,%s,%s)",
            (cid, pid, qty),
        )

        print("order placed!")


class BillingService:

    @staticmethod
    def generate_bill():
        oid = InputHelper.get_int("order id: ")

        row = DatabaseManager.execute(
            """
            select c.name, p.product_name, p.price, o.quantity 
            from order_details o 
            join customer c on o.customer_id=c.customer_id 
            join product_details p on o.product_id=p.product_id 
            where o.order_id=%s
            """,
            (oid,),
            fetch=True,
        )

        if not row:
            print("no order!")
            return

        r = row[0]
        total = r[2] * r[3]

        print("\n" + "-" * 30)
        print("      curry leave's")
        print("-" * 30)
        print("sr  menu    qty   price")
        print("-" * 30)
        print(f"1   {r[1]:<7} {r[3]:<5} {int(r[2])}")
        print("-" * 30)
        print(f"total{'':<18}{int(total)}")
        print("-" * 30)

        with open(f"bill_{oid}.txt", "w") as f:
            f.write("-" * 30 + "\n")
            f.write("welcome to curryleaves\n")
            f.write("-" * 30 + "\n")
            f.write("sr  menu    qty   price\n")
            f.write("-" * 30 + "\n")
            f.write(f"1   {r[1]:<7} {r[3]:<5} {int(r[2])}\n")
            f.write("-" * 30 + "\n")
            f.write(f"total{'':<18}{int(total)}\n")
            f.write("-" * 30 + "\n")

        print(f"saved to bill_{oid}.txt")

        if InputHelper.get_text("save to db? y/n: ").lower() == "y":
            DatabaseManager.execute(
                "insert into transaction_details(order_id, total_amount) values (%s, %s)",
                (oid, total),
            )
            print("transaction saved!")
