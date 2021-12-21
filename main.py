# CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS
import os
import datetime

from functions import *

#____________________________________________________________________________MENU
aukera = -1
while aukera != 0:
    print("Hello, %s! It is now" %os.getlogin())
    print("------------------------MENU------------------------")
    print("1) Stopwatch") #Count the time something takes
    print("2) Alarm") #Alarm clock that will ring at a determined hour
    print("3) Pomodoro") #automatic timer to work/rest
    print("4) To-do list")  #view or edit to-do list
    print("5) Calendar")
    print("0) Exit.")
    aukera = int(input())
    #if aukera == 1:

    #elif aukera == 2:

    #elif aukera == 3:

    #elif aukera == 4:

print("Goodbye!")
#____________________________________________________________________________MENU