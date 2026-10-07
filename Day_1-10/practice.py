students=[]
total_marks=0
small=None
large=None
high_stu=None
low_stu=None
numbers=int(input("Enter number fo students"))
for i in range(0,numbers):
    name=input("enter your name")
    marks=int(input("enter your marks"))
    # if small is None or marks<small:
    #     small=marks
    #     low_stu=name
    # if large is None or marks>large:
    #     large=marks
    #     high_stu=name
    # total_marks+=marks
    student={name:marks}
    students.append(student)
def average(marks):
    
    avg=total_marks/numbers
    return avg
average=total_marks/numbers
print(average)
print(small,low_stu)
print(large,high_stu)
