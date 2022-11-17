# (1) 현재 작업디렉터리
import os
print(f"현재 경로 : {os.getcwd()}")

# (2) 예외처리
try:
    # (3) 파일 읽기
    ftest1 = open("data/ftest1.txt", mode ='r')
    print(ftest1.read()) #파일 전체 읽기

    # (4) 파일 쓰기
    ftest2 = open("data/ftest2.txt", mode = 'w')
    ftest2.write("my first text~~~~~") #파일쓰기

    # (5) 파일쓰기 + 내용추가
    ftest3 = open("data/ftest3.txt", mode = 'a')
    ftest3.write("\nmy second text~~~~~") #파일쓰기(추가)

except Exception as e:
    print(f"Error 발생 : {e}")

finally:
    ftest1.close() # 파일객체닫기
    ftest2.close()
    ftest3.close()