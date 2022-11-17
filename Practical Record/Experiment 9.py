f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
c = f1.readlines()
L = []
for i in c:
    if 'a' not in i.lower():
        L.append(i)
f2.writelines(L)
f1.close()
f2.close()