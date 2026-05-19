import random
import time


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
    def storeMenu(self):
        