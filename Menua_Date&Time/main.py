# CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS

from functions import *

#____________________________________________________________________________MENU
option = -1
tasks = []
while option != 0:
    if option == 0:
        break
    else:
        amount = int(input("Enter the amount of events you want to add:"))
        tasks = addToList(tasks, amount)
        print(tasks)
        option = int(input("Do you want to continue? Press 0 for NO and other numbers for YES"))
#____________________________________________________________________________MENU
