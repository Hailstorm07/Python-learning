print(" Type 1 for writing in the file, \n2 for appending in the file \n3 for reading the file and 4 for exit.. ")
ch= int(input("enter your choice"))
while True:
    if ch==1:
        print("writing mode")
        content=input("What should we insert")
        with open("notes.txt", "w") as file:
            file.write(content)
        
    elif ch== 2:
        print("append mode")
        content=input("What should we add")
        with open("notes.txt", "a") as file:
            file.write(content)
    elif ch==3:
        print("reading mode")
        
        with open("notes.txt", "r") as file:
            content=file.readlines()
            for con in content:
                print(con, end="")
    elif ch==4:
        print("exiting")
        break

        