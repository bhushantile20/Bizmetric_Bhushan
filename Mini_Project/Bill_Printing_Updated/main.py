from database import (
    CustomerService,
    ProductService,
    OrderService,
    BillingService,
)

class BillingApp:

    def run(self):
        while True:
            print("\n-- Billing Menu --")
            print("1. Customer")
            print("2.Add Product")
            print("3.Show Customers")
            print("4.Show Products")
            print("5.Place Order")
            print("6.Generate Bill")
            print("0.Exit")

            ch = input("Choice: ")

            if ch == "1":
                CustomerService.add_customer()

            elif ch == "2":
                ProductService.add_product()

            elif ch == "3":
                CustomerService.show_customers()

            elif ch == "4":
                ProductService.show_products()

            elif ch == "5":
                OrderService.place_order()

            elif ch == "6":
                BillingService.generate_bill()

            elif ch == "0":
                print("thank you")
                break

            else:
                print("enter correct choice")


if __name__ == "__main__":
    app = BillingApp()
    app.run()
