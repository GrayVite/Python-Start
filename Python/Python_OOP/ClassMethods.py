# Class Mehtods = Allow operations related to the class itself
#                 Take (cls) as the first paramter, which represents the class itself
#                 Whereas, (self) represents the object of that class


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    # This is an instance method
    def get_info(self):
        return f"{self.name} - {self.gpa}"
    

    # To create class methods use the decorator @classmethod
    # Pass 'cls' as the first parameter
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    

# In order to use class method, use the class name, no need for object of class
print(Student.get_count())

# For instance methods, objects of class are needed
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_avg_gpa())