def LinearSearch():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    c = eval(input("Enter element to search : "))
    for i in range(len(L)):
        if L[i] == c:
            print("Element found at index", i)
            break
    else:
        print("Element not found")


def BinarySearch():
    L = [eval(i) for i in input("Enter the list items : ").split()]
    c = eval(input("Enter element to search : "))
    L.sort()
    low = found = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == c:
            found = 1
            break
        elif L[mid] > c:
            high = mid - 1
        else:
            low = mid + 1
    if found == 1:
        print("Element found")
    else:
        print("Element not found")


LinearSearch()
BinarySearch()