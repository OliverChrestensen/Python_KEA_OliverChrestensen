#generator

def even_generator(max):
    n = 0
    n += 2
    yield n
    n += 2
    yield n
    n += 2
    yield n

numbers = even_generator(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))


#decorator

def diplay_info(func):
    def inner():
        print("Executin", func.__name__, "function")
        func()
        print("finish executing")
    return inner()

@diplay_info
def printer():
    print("hello")


# context managers

with open("hello.txt","w") as file:
    file.write("vi er igang med pyton eksamen")
    

    #__enter__ method

    _#_exit__method
    

