# CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS

from Menu_functions import *

#____________________________________________________________________________MENU
aukera = ' '
while aukera != 'D':

    print("------------------------MENU------------------------")
    print("A) Print the word on uppercase or lowercase.")
    print("B) Print the amount of a letter inside a word.")
    print("C) Print an array entered.")
    print("D) Exit.")
    aukera = input().capitalize()
    if aukera == 'A':
        option = -1
        while option != 1 and option != 2:
            print("What do you want to do?")
            print("1) Lower case")
            print("2) Upper case")
            option = int(input('Enter the option: '))
        readoption(option)


    elif aukera == 'B':
        amount = amountofaletter()
        print("The amount of the letter entered on the word is:", amount)
    elif aukera == 'C':
        printarray()
print("Good bye")
#____________________________________________________________________________MENU