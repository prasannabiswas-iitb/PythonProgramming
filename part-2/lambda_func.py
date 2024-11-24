'''
What is a Lambda Function?
In Python, a lambda function is a quick, 
one-line function without a name. 

Think of it as a shortcut for creating
small, simple functions.

How to Write a Lambda Function
A lambda function has this format:

lambda arguments: expression
'''
# 1. Lambda for simple math
add = lambda a,b: a+b
print(add(2,3))

# 2. Sorted function (function which takes 
#                     function as input)

# num_list = [5,2,1,4,6]
# sorted_list = sorted(num_list)
# print(sorted_list)
# def func(tupe):
#     return tupe[-1]

name_age = [('John', 24), ('Bob', 20), ('Alice', 22)]
sorted_list = sorted(name_age, key= lambda tupe: tupe[-1])
print(sorted_list)



'''
Problem Solving Time

Matching Students with Scores and Ranking.

Input: 
    1. [students] with names of students.
    2. [scores] with their corresponding
        test scores.

Task:
    1. Pair students with their scores.
    2. Sort them by their scores in
       descending order.
    3. Print each student's ranking, name,
       and score.
'''