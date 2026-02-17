
from database import (
    add_customer, add_product, show_customers, 
    show_products, place_order, print_bill
)

while True:
    print("\n --Billing System Menu:--")
    print("1.add Customer")
    print("2.add Product")
    print("3.show Customers")
    print("4.show products")
    print("5.place order")
    print("6.print")
    print("0.exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_customer()
    elif choice == '2':
        add_product()
    elif choice == '3':
        show_customers()
    elif choice == '4':
        show_products()
    elif choice == '5':
        place_order()
    elif choice == '6':
        print_bill()
    elif choice == '0':
        print("thank you for using the my billing system")
        break
    else:
        print("enter correct choice")
