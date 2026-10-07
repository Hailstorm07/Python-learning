class Expense:
    def __init__(self, description, amount):
        self.description= description
        self.__amount= amount 
    @property
    def amount(self):
        return self.__amount
    def __str__(self):
        return f"Description : {self.description} Amount: {self.amount}"
expense1=Expense("Fuel", 250)
expense2=Expense("Food", 500)
expense3=Expense("Movie", 300)

class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self, expense):
        self.expenses.append(expense)
    def view_expenses(self):
        for index, expense in enumerate(self.expenses):
            print(f"{index+1}. {expense}")
        
    def total_expenses(self ):
        total=0
        for expense in self.expenses:
            total += expense.amount
        return total
    def delete_expense(self, index):
        
        if index <1 or index>len(self.expenses):
            print("Invalid number")
            return False    
        deleted_item=self.expenses.pop(index-1)
        print(f"Deleted : {deleted_item}")
        return True
        
        
tracker = ExpenseTracker()

tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)
tracker.view_expenses()
print(tracker.total_expenses())
index=int(input("Enter index to pop"))
tracker.delete_expense(index)