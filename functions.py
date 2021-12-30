import os
import linecache
from colorama import init, Fore, Back, Style


class Config:
    def __init__(self):
        self.name = linecache.getline('data.txt', 1).replace("", "")[:-1]
        self.date = linecache.getline('data.txt', 2).replace("", "")[:-1]
        self.seconds = linecache.getline('data.txt', 3).replace("", "")[:-1]
        self.theme = linecache.getline('data.txt', 4).replace("", "")[:-1]
        self.clean = linecache.getline('data.txt', 5).replace("", "")


def data():
    return Config()


d = data()


def create():
    with open("data.txt", "w", encoding="utf-8") as f:  # opens data.txt in write mode to edit settings
        d.name = os.getlogin()   # defaults name to the windows username
        d.date = 1  # defaults the date format to DD/MM/YYYY
        d.seconds = False  # defaults clock to not to show seconds
        d.theme = 1  # defaults theme to classic
        d.clean = False  # defaults to not clearing the terminal after switching menus


def save():
    with open("data.txt", "w", encoding="utf-8") as f:  # opens data.txt in write mode to save settings
        f.writelines(f"{d.name}\n")
        f.writelines(f"{d.date}\n")
        f.writelines(f"{d.seconds}\n")
        f.writelines(f"{d.theme}\n")
        f.writelines(f"{d.clean}")
    print("* Data has been saved")


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
    settings_option = -1
    while settings_option != 0:
        print("----------------------SETTINGS----------------------")
        print("1) Change name")  # change the username
        print("2) Change date format")  # change preferred date format for the calendar
        print("3) Show/hide seconds in the main menu")  # show or hide seconds in the main menu's clock
        print("4) Choose theme")  # change the colors of the interface
        print("5) Clean terminal")  # clean the terminal when you come back to the main menu
        print("9) Credits")  # credits
        print("0) MAIN MENU")   # go back to the main menu
        print("----------------------------------------------------")
        settings_option = int(input("Choose an option: "))
        if settings_option == 1:
            d.name = input("Enter your name: ")
        elif settings_option == 2:
            print("Choose your favorite date format for the calendar:")
            print("1) DD/MM/YYYY")
            print("2) MM/DD/YYYY")
            print("3) YYYY/MM/DD")
            tempinput = int(input("Choose a format: "))
            if tempinput == 1 or tempinput == 2 or tempinput == 3:
                d.date = tempinput
            else:
                print("Invalid input.")
        elif settings_option == 3:
            print("Do you want to see seconds in the main menu's clock?")
            print("1) Yes")
            print("2) No")
            tempinput = int(input("Choose an option: "))
            if tempinput == 1:
                d.seconds = True
            elif tempinput == 2:
                d.seconds = False
            else:
                print("Invalid input.")
        elif settings_option == 4:
            print("Choose a theme:")
            print("1) Classic")
            print("2) Kinda light")
            print("3) Hax0r")
            tempinput = int(input("Choose an option: "))
            if tempinput == 1:
                print(Style.RESET_ALL)
                d.theme = 1
            elif tempinput == 2:
                print(Back.WHITE + Fore.BLACK)
                d.theme = 2
            elif tempinput == 3:
                print(Back.BLACK + Fore.GREEN)
                d.theme = 3
        elif settings_option == 5:
            calendar()
        elif settings_option == 9:
            settings()
        elif settings_option == 0:
            print("* Saving changes...")
        else:
            print("invalid number")


def restore_theme():
    if d.theme == 1:
        print(Style.RESET_ALL)
    elif d.theme == 2:
        print(Back.WHITE + Fore.BLACK)
    elif d.theme == 3:
        print(Back.BLACK + Fore.GREEN)
