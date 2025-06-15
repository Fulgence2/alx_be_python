class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        return self.account_balance

    def __str__(self):
        return f"Account {self.account_number}: Balance {self.account_balance}"