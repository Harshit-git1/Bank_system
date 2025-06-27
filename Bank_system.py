class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def current_balance(self, amount):
        if amount < 1000:
            print("You are required to maintain a minimum balance of ₹1000.")
        else:
            self.__balance = amount

    def deposit(self, amount):
        if amount >= 1000:
            self.__balance += amount
            print(f"Deposited amount ₹{amount}. Total balance is {self.__balance}")

    def withdraw(self, amount):
        if (self.__balance - amount) >= 1000:
            self.__balance -= amount
            print(f"Withdraw amount is {amount}. Total balance is {self.__balance}")
        else:
            print(f"You cannot withdraw ₹{amount}. Minimum balance of ₹1000 is mandate.")
    def get_balance(self):
        return self.__balance
        
b = BankAccount(2000)
b.deposit(1200)
b.withdraw(2100)
print(f"Current balance is {b.get_balance()}")

