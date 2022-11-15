import csv
L = []
f = open('data.csv', 'w', newline='')
writer = csv.writer(f, delimiter=',')
writer.writerow(['Employee ID', 'Employee Name', 'Employee Salary'])
f.close()


def create():
    f = open('data.csv', 'a+', newline='')
    writer = csv.writer(f, delimiter=',')
    while True:
        idno = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salr = input("Enter Employee Salary: ")
        L.append([idno, name, salr])
        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break
    writer.writerows(L)
    f.close()


def search():
    f = open('data.csv', 'r')
    reader = csv.reader(f, delimiter=',')
    idno = input("Enter Employee ID: ")
    for row in reader:
        if idno == row[0]:
            print("Employee ID: ", row[0])
            print("Employee Name: ", row[1])
            print("Employee Salary: ", row[2])
            break
    f.close()


while True:
    print("Menu")
    print("1. Create\n2. Search\n3. Exit")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        create()
    elif ch == 2:
        search()
    elif ch == 3:
        exit()
    else:
        print("Invalid choice")