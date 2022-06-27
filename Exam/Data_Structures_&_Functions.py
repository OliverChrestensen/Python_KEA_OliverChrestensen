## List ##
# ordered og mutable og kan indeholde alle typer 
# Arraylist i java
# samme values
# slicing
#indekseret 
list1 = []

list2= ['a','dog', 10, True, 5.25]

#slice list2[start:slut:step]
print(list2[1:5:2])


## List Comprehension ##

y1 = [m for m in range(8)]


print('this is y1:', y1)

del(list2[3])


list1.append(20) #tilføjer element

list1.extend(y1) # tilføjer sequense til liste

list1.insert(1, "indelist1") #tilføjer element på index plads

list1.pop() # fjerner det sidste element og retunere det

list1.remove("indelist1") # fjerne første instans af det element

list1.reverse() #retunere liste baglæns

list1.sort() #sorter listen efter værdi


## Tuples ##
# ordered men immutable og duplicates
# kan ikke tilføje eller slette elementer
#slicing


Tuple = ()

tuple1 = (1,2,3)

tuple2 = 1,2,3

tuple3 = tuple(list1)

## Sets ##
# mutable, unordered men kan ikke indholde samme values.
#unique elementer

set1 = {3,5,3,5}  # {5,3}

set2 = set()    # tomt set

set4 = set(list1) # nyt set fra list

## Set comprehension ##

set3 = {x for x in range(10) if x >5 }

print('this is set3:', set3)

set1.add(2)


set1.remove(3)

len(set1)

print(2 in set1)

set1.pop()

set1.clear()


## Dictionaries ##
# unordered, mutable
# key value pair 
# ingen duplicates


dict1 = {'Danmark':  'Købenahvn', 'Tyskland': 'Berlin', 'Frankrig': 'Paris' }


dict1['Danmark'] ='Madrid'

del dict1['Danmark'] 

print('Danmark' in dict1)

len(dict1)

dict1.keys()

dict1.values()

# itere 

for key in dict1:
    print(key, dict1[key]) 


