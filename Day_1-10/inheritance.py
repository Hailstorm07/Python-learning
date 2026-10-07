class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount<=0:
            print("Amount should be greater than 0")
            return False
            
        self.__balance += amount
        return True
    def withdraw(self,amount):
        if amount<=0:
            print("Amount should be greater than 0")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        
        self.__balance -= amount
        return True
    def show_balance(self):
        return f"The Balance is {self.__balance}"


account1 = BankAccount("Aniket", 0)

print(account1.balance)

account1.deposit(1000)

print(account1.balance)
