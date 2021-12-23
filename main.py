#   CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS
import os
import datetime
from functions import *

initialized = False  # will be stored locally for the first time setup (NOT DONE OR PLANNED YET)
name = os.getlogin()  # get the username from the Windows user. Modifiable by the user itself
preferredDateFormat = 1  # will decide the user's date choice, we will attempt to store this locally
userTheme = 1  # will decide the color scheme, we will attempt to store this locally
now = datetime.datetime.now()  # gets the current date
CurrentDate = "%d/%m/%Y"  # formats the current date as 31/12/2000
CurrentDateStr = "%a, %b %d"  # formats the current date as Sun, Dec 31
CurrentTime = "%H:%M"  # formats the current time as 13:30
CurrentTimeSec = "%H:%M:%S"  # formats the current time as 13:30:00
#  ____________________________________________________________________________MENU
menuOption = -1
while menuOption != 0:
    print(f"Hello, {name}! It is now {now.strftime(CurrentTime)} of {now.strftime(CurrentDateStr)}.")
    print("------------------------MENU------------------------")
    print("1) Stopwatch")  # Count the time something takes
    print("2) Alarm")  # Alarm clock that will ring at a determined hour
    print("3) Pomodoro")  # automatic timer to work/rest
    print("4) To-do list")  # view or edit to-do list
    print("5) Calendar")  # print current month or let the user choose
    print(
        "9) Settings")  # (will probably not be added) change a few settings like date format preference, name or theme
    print("0) EXIT")
    print("----------------------------------------------------")
    menuOption = int(input("Choose an option: "))

    #  if menuOption == 1:

    #  elif menuOption == 2:

    #  elif menuOption == 3:

    #  elif menuOption == 4:

    #  elif menuOption == 5:

    #  elif menuOption == 9:

    #  elif menuOption == 0:

    #  else:
    #  print("invalid number")

print("Goodbye!")
#  ____________________________________________________________________________MENU
