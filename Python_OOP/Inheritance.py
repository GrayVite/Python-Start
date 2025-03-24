# Inheritance = allows a class to inherit attributes and methods from another class
#               helps with code resusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")

    

# This is a child class, [class name_of_child(name_of_parent_to_inherit_from)]
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("Squeek")

dog = Dog("Scobby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# Attributes of the parent class
print(dog.name)
print(cat.is_alive)
mouse.eat()

# Attributes of the child class
dog.speak()
cat.speak()
mouse.speak()