"""
stack = []
SItem = {"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}


def Push(SItem):
    for i in SItem:
        if SItem[i] > 75:
            stack.append(i)

def Pop():
    if len(stack) == 0:
        print("Stack is empty")

    else:
        for i in stack:
            if i[0].lower() == 'p':
                stack.remove(i)
"""


status = []

def Push_element(list):
    for i in list:
        if i[2] == 'Goa':
            status.append([i[0], i[1]])


def Pop_element():
    if status != []:
        print(status.pop())

    else:
        print("Stack Empty")


def COUNTLINES():
    fobj = open("TESTFILE.txt", "r")
    c = fobj.readlines()
    fobj.close()
    count = 0
    for i in c:
        if i[0].lower() not in 'aeiou':
            count += 1
    print("The number of lines not starting with any vowel -", count)