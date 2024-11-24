'''
zip: Looping Through Multiple Lists
Simultaneously.
Imagine you have two lists of related items,
like names and ages. 

You want to loop through both at the same
time—one item from each list.
That's where zip comes in handy!

How zip Works
zip combines multiple lists (or sequences)
into pairs, so you can loop through them
together
'''
# Example of zip
# fruits = ['apple', 'mango', 'grapes']
# count = [40, 55, 500]

# for fruit, count_ in zip(fruits, count):
#     print(f"There are {count_} {fruit} in the store.")

'''
enumerate: Adding a Counter to Your Loop
Now, let's say you want to loop through a
list but also need to know the index
(position) of each item as you go. 

Instead
of manually creating a counter, you can use
enumerate to get the index automatically!
'''
# Example of enumerate

fruits = ['apple', 'mango', 'grapes']
for index,fruit in enumerate(fruits):
    print(f'Fruit {index+1}: {fruit}')

