import datetime

from pygame import mixer


def alarm():
    print("-----------------------ALARM------------------------")
    mixer.init()
    timeNow = datetime.datetime.now()
    currentDate = timeNow.strftime('%d/%m/%y %H:%M')
    print(f'Current Date and Time is : {currentDate}')

    userInputDate = 'None'
    alarmDate = ''

    while userInputDate not in ('Y', 'N'):
        userInputDate = input('Want to set alarm on same date?(y/n): ').upper()
        if userInputDate == 'Y':
            userInput = input('Please Enter alarm time in %H:%M : ')
            alarmDate = timeNow.strftime('%d/%m/%y') + ' ' + userInput
            print(f'Alarm is set to : {alarmDate}')
        else:
            userInput = input('Please Enter alarm time in %d/%m/%y %H:%M : ')
            alarmDate = userInput
            print(f'Alarm is set to : {alarmDate}')

    while True:
        if datetime.datetime.now().strftime('%d/%m/%y %H:%M') == alarmDate:
            mixer.music.load("./aud/work.mp3")
            mixer.music.play()
            break


def calendar():
    print("----------------------CALENDAR----------------------")
    import calendar
    userInputDate = 'None'
    currentDateTime = datetime.datetime.now()

    while userInputDate not in ('Y', 'N'):
        userInputDate = input('do you want to see the calendar of this month?(y/n): ').upper()
        if userInputDate == 'Y':

            print(calendar.month(currentDateTime.year, currentDateTime.month))
        else:
            year = int(input("Input the year : "))
            month = int(input("Input the month : "))

            print(calendar.month(year, month))


