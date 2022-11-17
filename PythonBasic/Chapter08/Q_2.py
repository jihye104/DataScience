import os
print(os.getcwd())

while True:
    input_write = input("저장할 내용을 입력하세요 (종료는 엔터) : ")+"\n"

    if input_write == "\n":
        break

    try:
        test = open("test2.txt",mode="a")
        test.write(input_write)
        test.close()

    except Exception as e:
        print(f"Error 발생 : {e}")

