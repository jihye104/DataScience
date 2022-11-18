import os
import os.path
print(os.getcwd())

while True:
    msg = input("메시지를 입력하세요 : ")+"\n"

    if msg == "\n":
        break

    try:
        with open("\\Desktop-f1gtk6n/데이터분석_수업/김지혜/메세지.txt", mode="a", encoding="UTF-8") as file:
            file.write(msg)


    except Exception as e:
        print(f"Error 발생 : e")
