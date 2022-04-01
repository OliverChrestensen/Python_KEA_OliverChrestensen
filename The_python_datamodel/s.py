class S:
    def __init__(self,name):
        self.name = name

    def __repr__(self): #ToString
        return f'{self.__dict__}'    

    def __str__(self): #also a ToString
        return f'The variables in this object is  "name" = {self.name}'

    