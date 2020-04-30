command = ""
started = False

# while command != "quit":
while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("The Car Already Started: ")
        else:
            started = True
            print("The Car Started")

    elif command == "stop":
        if not started:
            print("The Car Already Stoped: ")

        else:
            started= False
            print("The Car Stopped")


    elif command == "help":
        print(f'''
        start- to start the car
        stop- to stop the car
        help- to see help ''')

    elif command == "quit":
        break

    else:
        print("Can not understand: ")
