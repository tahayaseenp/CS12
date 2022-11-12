def BubbleSort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

print(BubbleSort([10, 5, 74, 57, 54, 77, 69, 420, 1000, 8, 17, 16, 14, 10]))