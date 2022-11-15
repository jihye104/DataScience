def Func1(name, *names):
    print(name)
    print(names)

Func1("홍길동","이순신","유관순")

from statistics import mean,variance,stdev
def statis(func,*data):
    if func == 'avg':
        return mean(data)

    elif func == 'var':
        return variance(data)

    elif func == 'std':
        return stdev(data)

    else:
        return 'TypeError'

print(f"avg = {statis('avg', 1,2,3,4,5)}")
print(f"var = {statis('var', 1,2,3,4,5)}")
print(f"std = {statis('std', 1,2,3,4,5)}")

def emp_func(name,age,**other):
    print(name)
    print(age)
    print(other)

emp_func("홍길동",35,addr="서울시",height=175,weight=65)