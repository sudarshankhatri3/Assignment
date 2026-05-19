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
        updated_data=[]

        id=int(input("Enter th id of menu to update::"))


        # open file to find the data to update
        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'r') as file:
            for line in file:
                data=ast.literal_eval(line.strip())
                if data['id']==id:
                    new_name=input("Enter updated name:")
                    price=float(input('Enter the updated price:'))
                    category=str(input("Enter the updated category:"))
                    available=str(input("Enter the availability:"))
                    stock=int(input("Enter the updated stock:"))
                    description=str(input("Enter the updated description:"))
                    print("Data found")
                    data['Name']=new_name
                    data['Price']=price
                    data['Category']=category
                    data['Available']=available
                    data['Category']=category
                    data['Stock']=stock
                    data['Description']=description
                updated_data.append(data)

        #open file to rewrite the data after updated sucessfully

        with open("/home/sudu/Assignment/pythonAssignment/data/menu.txt",'w') as file:
            for items in updated_data:
                file.write(str(items))

        print("File updated and stored sucessfulluy")


                    
        





if __name__=="__main__":
    name=input('Enter the menuName:')
    price=float(input('Enter the price:'))
    category=input('Enter the category:')
    availability=input('Enter the availabilty:')
    stock=int(input('Enter the stock:'))
    description=input('Enter the description:')
    obj=Menu(name,price,category,availability,stock,description)
    obj.addMenu()
    obj.updateMenu()
