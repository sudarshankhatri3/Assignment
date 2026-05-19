import random
import time
import ast


#function to generate the unique id for every menu 
def menuId():
    id=random.randint(1000,9999)
    return id




class Menu:
    def __init__(self,name,price,category,availability,stock_quantity,description):
        self.name=name
        self.price=price
        self.category=category
        self.availability=availability
        self.stock_quantity=stock_quantity
        self.description=description


    # store the menu in the file and track the data 
    def addMenu(self):
        data={
            "id":menuId(),
            "Name":self.name,
            "Price":self.price,
            "Category":self.category,
            "Available":self.availability,
            "Stock":self.stock_quantity,
            "Description":self.description
        }

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'a') as menuFile:
            menuFile.write(str(data))

        print("Menu added sucessfully")

    def updateMenu(self):
        id=int(input("Enter th id of menu to update::"))

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'r') as file:
            for line in file:
                data=ast.literal_eval(line.strip())
                if data['id']==id:
                    print("Data found")
                    print(data)
                    break





if __name__=="__main__":
    name=input('Enter the menuName:')
    price=float(input('Enter the price:'))
    category=input('Enter the category:')
    availability=input('Enter the availabilty:')
    stock=int(input('Enter the stock:'))
    description=input('Enter the description:')
    obj=Menu(name,price,category,availability,stock,description)
    # obj.addMenu()
    obj.updateMenu()
