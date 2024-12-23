'''
Part 1: Types of Variables

1. Instance Variables  
    Variables that are unique to each object.
    These are defined inside the `__init__` method or within other instance methods.  
'''
# class Student:
#     def __init__(self, name, grade):
#         self.name =  name
#         self.grade = grade

# student1 = Student("John", 3.25)
# student2 = Student("Bob", 2.75)

# print(student1.name)
# print(student2.name)


'''
2. Class Variables  
    Variables that are shared across all objects of the class.
    They are defined inside the class but outside any methods.  
'''
# class Student:
#     school_name = "KV School"
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# student1 = Student("John", 3.25)
# student2 = Student("Bob", 2.75)
    
# print(student1.school_name)
# print(student2.school_name)










'''
Part 2: Types of Methods

1. Instance Methods  
    These methods work with instance variables.
    They take `self` as the first parameter, which refers to the current object.  
    Use Case: 
        Use instance methods to perform operations specific to an object.
'''

# class Student:
#     def __init__(self, name, grade):
#         self.name =  name
#         self.grade = grade

#     def introduce(self):
#         return f"Hi my name is {self.name} and I got {self.grade} gpa."

# student1 = Student("Gon", 4)
# student2 = Student("Eren", 5)

# print(student1.introduce())
# print(student2.introduce())

'''
2. Class Methods  
    These methods work with class variables and take `cls` as the first parameter, which refers to the class itself. 
    They are decorated with `@classmethod`.  
    Use Case: 
        Use class methods for operations that involve the entire class rather than a single object.
'''

# class Student:
#     school_name = "Tokyo academy"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self): #instance method
#         return f"Hi I am {self.name} and I am {self.age} years old."

#     @classmethod
#     def change_school_name(cls, sch_name):
#         cls.school_name = sch_name

# student1 = Student("Gon", 9)
# student2 = Student("Eren", 15)

# print(student1.introduce())
# print(student2.introduce())
# print(student1.school_name)
# print(student2.school_name)

# Student.change_school_name("Oak Academy")
# print(student1.school_name)
# print(student2.school_name)

'''
3. Static Methods  
    These methods do not work with instance or class variables. 
    They do not take `self` or `cls` as a parameter and are decorated with `@staticmethod`.  
    Use Case: 
        Use static methods for utility or helper functions that do not rely on class or instance data.
'''

class Student:
    school_name = "Oak Academy"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    @staticmethod
    def isvalid_roll(roll_no):
        if roll_no[0] == "O":
            return f"Valid Roll_number"
        return f"Invalid Roll_number" 

roll_no1 = "O12234"
roll_no2 = "K1234"

print(Student.isvalid_roll(roll_no1))
print(Student.isvalid_roll(roll_no2))



'''
Use Case Summary Table

| Type              | Works With              | Use Case                                              |
|-------------------|-------------------------|----------------------------------------------------------|
| Instance Variable | Object-specific data    | Store data unique to each object                         |
| Class Variable    | Shared across class     | Data common to all objects, e.g., school name            |
| Instance Method   | Instance variables      | Perform operations specific to an object                 |
| Class Method      | Class variables         | Perform operations related to the class, e.g., settings  |
| Static Method     | No specific data        | Utility functions like mathematical or string operations |
'''