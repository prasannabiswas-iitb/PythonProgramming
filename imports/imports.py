'''
import -> to import a python module.

module -> a python file to store functions, classes, and
          other definitions.
'''

# ---------- Existing module --------------
# math module
# Ref doc: https://docs.python.org/3/library/math.html

# import *, specific, alias
import math
# ceil(x)

# floor(x)

# comb(n,k) -> nCk -> n!/(k! * (n-k)!)
print(math.comb(3,2))

# factorial(x)
print("Factorial of 4: ",math.factorial(4))

# pow(x,y)
print("3 power 2: ", math.pow(3,2))

# sqrt(x)
print("Square root of 16: ", math.sqrt(16))

# pi
print("Value of Pi: ", math.pi)

# ---------- Custom Modules --------------
# Create a new .py file in same directory
import myMath as m
m.toDisplay()
print(m.powInt(3,2), type(m.powInt(3,2)))
# import the file and use

# using module as script - __name__ == '__main__'



