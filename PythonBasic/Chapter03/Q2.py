# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
num1 = tot = 0

while num1 <= 1000:
    num1 += 1

    if num1%3 == 0:
        tot += num1

print("1~1000까지의 자연수 중 3의 배수의 합 = %d" % tot)