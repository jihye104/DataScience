dataset = [5,10,18,22,35,55,75,103]
value = int(input("검색할 값 입력 : "))
low = 0
high = len(dataset)-1
loc = 0
state = False

while low <= high:
    mid = (low+high)//2

    if dataset[mid] > value:
        high = mid-1

    elif dataset[mid] < value:
        low = mid+1

    else:
        loc = mid
        state = True
        break

    if state:
        print('찾은위치 : %d번째'%(loc+1))

    else:
        print('찾는 값은 없습니다.')