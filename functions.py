import os
import linecache
import time
import datetime
import calendar

# from colorama import Fore, Back, Style
from pygame import mixer


class Config:
    def __init__(self):
        self.name = linecache.getline('data.txt', 1).replace("", "")[:-1]
        self.date = linecache.getline('data.txt', 2).replace("", "")[:-1]
        self.seconds = linecache.getline('data.txt', 3).replace("", "")[:-1]
        self.theme = linecache.getline('data.txt', 4).replace("", "")[:-1]
        self.clean = linecache.getline('data.txt', 5).replace("", "")[:-1]
        if linecache.getline('data.txt', 6) == "":
            self.stopwatch = None
        else:
            self.stopwatch = linecache.getline('data.txt', 6)


def data():
    return Config()


d = data()


def create():
    with open("data.txt", "w", encoding="utf-8"):  # opens data.txt in write mode to edit settings
        d.name = os.getlogin()  # defaults name to the windows username
        d.date = 1  # defaults the date format to DD/MM/YYYY
        d.seconds = False  # defaults clock to not to show seconds
        d.theme = 1  # defaults theme to classic
        d.clean = True  # defaults to clearing the terminal after switching menus
        d.stopwatch = None   # lets stopwatch save a null value


def save():
    with open("data.txt", "w", encoding="utf-8") as f:  # opens data.txt in write mode to save settings
        f.writelines(f"{d.name}\n")
        f.writelines(f"{d.date}\n")
        f.writelines(f"{d.seconds}\n")
        f.writelines(f"{d.theme}\n")
        f.writelines(f"{d.clean}\n")
        if d.stopwatch is None:
            f.writelines("")
        else:
            f.writelines(f"{d.stopwatch} ")
    print("* Data has been saved")


def stopwatch():
    stopwatch_option = -1
    while stopwatch_option != 0:
        print("---------------------STOPWATCH----------------------")
        print("What do you want to do?")
        if d.stopwatch is None:
            print("1) Start stopwatch")
            print("0) MAIN MENU")
            stopwatch_option = int(input("Choose an option: "))
            if stopwatch_option == 1:
                d.stopwatch = int(time.time())
                print("Stopwatch started.")
                save()
            elif stopwatch_option != 0:
                print("Invalid number")
        else:
            print("1) Stop stopwatch")
            print("0) MAIN MENU")
            stopwatch_option = int(input("Choose an option: "))
            if stopwatch_option == 1:
                end = int(time.time())
                elapsed = int(end) - int(d.stopwatch)
                if elapsed > 60:
                    elapsedmin = int(elapsed / 60)
                    elapsed = elapsed - 60 * elapsedmin
                    print(f"Your elapsed time is {elapsedmin} minutes and {elapsed} seconds")
                else:
                    print(f"Your elapsed time is {elapsed} seconds")
                d.stopwatch = None
                input("Press enter to continue...")
                save()


def alarm():
    print("-----------------------ALARM------------------------")
    mixer.init()
    timeNow = datetime.datetime.now()
    currentDate = timeNow.strftime('%d/%m/%y %H:%M')
    print(f'Current Date and Time is : {currentDate}')

    user_input_date = 'None'
    alarm_date = ''

    while user_input_date not in ('Y', 'N'):
        user_input_date = input('Want to set alarm on same date?(y/n): ').upper()
        if user_input_date == 'Y':
            user_input = input('Please Enter alarm time in %H:%M : ')
            alarm_date = timeNow.strftime('%d/%m/%y') + ' ' + user_input
            print(f'Alarm is set to : {alarm_date}')
        else:
            user_input = input('Please Enter alarm time in %d/%m/%y %H:%M : ')
            alarm_date = user_input
            print(f'Alarm is set to : {alarm_date}')

    while True:
        if datetime.datetime.now().strftime('%d/%m/%y %H:%M') == alarm_date:
            mixer.music.load("./aud/work.mp3")
            mixer.music.play()
            break
        input("Press enter to continue...")


