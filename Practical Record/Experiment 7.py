import pickle
L = []


def add_student():
    f = open("student.dat", "wb+")
    while True:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        L.append([roll, name])
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
            print("Roll number:", i[0], "Name:", i[1], '\n')
            break
    else:
        print("Roll number not found")
    f.close()


while True:
    print("Menu")
    print("1. Add student\n2. Search student\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        exit()