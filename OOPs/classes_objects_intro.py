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


# class Car:
#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color
    
#     def describe(self):
#         return f"This is {self.color} colored {self.brand} {self.model}"
    

# car1 = Car("Tata", "Nexon", "Black")
# car2 = Car("Tata", "Nexon-New", "Grey")
# print(car1.brand)
# print(car2.color)

# print(car1.describe())
# print(car2.describe())

class Student:
    def __init__(self, name, roll, grade):
        self.name = name
        self.roll = roll
        self.grade = grade
    
    def introduce(self):
        return f"Hi my name is {self.name} and roll number {self.roll}"

    def get_grade(self):
        return f"{self.name} has got {self.grade} gpa."

student1 = Student("John", 122467, 3.5)
student2 = Student("Bob", 244672, 2)

print(student2.introduce())
print(student2.get_grade())
