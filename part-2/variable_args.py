'''
Imagine you're writing a function that can
handle a mystery number of arguments.
Sometimes, you might know how many inputs
your function needs, but other times, you
just want to keep it flexible.

That's where *args and **kwargs come in!

*args lets your function take any number
of positional arguments (like numbers or
strings).

**kwargs lets your function take any
number of keyword arguments (where each
argument has a name and a value,
like name="Alice").
'''
# *args: Positional Arguments
# Question create a function add() which can
# take variable number of arguments

def add(*args):
    sum = 0
    for every_num in args:
        sum = sum + every_num
    return sum

print("Add result: ",add(1,2))
print("Add result: ",add(1,2,3))
print("Add result: ",add(1,2,3,4))

# **kwargs: Keyword  Arguments
# Question create a function to print student
# information which is available.

def student_info(**kwargs):
    for student_info_tupe in kwargs.items():
        print(student_info_tupe)
        print("=========")

student_info(name="John", age=20)
student_info(name="Bob", branch="CSE")
student_info(name="Charlie", branch="CSE", age=22)

