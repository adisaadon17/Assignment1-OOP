from securities import Stock, Bond, Option

def main():
    print("=== Securities Management System ===")
    print("please select the type of security to create:")
    print("1. Create a Stock")
    print("2. Create a Bond")
    print("3. Create an Option")
    print("4. Exit")
    
    choice = input("\nPlease choose an option (1-4): ")

    if choice == '1':
        print("\n--- Creating a Stock ---")
        name = input("Security Name: ")
        symbol = input("Symbol: ")
        price = float(input("Price: "))
        company = input("Issuing Company: ")
        
        my_stock = Stock(name, symbol, price, company)
        print("\n" + my_stock.get_details())
        print(my_stock.trade())

    elif choice == '2':
        print("\n--- Creating a Bond ---")
        name = input("Security Name: ")
        symbol = input("Symbol: ")
        price = float(input("Price: "))
        rate = float(input("Interest Rate (%): "))
        
        my_bond = Bond(name, symbol, price, rate)
        print("\n" + my_bond.get_details())
        print(f"Calculated Annual Interest: ${my_bond.calculate_interest()}")

    elif choice == '3':
        print("\n--- Creating an Option ---")
        name = input("Security Name: ")
        symbol = input("Symbol: ")
        price = float(input("Price: "))
        expiry = input("Expiration Date: ")
        
        my_option = Option(name, symbol, price, expiry)
        print("\n" + my_option.get_details())
        print(my_option.check_validity())

    elif choice == '4':
        print("Exiting... Goodbye!")
    else:
        print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()

