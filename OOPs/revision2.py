from revision1 import Point as P

p1 = P(2,4)
p2 = P(3,5)

print(p1)
print(p2)
print(type(p1))
print("======Result======")
print(p1 + p2)
print(p1.__add__(p2))


a = (1,2)
print(type(a))