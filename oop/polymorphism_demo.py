import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Demo of polymorphism
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
