total = 0
print('수열 = ')

for i in range(1, 101):
    if i%3 == 0 and i%2 != 0:
        print(i, end=" ")
        total += i

print("\n누적합 = %d" %total)