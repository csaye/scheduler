print("Welcome to scheduler! Type \"help\" for help.")

running = True

while (running):
    userInput = input("> ")
    if (userInput == "help"):
        print("Commands: help, quit")
    elif (userInput == "quit"):
        running = False;
