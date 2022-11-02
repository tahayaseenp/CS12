from mysql.connector import connect

cdb = connect(host='localhost', user='root', password='root')
db = cdb.cursor()
db.execute("CREATE DATABASE IF NOT EXISTS TPemployee")
db.execute("USE TPemployee")
db.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(10), department VARCHAR(255))")
cdb.commit()


def add():
    while True:
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        department = input("Enter department: ")
        db.execute("INSERT INTO employee VALUES (%s, %s, %s, %s)", (id, name, salary, department))
        cdb.commit()
        print("Employee added successfully\n")
        ch = input("Would you like to continue? (y/n) : ")
        if ch.lower() != 'y':
            break
        else:
            continue

def view():
    db.execute("SELECT * FROM employee")
    data = db.fetchall()
    print("%9s"%"ID","%20s"%"Name", "%10s"%"Salary", "%15s"%"Department")
    for row in data:
        print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%15s"%row[3])


while True:
    print("MENU")
    print("1. Add\n2. View\n3. Exit")

    c = int(input("Enter your choice: "))
    if c == 1:
        add()
    elif c == 2:
        view()
    elif c == 3:
        exit()
    else:
        print("Invalid choice")