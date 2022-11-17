# (1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# (2) 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg

# (3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data) #함수호출
    diff = [(d-avg)**2 for d in data] #list내포
    var = sum(diff)/(len(data)-1)
    sd = sqrt(var)

    return var,sd

# 프로그램 시작점 없음
data = [1,3,5,7]
print(f"평균 = {Avg(data)}")

var,sd = var_sd(data)
print(f"분산 = {var}")
print(f"표준편차 = {sd}")