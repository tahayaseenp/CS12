S = []


def isEmpty(S):
    return True if len(S) == 0 else False


def push(S, x):
    S.append(x)
    top = len(S) - 1


def pop(S):
    return "Underflow" if isEmpty(S) else S.pop()


def peek(S):
    return "Underflow" if isEmpty(S) else S[-1]


def show(S):
    print("No elements in the stack") if isEmpty(S) else None
    t = len(S) - 1
    while t >= 0:
        print(S[t], end=' ')
        t -= 1
    print()


while True:
    print("Menu")
    print("1. Push\n2. Pop\n3. Peek\n4. Show\n5. Exit")
    c = int(input("Enter your choice: "))
    if c == 1:
        x = input("Enter the element to be pushed: ")
        push(S, x)
    elif c == 2:
        print(pop(S))
    elif c == 3:
        print(peek(S))
    elif c == 4:
        show(S)
    elif c == 5:
        exit()
    else:
        print("Invalid choice")