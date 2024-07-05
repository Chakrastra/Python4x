class BankAccount:
    def __init__(self, acc_holder, bal=0.0):
        self.account_holder = acc_holder
        self.bal = bal

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
            print(f"Deposited {amount}. New balance is {self.bal}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.bal >= amount:
                self.bal -= amount
                print(f"Withdrew {amount}. New balance is {self.bal}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_bal(self):
        return self.bal

# Inst
account = BankAccount("Thors", 100.0)
 
print(f"Account holder: {account.acc_holder}")
print(f"Initial balance: {account.check_bal()}")

account.deposit(50)
account.withdraw(30)
current_bal = account.check_bal()
print(f"Current balance: {current_bal}")
account.withdraw(150)
account.deposit(-20)
account.withdraw(-10)