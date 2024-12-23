'''
What are Magic/Dunder Methods?

Magic/Dunder methods are special methods in Python surrounded by double underscores, like `__init__`, `__str__`, or `__add__`.
They're also called magic methods because they make objects in Python behave like built-in types.  

Here are some key use cases:
1. Creating custom object initialization.
2. Defining how objects are printed or represented.
3. Enabling operator overloading.
4. Supporting iteration, comparisons, and more.
'''

'''
1. __init__: Object Initialization  
- Purpose: Initializes an object when it's created.
- Use Case: Assign initial values to instance variables.
'''

'''
2. __str__ and __repr__: String Representation  
- __str__: Used when print() is called on an object.  
- __repr__: Used to provide an unambiguous string representation, mostly for debugging.
'''

# class Student:
#     def __init__(self, name, class_):
#         self.name =  name
#         self.class_ = class_

#     def __str__(self):
#         return f"Student: name - {self.name}, class - {self.class_}"

#     def __repr__(self):
#         return f"Student({self.name},{self.class_})"
    
# student1 = Student("Eren", "12th")
# student2 = Student("Mikasa", "11th")

# print(student1)
# print(type(student1))
# print(student1.__repr__())



'''
3. __add__, __sub__, etc.: Operator Overloading  
- Purpose: Customize how operators like `+`, `-`, `*`, etc., work for your objects.  
'''

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

#     def __add__(self, other):
#         return f"Point({self.x + other.x}, {self.y+ other.y})"

# p1 = Point(1,4)
# p2 = Point(5,6)

# print(p1)
# print(p2)
# print("Addition of points: ", p1+p2) #Point(6,10)






'''
4. `__len__`: Custom Length  
- Purpose: Define behavior for the `len()` function.
'''

# class Team:
#     def __init__(self, members):
#         self.members = members

#     def __len__(self):
#         return len(self.members)

# team = Team(["Eren", "Armin", "Levi", "Erwin", "Mikasa"])
# print(len(team))









'''
5. `__getitem__`: Indexing Support  
- Purpose: Allow objects to be accessed like lists or dictionaries.  
'''
# class Team:
#     def __init__(self, members):
#         self.members = members

#     def __getitem__(self, index):
#         return self.members[index]

# team = Team(["Eren", "Attack", "Founder", "Armin"])
# print(team[3])

# team = ["Eren", "Attack", "Founder", "Armin"]
# print(team[0])



'''
6. __eq__, __lt__, etc.: Comparisons  
- Purpose: Customize how objects are compared using operators like `==`, `<`, `>`.  
'''

class Student:
    def __init__(self, name, class_):
        self.name = name
        self.class_ = class_

    def __str__(self):
        return f"Student: Name - {self.name}, Class - {self.class_}"

    def __eq__(self, other):
        return self.class_ == other.class_

    def __lt__(self, other):
        return self.class_ < other.class_

student1 = Student("Killua", 10)
student2 = Student("Meruem", 12)

print(student1)
print(student2)

print(student1 > student2)


















'''
7. `__call__`: Making Objects Callable  
- Purpose: Allow an object to behave like a function.  
'''

# class Greeter:
#     def __init__(self, greeting):
#         self.greeting = greeting

#     def __call__(self, name):
#         return f"{self.greeting}, {name}!"

# hello = Greeter("Hello")
# print(hello("Aditi"))  # Output: Hello, Aditi!

'''
8. `__iter__` and `__next__`: Iteration  
- Purpose: Make an object iterable using `for` loops.
'''

# class Countdown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         self.current -= 1
#         return self.current

# for number in Countdown(5):
#     print(number)  # Output: 4, 3, 2, 1, 0

'''
Summary Table of Dunder Methods

| Dunder Method  | Purpose                 | Use Case                                 |
|--------------------|-----------------------------|----------------------------------------------|
| `__init__`         | Object initialization       | Set up attributes when an object is created. |
| `__str__`          | User-friendly string output | Customize `print()` output.                  |
| `__repr__`         | Debugging                   | Provide a developer-friendly representation. |
| `__add__`          | Operator overloading        | Define `+` for objects.                      |
| `__len__`          | Custom length               | Make `len(obj)` work.                        |
| `__getitem__`      | Indexing                    | Allow list-like behavior.                    |
| `__eq__`, etc.     | Comparisons                 | Enable `==`, `<`, `>`, etc.                  |
| `__call__`         | Callable objects            | Make an object behave like a function.       |
| `__iter__`         | Iteration                   | Enable `for` loops on objects.               |

'''