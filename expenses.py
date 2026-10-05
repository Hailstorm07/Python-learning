import json


def load_expenses():
    with open("expenses.json","r") as file:
        return json.load(file)
expenses=load_expenses()
def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
def add_expense():
    while True:
        description=input("enter description: : ")
        
        if description.lower() =="done":
            break
        try:
            expense=float(input("Enter amount: "))
        except ValueError:
            print("Enter Valid amount ")
            continue
        expense={
            "Name": description,
            "Amount": expense
        }
        expenses.append(expense)
        save_expenses()
        print("Type done to complete")
def view_expenses():
    for index, expense  in enumerate(expenses):
        
        print(
            f"{index+1}.Name:{expense['Name']},"
            f"Amount:{expense['Amount']}"
        )
def total_amount():
    total_expense=0
    for expense in expenses:
        total_expense += expense["Amount"]
    print(f"\n Total Expenses: ₹{total_expense}")
def delete_expense():
    view_expenses()
    index= int(input("Enter expense number to delete"))  -1
    expenses.pop(index)
    save_expenses()
