# 상속
class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good'   # private

    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
    
    def hello(self):
        print('안녕')
        print(self.__abc)
    
    @staticmethod
    def sbs(tel):
        print('sbs _ static method ', tel)
    
print(Person.say, Person.nai)
p = Person(22)
p.printInfo()
p.hello()   
        
print('***' * 10)  
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성장 ~~~')
        
    def printInfo(self):           # 부모에 있는 method override 한것 
        print('Employee 클래스 내의 printInfo')   
        
    def eprintInfo(self):
        self.printInfo()
        super().printInfo()   # super를 쓰면 위에 부모로 부터 받아왔다
        print(self.say, super().say)
        self.hello()
        
e = Employee()
print(e.say, e.nai)
print(e.subject)
e.printInfo()
e.eprintInfo()
      
print('***' * 10)
class Worker(Person):
    def __init__(self,nai):        
        print('Worker 생성자')
        super().__init__(nai)   # Bound method call
    
    def wprintInfo(self):
        super().printInfo()
        
w = Worker('25')
print(w.say,w.nai)
w.printInfo()
w.wprintInfo()
        
print('***' * 10)
class Programer(Worker):      
    def __init__(self, nai):
        print('Programer 생성자')
        Worker.__init__(self, nai)  # unBound method call
    
    def wprintInfo(self):    # method 오버라이딩
        print('Programer 내에 작성된 wprintInfo')

    def hello2(self):
        print(super().__abc)
    
pr = Programer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()

print()
p.hello()
# pr.hello2()  err
w.sbs('111-1111')  # static method 호출하기
pr.sbs('222-2222') # static method 호출하기

print('클래스 타입---')
a = 10
print(type(a))
print(type(pr))
print(Programer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)


        