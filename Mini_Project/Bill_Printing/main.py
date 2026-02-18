# main.py - Simple Billing Menu1

from database import add_cust, add_prod, show_cust, show_prod, order, bill

while True:
    print("\n --Billing Menu:--")

    print("1.add customer")
    print("2.add menu item")
    print("3.show customer")
    print("4.show menu item")
    print("5.orders")
    print("6.bill")
    print("0.exit")

    ch = input("Choice: ")

    if ch == "1":
        add_cust()
        
    elif ch == "2":
        add_prod()
        
    elif ch == "3":
        show_cust()
        
    elif ch == "4":
        show_prod()
        
    elif ch == "5":
        order()
        
    elif ch == "6":
        bill()
        
    elif ch == "0":
        print("thank you")
        break
    else:
        print("enter a correct choice ")


