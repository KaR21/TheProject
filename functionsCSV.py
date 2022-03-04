import csv

def csvManagement():
    print("------------------------MENU------------------------")
    print("1) Write")  # count the time something takes
    print("2) Read")  # alarm clock that will ring at a determined hour
    print("3) search")  # automatic timer to work/rest
    print("0) EXIT")
    print("----------------------------------------------------")
    menuOption = int(input("Choose an option: "))

    if menuOption == 1:
        write()
    elif menuOption == 2:
        read()
    elif menuOption == 3:
        search()




def write():
    f = open("names.csv", 'w')
    with f:
        fnames = ('first_name', 'last_name')
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        a = 'y'
        while a == 'y':
            fn = input("Enter a first name")
            sn = input("Enter a last name")
            writer.writerow({'first_name': fn, 'last_name': sn})
            a = input("Do you want to add another people? y/n")

def read():
    f = open("names.csv", 'r')
    with f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        print(headers)
        i = 0
        for row in reader:
            print(row['first_name'], row['last_name'])

    print(row)

def search():
    f = open("names.csv", 'r')
    with f:
        reader = csv.DictReader(f)

        for row in reader:
            answer = 1
            while(answer == 1):

                print("Do you want to search someone?")
                print("0) NO")
                print("1) YES")
                answer = int(input())
                if(answer == 1):
                    print("Who do yo want to search?")
                    name = input("Enter the name: ")
                    if name in reader:
                      print(row['first_name'], row['last_name'])

                elif(answer == 0):
                    answer = 0
