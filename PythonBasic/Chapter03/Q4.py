# A형
weight = int(input("짐의 무게는 얼마입니까?"))

if weight >= 10:
    print("수수료는 10,000원 입니다.")

else:
    print("수수료는 없습니다.")

# B형
weight2 = int(input("짐의 무게는 얼마입니까?"))

if weight2 >= 10:
    price = int(weight2/10)*10000
    print(f"수수료는 {format(price, '3,d')} 입니다.")

else:
    print("수수료는 없습니다.")