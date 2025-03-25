'''
What Are Aggregation and Composition?]  

- Aggregation:  
  - Represents a weak relationship.  
  - The lifetime of the contained object is independent of the container object.  
  - For example, a school has teachers, but a teacher can exist independently of a school.  

- Composition:  
  - Represents a strong relationship.  
  - The lifetime of the contained object is dependent on the container object.  
  - For example, a car has an engine, and the engine cannot exist without the car.  

| Aspect               | Aggregation                        | Composition                        |
|----------------------|------------------------------------|------------------------------------|
| Relationship         | Weak "has-a"                       | Strong "has-a"                     |
| Lifetime Dependency  | Contained obj exists independently | Contained obj depends on container |
| Example              | Teacher and School                 | Engine and Car                     |
'''


'''
1. Aggregation Use Case: Library System  
- A `Library` has `Books`.  
- Books exist independently and can belong to multiple libraries.  
'''

# class Books:
#   def __init__(self, author, title):
#     self.author = author
#     self.title = title

#   def details(self):
#     return f"{self.title} is wriiten by {self.author}"

# class Library:
#   def __init__(self, name):
#     self.name = name
#     self.list_of_books = []

#   def add_books(self, book_obj):
#     self.list_of_books.append(book_obj)

#   def show_all_books(self):
#     return [b.details() for b in self.list_of_books]


# b1 = Books("RV Chandra", "ChankyaNeeti")
# b2 = Books("Yuval", "Sapiens")

# lib = Library("Central Lib")
# lib.add_books(b1)
# lib.add_books(b2)

# print(lib.show_all_books())
# del lib
# print(b1.details())

'''
2. Composition Use Case: Computer System  
- A `Computer` has a `CPU` and `RAM`.  
- CPU and RAM cannot exist independently of the Computer.  
'''

# class CPU:
#   def __init__(self, brand, cores):
#     self.brand = brand
#     self.cores = cores

# class RAM:
#   def __init__(self,size):
#     self.size = size

# class Computer:
#   def __init__(self, comp_brand, brand, cores, size):
#     self. comp_brand = comp_brand
#     self.cpu = CPU(brand, cores)
#     self.ram = RAM(size)

#   def describe(self):
#     return f"{self.comp_brand} has {self.cpu.brand} cpu with {self.cpu.cores} and RAM {self.ram.size}"

# c1 = Computer("HP", "Intel", 8, 16)
# print(c1.describe())
# del c1

