cnt = 0
free_ticket = 3
sale_ticket = 5

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

    if price != 0:
        cnt += 1

        print(f"귀하는 {grade} 등급이며, 요금은 {price}원 입니다.")

        pay = int(input("요금 유형을 선택하세요. (1 : 현금, 2 : 공원 전용 신용 카드) : "))

        if pay == 1:
            fee = int(input("요금을 입력하세요 : "))

            if fee < price:
                print(f"{price-fee}원이 모자랍니다. 입력하신 {fee}를 반환합니다.")

            elif fee == price:
                print("감사합니다. 티켓을 발행합니다.")

            elif fee > price:
                print(f"감사합니다. 티켓을 발행하고 거스름돈 {fee-price}원을 반환 합니다.")

        elif pay == 2:
            price *= 0.9

            if age >= 60 and age <= 65:
                price *= 0.95

            print(f"{price}원 결제 되었습니다. 티켓을 발행합니다.")

        if cnt%7 == 0 and free_ticket > 0:
            free_ticket -= 1

            print(f"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 {free_ticket}장")

        elif cnt%4 == 0 and sale_ticket > 0:
            sale_ticket -= 1

            print(f"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 {sale_ticket}장")

    else:
        print(f"귀하는 {grade} 등급이며, 요금은 {price}원 입니다.")