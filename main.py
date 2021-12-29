#   CREATE A MENU WITH DIFFERENT OPTIONS THAT WILL BE ABLE TO WORK WITH STRINGS
import linecache
import os
import datetime
from functions import *

#  ___________________________________________________________________________SAVE AND LOAD DATA
if not(os.path.isfile("data.txt")):   # if data.txt does not exist
    create()   # creates save file


with open("data.txt", "r") as dataFile:  # these variables are stored locally, this opens data.txt in read mode
    name = linecache.getline('data.txt', 1).replace("", "")[:-1]  # username, defaults to windows username
    preferredDateFormat = linecache.getline('data.txt', 2).replace("", "")[:-1]  # the user's date format choice
    withSeconds = linecache.getline('data.txt', 3).replace("", "")[:-1]  # decides if the clock will show seconds
    userTheme = linecache.getline('data.txt', 4).replace("", "")[:-1]  # decides the color scheme
    keepItClean = linecache.getline('data.txt', 5)  # decides if lines will be cleared after returning to main menu

load(name, preferredDateFormat, withSeconds, userTheme, keepItClean)

#  ____________________________________________________________________________DATE AND TIME VARIABLES
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
    print("1) Stopwatch")  # count the time something takes
    print("2) Alarm")  # alarm clock that will ring at a determined hour
    print("3) Pomodoro")  # automatic timer to work/rest
    print("4) To-do list")  # view or edit to-do list
    print("5) Calendar")  # print current month or let the user choose
    print("9) Settings")  # change a few settings like date format preference, name or theme
    print("0) EXIT")
    print("----------------------------------------------------")
    menuOption = int(input("Choose an option: "))

    if menuOption == 1:
        stopwatch()
    elif menuOption == 2:
        alarm()
    elif menuOption == 3:
        pomodoro()
    elif menuOption == 4:
        todo()
    elif menuOption == 5:
        calendar()
    elif menuOption == 9:
        settings()
    elif menuOption == 0:
        print("Goodbye!")
    else:
        print("invalid number")
