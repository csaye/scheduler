print("Welcome to scheduler! Type \"help\" for help.")

running = True

while (running):
    userInput = input("> ")
    if (userInput == "help"):
        print("Commands: help, quit, write, read")
    elif (userInput == "quit"):
        running = False;
    elif (userInput == "write"):
        f = open("schedule.txt", "a")
        f.write("hello\n")
        f.close()
    elif (userInput == "read"):
        f = open("schedule.txt", "r")
        print(f.read())
        f.close()
    else:
        print("Invalid command. Type \"help\" for help.")
