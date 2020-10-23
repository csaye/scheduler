import datetime

print("Welcome to scheduler! Type \"help\" for help.")

running = True

def getTitle():
    title = ":"
    while (title.find(":") != -1):
        title = input("Please enter an event title: ")
    return title

def getDate():
    valid = False
    while (valid == False):
        try:
            year = int(input("Please enter a year: "))
            valid = True
        except:
            print("Invalid year.")
            continue
    valid = False
    while (valid == False):
        try:
            month = int(input("Please enter a month: "))
            valid = True
        except:
            print("Invalid month.")
            continue
    valid = False
    while (valid == False):
        try:
            day = int(input("Please enter a day: "))
            valid = True
        except:
            print("Invalid day.")
            continue
    try:
        date = datetime.datetime(year, month, day)
        return str(year) + "/" + str(month) + "/" + str(day)
    except:
        print("Invalid date.")
        return getDate()

def write():
    f = open("schedule.txt", "a")
    title = getTitle()
    date = getDate()
    f.write(title + " : " + date + "\n")
    f.close()

def read():
    f = open("schedule.txt", "r")
    for line in f:
        lineParts = line.split(" : ")
        dateParts = lineParts[1].split("/")
        date = datetime.datetime(int(dateParts[0]), int(dateParts[1]), int(dateParts[2]))
        extra = ""
        if (date > datetime.datetime.now()):
            extra = " <- passed"
        print(line.strip() + extra)
    f.close()

def clear():
    f = open("schedule.txt", "w")
    f.write("")
    f.close()

while (running):
    userInput = input("> ")
    if (userInput == "help"):
        print("Commands: help, quit, write, read, clear")
    elif (userInput == "quit"):
        running = False;
    elif (userInput == "write"):
        write()
    elif (userInput == "read"):
        read()
    elif (userInput == "clear"):
        clear()
    else:
        print("Invalid command. Type \"help\" for help.")
