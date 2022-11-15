def wrap(func):
    def input_ingredient():
        print("안녕하세요. 저희 가게에 방문해 주세서 감사합니다.")
        print("1. 주문")
        print("2. 종료")
        input_msg = int(input("입력 : "))

        func()
    return input_ingredient

@wrap
def make_sandwiches():
    print(input("안녕하세요. 원하시는 재료를 입력하세요."))
