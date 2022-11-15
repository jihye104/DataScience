#A형
size = int(input("vector 수 : "))
lst = []

for i in range(size):
    lst.append(int(input()))

print(f"vector 크기 : {len(lst)}")

#B형
if int(input()) in lst:
    print("YES")

else:
    print("NO")