'''
What is an abstract class?  

An abstract class is a class that cannot be instantiated directly. 
It serves as a blueprint for other classes. 
Abstract classes contain one or more methods that must be implemented by any class that inherits from them. 
These methods are called abstract methods.  

In Python, we use the `ABC` (Abstract Base Class) module from the `abc` package to define abstract classes.  

Key Points:  
- Abstract classes ensure that certain methods are implemented in the child classes.  
- They provide a structure to your code and promote consistency.  
- Abstract methods are declared using the `@abstractmethod` decorator.  
 
Why do we need abstract classes?  

- Enforce Implementation: Abstract classes enforce that child classes implement specific methods, ensuring uniformity.  
- Code Reusability: They define common behavior for related objects, reducing code duplication.  
- Structure: Abstract classes give a clear structure to your program, especially in large projects.  
'''

from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         return f"Animal makes sound."

#     def sleep(self):
#         return "Animal is sleeping."

# class Dog(Animal):
#     def sound(self):
#         return f"Barks!!"

# class Fish(Animal):
#     def sound(self):
#         return f"Some sound!!"

# d1 = Dog()
# print(d1.sound())
# print(d1.sleep())

# f1 = Fish()
# print(f1.sound())
# print(f1.sleep())

'''
Section 6: Abstract Properties 
'''

# class Animal(ABC):
#     @property
#     @abstractmethod
#     def num_legs(self):
#         return 10

# class Dog(Animal):
#     @property
#     def num_legs(self):
#         return 4

# class Human(Animal):
#     pass
#     # @property
#     # def num_legs(self):
#     #     return 2

# d1 = Dog()
# print(d1.num_legs)

# h1 = Human()
# print(h1.num_legs)


'''
Section 7: Abstract Class with Multiple Abstract Methods
'''

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2*(self.length + self.width)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

#     # def perimeter(self):
#     #     return 4*self.side

# r1 = Rectangle(10, 20)
# s1 = Square(10)

# print(r1.area())
# print(r1.perimeter())
# print(s1.area())
# print(s1.perimeter())
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        return 1

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # self.area = self.length * self.width
    @property
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

    # def perimeter(self):
    #     return 4*self.side

r1 = Rectangle(10, 20)
# s1 = Square(10)

print(r1.area)
print(r1.perimeter())
# print(s1.area())
# print(s1.perimeter())