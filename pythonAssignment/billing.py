import ast


class OrderBilling:

    def __init__(self):
        self.orders = []

    # read orders from file
    def readOrders(self):
        try:
            with open('/home/sudu/Assignment/pythonAssignment/data/order.txt', 'r') as file:
                for line in file:
                    data = ast.literal_eval(line.strip())
                    self.orders.append(data)

        except FileNotFoundError:
            print("Order file not found")

    # calculate subtotal
    def calculateSubtotal(self):

        subtotal = 0

        for item in self.orders:

            item_total = item['Price'] * item['Quantity']
            subtotal += item_total

        return subtotal

    # generate bill
    def generateBill(self):

        if len(self.orders) == 0:
            print("No order data found")
            return

        print("\n============= FINAL BILL =============")

        subtotal = 0

        # print itemized bill
        for item in self.orders:

            item_total = item['Price'] * item['Quantity']
            subtotal += item_total

            print(f"""
                Order ID : {item['orderId']}
                Table No : {item['tableNo']}
                Item     : {item['Name']}
                Price    : Rs. {item['Price']}
                Quantity : {item['Quantity']}
                Total    : Rs. {item_total}
                ---------------------------------------
                """)

        # apply discount
        discount = 0

        if subtotal >= 1000:
            discount = subtotal * 0.10

        # amount after discount
        taxable_amount = subtotal - discount

        # apply VAT
        vat = taxable_amount * 0.13

        # final total
        grand_total = taxable_amount + vat

        # summary
        print("\n=============== SUMMARY ===============")
        print(f"Subtotal            : Rs. {subtotal}")
        print(f"Discount (10%)      : Rs. {discount}")
        print(f"VAT (13%)           : Rs. {vat}")
        print(f"Grand Total         : Rs. {grand_total}")
        print("=======================================")


# object creation
bill = OrderBilling(
    "/home/sudu/Assignment/pythonAssignment/data/order.txt"
)

# read order file
bill.readOrders()

# generate final bill
bill.generateBill()