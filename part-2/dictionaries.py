'''
Let's dive into **dictionaries** in Python, a super
useful data type that works like a real-life dictionary,
matching **keys** with **values**.

# What is a Python Dictionary?

A **dictionary** in Python is a collection of key-value
pairs. Think of it as a phone book where the **key** is
the name of a person and the **value** is their
phone number.

- **Keys** are like labels. They need to be unique and
    immutable (think strings, numbers, or tuples).

- **Values** can be anything—numbers, strings, lists,
    even other dictionaries!

#Creating a Dictionary

You can create a dictionary using curly braces `{}`
and colons `:` to separate keys from values.

'''

# Example dictionary
# student_info = {"name": "John",
#                 "age": 20,
#                 "branch": "CSE"}
# print(student_info)
# print(type(student_info))

# Accessing Values
'''
You can access the value of a specific key using square
brackets [].
'''
# print("======================")
# print(student_info["name"])
# print(student_info["age"])

# Modifying a Dictionary
'''
Dictionaries are mutable.
  1. Adding or Updating a Value
  2. You can add new keys
'''
# print("=====================")
# print(student_info)
# print("after modifying")
# student_info["age"] = 21
# student_info["College"] = "ABC"
# print(student_info)

# Removing a Key-Value Pair
'''
1. using the del statement.
2. using pop() method.
'''
# print("=====after deleting college====")
# del student_info["College"]
# print(student_info)
# student_info.pop("age")
# print("==================")
# print(student_info)









# Other ways of creating a dictionary

# Using the dict() constructor
# name_age = [("John", 22), ("Bob", 24), ("Alice", 26)]
# print(name_age)
# print(type(name_age))

# new_dic = dict(name_age)
# print(new_dic)
# print(type(new_dic))




# Using dict.fromkeys()
# names = ["John", "Bob", "Alice"]
# name_age = dict.fromkeys(names, 22)
# print(name_age)
# print(type(name_age))

# Check if a key exists in a dictionary
# print("===================")
# print("John" in name_age)
# print("Charlie" in name_age)


# Getting the length of a dictionary
# print("===================")
# print("Length of dictionary: ", len(name_age))

# dict.keys(), dict.values(), dict.items()
# print("===================")
# dict_keys = name_age.keys()
# dict_values = name_age.values()
# dict_elements = name_age.items()

# print(dict_keys)
# print(dict_values)
# print(dict_elements)

# for name,age in dict_elements:
#   print(f"{name} is {age} years old.")

# Merging dictionaries
# |
# unpacking
# dict1 = {"John": 20, "Charlie": 24}
# dict2 = {"Bob": 22, "Alice": 26}

# final_dict = dict1 | dict2
# print(final_dict)

# unpacking_merge = {**dict1, **dict2}
# print(unpacking_merge)

# Comparing dictionaries
# InOrder
# OutofOrder

d1 = {"a": 1, "b":2, "c":3}
d2 = {"a": 1, "c":3, "b":2}

print(d1)
print(d2)
print(d1 == d2)


