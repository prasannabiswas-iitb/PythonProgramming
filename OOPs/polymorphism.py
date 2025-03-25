'''
What Is Polymorphism?  

Polymorphism means "many forms." 
In programming, it allows objects of different types to be treated uniformly. 
For example, the same method name can perform different actions depending on the object calling it.  

Why Use Polymorphism?
 
1. Flexibility: You can use the same interface for different objects.  
2. Code Reusability: A single function or method can handle different types of objects.  
3. Scalability: It's easier to extend and maintain your codebase.  

Polymorphism ensures that your code adheres to the principle of "programming to an interface, not an implementation."  
'''

'''
Polymorphism Through Inheritance  
'''
# class Animal:
#     def sound(self):
#         raise ValueError("Please Implement this method..")

# class Dog(Animal):
#     def sound(self):
#         print("Barks!!")

# class Cat(Animal):
#     def sound(self):
#         print("Meow!!")
#     pass

# c1 = Cat()
# d1 = Dog()


# #polymorphic method
# def make_sound(animal_obj):
#     animal_obj.sound()



'''
Polymorphism and Duck Typing  


The phrase "If it looks like a duck and quacks like a duck, it's a duck" is at the heart of Python's approach to polymorphism.  

In duck typing, the type of the object is less important than the methods and properties it has.  
'''

# class Car:
#     def sound(self):
#         print("Vroom!!")

# car = Car()

# make_sound(d1)
# make_sound(c1)
# make_sound(car)


