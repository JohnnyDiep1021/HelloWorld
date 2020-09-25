#classes
# Naming convention: capitalize all of the first letter in the words
class Vector:
    # Constructor, to initialize/ create an object
    # Self is a reference to a current object

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')
coordinates = (20, 10)
v1 = Vector(coordinates[0], coordinates[1])

# Set attributes/ data members anywhere in the program
v1.draw()


print(v1.x, v1.y)
"Exercise 1: create a class Person with name attribute and talk() method"
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi there! I am {self.name}!')

p1 = Person("Johnny Diep")
p1.talk()
