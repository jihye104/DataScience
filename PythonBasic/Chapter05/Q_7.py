# 7. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def wrap(func):
    def make_url():
        print("www.",end="")
        func()
        print(".com")

    return make_url

@wrap
def url():
    print("naver",end="")

url()