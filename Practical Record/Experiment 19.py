import csv


def create():
    f = open('employee.csv', 'w', newline='')
    w = csv.writer(f)
    w.writerow(['ID', 'Name', 'Salary', 'Department'])
    f.flush()
    while True:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        basic = int(input("Enter Basic Salary: "))
        hra = 0.1 * basic  # House Rent Allowance
        sal = basic + hra
        w.writerow([id, name, dept, str(basic), str(hra), str(sal)])
        f.flush()
        ch = input("Do you want to add more records? (y/n): ")
        if ch != 'y':
            break
    f.close()


create()