def pomodoro():
    mixer.init()
    pomodoro_option = -1
    while pomodoro_option != 0:
        print("----------------------POMODORO----------------------")
        print("WARNING: Once you enable Pomodoro mode you won't be")
        print("able to use the rest of the features here. The only")
        print("way to stop it is to close the program.")
        print("Learn more in the HELP (9) section.")
        print()
        print("What do you want to do?")
        print("1) Start")
        print("9) Help")
        print("0) MAIN MENU")
        print("----------------------------------------------------")
        pomodoro_option = int(input("Choose an option: "))
        print(pomodoro_option)
        if pomodoro_option == 1:
            pomodoro_time = -1   # the index of the options
            pomodoro_work = 0   # amount of work minutes
            pomodoro_rest = 0  # amount of rest minutes
            pomodoro_current = "stop"   # current pomodoro status (start/stop)
            clear()
            while pomodoro_time != 0:
                print("----------------------POMODORO----------------------")
                print("Please choose an option:")
                print("1) 50/10")
                print("2) 25/5")
                print("3) 45/15")
                print("0) EXIT")
                print()
                print("If you don't know how this mode works, return to the HELP menu.")
                print("----------------------------------------------------")
                pomodoro_time = int(input("Choose an option: "))
                if pomodoro_time == 1:
                    pomodoro_work = 50
                    pomodoro_rest = 10
                    pomodoro_current = "start"
                elif pomodoro_time == 2:
                    pomodoro_work = 25
                    pomodoro_rest = 5
                    pomodoro_current = "start"
                elif pomodoro_time == 3:
                    pomodoro_work = 45
                    pomodoro_rest = 15
                    pomodoro_current = "start"
                elif pomodoro_time == 0:
                    break
                else:
                    print("invalid number")
                if pomodoro_current == "start":
                    clear()
                    pomodoro_time = 0   # discards menu choice to avoid a bug
                    pomodoro_work_restore = pomodoro_work
                    pomodoro_rest_restore = pomodoro_rest
                    while pomodoro_current == "start":
                        mixer.music.load("./aud/work.mp3")
                        mixer.music.play()
                        while pomodoro_work > 0:
                            print("-------------------------------POMODORO-------------------------------".center(70))
                            print()
                            print("The only way to exit Pomodoro mode is by closing the program.".center(70))
                            print()
                            print("----------------------------------------------------------------------".center(70))
                            print("Time to work!".center(70))
                            if pomodoro_work != 1:
                                print(f"{pomodoro_work} minutes left".center(70))
                            else:
                                print("Less than a minute left".center(70))
                            print("----------------------------------------------------------------------".center(70))
                            time.sleep(60)
                            pomodoro_work = pomodoro_work - 1
                            clear()
                        pomodoro_work = pomodoro_work_restore
                        mixer.music.load("./aud/rest.mp3")
                        mixer.music.play()
                        while pomodoro_rest > 0:
                            print("----------------------POMODORO----------------------".center(70))
                            print()
                            print("The only way to exit Pomodoro mode is by closing the program.".center(70))
                            print()
                            print("----------------------------------------------------")
                            print("Time to rest!".center(70))
                            if pomodoro_rest != 1:
                                print(f"{pomodoro_rest} minutes left".center(70))
                            else:
                                print("Less than a minute left".center(70))
                            print("----------------------------------------------------")
                            time.sleep(60)
                            pomodoro_rest = pomodoro_rest - 1
                            clear()
                        pomodoro_rest = pomodoro_rest_restore
                else:
                    print("An exception has occurred.")

        elif pomodoro_option == 9:
            clear()
            print("-------------------POMODORO HELP--------------------")
            print("Welcome to Pomodoro, a technique to work or study")
            print("and take breaks in previously determined intervals.")
            print("By reading this short guide, you'll learn how to use")
            print("this mode in its intended way.")
            print("----------------------------------------------------")
            print("(1/5)".center(70))
            print()
            input("Press enter to continue...")
            clear()
            print("-------------------POMODORO HELP--------------------")
            print("Remember that, because this is a focusing mode, you")
            print("will not be able to access most features from here,")
            print("you will only the timer of the pomodoro.")
            print("The timer will have different time options.")
            print("----------------------------------------------------")
            print("(2/5)".center(70))
            print()
            input("Press enter to continue...")
            clear()
            print("-------------------POMODORO HELP--------------------")
            print("These time options contain two amounts of minutes,")
            print("the first one is for productivity, the second one is")
            print("to take a break. For example, 25/5 means 25 for work,")
            print("5 to rest. In the next slide you will hear a sound.")
            print("----------------------------------------------------")
            print("(3/5)".center(70))
            print()
            input("Press enter to continue...")
            mixer.music.load("./aud/work.mp3")
            mixer.music.play()
            clear()
            print("-------------------POMODORO HELP--------------------")
            print("This sound will be played when you enter work mode,")
            print("that is, you will have to start working when you hear")
            print("this sound. After finishing work mode and entering rest")
            print("mode, you will hear another one, it's in the next page.")
            print("----------------------------------------------------")
            print("(4/5)".center(70))
            print()
            input("Press enter to continue...")
            clear()
            mixer.music.load("./aud/rest.mp3")
            mixer.music.play()
            print("-------------------POMODORO HELP--------------------")
            print("This other sound will play when you enter rest mode,")
            print("which means you can take a break for a few minutes. Don't")
            print("worry if you miss a sound, this program will also show the")
            print("current pomodoro status on its window.")
            print("----------------------------------------------------")
            print("(5/5)".center(70))
            print()
            input("Press enter to continue...")
            clear()
        elif pomodoro_option != 0:
            print("Invalid number")


