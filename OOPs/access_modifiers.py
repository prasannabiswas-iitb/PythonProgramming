'''
Access Modifiers in Python

Access modifiers in Python control the accessibility of class attributes and methods. While Python does not have strict access control like some other languages (e.g., Java or C++), it provides naming conventions to indicate how accessible a variable or method is. 


Types of Access Modifiers in Python

1. Public
2. Protected
3. Private

'''

'''
1. Public
    - Public attributes and methods are accessible from anywhere—inside and outside the class.
    - Naming Convention: No underscores (`_`) before the name.
'''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def show_salary(self):
#         return f"Employee earns {self.salary} per month."

# e = Employee("John", 50000)
# e.salary = 80000
# print(e.show_salary())


'''
2. Protected
    - Protected attributes and methods are intended to be accessible within the class and its subclasses. They are not strictly enforced in Python.
    - Naming Convention: One leading underscore (`_`).
'''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
    
#     def show_salary(self):
#         return f"Employee earns {self._salary} per month."
    
# # class Manager(Employee):
# #     def __init__(self, name, salary):
# #         super().__init__()
    
# #     def update_salary(self, name, salary):
# #         self._salary = 80000

# e = Employee("John", 50000)
# e.salary = 80000
# print(e.show_salary())


'''
3. Private
    - Private attributes and methods are accessible only within the class where they are defined. Python achieves this through name mangling.
    - Naming Convention: Two leading underscores (`__`).
    - Name Mangling:
    - Python internally renames the private attribute `__salary` to `_Employee__salary` to make it inaccessible directly.
'''
class Employeee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show_salary(self):
        return f"Employeee earns {self.__salary} per month."
    
# class Manager(Employeee):
#     def __init__(self, name, salary):
#         super().__init__()
    
#     def update_salary(self, name, salary):
#         self._salary = 80000

e = Employeee("John", 50000)
print(e.__dict__)
e._Employee__salary = 80000
print(e.show_salary())


