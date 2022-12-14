# Write a program to accept the input of employees from the user and store it in a CSV file and retrieve it to display to the user
import csv
import sys
rec=[]


def write():
    while True:
        emno = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salr = float(input("Enter employee salary: "))
        dept = input("Enter employee department: ")
        rec.append([emno, name, salr, dept])
        c = input("Would you like to continue? (y/n) : ")
        if c.lower() != 'y':
            break

    file = open("employee.csv", "w")
    w = csv.writer(file)
    w.writerow(["Employee ID", "Employee Name", "Employee Salary", "Employee Department"])
    w.writerows(rec)
    file.close()


def read():
    file = open("employee.csv", "r")
    r = csv.reader(file)
    for i in r:
        print(i)


def clear():
    file = open("employee.csv", "w")
    file.close()


while True:
    print("""
1. Write data to CSV file
2. Read data from CSV file
3. Clear CSV file
4. Print sorted data from CSV file (Sorted by Employee ID)
5. Find sum of salaries of all employees
0. Exit
    """)

    ch = int(input("Enter your choice: "))

    if ch == 1:
        write()

    elif ch == 2:
        read()
    
    elif ch == 3:
        clear()

    elif ch == 4:
        rec.sort()
        print(rec for i in rec)

    elif ch == 5:
        print(sum([i[2] for i in rec]))

    elif ch == 0:
        sys.exit("Thank You!")

    else:
        print("Wrong option!")