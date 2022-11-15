name = ['홍길동','이순신','강감찬']
print(id(name))

name2 = name
print(id(name2))

name2[0] = '김길동'
print(name)
print(name2)

import copy
name3 = copy.deepcopy(name)
print(id(name))
print(id(name3))

name[1] = '이순신장군'
print(name)
print(name3)