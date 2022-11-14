while True:
    num1 = int(input("홀수를 입력하세요(0 <- 종료 ) : "))

    if not num1:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    middle = int(num1/2)+1

    for i in range(1, middle*2):
        if i <= middle:
            for j in range(middle-i):
                print(" ", end=" ")

            for j in range((2*i)-1):
                print("*", end=" ")

            print("")

        else:
            for j in range(i-middle):
                print(" ", end=" ")

            for j in range((((2*middle)-i)*2)-1):
                print("*", end=" ")

            print("")




