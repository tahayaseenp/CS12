def split():
    f = open("data.txt", "r")
    for line in f.readlines():
        print(line.replace(' ', '#'), end='')
    f.close()


split()