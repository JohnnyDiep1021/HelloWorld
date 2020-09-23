greet = "Hello everyone"

'len() return the number of character in the string literal'
num_of_word = len(greet)

print("The number of character in greet =", num_of_word)
print(greet.upper())
print(greet.lower())

'find() look for the exact index of the available character in the string-literal'
print(greet.find("o"))
print(greet.replace("o", "ooooo"))
print("everyone" in greet)
