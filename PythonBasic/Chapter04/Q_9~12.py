temp = {'월': 25.5,
        '화': 28.3,
        '수': 33.2,
        '목': 32.1,
        '금': 17.3,
        '토': 35.3,
        '일': 33.3}

#9
print("9번-----")

LINE = 54
print('-'*LINE)
for day in temp:
    print(f"  {day}\t",end="")

print()

print('-'*LINE)
for day in temp:
    print(f" {temp[day]}\t",end="")

print()

print('-'*LINE)

#10
print("10번-----")

low_temp = []

for day in temp:
    low_temp.append(temp[day])

result = min(low_temp)

print('가장 낮은 최고 기온 : %.1f˚' % result)

#11
print("11번-----")

high_temp = []

for day in temp:
    if temp[day] >= 30:
        high_temp.append(day)

print("기온이 30˚ 이상인 요일 : ",end="")
print(f"{', '.join(high_temp)}")

#12
print("12번-----")

sum = 0

for day in temp:
    sum += temp[day]

avg = sum/len(temp)

print("일주일간 최고 기온의 평균 : %.1f˚" %avg)