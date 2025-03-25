'''
What Is `__slots__`?  
'''

'''
In Python, we can dynamically add attributes to objects of a class because every object has a built-in `__dict__` attribute. 
This dictionary stores all the instance attributes of the object.
While this flexibility is great, it comes at the cost of memory usage because each object maintains its own dictionary. 
''' 
# class Person:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def introduce(self):
#       return f"{self.name} is {self.age} years old."

# p1 = Person("Thomson", 32)
# print(p1.introduce())
# p1._name = "John"
# print(p1.introduce())
# print(p1.__dict__)

'''
What Does `__slots__` Do?

The `__slots__` attribute restricts the attributes an object can have by specifying a fixed set of attribute names.
When you define `__slots__`, Python doesn't create a `__dict__` for each object, and the attributes are stored in a more memory-efficient way. 
'''
# class ots__ = ('name', 'age')
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def introduce(self):
#       return f"{self.name} is {self.age} years old."

# p1 = Person("Thomson", 32)
# print(p1.introduce())
# p1.country = "John"
# print(p1.introduce())
# Person:
#    __sl
'''
Why Use `__slots__`?  

The primary benefits of using `__slots__` are:  

1. Memory Optimization:  
   - Without `__slots__`, every object has a `__dict__`, which can consume a lot of memory when you have many instances.  
   - With `__slots__`, attributes are stored in a smaller, fixed structure, reducing memory overhead.  

2. Attribute Validation:  
   - By restricting attributes to a fixed set, `__slots__` prevents accidental typos or adding unintended attributes.  

3. Performance Improvement:  
   - Access to attributes defined in `__slots__` is slightly faster compared to attributes stored in a dictionary.  
'''
import sys
class PersonWithSlots:
   __slots__ = ('name', 'age')
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def introduce(self):
      return f"{self.name} is {self.age} years old."

class PersonWithDict:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def introduce(self):
      return f"{self.name} is {self.age} years old."

p1 = PersonWithSlots("Thomson", 32)
p2 = PersonWithDict("Thomson", 32)
print(p1.introduce())
print(p2.introduce())

print(f"Size of instance p1: {sys.getsizeof(p1.__slots__)}")
print(f"Size of instance p2: {sys.getsizeof(p2.__dict__)}")


'''Limitations of `__slots__`  
  
While `__slots__` is powerful, it has some limitations:  

1. No Dynamic Attributes:  
   - You can only use attributes defined in `__slots__`.  

2. Inheritance Challenges:  
   - Subclasses of a class with `__slots__` will not inherit `__slots__` unless explicitly redefined.  
'''
class PersonWithSlots:
   __slots__ = ('name', 'age')
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def introduce(self):
      return f"{self.name} is {self.age} years old."

class Child(PersonWithSlots):
   pass

c1 = Child("Thomson", 6)
c1.country = "India"
print(c1.country)




'''
When to Use `__slots__`? 

Prasanna:  
Use `__slots__` when:  
1. You have many instances of a class, and memory efficiency is crucial.  
2. You want to restrict attributes for better control and performance.  

Avoid `__slots__` when:  
1. You need to dynamically add attributes.  
2. You have a complex inheritance hierarchy.  
'''