# age = int(input("나이를 입력하세요."))
#
# if age<0:
#     print("다시 입력하세요")
#     quit()
#
# if age >= 0 and age <= 3:
#     print("귀하는 유아 등급이며 요금은 무료입니다.")
#
# elif age >= 4 and age <= 13:
#     print("귀하는 어린이 등급이며 요금은 2,000원 입니다.")
#
# elif age >= 14 and age <= 18:
#     print("귀하는 청소년 등급이며 요금은 3,000원 입니다.")
#
# elif age >= 19 and age <= 65:
#     print("귀하는 성인 등급이며 요금은 5,000원 입니다.")
#
# elif age >= 66:
#     print("귀하는 노인 등급이며 요금은 무료입니다.")

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

    elif age < 0:
        print("다시 입력하세요")
        continue

    print(f"귀하는 {grade} 등급이며, 요금은 {price}원 입니다.")
