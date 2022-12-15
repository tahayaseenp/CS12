import pickle
L = []


def Add_Mobile():
    while True:
        Model = input("Enter Model: ")
        Company = input("Enter Company: ")
        Price = int(input("Enter Price: "))
        L.append([Model, Company, Price])
        ch = input("Do you want to add more? (y/n): ")
        if ch != 'y':
            break
    
    f = open("Mobile.dat", "wb")
    pickle.dump(L, f)
    f.close()
    print("Mobiles added successfully")


def Display():
    f = open("Mobile.dat", "rb")
    L = pickle.load(f)
    f.close()
    print("Model\t\tCompany\t\tPrice")
    for i in L:
        print(i[0], "\t", i[1], "\t", i[2])


def Count_Company(company):
    f = open("Mobile.dat", "rb")
    L = pickle.load(f)
    f.close()
    count = 0
    for i in L:
        if i[1] == company:
            count += 1
    print("Number of mobiles of", company, "are", count)


while True:
    print("Menu")
    print("1. Add Mobile\n2. Display\n3. Count Mobiles of a Company\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Add_Mobile()
    elif ch == 2:
        Display()
    elif ch == 3:
        company = input("Enter company name: ")
        Count_Company(company)
    elif ch == 4:
        exit()