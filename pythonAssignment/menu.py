import random
import ast


# generate menu id
def menuId():
    return random.randint(1000, 9999)


class Menu:
    def __init__(self, name, price, category,availability, stock_quantity, description):
        self.name = name
        self.price = price
        self.category = category
        self.availability = availability
        self.stock_quantity = stock_quantity
        self.description = description

    # add menu
    def addMenu(self):
        data = {
            "id": menuId(),
            "Name": self.name,
            "Price": self.price,
            "Category": self.category,
            "Available": self.availability,
            "Stock": self.stock_quantity,
            "Description": self.description
        }

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'a') as file:
            file.write(str(data) + "\n")
        print("Menu added successfully")

    # update menu
    def updateMenu(self):
        updated_data = []
        menu_id = int(input("Enter menu id to update: "))
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'r') as file:
            for line in file:
                data = ast.literal_eval(line.strip())
                if data['id'] == menu_id:
                    data['Name'] = input("Enter new name: ")
                    data['Price'] = float(input("Enter new price: "))
                    data['Category'] = input("Enter category: ")
                    data['Available'] = input("Available: ")
                    data['Stock'] = int(input("Enter stock: "))
                    data['Description'] = input("Enter description: ")

                    print("Menu updated")

                updated_data.append(data)

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'w') as file:
            for item in updated_data:
                file.write(str(item) + "\n")

    # remove menu
    def removeMenu(self):
        new_data = []
        menu_id = int(input("Enter menu id to remove: "))
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'r') as file:
            for line in file:
                data = ast.literal_eval(line.strip())

                if data['id'] != menu_id:
                    new_data.append(data)

                else:
                    print("Deleted:", data)

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'w') as file:
            for item in new_data:
                file.write(str(item) + "\n")

        print("Menu removed successfully")