def todo():
    print("---------------------TO DO LIST---------------------")


def thecalendar():
    print("----------------------CALENDAR----------------------")
    user_input_date = 'None'
    current_date_time = datetime.datetime.now()

    while user_input_date not in ('Y', 'N'):
        user_input_date = input('do you want to see the calendar of this month?(y/n): ').upper()
        if user_input_date == 'Y':
            print(calendar.month(current_date_time.year, current_date_time.month))
        else:
            year = int(input("Input the year : "))
            month = int(input("Input the month : "))

            print(calendar.month(year, month))
        input("Press enter to continue...")


def settings():
    settings_option = -1
    while settings_option != 0:
        print("----------------------SETTINGS----------------------")
        print("1) Change name")  # change the username
        print("2) Change date format")  # change preferred date format for the calendar
        print("3) Show/hide seconds in the main menu")  # show or hide seconds in the main menu's clock
        print("4) Clean terminal")  # clean the terminal when you come back to the main menu
        # print("5) Choose theme")  # change the colors of the interface
        print("9) Credits")  # credits
        print("0) MAIN MENU")  # go back to the main menu
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
            print("Do you want to clear the terminal after each operation?")
            print("1) Yes")
            print("2) No")
            tempinput = int(input("Choose an option: "))
            if tempinput == 1:
                d.clean = True
            elif tempinput == 2:
                d.clean = False
            else:
                print("Invalid input.")
                '''
        elif settings_option == 5:
            print("Choose a theme:")
            print("1) Classic")
            print("2) Miami")
            print("3) Hax0r")
            print("4) ")
            tempinput = int(input("Choose an option: "))
            if tempinput == 1:
                print(Style.RESET_ALL)
                d.theme = 1
            elif tempinput == 2:
                print(Back.BLACK + Fore.MAGENTA)
                d.theme = 2
            elif tempinput == 3:
                print(Back.BLACK + Fore.GREEN)
                d.theme = 3
                '''
        elif settings_option == 9:
            clear()
            print("----------------------CREDITS-----------------------")
            print("------MADE BY------".center(51))
            print("GitPushErlantz".center(51))
            print("KaR21".center(51))
            print("markelrodri1".center(51))
            print("-------------------".center(51))
            print()
            print("----------AUDIO LIBRARIES----------".center(51))
            print("Pomodoro SFX: soundeffect-lab.info".center(51))
            print("-----------------------------------".center(51))
            print("----------------------------------------------------".center(51))
            input("Press enter to continue...")
            clear()
        elif settings_option == 0:
            print("* Saving changes...")
        else:
            print("invalid number")


'''
# THEME RESTORER (unnecessary)
def restore_theme():
    print(Style.RESET_ALL)
    if d.theme == 2:
        print(Back.WHITE + Fore.BLACK)
    elif d.theme == 3:
        print(Back.BLACK + Fore.GREEN)
'''


def clear():   # clears the terminal
    # for cmd
    if os.name == 'nt':
        _ = os.system('cls')

    # for bash
    else:
        _ = os.system('clear')


def others():
    tempinput = -1
    print("----------------------OTHERS---------------------")
    print("What do you want to do?")
    print("1) Draw a number triangle")
    print("0) MAIN MENU")
    tempinput = int(input("Choose an option:"))
