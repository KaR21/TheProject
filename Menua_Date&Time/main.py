# CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS

from functions import *

#____________________________________________________________________________MENU
def sartulistan():
    tasks=[]
    task=[]
    for i in range(2):
        TName=input("Enter the name of the task:")
        task.append(TName)
        deadline=input("Enter the deadline")
        task.append(deadline)
        tasks.append(task)
    return tasks

def badago(pertsonak,abizena):
    for i in range (2):
        if pertsonak[i][2]==abizena:
            return pertsonak[i]

e=sartulistan()
abizena=input("Sar ezazu nahi duzun pertsonaren abizena:")
abiz=badago(e,abizena)

print(abiz)

#____________________________________________________________________________MENU