# Polymorphism = greek work that means to "have many forms or faces"
# Poly = many
# Morphe = form

# Two ways to achive polymorphism
# 1. Inheritance = An object could be treated as smae type as a parent class
# 2. "Duck Typing" = object must have necessary attributes/methods

from abc import ABC, abstractmethod
from math import pi

# Through Inheritance
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        # aS pizza is grandchild it inherits from circle and shape
        super().__init__(radius) # Using the area function of circle as pizza is circular


# As our circle inherits from shape
# It is also considered a shape, thus having two forms, 
# a circle and a shape
# Similarly, for Square and Triangle

# Our pizza inherits from circle
# It is a pizza, circle and a shape, having three forms

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepporoni", 15)]

for shape in shapes:
    print(f"{shape.area():.2f}cm^2")



