from mysql.connector import connect as c
cdb = c(user='root', password='root', host='localhost')
db = cdb.cursor()

db.execute("CREATE DATABASE IF NOT EXISTS company")
db.execute("USE company")
db.execute("CREATE TABLE IF NOT EXISTS employee (id INT PRIMARY KEY, name VARCHAR(255), salary INT, department VARCHAR(255))")
cdb.commit()


def add_records():
    while True:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        department = input("Enter Department: ")
        db.execute("INSERT INTO employee VALUES (%s, %s, %s, %s)", (id, name, salary, department))
        cdb.commit()
        print("Record Added Successfully")
        ch = input("Do you want to add more records? (y/n): ")
        if ch != 'y':
            break


def show_records():
    db.execute("SELECT * FROM employee")
    rs = db.fetchall()
    print("%10s" % "Employee ID", "%20s" % "Employee Name", "%10s" % "Salary", "%20s" % "Department")
    for i in rs:
        print("%7s" % i[0], "%20s" % i[1], "%12s" % i[2], "%17s" % i[3])

    
while True:
    print("Menu")
    print("1. Add Records\n2. Show Records\n3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_records()
    elif ch == 2:
        show_records()
    elif ch == 3:
        exit()