# object = A 'bundle' of related structures (variables) and methods (functions)
#          Ex, a phone can be on/off, 
#          a cup could have water, coffee or other items

# Methods are functions that an object can perform
# For example, phone can place a call, take a call etc

# To create many objects you need a 'class'

# class = (blueprint) used to help design the structure and layour of an object


from car import Car
# It's also possible to create a class within the same python file.
# This was done to show that a class can be imported from a module.

car_1 = Car("Mustang", 2024, "red", False)
car_2 = Car("Corvette", 2025, "blue", True)

print(car_1) # Printing the car object, just prints it's address

print(car_1.model) # Use the dot to access an attribute of the object
print(car_1.year)
print(car_1.color)
print(car_1.for_sale)

print(car_2.model) # You can create mutliple objects of the same class
print(car_2.year)
print(car_2.color)
print(car_2.for_sale)


car_1.drive()
car_2.stop()

car_1.describe()
car_2.describe()