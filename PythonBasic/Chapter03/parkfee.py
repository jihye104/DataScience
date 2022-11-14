# age = int(input("나이를 입력하세요."))
#
# if age >= 0 and age <= 3:
#     print("요금은 무료입니다.")
#
# elif age >= 4 and age <= 13:
#     print("요금은 2,000원 입니다.")
#
# elif age >= 14 and age <= 18:
#     print("요금은 3,000원 입니다.")
#
# elif age >= 19 and age <= 65:
#     print("요금은 5,000원 입니다.")
#
# elif age >= 66:
#     print("요금은 무료입니다.")

while True:
    age = int(input("나이를 입력하세요 : "))

    if age >= 4 and age <= 13:
        price = 2000

    elif age >= 14 and age <= 18:
        price = 3000

    elif age >= 19 and age <= 65:
        price = 5000

    else:
        price = 0

    print(f"요금은 {price}원 입니다.")