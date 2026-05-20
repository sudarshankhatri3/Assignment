import random
import ast


# generate order id
def orderID():
    return random.randint(1000, 9999)


class Order:
    def __init__(self):
        self.orders = []

    # add order
    def addOrder(self):
        tableNo = int(input("Enter table no: "))
        menuId = int(input("Enter menu id: "))
        quantity = int(input("Enter quantity: "))

        updated_menu = []

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'r') as file:
            for line in file:
                data = ast.literal_eval(line.strip())
                if data['id'] == menuId:
                    if data['Stock'] >= quantity:
                        data['Stock'] -= quantity
                        order_item = {
                            "orderId": orderID(),
                            "tableNo": tableNo,
                            "menuId": data['id'],
                            "Name": data['Name'],
                            "Price": data['Price'],
                            "Quantity": quantity,
                            "Total": data['Price'] * quantity
                        }

                        self.orders.append(order_item)

                        print("Order added successfully")

                    else:
                        print("Insufficient stock")

                updated_menu.append(data)

        # update stock
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'w') as file:
            for item in updated_menu:
                file.write(str(item) + "\n")

        # save order
        with open("/home/sudu/Assignment/pythonAssignment/data/order.txt",'a') as file:
            for item in self.orders:
                file.write(str(item) + "\n")

    # display order
    def displayOrder(self):
        try:
            with open("/home/sudu/Assignment/pythonAssignment/data/order.txt",'r') as file:
                print("\n======= ALL ORDERS =======")
                grand_total = 0
                for line in file:
                    item = ast.literal_eval(line.strip())
                    print(f"""
                            Order ID : {item['orderId']}
                            Table No : {item['tableNo']}
                            Item     : {item['Name']}
                            Price    : Rs. {item['Price']}
                            Quantity : {item['Quantity']}
                            Total    : Rs. {item['Total']}
                            --------------------------------
                        """)

                    grand_total += item['Total']
                print(f"Grand Total = Rs. {grand_total}")

        except FileNotFoundError:
            print("Order file not found")