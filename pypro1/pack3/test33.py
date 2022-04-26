# 다중 상속    
class Animal:
    def move(self):
        pass

class Dog(Animal):     # 단일 상속
    name = '개'
    
    def move(self):
        print('개는 낮에 돌아 다님')
    
class Cat(Animal):     # 단일 상속
    name = '냥이'
    
    def move(self):
        print('고양이는 밤에 움직임')
        print('눈빛이 빛남')

class Wolf(Dog,Cat):
    pass

class Fox(Cat,Dog):
    def move(self):
        print('나는 여우~')
    
    def foxMethod(self):
        print('fox 고유 메소드')

dog = Dog()
print(dog.name)
dog.move()

print()
cat = Cat()
print(cat.name)
cat.move()

print()
wolf = Wolf()
wolf.move()
print(wolf.name)

print()
print(Wolf.__mro__)














