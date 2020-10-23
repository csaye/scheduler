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
            continue
    valid = False
    while (valid == False):
        try:
            month = int(input("Please enter a month: "))
            valid = True
        except:
            continue
    valid = False
    while (valid == False):
        try:
            day = int(input("Please enter a day: "))
            valid = True
        except:
            continue
    try:
        return datetime.datetime(year, month, day)
    except:
        return getDate()

def write():
    f = open("schedule.txt", "a")
    title = getTitle()
    date = getDate().strftime("%x")
    f.write(title + ":" + date + "\n")
    f.close()

def read():
    f = open("schedule.txt", "r")
    print(f.read())
    f.close()

while (running):
    userInput = input("> ")
    if (userInput == "help"):
        print("Commands: help, quit, write, read")
    elif (userInput == "quit"):
        running = False;
    elif (userInput == "write"):
        write()
    elif (userInput == "read"):
        read()
    else:
        print("Invalid command. Type \"help\" for help.")
