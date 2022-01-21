
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
