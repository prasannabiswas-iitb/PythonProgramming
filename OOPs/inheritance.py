'''
What is Inheritance?

Inheritance is a mechanism where one class can inherit attributes and methods from another class. It allows us to reuse code and establish relationships between classes.

For example, think of a family tree: 
    Traits passed down from parents to children. Similarly, in programming, child classes can inherit features from parent classes.

Why use inheritance? Here are some key benefits:
1. Code Reusability: Avoid rewriting common code.
2. Hierarchy: Establish clear relationships between classes.
3. Scalability: Easily extend your codebase by adding new classes.

'''

# Person -> name age
# Student -> is a Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name}, and I'm {self.age} years old."

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def describe(self):
#         return f"Hi, I am {self.name}, and I'm {self.age} years old. I got {self.grade} CPI."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def describe(self):
        return f"{self.introduce()} I got {self.grade} CPI."

s1 = Student("Bob", 25, 9.01)
print(s1.describe())
# s1.grade = 10
print(s1.grade)


'''
Types of Inheritance
'''

'''
1. Single Inheritance
    This is the simplest type, where one child class inherits from a single parent class.
'''
# Method over-riding -> Inheritance

# class Animal:
#     def sound(self):
#         return f"Animal is making a sound."

# class Dog(Animal):
#     def sound(self):
#         return f"Barks!!!!!"

# d1 = Animal()
# print(d1.sound())



'''
2. Multiple Inheritance
    In Python, a class can inherit from multiple parent classes. Let's look at an example.
'''

# class canFly:
#     def fly(self):
#         return f"I can fly."

# class canSwim:
#     def swim(self):
#         return f"I can swim."

# class Duck(canFly, canSwim):
#     pass

# duck = Duck()
# print(duck.fly())
# print(duck.swim())



'''
3. Hierarchical Inheritance
    In hierarchical inheritance, multiple child classes inherit from a single parent class.
'''

# class Vehicle:
#     def description(self):
#         return f"I was manufactured at TATA facility."

# class Car(Vehicle):
#     def wheels(self):
#         return f"I have 4 wheels."

# class Truck(Vehicle):
#     def wheels(self):
#         return f"I have 10 wheels."

# c1 = Car()
# t1 = Truck()

# print(c1.description(), c1.wheels())
# print(t1.description(), t1.wheels())

'''
4. Hybrid Inheritance
    This is a mix of two or more types of inheritance. Let's see how it works.
'''

# class A:
#     def method_a(self):
#         return "A is called."

# class B(A):
#     def method_b(self):
#         return "B is called."

# class C(A):
#     def method_c(self):
#         return "C is called."

# class D(B, C):
#     def method_d(self):
#         return "D is called."

# d = D()
# print(d.method_a())
# print(d.method_b())
# print(d.method_c())
# print(d.method_d())


