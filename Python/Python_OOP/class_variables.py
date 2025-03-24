# class varibles: shared among all instances of a class
#                 defined outside the constructor
#                 allow you to share data among all objects created from that class

# For variables created in the constructor, 
# each instace of the class will have a copy of it's own of that variable
# However, class variables are shared by all instances

class Student:
    class_year = 2025 # A class variable
    num_students = 0

    def __init__(self, name, age):
        # Every time a class instance/object is created the constructor is executed
        # So, the num_students += 1 will be equal to the number of class instances, starting from zero (as initialized)

        self.name = name
        self.age = age

        # using self means we are editing for any created instance
        # using class name means we are editing for the class (every instance)
        Student.num_students += 1 


student1 = Student("Sponegebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name + " " + str(student1.age) + " " + str(student1.class_year))
print(student2.name + " " + str(student2.age) + " " + str(student2.class_year))


# It's good practice to access class variables using the class
# Not using an instance or object of the class 
# This helps to clarify that the variable is a class var, not an instance var
print(Student.class_year) # Accessing class variable using the class


# Student.um_students += 1, executed 4 times, for four instances
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)