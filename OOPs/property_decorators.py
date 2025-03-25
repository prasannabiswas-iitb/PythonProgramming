'''
What Are Getters, Setters, and Deleters? 

In Python, we often work with attributes of a class. Sometimes, we want to:  
1. Control how an attribute's value is accessed.  
2. Validate or modify data when setting an attribute.  
3. Perform cleanup or logging when an attribute is deleted.  

This is where getters, setters, and deleters come into play.  

Why Use Getters and Setters?

While Python allows direct access to attributes, getters and setters give us:  
- Data validation: Ensuring only valid data is set.  
- Encapsulation: Hiding internal details and providing controlled access.  
- Read-only or write-only properties: Allowing access in specific scenarios.  
'''

'''
Implementing Getters and Setters Using `property()`  -> inbuilt
'''

# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary

#     def intro(self):
#         return f"{self._name} earns {self._salary}."

#     def get_name(self):
#         print("Fetch...")
#         return self._name.capitalize()

#     def set_name(self, name):
#         print("Setting name...")
#         if name != "":
#             self._name = name
#         else:
#             print("Invalid string.")

#     def del_name(self):
#         print("Deleting...")
#         del self._name

#     def get_salary(self):
#         print("Fetch...")
#         return self._salary

#     def set_salary(self, salary):
#         print("Setting salary...")
#         if salary > 0:
#             self._salary = salary
#         else:
#             print("Invalid salary.")

#     def del_salary(self):
#         print("Deleting...")
#         del self._salary

#     name = property(get_name, set_name, del_name)
#     salary = property(get_salary, set_salary, del_salary)

# emp1 = Employee("charlie", 20000)
# # print(emp1.intro())
# print(emp1.salary)
# del emp1.salary
# # print(emp1.intro())

'''
Using Decorators for Getters, Setters, and Deleters   

- `@property`: Marks a method as a getter.  
- `@<property_name>.setter`: Marks a method as a setter.  
- `@<property_name>.deleter`: Marks a method as a deleter.  
'''
# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary

#     def intro(self):
#         return f"{self._name} earns {self._salary}."

#     @property
#     def name(self):
#         print("Fetch...")
#         return self._name.capitalize()

#     @name.setter
#     def name(self, name):
#         print("Setting name...")
#         if name != "":
#             self._name = name
#         else:
#             print("Invalid string.")

#     @name.deleter
#     def name(self):
#         print("Deleting...")
#         del self._name

    # def get_salary(self):
    #     print("Fetch...")
    #     return self._salary

    # def set_salary(self, salary):
    #     print("Setting salary...")
    #     if salary > 0:
    #         self._salary = salary
    #     else:
    #         print("Invalid salary.")

    # def del_salary(self):
    #     print("Deleting...")
    #     del self._salary

    # name = property(get_name, set_name, del_name)
    # salary = property(get_salary, set_salary, del_salary)

# emp1 = Employee("charlie", 20000)
# # print(emp1.intro())
# print(emp1.name)
# del emp1.name
# print(emp1.intro())


'''
Derived Properties  
You can use getters to define derived or computed properties.  
'''

# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width

#     @property
#     def area(self):
#         return self._length*self._width

# r1 = Rectangle(10, 20)
# print(r1.area)

# r1.area = 100