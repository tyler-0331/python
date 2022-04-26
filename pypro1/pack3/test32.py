# 다중상속 
# 복수의 클래스를 상속 가능: 순서가 중요 
class Donkey:
    data = '당나귀 만세'
    
    def skill(self):
        print('당나귀:짐 나르기')

class Horse:
    def skill(self):
        print('말:달리기')
        
    def hobby(self):
        print('프로그램 짜기')

class Mule1(Donkey,Horse):
    pass

mu1 = Mule1()
print(mu1.data)
mu1.skill()       # 먼저 쓰여진걸로 따른다 그래서 Donkey의 skill이 나온다        
mu1.hobby()
        
print()        
class Mule2(Horse,Donkey):
    def play(self):
        print('노새 고유 메소드')
    
    def hobby(self):
        print('노새는 걷기를 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()           # 부모 객체로 곧바로 간다 !!
        print(self.data, super().data)
        
mu2 = Mule2()
mu2.skill()
mu2.hobby()
mu2.play()
mu2.showHobby()
        
        
        
        
        
        
        
        
        
        
        
        