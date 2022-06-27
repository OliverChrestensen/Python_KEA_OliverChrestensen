class Dog:
#class attributes
    amount_of_legs = 4
    #contructor
    def __init__(self,name,age):
        #instace attributes
        self.name = name
        self.age = age
    
    #instace method
    def eat(self):
        print("I can eat")

    def description(self):
        print("Animal name:", self.name, "& age:", self.age)

    def bark(self):
        print("I can bark")
    

obj=Dog("Dog", 5)

obj.description()
print("Dog Name:",obj.name, "-" " Dog age:", obj.age)

print(obj)

obj.name = "Cat"
print(obj.name)


#Inheritance / polymorphism

class Bulldog(Dog):
    def __init__(self,name, age):
        super().__init__(name, age)

    def bark(self):
        print("Dog bark")

bulldog = Bulldog("Billy",2)


bulldog.bark()
bulldog.eat()
bulldog.description()
print( "Billys amount of legs: ", bulldog.amount_of_legs)


class Labrador(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print ("Labrador bark")

labrador = Labrador("labby",3)

labrador.bark()


#encapsulation

class Car:
    def __init__(self,model,year):
        self.model = model
        self.__year = year #private

    def set__year(self,x):  
        self.__year = x
    
    def get__year(self): 
        return self.__year

car1 = Car("Audi", "2020")

print(car1.model)
car1.set__year("2022")

print(car1.get__year())




