'''
Functions in python:

Uses:

1. code reuse
2. keeps code short and readable

Built-In functions (print, len, etc.)
print -> list, int, strings, etc.
len -> list, strings, tuples, etc.
'''
return_value = print("Hello world")
print(return_value)

len_string = len("Hello World")
len_list = len([1,2,3,4,5])
print("length of string = ", len_string)
print("length of list = ", len_list)


'''
syntax:

def <function_name> (<parameter list>):
    ....perform action....
    ....<return - optional>...

Default None
'''
#Example function
def welcome_message():
    print("Welcome back to our channel")

print(welcome_message())

# variable scope
def welcome_message():
    welcome_string = "Welcome back to our channel"
    print(welcome_string)

welcome_message()


# code-reusability
def welcome_message(group, platform):
    welcome_string = "Welcome back " + group + " to our platform: " + platform
    print(welcome_string)

welcome_message("Coders", "Youtube Channel")
welcome_message("Students", "Instagram Page")

# refactor same function with named parameters
def welcome_message(group = "Coders", platform = "YouTube Channel"):
    welcome_string = "Welcome back " + group + " to our platform: " + platform
    print(welcome_string)

welcome_message("Students", "Instagram page")

# return more than one variable
def add(x,y):
    return x+y, True

result, passed = add(30,4)
if(passed == True):
    print("addition was successful, and the result is: ", result)


