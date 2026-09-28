class Account:
    def __init__(self, number, name, account_type):
        self.number = number
        self.name = name
        self.account_type = account_type
        self.balance = 0

    def show(self):
        print("Account Number:", self.number)
        print("Name:", self.name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)

    def deposit(self, amount):
     self.balance += amount

    def withdraw(self, amount):
      if amount <= self.balance:
        self.balance -= amount
        return True
      return False