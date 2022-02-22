import csv

def csvManagement():
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

    f = open("names.csv", 'r')
    with f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        print(headers)
        for row in reader:
            print(row['first_name'], row['last_name'])

