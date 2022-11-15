def search_in_string():
    s = input("Enter a string: ")
    t = input("Enter a substring to search in string: ")
    if t in s:
        print("Substring found")
        print("The number of times the substring is present in the string is", s.count(t))
    else:
        print("Substring not found")


search_in_string()