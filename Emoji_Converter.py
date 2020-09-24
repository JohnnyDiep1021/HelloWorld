
def emoji(prompt):
    emoji = prompt.split()
    emo = {
        ';)': '😉',
        ":)": "😊",
        ":(": "🙁"
    }
    output = ""
    for icon in emoji:
        output += emo.get(icon, icon) + " "
    return output
user = input("> ")
print(emoji(user))

"Exercise 1: get clerks' information and calculate their salary"
nofs = int(input("Enter the number of employee: "))
Name = ""
ID = ""
WorkingHours = ""
employee = [Name, ID, WorkingHours]
for i in range(nofs):
    Name = input("What your name? ")
    ID = input("Enter your ID: ")
    WorkingHours = input("Enter your wage/h: ")
    employee[i] = [Name, ID, WorkingHours]
print(employee[0][2])
MinimumSalary = (40, 60, 80)
staff, manager, director = MinimumSalary

for i in range(nofs):
    if int(employee[i][2]) <= 40:
        print(f'Staff get ${staff}/hour(s)')
    elif int(employee[i][2]) <= 60:
        print(f'Manager get ${manager}/hour(s)')
    else:
        print(f'Director get ${director}/hour(s)')