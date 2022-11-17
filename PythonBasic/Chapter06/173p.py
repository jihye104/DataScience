# (1) 리스트 열거형 객체 이용
lst = [1,3,5]

for i,c in enumerate(lst):
    print(f"색인 : {i}, 내용 : {c}")

# (2) 튜플 열거형 객체 이용
dit = {"name":"홍길동","job":"회사원","addr":"서울시"}

for i,k in enumerate(dit):
    print(f"순서 : {i}, 키 : {k}, 값 : {dit[k]}")