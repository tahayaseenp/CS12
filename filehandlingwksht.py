import pickle


def replace():
    f = open("story.txt", "r")
    c = f.read()
    f.close()

    c = c.replace("the", "them")
    f = open("story.txt", "w")
    f.write(c)
    f.close()


def replace_user():
    a = input("Enter a word to replace: ")
    b = input("Enter a word to replace it with: ")
    f = open("poem.txt", "r")
    c = f.read()
    f.close()
    
    c = c.replace(a, b)
    f = open("poem.txt", "w")
    f.write(c)
    f.close()


def length40():
    f = open("school.txt", "r")
    c = f.readlines()
    f.close()
    for i in c:
        if len(i) > 40:
            print(i)


def remove_duplicate():
    f = open("hello.txt", "r")
    c = f.readlines()
    f.close()
    c = list(dict.fromkeys(c))
    f = open("hello.txt", "w")
    f.writelines(c)
    f.close()


def unique_words_only():
    f = open("story.txt", "r")
    c = f.read()
    f.close()
    c = c.split()
    c = list(dict.fromkeys(c))
    for i in c:
        print(i, end=" | ")


def count_vowels():
    f = open("task.txt", "r")
    c = f.read()
    f.close()
    c = c.lower()
    a = e = i = o = u = 0
    for j in c:
        if j.lower() == "a":
            a += 1
        elif j.lower() == "e":
            e += 1
        elif j.lower() == "i":
            i += 1
        elif j.lower() == "o":
            o += 1
        elif j.lower() == "u":
            u += 1

    print("a: ", a, "\ne: ", e, "\ni: ", i, "\no: ", o, "\nu: ", u)


def length7():
    f = open("school.txt", "r")
    c = f.readlines()
    f.close()
    for i in c:
        if len(i) > 7:
            print(i)


def StartTandM():
    f = open("div.txt", "r")
    c = f.readlines()
    f.close()
    count = 0
    for i in c:
        if i[0] == "T" or i[0] == "M":
            count += 1
    print(count)


def StartNotM():
    f = open("div.txt", "r")
    c = f.readlines()
    f.close()
    count = 0
    for i in c:
        if i[0] != "M":
            count += 1
    print(count)


def startm():
    f = open("div.txt", "r")
    c = f.readlines()
    f.close()
    count = 0
    for i in c:
        if i[0] == "m":
            count += 1
    print(count)


def readlineonly():
    f = open("hello.txt", "r")
    m = ""
    while True:
        m += f.readline()
        if f.readline() == "":
            break
    f.close()
    

def copy():
    f = open("story.txt", "r")
    c = f.read()
    f.close()
    f = open("Hello.txt", "w")
    f.write(c)
    f.close()


def copyalternate():
    f = open("story.txt", "r")
    c = f.readlines()
    f.close()
    f = open("Hello.txt", "w")
    for i in range(0, len(c), 2):
        f.write(c[i])
    f.close()


def copywordswithvowels():
    f = open("World.txt", "r")
    c = f.read()
    f.close()
    c = c.split()
    f = open("Entire.txt", "w")
    for i in c:
        if i[0].lower() == "a" or i[0].lower() == "e" or i[0].lower() == "i" or i[0].lower() == "o" or i[0].lower() == "u":
            f.write(i + " ")
    f.close()


def copyaandt():
    f = open("World.txt", "r")
    c = f.read()
    f.close()
    c = c.split()
    f = open("Entire.txt", "w")
    for i in c:
        if i[0].lower() == "a" or i[0].lower() == "t":
            f.write(i + " ")
    f.close()


def printlongestline():
    f = open("World.txt", "r")
    c = f.readlines()
    f.close()
    max = 0
    for i in c:
        if len(i) > max:
            max = len(i)
    print(max)


def notrailingandleadingspaces():
    f = open("story.txt", "r")
    c = f.readlines()
    f.close()
    f = open("World.txt", "w")
    for i in c:
        print(i.strip() + "\n")
    f.close()


def displayallnumbers():
    f = open("sumit.txt", "r")
    c = f.read()
    f.close()
    for i in c:
        print(i) if i.isdigit() == True else None
    

def displaysecondandsecondlast():
    f = open("life.txt", "r")
    c = f.readlines()
    f.close()
    print(c[1], c[-2])


def addrec():
    roomn = input("Enter room no: ")
    price = input("Enter price: ")
    rtype = input("Enter room type: ")
    f = open("data.dat", "wb+")
    pickle.dump([roomn, price, rtype], f)
    f.close()


def disp():
    f = open("data.dat", "rb")
    c = pickle.load(f)
    f.close()
    print(c)


def specific_room(Room_No):
    f = open("data.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if c[0] == Room_No:
            print("Price = ", c[1], "\nRoom Type = ", c[2])
 

def modifi(Room_No):
    f = open("data.dat", "rb+")
    c = pickle.load(f)
    f.close()
    for i in c:
        if c[0] == Room_No:
            print("Price = ", c[1], "\nRoom Type = ", c[2])
            c[1] = input("Enter new price: ")
            c[2] = input("Enter new room type: ")
            f = open("data.dat", "wb+")
            pickle.dump(c, f)
            f.close()
            print("Updated")


def delete(Room_No):
    f = open("data.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if c[0] == Room_No:
            c.remove(i)
    f = open("data.dat", "wb")
    pickle.dump(c, f)
    f.close()
    print("Deleted")


def disp75():
    f = open("student.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if i[3] > 75:
            print(i)


def dispname():
    n = input("Enter name to search: ")
    f = open("student.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if i[1] == n:
            print(i)


def rem():
    f = open("student.dat", "rb")
    c = pickle.load(f)
    f.close()
    for i in c:
        if i[3] < 30:
            c.remove(i)
    f = open("student.dat", "wb")
    pickle.dump(c, f)
    f.close()


def COUNTLINES():
    f = open("TESTFILE.txt", "r")
    c = f.readlines()
    n = 0
    f.close()
    for i in c:
        if i[0].lower() not in 'aeiou':
            n += 1
    print('The number of lines not starting with any vowel -', n)
    

def ETCount():
    f = open("TESTFILE.txt", "r")
    ec = tc = 0
    c = f.read()
    f.close()
    for i in c:
        if i.lower() == 'e':
            ec += 1
        elif i.lower() == 't':
            tc += 1
    print("E or e:", ec)
    print("T or t:", tc)