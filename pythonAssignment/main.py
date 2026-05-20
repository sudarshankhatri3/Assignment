from menu import Menu
from order import Order
from billing import OrderBilling


order_obj = Order()

while True:

    print("""
========= RESTAURANT SYSTEM =========

1. Add Menu
2. Update Menu
3. Remove Menu
4. Add Order
5. Display Orders
6. Generate Bill
7. Exit

=====================================
""")

    choice = int(input("Enter choice: "))

    # add menu
    if choice == 1:

        name = input("Enter menu name: ")
        price = float(input("Enter price: "))
        category = input("Enter category: ")
        availability = input("Enter availability: ")
        stock = int(input("Enter stock: "))
        description = input("Enter description: ")

        menu = Menu(
            name,
            price,
            category,
            availability,
            stock,
            description
        )

        menu.addMenu()

    # update menu
    elif choice == 2:

        menu = Menu("", 0, "", "", 0, "")
        menu.updateMenu()

    # remove menu
    elif choice == 3:

        menu = Menu("", 0, "", "", 0, "")
        menu.removeMenu()

    # add order
    elif choice == 4:
        order_obj.addOrder()

    # display order
    elif choice == 5:
        order_obj.displayOrder()

    # generate bill
    elif choice == 6:

        bill = OrderBilling()
        bill.readOrders()
        bill.generateBill()

    # exit
    elif choice == 7:
        print("Program exited")
        break

    else:
        print("Invalid choice")