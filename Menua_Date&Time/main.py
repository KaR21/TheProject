# CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS

from functions import *

#____________________________________________________________________________MENU
amount = -1
tasks = []
while amount != 0:
    if amount == 0:
        break
    else:
        tasks = addToList(tasks)
        print(tasks)
        amount = int(input("Do you want to continue? Press 0 for NO and other numbers for YES"))
#____________________________________________________________________________MENU
