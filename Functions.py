'Function, parameters, argument keywords, and return statement'


def cal_total(num1, num2):
    total = num1 + num2
    return total

number1 = 30
number2 = 30
print(cal_total(num1 = 30, num2 = 30))

"keyword argument should come after the positional argument"
"keyword argument improve the readability of the code"

'Exceptions'

'0 => interpret/ compile sucessfully, 1 => unsucessful interpration'
'''
    try: 
    except
    is used to handle anticipated problem in programming 
'''

is_correct = True
while is_correct:
    try:
        birthyear = int(input("Enter your birthyear: "))
        ratio_of_age = 2020/birthyear
        print(ratio_of_age)
        is_correct = False
    except ValueError:
        is_correct = True
        print('Invalid input!')
    except ZeroDivisionError:
        is_correct = True
        print('Input cannot be 0')

'Add as many as except(s) for the anticipated error'

# This is the correct form of comment
# Use comment to explain why/ how not what and make note.
