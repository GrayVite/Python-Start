# super = Function used in a child class (sub class) to call methods from a parent class (superclass)
#         Allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
    

class Circle(Shape):
    def __init__(self, color, filled, radius):
        # Rather then re-writing the code mutliple times we are re-using the already written code
        # Use the super funtion to call the constructor of parent (super) class
        # When calling the super function make sure to add the () after super and before access operator
        super().__init__(color, filled)
        self.radius = radius

    # Below we have method overwriting by creating a method already present in parent class
    # The child method overshadows the parent method
    # By using super we can extend the functionality of the describe method
    # This will execute the describe function of the parent class as well
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side

    def describe(self):
        print(f"It is a square of an area {self.side * self.side}cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.height = height
        self.base = base
    
    def describe(self):
        super().describe()
        print(f"It is a triangle of area {self.base * self.height}cm^2")

circle = Circle(color="red", filled=True, radius=5)
square = Square("blue", side=7, filled=False)
triangle = Triangle("yellow", True, 7, 8)

print(f"Circle of {circle.color} color and radius {circle.radius}cm")
print(f"Square of {square.color} color and side {square.side}cm")
print(f"Triangle of color {triangle.color}, base {triangle.base}cm and height {triangle.height}cm")

circle.describe()
triangle.describe()

# Both circle and triangle contain super().describe(), borrowing the parent class method
# However, square doesn't have super().describe(), overwriting the describe method of parent with it's own

square.describe()

# As is_filled is the function in the parent class,
# using the super function we get the is_filled attribute
print(square.is_filled)