"Tuples"
numbers = (5,2,32)
print(numbers[0])
"Tuples's data cannot be modified. In other words, it's data is immutable"

"Unpacking"
coordinates1 = (2,3,4)
coordinates2 = [1,2,3]

x, y, z = coordinates1
i, j, r = coordinates2

print(x, y, z)
print(i, j, r)

"Dictionaries"

" Include 2 parts: {'keywords': data/value (number, string, boolean)} "

Profile = {'Customers': 'Johnny Diep',
            'Major': 'Student',
            'Age': 19,
            'Skills': 'Computer Programming',
            'Is_graduated': False
           }

print(Profile["Customers"])
print(Profile.get("Customers"))

Profile["Education"] = "George Brown College"
print(Profile.get("Birthdate", "10th Oc 2001"))
print(Profile)
"""
    Searching keywords
    1. Check for availability/ existence
    2. Notice case sensitivity (Upper, Lower)
"""

"Exercise 1: type in number result in words"
numbers = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four'}
Phone = input("Phone: ")

"Pro-Solution"
output = ''
for digit in Phone:
    output += numbers.get(digit, 'Invalid') + ' '
print(output)

"Self-Solution"
for ch in Phone:
    if ch in numbers:
        print(numbers[ch])
    else:
        print("Invalid!")
