# Inheritance
# pass for empty class

class Shape:
    def __init__(self, w = 0, l = 0, h = 0):
        self.width = w
        self.length = l
        self.height = h


class Square(Shape):
    pass


class Rectangle(Shape):
    def area(self):
        return self.width * self.length


class Triangle(Shape):

    def base(self, b):
        self.base = b

    def area(self):
        return (self.base * self.height) / 2


r1 = Rectangle(2,4,2)
print(r1.area())

t1 = Triangle(6, 5, 7)

t1.base(10)
t1.base = 10

print(t1.area())