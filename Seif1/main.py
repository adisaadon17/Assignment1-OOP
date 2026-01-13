from invoice import Invoice

print("Please enter invoice details:")
c_name = input("Customer Name: ")
i_name = input("Item Name: ")
qty = int(input("Quantity: "))
price = float(input("Price per Unit: "))
inv_id = input("Invoice ID: ")

my_invoice = Invoice(c_name, i_name, qty, price, inv_id)

print("\nShowing initial invoice details:")
my_invoice.display_invoice()

discount = float(input("Enter discount percentage (e.g. 10 for 10%): "))
my_invoice.apply_discount(discount)

print("\nShowing updated invoice details:")
my_invoice.display_invoice()


