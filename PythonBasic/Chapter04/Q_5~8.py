mem = {'kim99':12000,
       'lee66':11000,
       'han55':3000,
       'hong77':5000,
       'hwang33':18000}

#5
print("5번-----")

num = 1

for i in mem:
    print(f"{num}. 아이디 : {i}, 마일리지 : {mem[i]}점")
    num += 1

#6
print("6번-----")

MEM_ID = 'han55'
mem[MEM_ID] = 5000

print(mem)

#for문
for id in mem:
    if MEM_ID == id:
        print(f"{id}님의 마일리지가 {mem[id]}점으로 수정되었습니다.")

#get
print(f"{MEM_ID}님의 마일리지가 {mem.get(MEM_ID)}점으로 수정되었습니다.")

#7
print("7번-----")

MEM_ID = 'jang88'
mem[MEM_ID] = 7000

print(f"전체 딕셔너리 : {mem}")
print(f"{MEM_ID}님의 마일리지({mem.get(MEM_ID)}점)가 추가되었습니다.")

#8
print("8번-----")

score = []

for i in mem:
    score.append(mem[id])

result = max(score)

for id in mem:
    if mem[id] == result:
        max_id = id

print(f"{max_id}님의 {result}점이 가장 높은 점수입니다.")