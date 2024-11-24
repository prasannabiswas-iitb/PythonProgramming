'''
What Are Exceptions?

Exceptions are runtime errors that occur when something unexpected happens in your code. For example:
- Trying to divide a number by zero.
- Accessing a file that doesn't exist.
- Using a variable that hasn't been defined.

Why Handle Exceptions?

Handling exceptions is crucial to:
1. Prevent your program from crashing.
2. Provide meaningful error messages to users.
3. Handle unexpected scenarios gracefully.

'''

# Basic Exception Handling
#ZeroDivisionError
num1 = 2
num2 = 0
# result = num1/num2
# print("Result: ", result)
#Error
#Resolve

# try:
#     num1 = 2
#     num2 = 0
#     result = num1/num2
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("value of num2 is zero, please define denominator other than 0.")


# Handling Multiple Exceptions   
# ZeroDivisionError
# ValueError
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1/num2
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("Value of num2 is zero, please define denominator other than 0.")
# except ValueError:
#     print("You have entered a value or literal which is not a number.")

# Using else and finally

# try:
#     num1 = 1
#     num2 = 1
#     result = num1/num2
# except ZeroDivisionError:
#     print("Value of num2(denominator) is zero.")
# else:
#     print("Result: ", result)
# finally: #always runs
#     print("Sucessfully ran the code.")


# Raising Exceptions 

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Age: ", age)

try:
    check_age(-5)
except ValueError as e:
    print("Error: ",e)



