import datetime
from functions import *
#  ___________________________________________________________________________SAVE AND LOAD DATA
if not(os.path.isfile("data.txt")):   # if data.txt does not exist
    create()   # creates save file with default data
    save()
# restore_theme() used to restore color scheme when it was a thing

#  ____________________________________________________________________________DATE AND TIME VARIABLES
now = datetime.datetime.now()  # gets the current date
CurrentDate = "%d/%m/%Y"  # formats the current date as 31/12/2000
CurrentDateStr = "%a, %b %d"  # formats the current date as Sun, Dec 31
CurrentTime = "%H:%M"  # formats the current time as 13:30
CurrentTimeSec = "%H:%M:%S"  # formats the current time as 13:30:00

#  ____________________________________________________________________________MENU
menuOption = -1
while menuOption != 0:
    if d.clean:   # will clear the terminal if the user asked to do so
        clear()
    if d.seconds:
        print(f"Hello, {d.name}! It is now {now.strftime(CurrentTimeSec)} of {now.strftime(CurrentDateStr)}.")
    else:
        print(f"Hello, {d.name}! It is now {now.strftime(CurrentTime)} of {now.strftime(CurrentDateStr)}.")
    print("------------------------MENU------------------------")
    print("1) Stopwatch")  # count the time something takes
    print("2) Alarm")  # alarm clock that will ring at a determined hour
    print("3) Pomodoro")  # automatic timer to work/rest
    print("4) To-do list")  # view or edit to-do list
    print("5) Calendar")  # print current month or let the user choose
    print("6) Other functions")
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
        thecalendar()
    elif menuOption == 6:
        others()
    elif menuOption == 9:
        settings()
        save()
    elif menuOption == 0:
        print("Goodbye!")
        input("Press enter to close...")
    else:
        print("invalid number")
