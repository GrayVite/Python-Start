# "Duck Typing" = Another way to achieve polymorphism besides inheritance
#                 Object must have necessary attributes/methods
#                 "If it looks like a duck and it quacks like a duck, it must be a duck"
# As long as an object behave like another, it could be treated of that type

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    # Our car class has the minimum necessary attributes to be an animal
    alive = False
    # Our car class has the minimum necessary methods to be considered an animal
    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)