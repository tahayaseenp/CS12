import csv
L = []


def create():
    k = open("Voters.csv", "w")
    f = csv.writer(k)
    while True:
        VoterID = input("Enter Voter ID: ")
        Votername = input("Enter Voter Name: ")
        Age = input("Enter Age: ")
        L.append([VoterID, Votername, Age])
        ch = input("Do you want to continue? (y/n): ")
        if ch.lower() != "y":
            break

    f.writerows(L)


def display():
    k = open("Voters.csv", "r")
    f = csv.reader(k)
    print("VoterID\t\tVoterName\t\tAge")
    for i in f:
        print(i[0], "\t\t", i[1], "\t\t", i[2])


def search():
    k = open("Voters.csv", "r")
    f = csv.reader(k)
    VoterID = input("Enter Voter ID to be searched: ")
    for i in f:
        if VoterID == i[0]:
            print("Voter ID: ", i[0], "\tVoter Name: ", i[1], "\tAge: ", i[2])
            break
    else:
        print("Voter ID not found")


while True:
    print("Menu")
    print("1. Create File\n2. Display File\n3. Search\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        exit()