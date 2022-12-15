stack = []


def Push():
    Eno = input("Enter Employee ID: ")
    Ename = input("Enter Employee Name: ")
    Salary = input("Enter Salary: ")
    stack.append([Eno, Ename, Salary])


def Pop():
    print(stack.pop())


def display():
    print("Employee ID\tEmployee Name\tSalary")
    for i in stack[::-1]:
        print(i[0], "\t", i[1], "\t", i[2])


while True:
    print("Menu")
    print("1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Push()
    elif choice == 2:
        Pop()
    elif choice == 3:
        display()
    elif choice == 4:
        exit()