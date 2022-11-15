# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
num = int(input("숫자입력 : "))

def is_odd():
    if num%2 == 0:
        return "짝수"

    else:
        return "홀수"

print(is_odd())

