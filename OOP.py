from mimetypes import init


class Dog:
   

    def __init__(self,name,age):
        self.__name = name
        self.age  = age

    def bark(self):
        print("dog barks")

    def set__name(self,x):
        self.__name = x

    def get__name(self):
        return self.__name

dog1 = Dog("bobby", 5)
dog1.bark()
print("DOG1'S name: ", dog1.get__name())
#print(dog1.__name)


class Bulldog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print("bulldog barks")
bulldog = Bulldog("billy", 10)

bulldog.bark()