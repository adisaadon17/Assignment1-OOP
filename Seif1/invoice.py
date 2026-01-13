from locale import currency


class Invoice:
    def __init__(self, customer_name, item_name, quantity, price_per_unit, invoice_id,):
        self.customer_name = customer_name
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.__invoice_id = invoice_id
    
    
    @property
    def invoice_id(self):
        return self.__invoice_id

    def calculate_total(self):
        return self.quantity * self.price_per_unit

    def display_invoice(self):
        print("--- Invoice Details ---")
        print(f"Customer: {self.customer_name}")
        print(f"Item: {self.item_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per unit: ${self.price_per_unit}")
        print(f"Invoice ID: {self.invoice_id}")
        print(f"Total Amount: {self.calculate_total()}")
        print("-----------------------")

    def apply_discount(self, percent):
        if 0 < percent < 100:
            discount_amount = self.price_per_unit * (percent / 100)
            self.price_per_unit -= discount_amount
            print(f"New price updated after {percent}% discount!")
        else:
            print("Invalid discount percentage")
