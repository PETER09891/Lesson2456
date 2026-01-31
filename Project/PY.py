import math

class Polygon:
    def area(self):
        pass

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

square = Square(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print("Area of Square:", square.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Triangle:", triangle.area())
