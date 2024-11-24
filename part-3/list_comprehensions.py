'''
What Are List Comprehensions? 

List comprehensions are a concise way to create lists in Python. Instead of writing multiple lines of code, you can do it all in just one line!
'''

# Example 1: Creating a List of Squares
#normal
numbers = [1,2,3,4,5,6]
square = []
for num in numbers:
    square.append(num**2)
# print(square)

#listcomp
numbers = [1,2,3,4,5,6]
square = [num**2 for num in numbers]
# print(square)


# Example 2: Filtering Even Numbers
#normal
numbers = [1,2,3,4,5,6]
even_numbers = []
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
# print(even_numbers)

#listcomp
# print("======= list comp ========")
numbers = [1,2,3,4,5,6]
even_numbers = [num for num in numbers if num%2==0]

# print(even_numbers)


# Example 3: Nested Loops in List Comprehensions 

rolling_dice_possi = [(x,y) for x in range(1,7) for y in range (1,7)] 

# print(rolling_dice_possi)


# Example 4: Conditional Expressions in List Comprehensions
#listcomp

numbers = [-4, 6, -5, 7, 2]
# out = [0, 6, 0, 7, 2]

filter_numbers = [num if num > 0 else 0 for num in numbers]

print(filter_numbers)

