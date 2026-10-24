import json

FILENAME = "bank.json"


class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load()

    def load(self):
        try:
            with open(FILENAME) as f:
                data = json.load(f)
            for name, balance in data.items():
                self.accounts[name] = Account(name, balance)
        except FileNotFoundError:
            pass

    def save(self):
        data = {n: a.balance for n, a in self.accounts.items()}
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)

    def get(self, name):
        if name not in self.accounts:
            raise ValueError("No such account.")
        return self.accounts[name]

    def create(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        if name in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[name] = Account(name)

    def transfer(self, sender, receiver, amount):
        source = self.get(sender)
        target = self.get(receiver)
        source.withdraw(amount)
        target.deposit(amount)


def ask_amount():
    return float(input("Amount: "))


bank = Bank()

while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View all")
    print("6. Quit")
    choice = input("Choose: ").strip()

    try:
        if choice == "1":
            bank.create(input("Account name: ").strip().lower())
            print("Account created.")
        elif choice == "2":
            account = bank.get(input("Account name: ").strip().lower())
            account.deposit(ask_amount())
            print(f"New balance: {account.balance:.2f}")
        elif choice == "3":
            account = bank.get(input("Account name: ").strip().lower())
            account.withdraw(ask_amount())
            print(f"New balance: {account.balance:.2f}")
        elif choice == "4":
            sender = input("From: ").strip().lower()
            receiver = input("To: ").strip().lower()
            bank.transfer(sender, receiver, ask_amount())
            print("Transfer complete.")
        elif choice == "5":
            if not bank.accounts:
                print("No accounts yet.")
            for acc in bank.accounts.values():
                print(f"{acc.name}: {acc.balance:.2f}")
        elif choice == "6":
            bank.save()
            print("Saved. Goodbye!")
            break
        else:
            print("Please choose 1 to 6.")
            continue
        bank.save()
    except ValueError as error:
        print("Error:", error)
