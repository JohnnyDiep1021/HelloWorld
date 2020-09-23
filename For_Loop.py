"For & nested loop"
item = [1,2,3,4,5,6,7,8,9]
total = 0
for list in item:
    total += list
    print(total)

'Exercise 1'
list = [5,2,5,2,2]
for x_count in list:
    string = ""
    for count in range(x_count):
        string += '*'
    print(string)
