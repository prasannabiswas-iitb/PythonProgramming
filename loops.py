'''
for loop -> used for known number of iterations

Syntax:
for <variable> in <iterable>:
    ....perform actions....

'''
hunters = ["gon", "killua", "leorio", "kurapika"]
for hunter in hunters:
    print(hunter)

# range(start, end, step)
for even_num in range(0,11,2):
    print(even_num)

'''
while loop -> used for unknown number of iterations

syntax:
while <expr is true>:
    ....perform actions....
    ....update condition expr....
'''
#Guessing zero
user_input = int(input("Guess a number: "))
while user_input != 0:
    print("Keep guessing!!!!!!!!")
    user_input = int(input("Guess a number again: "))
print("You entered a correct number")
