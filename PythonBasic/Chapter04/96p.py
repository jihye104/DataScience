s = {1,3,5,3,1}

print(s)

for d in s:
    print(d,end=" ")

print()

s2 = {3,6}

print(s.union(s2))
print(s|s2)

print(s.difference(s2))
print(s-s2)

print(s.intersection(s2))
print(s&s2)

s3 = {1,3,5}

s3.add(7)
print(s3)

s3.discard(3)
print(s3)