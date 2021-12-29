import os
import linecache


def create():
    with open("data.txt", "w", encoding="utf-8") as f:  # opens data.txt in write mode to edit settings
        f.writelines(f"{os.getlogin()}\n")  # defaults name to the windows username
        f.writelines("1\n")  # defaults the date format to DD/MM/YYYY
        f.writelines("False\n")  # defaults clock to not to show seconds
        f.writelines("1\n")  # defaults theme to classic
        f.writelines("False")  # defaults to not clearing the terminal after switching menus


def load(name, preferredDateFormat, withSeconds, userTheme, keepItClean):
    with open("data.txt", "r") as dataFile:  # these variables are stored locally, this opens data.txt in read mode
        name = linecache.getline('data.txt', 1).replace("", "")[:-1]  # username, defaults to windows username
        preferredDateFormat = linecache.getline('data.txt', 2).replace("", "")[:-1]  # the user's date format choice
        withSeconds = linecache.getline('data.txt', 3).replace("", "")[:-1]  # decides if the clock will show seconds
        userTheme = linecache.getline('data.txt', 4).replace("", "")[:-1]  # decides the color scheme
        keepItClean = linecache.getline('data.txt', 5)  # decides if lines will be cleared after returning to main menu



def stopwatch():
    print("---------------------STOPWATCH---------------------")


def alarm():
    print("-----------------------ALARM-----------------------")


def pomodoro():
    print("----------------------POMODORO----------------------")


def todo():
    print("---------------------TO DO LIST---------------------")


def calendar():
    print("----------------------CALENDAR----------------------")


def settings():
    print("----------------------SETTINGS----------------------")
