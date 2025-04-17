class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawing {amount}")
        else:
            print("Error: Insufficient funds for this withdrawal.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

# Program Execution
account = BankAccount("123456789")  # Creating an account

account.deposit(5000)               # Depositing money
account.withdraw(2000)              # Withdrawing money
account.get_balance()               # Checking balance
