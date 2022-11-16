L = []
d = {}


def findmostoccuringdomain():
    while True:
        c = input("Enter phishing emails (enter q to exit loop): ")
        if c == "q":
            break
        else:
            L.append(c)
    for i in range(len(L)):
        L[i] = L[i].split("@")[1]

    for i in L:
        d[i] = d.get(i, 0) + 1

    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
            domain = i
    print("\nMost occuring domain is", domain, "with", max, "occurences")


findmostoccuringdomain()