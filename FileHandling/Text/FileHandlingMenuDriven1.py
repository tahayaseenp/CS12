"""
WAP to read a text file paragraph and display the following:
1. create the file para.txt
2. number of lines
3. number of words
4. number of 'the' words in the file
5. number of digits
6. number of alphanumeric characters
7. number of alphabets
8. number of space
0. exit
"""
import sys


def create_file():
    file = open("para.txt", "w+")
    print("Enter text to write to file")
    text = input("> ")
    file.write(text)
    while True:
        c = input("Write another line? (y/n)")
        if c.lower() != 'y' : break
        else: file.write('\n'+input("> "))
    file.close()
    return "Created successfully"


def lines():
    file = open("para.txt", "r")
    return len(file.readlines())


def words():
    file = open("para.txt", "r")
    return len(file.read().split())


def the():
    file = open("para.txt", "r")
    return file.read().count('the')


def num():
    file = open("para.txt", "r")
    return sum(c.isdigit() for c in file.read())


def alphanum():
    file = open("para.txt", "r")
    return sum(c.isalnum() for c in file.read())


def alpha():
    file = open("para.txt", "r")
    return sum(c.isalpha() for c in file.read())


def space():
    file = open("para.txt", "r")
    return sum(c.isspace() for c in file.read())


while True:
    print("Menu")
    print("1. Create the file para.txt")
    print("2. Count number of lines")
    print("3. Count number of words")
    print("4. Count number of 'the' words in the file")
    print("5. Count number of digits")
    print("6. Count number of alphanumeric characters")
    print("7. Count number of alphabets")
    print("8. Count number of space")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print(create_file())
        print()

    elif ch == 2:
        print(lines())
        print()

    elif ch == 3:
        print(words())
        print()

    elif ch == 4:
        print(the())
        print()

    elif ch == 5:
        print(num())
        print()
    
    elif ch == 6:
        print(alphanum())
        print()
    
    elif ch == 7:
        print(alpha())
        print()
    
    elif ch == 8:
        print(space())
        print()

    elif ch == 0:
        sys.exit("Bye")
    
    else:
        print("Wrong choice!\n")