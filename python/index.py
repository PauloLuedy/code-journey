class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    @property
    def balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Balance: ${account.balance}")