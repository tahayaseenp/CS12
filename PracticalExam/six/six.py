def create():
    f = open("poem.txt", "w")
    f.writelines("I have A Tree, a Green, green tree\nTo shade me from the Sun.")
    f.close()


def display():
    f = open("poem.txt", "r")
    c = f.read()
    c = c.split(' ')
    for i in c:
        if i[0].isupper():
            print(i, end='\t')
    print()
    f.close()


def AECount():
    a = 0
    e = 0
    f = open("poem.txt", "r")
    c = f.read()
    for i in c:
        if i.lower() == 'a':
            a += 1
        elif i.lower() == 'e':
            e += 1
    print("A: ", a, "\nE: ", e)
    f.close()


while True:
    print("Menu")
    print("1. Create a file\n2. Display the words starting with capital letter\n3. Count the number of A's and E's\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        AECount()
    elif ch == 4:
        exit()