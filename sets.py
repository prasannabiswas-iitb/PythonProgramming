'''
Meet Python Sets!

A **set** in Python is like a special collection of items, 
but with two important rules:

1. **No duplicates allowed**: Every item in a set must be
unique. If you try to add the same thing twice, the set 
will automatically remove the duplicate.

2. **No specific order**: Unlike lists or tuples, 
sets don't care about the order of items. It's like 
throwing things in a bag—you can pull them out, but 
they won't come out in any particular order.

### 

So, what makes sets different from lists and tuples?
- **Unique values only**: If you add the same value twice,
    the set will only keep one copy. It's great for making 
    sure there are no repeats!

- **No order**: While lists and tuples keep the order of
    the elements, sets don't. You can't access items by
    their position because sets don't assign positions.

### 

Why use sets?
Sets aren't just another version of lists or tuples. 
They come with some cool extra features that make them 
super useful, especially when you need to deal with unique
data or compare different groups of items.

We'll explore those fun extras as we dive deeper
into sets!

'''

# How to create a set
# {}
set_h = {"yuji", "fushiguro", "gojo", "mai", "panda"}
print(set_h)
print(type(set_h))

list_h = ["yuji", "fushiguro", "gojo", "mai", "panda"]
print(list_h)
print(type(list_h))


# set()
new_set = set()
print(new_set, type(new_set))

another_set = set([1,2,3])
print(another_set, type(another_set))

# Unordered
# access elements using for loop
list_h = ["yuji", "fushiguro", "gojo", "mai", "panda"]
print(list_h[0])
print(type(list_h))

set_h = {"yuji", "fushiguro", "gojo", "mai", "panda"}
print(set_h)
print(type(set_h))
print("==============")
for word in set_h:
    print(word)


# in
print("gojo" in set_h)
print("toji" in set_h)

# Adding elements
# 1. add()
set_h = {"yuji", "fushiguro", "gojo", "mai", "panda"}
print(set_h)
print(len(set_h))
print("===================")
set_h.add("toji")
print(set_h)
print(len(set_h))

# 2. update()
print("===================")
set_h.update(["red", "purple", "blue"])
print(set_h)
print(len(set_h))


# Problem: Deduplicate list
# set()
l = [1,2,1,1,2,3,3,3,3,3,3,"a","a","b"]
print(l)
print(len(l))
print("=========list to set==========")
set_l = set(l)
print(set_l)
print(len(set_l))
print("=========set to list==========")
new_l = list(set_l)
print(new_l)
print(len(new_l))

# set to list
# list()

'''
Name                    Operator example     Method example                   What it does
Union                   A | B                A.union(B)                       Create a set that combines A and B
Intersection            A & B                A.intersection(B)                Create a set with elements common between A and B
Difference              A - B                A.difference(B)                  Create a set with elements that are not in B
Symmetric difference     A ^ B               A.symmetric_difference(B)        Create a set with elements that are in A or B, but not in both
Is superset?            A >= B               A.issuperset(B)                  Returns True if every element of B is in A
Is subset?              A <= B               A.issubset(B)                    Returns True if every element of A is in B
Is disjoint?            No operator          A.isdisjoint(B)                  Returns True if A has no elements in common with B
Is proper superset?     A > B                No method                        True if A >= B and A != B
Is proper subset?       A < B                No method                        True if A <= B and A != B
'''
A = {1,2,3,4,5,8,9}
A1 = {3,4,8,9}
B = {3,4,8,9,10}
B1 = {10,11,12,13}

print("Is proper subset? ")
print(A1 < B)

print("\n Is proper superset? ")
print(A1 > B)

print("Is Disjoint? ")
print(A.isdisjoint(B1))

print("New Intersection: ")
print(A & B1)
print(A.intersection(B1))


print("Is subset? ")
print(A <= B)
print(A.issubset(B))

print("Is superset? ")
print(A >= B)
print(A.issuperset(B))

print("Symmetric Difference: ")
print(A ^ B)
print(A.symmetric_difference(B))

print("Difference: ")
print(A - B)
print(A.difference(B))

print("Union: ")
print(A|B)
print(A.union(B))

print("Intersection: ")
print(A & B)
print(A.intersection(B))