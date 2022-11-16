print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input("사각형의 가로 입력 : "))
h = int(input("사각형의 세로 입력 : "))

print("-"*50)

class Square:
    width = height = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_calc(self):
        return self.width*self.height

    def circum_calc(self):
        return (self.width+self.height)*2

obj = Square(w,h)
print(f"사각형의 넓이 : {obj.area_calc()}")
print(f"사각형의 둘레 : {obj.circum_calc()}")

print("-"*50)