def userfunc1():
    print("인수가 없는 함수")
    print("userFunc1")

userfunc1()

def userfunc2(x,y):
    print("userfunc2")
    z = x+y
    print(f"z = {z}")

userfunc2(10,20)

def userfunc3(x,y):
    print("userfunc3")

    tot = x+y
    sub = x-y
    mul = x*y
    div = x/y

    return tot,sub,mul,div

x = int(input("x 입력 : "))
y = int(input("y 입력 : "))

t,s,m,d = userfunc3(x,y)

print(f"tot = {t}")
print(f"sub = {s}")
print(f"mul = {m}")
print(f"div = {d}")