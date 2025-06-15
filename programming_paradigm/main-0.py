import sys
from bank_account import BankAccount
def main():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    
    account = BankAccount(account_number, initial_balance)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            if account.deposit(amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Amount must be positive.")
        
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Check your balance or amount.")
        
        elif choice == '3':
            print(f"Current Balance: {account.display_balance()}")
        
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
# This code is a simple bank account management system.
# It allows users to create a bank account, deposit money, withdraw money, and display the current balance.
# The BankAccount class encapsulates the account's properties and methods.      