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
is_stop = False

while is_running:
    prompt = input("> ").lower()
    if prompt == "help":
        print('''
start - to start the run
stop - to stop the car
exit - to exit the game''')
    elif prompt == "start":
        if is_stop:
            print("Car is already started!")
        else:
            print("Car is ready to race!")
        is_stop = True
    elif prompt == "stop":
        if not is_stop:
            print("car is already stopped!")

        else:
            print("car is stopped!")
            is_stop = False
    elif prompt == "exit":
        is_running = False
    else:
        print("Invalid choice! Enter your option again!")
goodbye = "See ya in the next game!"
if ("See ya" in goodbye):
    print(goodbye)