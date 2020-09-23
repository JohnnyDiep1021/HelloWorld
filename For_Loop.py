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

"List"
item = ['kiwi', 'strawberry', 'mango', 'durian', 'jackfood']
print(item[:])

'Exercise 1: Find max'
num = [1,2,12,23,333,24,900,3240,38,40,100]
max = num[0]
for x in num:
    if max <= x:
        max = x
print(max)

'Exercise 2: Find min'
num = [1,2,12,23,-290,-900,3240,100]
min = num[0]
for x in num:
    if min >= x:
        min = x
print(min)

'2D list'
list_with2D = [
    [2,3,4],
    [3,4,1],
    [8,9,1]
]
for row in list_with2D:
    for item in row:
        print(item)

print(list_with2D[2][2])

'List methods'

'append() add new items at the last index'
list_with2D.append([20,32,213,123])
print(list_with2D)

'insert() add new items at the selected index'
list_with2D.insert(1, [1,2,3])
print(list_with2D)

'clear() clear the list'
list_with2D.clear()
print(list_with2D)



list_withitem =[0,1,3,4,1,6,1,2,5,9,5,2,5,2,7,1,4]
print(list_withitem.sort())
list_withitem.reverse()
list_withitem2 = list_withitem.copy()
'none is an object in Python showing the absence of value'
'pop() remove the last item in the list'
list_withitem.pop()
print(list_withitem)

'remove() remove the existed item in the list'
list_withitem.remove(2)
print(list_withitem)

'count() count the number of selected/ preferred item(s) in the list'
print(list_withitem.count(1))

if(list_withitem.count(1)):
    print(1 in list_withitem)
'use in for checking condition will return True/ False'


'any changes made in the original item will not affect the copied list'
print(list_withitem2)

'Exercise: remove the duplicates in the list'

'solution'

uniques = []
for x in list_withitem2:
    if(x not in uniques):
        uniques.append(x)
print(uniques)

'self-solution'
for x in list_withitem2:
    if(list_withitem2.count(x) > 1):
        print(f'delete {x}')
        list_withitem2.remove(x)
        print(f'{x} remained: {list_withitem2.count(x)}')
    else:
        print(f'{x} has only 1')

print(list_withitem2)
