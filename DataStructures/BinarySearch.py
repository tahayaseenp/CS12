def BinarySearch(L, s):
    L.sort()
    low = found = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == s:
            found = 1
            break
        elif L[mid] > s:
            high = mid - 1
        else:
            low = mid + 1
    if found == 1:
        return "Element found"
    else:
        return "Element not found"

print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))