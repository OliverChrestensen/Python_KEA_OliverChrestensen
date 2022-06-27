# list #

lsit1 = [2,"to", True, 10.1,2]

print(lsit1) 

print( "list before:", lsit1[1])

lsit1.append(25)
del(lsit1[1])

print(lsit1[1:4:2])
print(len(lsit1))
lsit1.remove(True)

#newlist = [expression for item in iterable if condition == True]

list2 = [n for n in range(8) if n > 5]



print("list after append method:", lsit1)

#tuple"

tuple1 = (1,2,3,4,5,2)

print(tuple1[3])

print(tuple1)

#tuple1[1] = "hej"

# sets 

set1 = {1,1,2,2,3,4}

print(set1)

set1.add(10)
print(set1.__contains__(1))

isitinset = 9 in set1
print(isitinset)
print(set1)


# dictionaries #

dict1 = {"Danmark": "københavn", "frankirg":"paris", "Tysland":"Berlin", "Danmark": "Oslo"}
print(dict1)

dict1["Danmark"] = "købehavn"
print(dict1["Danmark"])
