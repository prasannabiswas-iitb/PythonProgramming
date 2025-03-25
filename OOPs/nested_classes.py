'''
What Are Nested Classes?

A nested class is simply a class defined inside another class. 
It's like a container where one class logically belongs to another class.  

Why use nested classes?  
- Encapsulation: Helps group related classes together.  
- Scope limitation: Keeps the inner class tightly coupled to the outer class.  
- Better organization: Simplifies code for complex structures.  
'''

'''
1. Grouping Related Logic  
 
Suppose we're building a university management system. 
A `University` class might have a nested `Department` class.  
'''



class Computer:
    def __init__(self, comp_brand, brand, cores, size):
        self.comp_brand = comp_brand
        self.cpu = self.CPU(brand, cores)
        self.ram = self.RAM(size)

    class CPU:
        def __init__(self, brand, cores):
            self.brand = brand
            self.cores = cores

    class RAM:
        def __init__(self,size):
            self.size = size

    def describe(self):
        return f"{self.comp_brand} has {self.cpu.brand} cpu with {self.cpu.cores} and RAM {self.ram.size}"

c1 = Computer("HP", "Intel", 8, 16)
print(c1.describe())

# r1 = RAM(16)
