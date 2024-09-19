import math

def powInt(x = 2, y =2):
    return int(math.pow(x,y))

def toDisplay():
    print("Welcome to my module.")

if __name__ == '__main__':
    toDisplay()
    print(powInt())