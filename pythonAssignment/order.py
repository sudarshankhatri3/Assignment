import random
import ast


# generate unique order id
def orderID():
    return random.randint(1000, 9999)


class Order:

    def __init__(self):
        self.orders = []   # store current order items

    # add item to order
    def addOrder(self):

        tableNo = int(input("Enter table no: "))
        menuId = int(input("Enter menu id: "))
        quantity = int(input("Enter quantity: "))

        updated_menu = []
        item_found = False

        # read menu file
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt", 'r') as file:
            for line in file:
                data = ast.literal_eval(line.strip())
                # check menu item
                if data['id'] == menuId:
                    item_found = True
                    # check stock
                    if data['Stock'] >= quantity:
                        data['Stock'] -= quantity
                        # create order item
                        order_item = {
                            "orderId": orderID(),
                            "tableNo": tableNo,
                            "menuId": data['id'],
                            "Name": data['Name'],
                            "Price": data['Price'],
                            "Quantity": quantity,
                            "Total": data['Price'] * quantity
                        }
                        # store in list
                        self.orders.append(order_item)
                        print("Order added successfully")
                    else:
                        print("Insufficient stock")
                updated_menu.append(data)

        if not item_found:
            print("Menu item not found")

        # update menu stock
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt", 'w') as file:
            for item in updated_menu:
                file.write(str(item) + "\n")

        # save order into order file
        with open("/home/sudu/Assignment/pythonAssignment/data/order.txt", 'a') as file:
            for item in self.orders:
                file.write(str(item) + "\n")

    # remove item from order
    def removeOrder(self):

        remove_id = int(input("Enter order id to remove: "))

        found = False

        for item in self.orders:

            if item['orderId'] == remove_id:
                self.orders.remove(item)
                found = True
                print("Order removed successfully")
                break

        if not found:
            print("Order not found")

    # display all current orders
    def displayOrder(self):

        if len(self.orders) == 0:
            print("No orders available")

        else:

            print("\n------ Current Orders ------")

            grand_total = 0

            for item in self.orders:

                print(f"""
                        Order ID : {item['orderId']}
                        Table No : {item['tableNo']}
                        Item     : {item['Name']}
                        Price    : {item['Price']}
                        Quantity : {item['Quantity']}
                        Total    : {item['Total']}
                        """)

                grand_total += item['Total']

            print(f"Grand Total = {grand_total}")


# object
obj = Order()

while True:

    print("""
          1. Add Order
          2. Remove Order
          3. Display Order
          4. Exit
            """)

    choice = int(input("Enter choice: "))
    if choice == 1:
        obj.addOrder()

    elif choice == 2:
        obj.removeOrder()

    elif choice == 3:
        obj.displayOrder()

    elif choice == 4:
        print("Program exited")
        break
    else:
        print("Invalid choice")