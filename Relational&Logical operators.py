"Relational/ comparison operators: <, >, <=, >=, =="
"Logical operator: and, or, not"

'Exercise 1:'
name = "NA"
is_named = input("Do you want to create your username (Y/N))? ")
if is_named.upper() == "Y":
    name = input("What's your name? ")
    if len(name) < 3:
        print("Your name must be at least 3 characters")
    elif len(name) > 50:
        print("Your name must not be over 50 characters ")
    else:
        print(f"Hi! {name}")
elif is_named.upper() == "N":
    print("Ok! See ya later!")
else:
    print("Invalid input!")

'Exercise 2:'
weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ").upper()
while unit != "L" and unit !="K":
    print("Invalid choice! Enter again (L or K)!")
    unit = input("(L)bs or (K)g: ").upper()
if unit == "L":
    print("Your Kg is", weight * 0.45)
else:
    print("Your Lbs is:", weight / 0.45)

'Exercise 3:'

is_running = True
is_start = False
is_stop = False
while is_running:
    prompt = input("> ").lower()
    if prompt == "help":
        print('''
start - to start the run
stop - to stop the car
exit - to exit the game''')
    elif prompt == "start":
        if is_start:
            print("Car is already started!")
            is_stop = False
        else:
            print("Car is ready to race!")
        is_start = True
    elif prompt == "stop":
        if is_stop:
            print("car is already stopped!")
            is_start = False
        else:
            print("car is stopped!")
        is_stop = True
    elif prompt == "exit":
        is_running = False
    else:
        print("Invalid choice! Enter your option again!")
print("See ya in the next game!")