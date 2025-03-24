# Static Methods = A method that belong to a class rather than any object from that class (instance) 
#                  Usually used for general utility functions

# Instance Methods = Best for operations on instances of the class (objects)
# Static Mehtods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


    # get_info(self) is an instance method
    # Any object of this class will have it's get_info method to return object's name and position
    def get_info(self):
        return f"{self.name} - {self.position}"
    

    # To create a static method use a decorator @staticmethod
    # Do not pass 'self' couse we are not dealing with any object
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions # returns a boolean
    

# In order to access a static method we do not need a class object
# Rather we just use the class name and the method we want to use
print(Employee.is_valid_position("Rocket Scientist"))


# With instance methods we have to create objects of that class
employee1 = Employee("Eugiene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())