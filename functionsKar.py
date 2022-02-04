def printATree():
    num = int(input("Enter the size of the tree: "))

    for i in range(num):
        print(' ' * (num - i - 1) + "*" * (2 * i + 1))

    for n in range(int(num / 2)):
        print(' '
