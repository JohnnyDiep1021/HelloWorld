First = input("What's your fist name? ")
Last = input("What's your last name? ")
son = input("What is your year of birth? ")
father = input("What is your father's year of birth? ")

'No need for declaring the data type for the variable in Pythons'
'an input/ typed-in character will be considered as string which need to be converted for numeric calculation'
'using single/double quotation mark for writing comment which will be ignored by the compiler'
'datatype() [int(), float(),...etc] is a function using for numeric conversion'
'''using '''''' (triple quotation mark) for typing multiple lines of word/ sentence'''

num_of_word = int(father)
print(num_of_word)
msg = f"{First} [{Last}] is a coder"
print(msg + ".", First + Last, "is less than his father",  int(son) - int(father), "year(s) old")
