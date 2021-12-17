
#____________________________________________________________________________FUNCTIONS
def askforaword():
    word = input("Enter a word:")
    return word

def amountofaletter():
    word = askforaword()
    letter = input("Enter the letter you want to search:")
    amount = word.count(letter)

    return amount

def writearray():
    i = int(input("Enter the amount of elements you want to add:"))
    array = []
    for i in range(0, i):
        array.append(input("Enter the element you want to add:"))
    return array


def printarray():
    array = writearray()
    print("Your array is: ", array)

def lowercase():
    word = askforaword()
    word = word.lower()
    print(word)

def uppercase():
    word = askforaword()
    word = word.upper()
    print(word)

def readoption(lowerorupper):
    if lowerorupper == 1:
        lowercase()
    else:
        uppercase()
#____________________________________________________________________________FUNCTIONS