from account import Account
from bank_manager import BankManager

bank = BankManager()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = input("Account Number: ")
        name = input("Name: ")
        account_type = input("Account Type: ")

        bank.add_account(Account(number, name, account_type))
        print("Account created successfully!")

    elif choice == "2":
     bank.view_accounts()

    elif choice == "3":
     number = input("Account Number: ")
     bank.search_account(number)

    elif choice == "4":
     number = input("Account Number: ")
     amount = float(input("Amount: "))

     for account in bank.accounts:
        if account.number == number:
            account.deposit(amount)
            print("Money deposited successfully!")
            break

    elif choice == "5":
     number = input("Account Number: ")
     amount = float(input("Amount: "))

     for account in bank.accounts:
         if account.number == number:
            if account.withdraw(amount):
                print("Money withdrawn successfully!")
            else:
                print("Insufficient balance.")
            break

    elif choice == "6":
          print("Thank you for using the Bank Management System!")
          break

    else:
        print("Invalid choice.")