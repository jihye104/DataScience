# (1) 함수정의
def calc_func(a,b): #외부함수
    # 변수선언 : 자료저장
    x = a #10
    y = b #20

    def plus(): #내부함수
        p = x+y
        return p

    def minus(): #내부함수
        m = x-y
        return m
    return plus,minus

# (2) 함수호출
p,m = calc_func(10,20)
print(f"plus = {p()}")
print(f"minus = {m()}")

# (3) 클래스정의
class calc_class:
    #클래스변수 : 자료저장
    x = y = 0

    #생성자 : 객체생성 + 멤버변수 초기화
    def __init__(self,a,b): # private -> __x__(외부에서 보이고, 접근가능), __x(외부에서 안보이고, 접근불가능)
        self.x = a #10
        self.y = b #20

    #클래스함수
    def plus(self):
        p = self.x+self.y #변수연산
        return p

    #클래스함수
    def minus(self):
        m = self.x-self.y #변수연산
        return m

# (4) 객체생성
obj = calc_class(10,20)

# (5) 멤버호출
print(f"plus = {obj.plus()}")
print(f"minus = {obj.minus()}")