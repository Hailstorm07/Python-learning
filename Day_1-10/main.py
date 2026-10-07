from expenses import add_expense, view_expenses, total_amount, delete_expense

        
while  True:
    print("Menu\n")
    print("Press 1 to add expense")
    print("Press 2 to view expenses")
    print("Press 3 to view total expenses")
    print("Press 4 to delete expense")
    print("Press 5 to exit: ")
    try:
        ch=int(input("Enter your choice: "))
            
    except ValueError:
        print("Enter Valid number")
        continue
    
    if ch==1:
        add_expense()
    elif ch==2:
        view_expenses()
    elif ch==3:
        total_amount()
    elif ch==4:
        delete_expense()
    elif ch==5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        
        