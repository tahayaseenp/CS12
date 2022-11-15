def BubbleSort():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


print(BubbleSort())