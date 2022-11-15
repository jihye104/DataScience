lst = [10,1,5,2]

#단계1
result = lst*2
print(result)

#단계2
num = lst[0]*2
result.append(num)
print(result)

#단계3
result2 = result[1::2]
print(result2)

result2 = []
i = 0

for n in result:
    if (i%2) != 0:
        result2.append(n)
    i += 1