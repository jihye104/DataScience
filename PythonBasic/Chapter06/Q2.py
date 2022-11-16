from statistics import mean
from math import sqrt

x = [5,9,1,7,4,6]

class Scattering:

    def __init__(self,x):
        self.x = x

    def var_func(self):
        avg = mean(self.x)
        diff = [(d-avg)**2 for d in self.x]
        self.var = sum(diff)/(len(self.x)-1)
        return self.var

    def std_func(self):
        sd = sqrt(self.var)
        return sd

obj = Scattering(x)
print(f"분산 : {obj.var_func()}")
print(f"표준편차 : {obj.std_func()}")