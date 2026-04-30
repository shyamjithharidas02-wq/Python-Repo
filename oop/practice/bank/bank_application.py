import random

# GLOBAL VARIABLES (App-level config)
BANK_NAME = "Federal Bank"
MIN_BALANCE = 1000

# DATABASE (simulated using dict)
users_db = {}  # username -> User object


class BankAccount:
    # CLASS VARIABLE (shared across all accounts)
    total_accounts = 0

    def __init__(self, user, account_type):
        self.user = user
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transactions = []  # list to store history

        BankAccount.total_accounts += 1

    # INSTANCE METHOD
    def deposit(self, amount):
        if self.validate_amount(amount):
            self.balance += amount
            self._log("DEPOSIT", amount)

    # INSTANCE METHOD
    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid amount")
            return

        if self.balance - amount < MIN_BALANCE:
            print("Minimum balance violation")
            return

        self.balance -= amount
        self._log("WITHDRAW", amount)

    # TRANSFER MONEY
    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self._log("TRANSFER SENT", amount)
            target_account._log("TRANSFER RECEIVED", amount)
        else:
            print("Insufficient balance")

    # ENCLOSING VARIABLE (closure logging)
    def _log(self, txn_type, amount):
        prefix = f"[{BANK_NAME} - {self.user.username}]"  # enclosing

        def logger():
            entry = f"{txn_type}: ₹{amount}, Balance: ₹{self.balance}"
            self.transactions.append(entry)
            print(prefix, entry)

        logger()

    # STATIC METHOD (utility)
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    # STATIC METHOD (no object needed)
    @staticmethod
    def calculate_interest(balance):
        return balance * 0.04

    # CLASS METHOD
    @classmethod
    def generate_account_number(cls):
        return f"ACC{1000 + cls.total_accounts}"

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts


class User:
    def __init__(self, first_name, last_name, email, place):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.place = place

        self.username = self._generate_username()
        self.password = self._generate_password()

        self.accounts = []  # list of BankAccount

    # ENCLOSING (used internally)
    def _generate_username(self):
        return self.first_name.lower() + str(random.randint(100, 999))

    def _generate_password(self):
        return str(random.randint(1000, 9999))

    # INSTANCE METHOD
    def create_account(self, account_type):
        acc = BankAccount(self, account_type)
        self.accounts.append(acc)
        print(f"{account_type} Account Created: {acc.account_number}")

    def get_account(self):
        if self.accounts:
            return self.accounts[0]  # simple (first account)
        return None


# MAIN PROGRAM LOOP
def main():
    while True:
        print(f"\n--- Welcome to {BANK_NAME} ---")
        print("1. New User")
        print("2. Existing User")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            login_user()

        elif choice == "3":
            break


def register_user():
    print("\n--- Create Account ---")

    first = input("First Name: ")
    last = input("Last Name: ")
    email = input("Email: ")
    place = input("Place: ")

    user = User(first, last, email, place)
    users_db[user.username] = user

    print("\n✅ Account Created Successfully")
    print("Username:", user.username)
    print("Password:", user.password)


def login_user():
    username = input("Username: ")
    password = input("Password: ")

    user = users_db.get(username)

    if user and user.password == password:
        print("Login successful")
        user_dashboard(user)
    else:
        print("Invalid credentials")


def user_dashboard(user):
    while True:
        print("\n--- Bank Services ---")
        print("1. Create Bank Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Logout")

        choice = input("Enter choice: ")

        acc = user.get_account()

        if choice == "1":
            acc_type = input("Savings / Current: ")
            user.create_account(acc_type)

        elif choice == "2":
            if acc:
                amount = int(input("Amount: "))
                acc.deposit(amount)

        elif choice == "3":
            if acc:
                amount = int(input("Amount: "))
                acc.withdraw(amount)

        elif choice == "4":
            if acc:
                print("Balance:", acc.balance)

        elif choice == "5":
            if acc:
                target_user = input("Enter receiver username: ")
                target = users_db.get(target_user)
                if target:
                    target_acc = target.get_account()
                    amount = int(input("Amount: "))
                    acc.transfer(target_acc, amount)

        elif choice == "6":
            if acc:
                print("\n--- Transactions ---")
                for t in acc.transactions:
                    print(t)

        elif choice == "7":
            break


# RUN
main()
