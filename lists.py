# Stores more than one object of different data type

list_ele = [1, 'hello', 3.21, True]
print("Printing first element")
print(list_ele[0])


print()
print("Printing last element")
print(list_ele[-1])

print()
print("Printing all elements")
for ele in list_ele:
    print(ele)
print()

hunters = ["Gon", "Killua", "Kurapika", "Leorio"]

# length of a list
print(len(hunters))

# append
hunters.append("Gon")
hunters.append("Netero")
print(hunters)
print(len(hunters))

# count element of a list
count_gon = hunters.count("Gon")
count_killua = hunters.count("Killua")
print("Gon: ", count_gon, " Killua: ", count_killua)

# sort a list
print("List before sorting: ", hunters)
hunters.sort()
print("Lits after sorting: ", hunters)

# reverse a list
hunters.reverse()
print("After reversing: ", hunters)

# see all the operations of a list
print(dir(hunters))