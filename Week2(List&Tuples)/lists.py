#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we' 

#Exercise 0.1

from re import S


a = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
print("_________________________________________")
print(a[1:5])
print("_________________________________________")
print(a[0:2])
print("_________________________________________")
print(a[4:5])
print("_________________________________________")
print(a[0:6:2])
print("_________________________________________")
print(a[::-1])
print(a[1:5])

#Exercise 2.
"""
Create a function that takes a string as a parameter and returns a list.
The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
"""



def sortTextfunction(s):
 words = []
 vowels = ['a','e','i','o','u']

 for ch in s.lower():
     if ch in vowels:
         s = s.replace(ch,"")
         s.sorted()
         
 words.append(s)         
        
 print(words)
 
 
 return words
 
sortTextfunction("hundemad")


#Exercise 3

