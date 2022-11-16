from mysql.connector import connect as c
cdb = c(user='root', password='root', host='localhost')
db = cdb.cursor()

db.execute("CREATE DATABASE IF NOT EXISTS company")
db.execute("USE company")
db.execute("CREATE TABLE IF NOT EXISTS employee (id INT PRIMARY KEY, name VARCHAR(255), salary INT, department VARCHAR(255))")
cdb.commit()


def edit_records():
    id = int(input("Enter ID: "))
    db.execute("SELECT * FROM employee WHERE id = %s", (id,))
    rs = db.fetchall()
    if len(rs) == 0:
        print("Employee not found")
        exit()
    else:
        print("Employee ID: ", rs[0][0], "\nEmployee Name: ", rs[0][1], "\nSalary: ", rs[0][2], "\nDepartment: ", rs[0][3], "\n")

    name = input("Enter new name: ")
    salary = int(input("Enter new salary: "))
    department = input("Enter new department: ")
    db.execute("UPDATE employee SET name = %s, salary = %s, department = %s WHERE id = %s", (name, salary, department, id))
    cdb.commit()
    print("Record updated successfully")


print("Employee Updation")
edit_records()