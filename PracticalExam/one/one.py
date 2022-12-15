import pickle
L = []


def create():
    f = open("items.dat", "wb")
    n = int(input("Enter the number of items: "))
    for i in range(n):
        itemno = int(input("Enter item number: "))
        itemname = input("Enter item name: ")
        price = float(input("Enter price: "))
        data = [itemno, itemname, price]
        L.append(data)
        f.flush()
    pickle.dump(L, f)
    f.close()


def display():
    f = open("items.dat", "rb")
    try:
        c = pickle.load(f)
        for i in c:
            print("Item Number: ", i[0], "\tItem Name: ", i[1], "\tPrice: ", i[2], "\n")
    except EOFError:
        f.close()


def search():
    itemno = int(input("Enter item number to search: "))
    f = open("items.dat", "rb")
    try:
        c = pickle.load(f)
        for i in c:
            if i[0] == itemno:
                print("Item Number: ", i[0], "\nItem Name: ", i[1], "\nPrice: ", i[2])
        else:
            print("Item not found!\n")
    except EOFError:
        f.close()


while True:
    print("Menu")
    print("1. Create\n2. Display\n3. Search\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        exit()