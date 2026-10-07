class BankAccount:
    def __init__(self, name, balance):
        self.name= name
        self.balance=balance
        self.transactions=[]
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        return True
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
            return False

        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount}")
        return True
    def show_balance(self):
        return f"{self.name }'s balance : {self.balance}"
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)
    def transfer(self,other_account,amount):
        if self.balance<amount:
            print("Insufficient funds")
            return False
        self.balance-=amount
        other_account.balance +=amount
        self.transactions.append(f"Transferred ₹{amount} to {other_account.name}")
        other_account.transactions.append(f"Received ₹{amount} from {self.name}")
        return True
        
account=BankAccount("Aniket", 500000)
account2=BankAccount("Radha",450)
while True:
    print("""
    1. Show Balance
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Show Transactions
    6. Exit
        """)

    try:
        ch=int(input("Enter Choice: "))
    except ValueError:
        print("INVALID CHOICE  ")
        continue
    if ch==1:
    
        print(account.show_balance())
    elif ch==2:
        amount = int(input("Enter amount to deposit"))
        account.deposit(amount)
    elif ch==3:
        amount = int(input("Enter amount to withdraw"))
        account.withdraw(amount)
    elif ch == 4:
        other_account = input("Enter account name to transfer to: ")

        if other_account.lower() == "radha":
            amount = int(input("Enter amount to transfer: "))
            account.transfer(account2, amount)
        else:
            print("Account not found")
    elif ch==5:
        account.show_transactions()
    elif ch==6:
        print("Exiting....")
        break
    else:
        print("Invalid Choice")
        continue
        
    