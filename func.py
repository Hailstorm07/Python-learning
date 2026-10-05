marks=[]
def get_marks():
    while True:
        mark=input("Enter marks")
        
        if mark=="":
            print("Please enter valid marks")
            continue
        elif  mark== "done":
            break
        try:
            mark = int(mark)
            marks.append(mark)
        except ValueError:
            print("Please enter a number")
    return marks
        
marks=get_marks()
print("Marks: ",marks)
