started = False
while True:
    command = input("> ").lower()
    if command == 'help':
        print('''start - start the car
stop - stop the car
quit - to exit''')
    elif command == 'start':
        if not started:
            print("Car started...Ready to go!")
            started = True
        else:
            print("Car already started!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            print('Car Stopped.')
            started = False
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")