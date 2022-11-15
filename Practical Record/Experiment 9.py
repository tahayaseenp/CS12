f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
c = f1.readlines()
for i in c:
    if 'a' in i:
        c.remove(i)
f2.writelines(c)
f1.close()
f2.close()