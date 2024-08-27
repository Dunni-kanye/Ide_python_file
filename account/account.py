from decimal import Decimal


class Account:

    def __init__(self, name, pin, balance=0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance


    def deposit(self, amount):
        if amount < Decimal(0.00):
            raise ValueError("Amount cannot be less than 0.00")
        self.balance += amount

account1 = Account(  "chidinma","0000")
account2 = Account( "stanley","0000")
#print(account1.name, account1.pin, account1.balance)
#print(account2.name, account2.pin, account2.balance)


account1.deposit(100)
print(account1.balance)