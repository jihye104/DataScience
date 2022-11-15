# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

# num = int(input("숫자입력 : "))
# sum = 0
# cnt = 0
# def num_avg(num):
#     sum += num
#     avg = sum/cnt
#     print(f"입력숫자 평균 : {avg}")

def avg(num_list):
    tot = 0

    for num in num_list:
        tot += int(num)

    return tot/len(num_list)

num_list = input("원하는 만큼 숫자입력(예:10 20 30 40 50) : ").split()
avg = avg(num_list)
print(avg)