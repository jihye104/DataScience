dataset = [3,5,1,2,4]
n = len(dataset)

#오름차순 정렬
for i in range(0,n-1):
    for j in range(i+1,n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset)

print(dataset)

print("===================")

#내림차순 정렬
for i in range(0,n-1):
    for j in range(i+1,n):
        if dataset[i] < dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset)

print(dataset)