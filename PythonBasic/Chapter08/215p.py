# 유형별 예외처리
print("유형별 예외처리")

try:
    div = 1000/2.53
    print("div = %5.2f" %div)

    div = 1000/0
    f = open("c:\\test.txt")
    num = int(input("숫자입력 : "))
    print(f"num = {num}")

# 다중 예외처리 클래스
except ZeroDivisionError as e: #산술적 예외처리
    print(f"오류정보 : {e}")

except FileNotFoundError as e: #파일 열기 예외처리
    print(f"오류정보 : {e}")

except Exception as e: #기타 예외처리
    print(f"오류정보 : {e}")

finally:
    print("finally 영역 - 항상 실행되는 영역")