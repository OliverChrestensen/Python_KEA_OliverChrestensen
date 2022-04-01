class Car:
    def __init__(self,make):  #init = initiliaze
        self.make = make

    @property #getter
    def make(self):
        return self.__make

    @make.setter # setter
    def make(self,x):
        self.__make = x    

    def info(self):
        return f'The variable of this class is {self.__dict__}'    # f after return means its a formatted string. 

    