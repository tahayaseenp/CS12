import pickle
L = []


def add_student():
    f = open("student.dat", "wb+")
    while True:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        L.append([roll, name, marks])
        if input("Would you like to add another student? (y/n): ") != "y":
            break
        else:
            continue
    print()
    pickle.dump(L, f)
    f.close()


def search_student():
    roll = int(input("Enter roll number to search: "))
    f = open("student.dat", "rb")
    c = pickle.load(f)
    for i in c:
        if roll == i[0]:
            print("Roll number:", i[0], "Name:", i[1], "Marks: ", i[2], '\n')
            break
    else:
        print("Roll number not found")
    f.close()


def edit_student():
    roll = int(input("Enter roll number to edit: "))
    mark = int(input("Enter new marks: "))
    f = open("student.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if roll == i[0]:
            i[2] = mark
            f = open("student.dat", "wb")
            pickle.dump(c, f)
            f.close()
            break
    else:
        print("Roll number not found")
    print("Marks updated")


while True:
    print("Menu")
    print("1. Add student\n2. Search student\n3. Edit student\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        exit()