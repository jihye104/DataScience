# 3. 하나의 문자열를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def wrap(func):
    def print_with_smile():
        func()
        print(":D")
    return print_with_smile

@wrap
def hello():
    str1 = input("문자열 입력 : ")
    print(str1)

hello()