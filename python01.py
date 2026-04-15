class BankAccount:
    def __init__(self, balance):
     self.__balance = balance

    def Deposit(self, amount):
        self.__balance += amount

    def Withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

b1=BankAccount(15000)
print(b1.get_balance())
b1.Deposit(5000)
print(b1.get_balance())
b1.Withdraw(10000)
print(b1.get_balance())
