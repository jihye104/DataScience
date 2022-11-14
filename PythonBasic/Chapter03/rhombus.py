while True:
    num1 = int(input("홀수를 입력하세요(0 <- 종료 ) : "))

    if not num1:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    for i in range(1, num1+1):
        for j in range((num1+1)-i):
            print(" ", end=" ")

        for j in range((2*i)-1):
            print("*", end=" ")

        print("")

