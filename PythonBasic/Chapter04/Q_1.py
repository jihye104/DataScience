lst = [1,3,5,4,2]
n = len(lst)

print(lst)

for i in range(0,n-1):
    for j in range(i+1,n):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print(lst)