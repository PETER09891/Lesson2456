import math

# Base class
class Polygon:
    def area(self):
        pass


# Derived class for Square
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Main program
square = Square(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print("Area of Square:", square.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Triangle:", triangle.area())
