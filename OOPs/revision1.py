'''
First, what is Object-Oriented Programming? 

1. Programming Paradigm: 
    OOP is a way of programming that organizes code around objects.

2. Objects: 
    Objects are entities that bundle data (attributes) and behavior (methods).

====== Example ======
Object: A Car
Attributes: brand, color, model
Methods: start(), stop(), accelerate()

====== Key Features ======
1. Classes and Objects: 
    Blueprints and their instances.

2. Inheritance:
    Reusing and extending existing code.

3. Polymorphism:
    Different ways to perform a task.

4. Encapsulation:
    Hiding details and exposing only necessary parts.

====== Why should you care about OOP? ======

1. Modularity:
    Break your code into smaller, manageable pieces.

2. Reusability:
    Once a class is defined, it can be reused across your project.

3. Real-world Modeling:
    OOP lets you model real-world entities, making your programs intuitive and relatable.
'''

class Student:
    school_name = "asc_class"
    def __init__(self, name, std, marks):
        self.name = name
        self.std = std
        self.marks = marks

    def exam_score(self): #->Instance method?
        return f"{self.name} studying in class {self.std} got {self.marks} marks."
        pass

    def promote(self, num_class): #-> Instance method
        self.std += num_class

    @classmethod
    def change_school_name(cls, new_school_name):
        cls.school_name = new_school_name

    @staticmethod
    def isvalidRollno(roll_no):
        if roll_no[0:3] == "asc":
            return True
        return False

    def __str__(self):
        return f"{self.name} studying in class {self.std}."

    # def __add__(self, other):
    #     return 

rollno1 = "asc1234"
rollno2 = "kvp1234"

# print(Student.isvalidRollno(rollno1))
# print(Student.isvalidRollno(rollno2))

# student1 = Student("John", 12, "80%")
# student2 = Student("Bob", 10, "90%")
# # print(student1 + student2)
# print(student2)
# print(type(student2))

# num = [1,2,3,4]
# print(num)
# print(type(num))

# a = 10
# b =20
# print(a+b)
# print(type(a))
# print(student2.exam_score())
# print(student1.exam_score())
# print(isinstance(student1, Student))

# print(student1.school_name)
# print(student2.school_name)

# print(student2.std)
# student2.promote(2)
# print(student2.std)
# print(student1.std)
# Student.change_school_name("asc_coding")
# print(student1.school_name)
# print(student2.school_name)

# if __name__ == "__main__" -> module, custom module
'''
Part 1: Types of Variables

1. Instance Variables  
    Variables that are unique to each object.
    These are defined inside the `__init__` method or within other instance methods.  
'''

'''
2. Class Variables  
    Variables that are shared across all objects of the class.
    They are defined inside the class but outside any methods.  
'''

'''
Part 2: Types of Methods

1. Instance Methods  
    These methods work with instance variables.
    They take `self` as the first parameter, which refers to the current object.  
    Use Case: 
        Use instance methods to perform operations specific to an object.
'''

'''
2. Class Methods  
    These methods work with class variables and take `cls` as the first parameter, which refers to the class itself. 
    They are decorated with `@classmethod`.  
    Use Case: 
        Use class methods for operations that involve the entire class rather than a single object.
'''

'''
3. Static Methods  
    These methods do not work with instance or class variables. 
    They do not take `self` or `cls` as a parameter and are decorated with `@staticmethod`.  
    Use Case: 
        Use static methods for utility or helper functions that do not rely on class or instance data.
'''

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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return f"Point({self.x + other.x}, {self.y + other.y})"

p1 = Point(2,4)
p2 = Point(3,5)

print(p1)
print(p2)
print(type(p1))
print("======Result======")
print(p1 + p2)
print(p1.__add__(p2))