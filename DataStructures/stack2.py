import sys
stack=[]
employees={}
ages=[]

def create():
    n = int(input("Enter range of list: "))
    for i in range(n):
        emp_name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        ages.append(age)
        employees[emp_name] = age
        print(employees)
    
def push():
    for i in employees:
        print(i)
        for j in employees[i]:
            print(j)
            if j < 60:
                stack.append(i)
                
def pop():
    if len(stack) == 0:
        return None
    else:
        return stack.pop()
    
while True:
    print("1. Create stack")
    print("2. Pop from stack")
    print("3. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        create()
        push()
    
    elif ch == 2:
        pop()
    
    elif ch == 3:
        sys.exit()