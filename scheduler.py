print("Welcome to scheduler! Type \"help\" for help.")

running = True

while (running):
    userInput = input("> ")
    if (userInput == "help"):
        print("Commands: help, quit, new")
    elif (userInput == "quit"):
        running = False;
    elif (userInput == "new"):
        f = open("schedule.txt", "a")
        f.write("hello\n")
        f.close()
    else:
        print("Invalid command. Type \"help\" for help.")
