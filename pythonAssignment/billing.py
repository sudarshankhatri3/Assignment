import ast


class OrderBilling:
    def __init__(self):
        self.orders = []

    # read orders
    def readOrders(self):
        try:
            with open("/home/sudu/Assignment/pythonAssignment/data/order.txt",'r') as file:
                for line in file:
                    data = ast.literal_eval(line.strip())
                    self.orders.append(data)

        except FileNotFoundError:
            print("Order file not found")

    # generate bill
    def generateBill(self):
        if len(self.orders) == 0:
            print("No order found")
            return
        
        subtotal = 0

        print("\n=========== FINAL BILL ===========")

        for item in self.orders:

            subtotal += item['Total']

            print(f"""
                    Item      : {item['Name']}
                    Price     : Rs. {item['Price']}
                    Quantity  : {item['Quantity']}
                    Total     : Rs. {item['Total']}
                    -----------------------------------
                """)

        # discount
        discount = 0

        if subtotal >= 1000:
            discount = subtotal * 0.10

        # taxable amount
        taxable_amount = subtotal - discount

        # VAT
        vat = taxable_amount * 0.13

        # final total
        grand_total = taxable_amount + vat

        print("\n============= SUMMARY =============")
        print(f"Subtotal        : Rs. {subtotal}")
        print(f"Discount (10%)  : Rs. {discount}")
        print(f"VAT (13%)       : Rs. {vat}")
        print(f"Grand Total     : Rs. {grand_total}")
        print("===================================")