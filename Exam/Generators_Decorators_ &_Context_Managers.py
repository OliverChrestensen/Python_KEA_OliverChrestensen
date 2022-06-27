## Generators ##

# returns iterator object, we can iterate over.(en value af gangen)
# yield pauses the function and save the states, later continues from the last value it got.
# automatically implemneted _iter_ & _next_()
# if we iterate over big lists etc. we would run out of memory but with generators we take one item at a time.

def even_generator(max):
    n = 0
    n += 2
    yield n
    n += 2
    yield n
    n += 2
    yield n
    


numbers = even_generator(8)
print( "this is first print:",next(numbers))
print("this is second print:",next(numbers))
print("this is third print:", next(numbers))


def my_gen(max):
    n=2

    while n <= max:
        yield n
        n +=2
    

gen = my_gen(6)

print(next(gen))
print(next(gen))
print(next(gen))
##print(next(gen)) #n = 8 and StopIteration exception is called


## Decorators ##

## function that takes another function,  add some functionality to it and returns it

#decorator function
def display_info(func):
    def inner():
        print("executing", func.__name__,"function")
        func()
        print("finished executing function")

    return inner()

@display_info
def printer():
    print("Hello")

#istead of writing 
# def printer():
    # print("Hello")
# printer = display_info(printer)

## context Managers ##
#manage files or connection to database or internet ect.
#interface/contract the objects follow, to use the with statement
#should have __enter__ and __exit__

# The "with" Statement 
#helps open the file, and automaticaly closes it
#calls the __enter__ method 
#calls the __exit__ method after the .write method is done.
# 'w' = modes for the open() - w is write-only mode.
with open('hello.txt', 'w') as file:
    file.write('Hello Python!')



##examle of enter and exit method. hvad der sker bag i with keyword.

def __enter__(self):
    self.file = open(self.name,'w')
    return self.file

def __exit__(self, exc_type, exc_val, exc_tb):
    if self.file:
        self.file.close()

