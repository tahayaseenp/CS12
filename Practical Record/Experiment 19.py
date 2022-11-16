import csv
L = []
f = open('employee.csv', 'w', newline='')
w = csv.writer(f)
w.writerow(['ID', 'Name', 'Salary', 'Department'])


def create():
    f = open('employee.csv', 'a', newline='')
    w = csv.writer(f)
    while True:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        basic = int(input("Enter Basic Salary: "))
        hra = int(input("Enter HRA: "))  # House Rent Allowance
        sal = basic + hra
        L.append([id, name, dept, basic, hra, sal])
        ch = input("Do you want to add more records? (y/n): ")
        if ch != 'y':
            break
    w.writerows(L)
    f.close()


create()