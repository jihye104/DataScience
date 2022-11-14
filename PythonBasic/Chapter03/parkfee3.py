while True:
    age = int(input("나이를 입력하세요 : "))
    price = 0

    if age >= 0 and age <= 3:
        grade = "유아"

    elif age >= 4 and age <= 13:
        price = 2000
        grade = "어린이"

    elif age >= 14 and age <= 18:
        price = 3000
        grade = "청소년"

    elif age >= 19 and age <= 65:
        price = 5000
        grade = "성인"

    elif age >= 66:
        grade = "노인"

    if price == 0:
        print(f"귀하는 {grade} 등급이며, 요금은 {price}원 입니다.")

    else:
        print(f"귀하는 {grade} 등급이며, 요금은 {price}원 입니다.")

        fee = int(input("요금을 입력하세요 : "))

        if fee < price:
            print(f"{price-fee}원이 모자랍니다. 입력하신 {fee}를 반환합니다.")

        elif fee == price:
            print("감사합니다. 티켓을 발행합니다.")

        elif fee > price:
            print(f"감사합니다. 티켓을 발행하고 거스름돈 {fee-price}원을 반환 합니다.")
