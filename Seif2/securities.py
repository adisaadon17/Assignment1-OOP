class Security:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def get_details(self):
        return f"Security: {self.name} ({self.symbol}), Current Price: {self.price}"
    
class Stock(Security):
        def __init__(self, name, symbol, price, company):
            super().__init__(name, symbol, price)
            self.company = company

        def trade(self):
            return f"Trading stock of {self.company}"
        
class Bond(Security):
    def __init__(self, name, symbol, price, interest_rate):
        super().__init__(name, symbol, price)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.price * (self.interest_rate / 100)

class Option(Security):
    def __init__(self, name, symbol, price, expiration_date):
        super().__init__(name, symbol, price)
        self.expiration_date = expiration_date

    def check_validity(self):
        return f"The option {self.name} is valid until {self.expiration_date}"