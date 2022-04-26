from abc import *

class Employee (metaclass = ABCMeta):
    irum = ''
    age = 0
    
    def __init__(self,irum,age):
        self.irum = irum
        self.age = age
    
    @abstractmethod
    def pay (self):
        pass

    @abstractmethod
    def data_print(self):
        pass

    def name_print(self):
        print(self.irum +str( self.age))

class Temporary(Employee):
    ilsu = 0
    ildang = 0
    
    def __init__(self,irum,age,ilsu,ildang):
        super().__init__(irum, age)
        self.ilsu = ilsu 
        self.ildang = ildang
        
        
    
    def pay(self):
        print(self.ilsu * self.ildang)
    
    @abstractmethod
    def data_print(self):
        

t = Temporary('홍길동',25,20,15000)
print(t.pay())
t.name_print()
t.age_print()