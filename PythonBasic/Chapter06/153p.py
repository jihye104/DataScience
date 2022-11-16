class car:
    # (1) 멤버변수
    cc = 0 #엔진cc
    door = 0 #문짝개수
    carType = None #null

    # (2) 생성자
    def __init__(self,cc,door,carType):
        #멤버변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType

    # (3) 메서드
    def display(self):
        print(f"자동차는 {self.cc}cc이고, 문짝은 {self.door}개, 타입은 {self.carType}")

# (4) 객체생성
car1 = car(2000,4,"승용차") #객체생성+초기화
car2 = car(3000,5,"SUV")

# (5) 멤버호출 : object.member()
car1.display()
car2.display()