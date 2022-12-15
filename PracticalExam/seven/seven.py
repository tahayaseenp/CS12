Arr = []
stack = []


def create():
    global Arr
    Arr = [int(x) for x in range(int(input("Enter max range of numbers: ")) + 1)]

def Push(Arr):
    global stack
    for i in Arr:
        if i % 5 == 0:
            stack.append(i)
    print("Stack: ", stack)


def Pop():
    print("Popped element: ", stack.pop())


def Display():
    print("Stack: ")
    for i in stack[::-1]:
        print(i, end=" ")
    print()

while True:
    print("Menu")
    print("1. Create\n2. Push\n3. Pop\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create()
    elif choice == 2:
        Push(Arr)
    elif choice == 3:
        Pop()
    elif choice == 4:
        Display()
    elif choice == 5:
        exit()