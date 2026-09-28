from account import Account

class BankManager:
    def __init__(self):
        self.accounts = []
        self.load()

    def add_account(self, account):
        self.accounts.append(account)
        self.save()

    def view_accounts(self):
        for account in self.accounts:
            account.show()

    def search_account(self, number):
        for account in self.accounts:
            if account.number == number:
                account.show()

    def save(self):
        with open("accounts.txt", "w") as file:
            for account in self.accounts:
                file.write(
                    f"{account.number}|{account.name}|{account.account_type}|{account.balance}\n"
                )

    def load(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    number, name, account_type, balance = line.strip().split("|")
                    account = Account(number, name, account_type)
                    account.balance = float(balance)
                    self.accounts.append(account)
        except FileNotFoundError:
            pass