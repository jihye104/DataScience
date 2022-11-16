# (1) 부모 클래스
class Parent:
    #생성자 : 객체+초기화
    def __init__(self,name,job):
        self.name = name
        self.job = job

    #멤버함수(method)
    def display(self):
        print(f"namd : {self.name}, job : {self.job}")

#부모클래스 객체생성
p = Parent("홍길동","회사원")
p.display()

# (2) 자식 클래스
class Children(Parent): #부모클래스 상속
    gender = None #자식클래스 멤버변수 추가

    # (3) 자식 클래스 생성자
    def __init__(self,name,job,gender):
        #부모 클래스 생성자 호출
        super().__init__(name,job) #초기화
        self.gender = gender

    #멤버함수(method)
    def display(self): #함수 재정의
        print(f"name : {self.name}, job : {self.job}, gender : {self.gender}")

#자식클래스 객체생성
chil = Children("이순신","해군장군","남자")
chil.display()