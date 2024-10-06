# Creating a Python tuple
# 1. ()
t1 = (1,2,3)
print(t1)
print(type(t1))

# 2. tuple()
t1_1 = tuple([1,2,3])
print(t1_1)
print(type(t1_1))

## Properties
#1. Holding Multiple Items & Ordering 
'''Both lists and tuples can store multiple items,
and the order of items is preserved'''

# Create a List (mutable)
fruits_list = ["orange", "banana", "mango"]
print("List of fruits: ", fruits_list)

# Create a Tuple (immutable)
fruits_tuple = ("orange", "banana", "mango")
print("Tuple of fruits: ", fruits_tuple)

#2. Indexed Access  
'''You can access items using their position,
starting from zero!'''

# Accessing by index
print(fruits_list[0])
print(fruits_tuple[1])

#3. Allowing Duplicates
'''Both lists and tuples can hold duplicate 
values.'''

# List with duplicates
fruits_list = ["orange", "banana", "mango", "orange"]
print(fruits_list)

# Tuple with duplicates
fruits_tuple = ("orange", "banana", "mango", "mango")
print(fruits_tuple)

#4. Mutable vs Immutable 
'''Here's where things get interesting! A list can
be changed, but a tuple cannot.'''

# List can be modified
fruits_list = ["orange", "banana", "mango", "orange"]
fruits_list[0] = "cherry"
print(fruits_list)

# Tuple cannot be modified
fruits_tuple = ("orange", "banana", "mango", "mango")
fruits_tuple[2] = "apple"
print(fruits_tuple)

#5. Adding and Removing Items
'''Lists allow you to add or remove items, but
tuples won't let you do that.'''

# Adding to a list
fruits_list = ["orange", "banana", "mango"]
fruits_tuple = ("orange", "banana", "mango")

print(fruits_list, len(fruits_list))
fruits_list.append("cherry")
print(fruits_list, len(fruits_list))

print(fruits_tuple, len(fruits_tuple))
fruits_tuple.append("cherry")
print(fruits_tuple, len(fruits_tuple))

# Removing from a list

fruits_list = ["orange", "banana", "mango"]
fruits_tuple = ("orange", "banana", "mango")

print(fruits_list, len(fruits_list))
fruits_list.remove("banana")
print(fruits_list, len(fruits_list))

print(fruits_tuple, len(fruits_tuple))
fruits_tuple.remove("banana")
print(fruits_tuple, len(fruits_tuple))

# Trying to modify a tuple (it won't let you)

#6. Tuples as Dictionary Keys
'''Since tuples are immutable, they can be used
as dictionary keys, unlike lists.'''

# Tuples as dictionary keys
phone_numbers= {}
phone_numbers[('John', 'Peter', 'Parker')] = 98423
phone_numbers[('Gon', 'Killua', 'Meruem')] = 89754
print(phone_numbers)

# Lists cannot be used as dictionary keys
phone_numbers= {}
phone_numbers[['John', 'Peter', 'Parker']] = 98423
phone_numbers[['Gon', 'Killua', 'Meruem']] = 89754
print(phone_numbers)

#7.Performance: Lists vs Tuples 
'''Tuples are faster because they are immutable.
While this might not be obvious for small datasets,
it becomes clearer when you measure performance in 
large ones. For now, you can simply understand that 
Python can optimize tuples better than lists because 
they don't change.'''

#8. Append to a Tuple
fruits_tuple = ("orange", "banana", "mango")
fruits_tuple2 = (*fruits_tuple, "cherry", "mango")

print(fruits_tuple)
print(fruits_tuple2)

#9. length of a Tuple

print(len(fruits_tuple))
print(len(fruits_tuple2))

#10. Convert Tuple to List
# list()

fruits_tuple = ("orange", "banana", "mango")
fruits_tuple2 = (*fruits_tuple, "cherry", "mango")
print(type(fruits_tuple), type(fruits_tuple2))

fruit_list = list(fruits_tuple)
fruit_list2 = list(fruits_tuple2)

print(fruit_list, type(fruit_list))
print(fruit_list2, type(fruit_list2))

# Unpacking

fruit_list = [*fruits_tuple]
fruit_list2 = [*fruits_tuple2]

print(fruit_list, type(fruit_list))
print(fruit_list2, type(fruit_list2))

#11. Convert Tuple to Set
# set()

fruits_tuple = ("orange", "banana", "mango")
fruits_tuple2 = (*fruits_tuple, "cherry", "mango")

fruits_set = set(fruits_tuple)
fruits_set2 = set(fruits_tuple2)

print(fruits_set, type(fruits_set))
print(fruits_set2, type(fruits_set2))

# Unpacking
fruits_tuple = ("orange", "banana", "mango")
fruits_tuple2 = (*fruits_tuple, "cherry", "mango")

fruits_set = {*fruits_tuple}
fruits_set2 = {*fruits_tuple2}

print(fruits_set, type(fruits_set))
print(fruits_set2, type(fruits_set2))

#Conclusion
'''By using **tuples**, you're saying,
"Hey Python, this data is locked in!" 
But if you need something more flexible,
like being able to change your shopping list,
**lists** are the way to go!'''