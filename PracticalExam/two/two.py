def create():
    f = open('story.txt', 'w')
    c = 'Whose woods these are I think I know\nHis house is in the village though\nHe will not see me stopping here\nTo watch his woods, fill up with snow'
    f.writelines(c)
    f.close()


def count():
    f = open('story.txt', 'r')
    c = f.read()
    c = c.split(' ')
    for i in c:
        if len(i) == 3:
            print(i, end='\t')
    print()
    f.close()

        
def display():
    f = open('story.txt', 'r')
    c = f.readlines()
    for i in c:
        if i[0] == 'H':
            print(i)
    f.close()


while True:
    print('Menu')
    print('1. Create a file\n2. Count words of length 3\n3. Display lines starting with H\n4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        create()
    elif ch == 2:
        count()
    elif ch == 3:
        display()
    elif ch == 4:
        exit()