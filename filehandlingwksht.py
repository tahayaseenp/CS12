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
    f = open("story.txt", "w")
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
    f = open("div.txt", "r")
    m = ""
    m += f.readline()
    
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