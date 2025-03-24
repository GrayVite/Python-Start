# Class of Car
class Car:
    # To create a class we need a special method called 'constructor'
    # Below we have initialized a constructor. It is a dunder(double underscore) method
    def __init__(self, model, year, color, for_sale): # self -> the object we are creating rn
        self.model = model  # When we recieve the name of the model, we will assign it to the object
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")