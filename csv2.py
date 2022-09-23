# Write a program to accept the input of employees from the user and store it in a CSV file and retrieve it to display to the user
import csv
import sys


def write():
    def em_in():
        while True:
            emno = int(input("Enter employee ID: "))
            name = input("Enter employee name: ")
            salr = float(input("Enter employee salary: "))
            dept = input("Enter employee department: ")
            w.writerow([emno, name, salr, dept])
            c = input("Would you like to continue? (y/n) : ")
            if c.lower() != 'y':
                break

    file = open("employee.csv", "a")
    w = csv.writer(file)
    w.writerow(["Employee ID", "Employee Name", "Employee Salary", "Employee Department"])
    em_in()
    file.close()
    

def read():
    file = open("employee.csv", "r")
    r = csv.reader(file)
    for i in r:
        print(i)


while True:
    print("""
1. Write data to CSV file
2. Read data from CSV file
0. Exit
    """)

    ch = int(input("Enter your choice: "))

    if ch == 1:
        write()

    elif ch == 2:
        read()

    elif ch == 0:
        sys.exit("Thank You!")

    else:
        print("Wrong option!")