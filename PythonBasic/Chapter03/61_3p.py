#var = 10
var = 3

#들여쓰기(Indentation)으로 블럭을 표현
# 컨트롤+/ 해당 줄 자동 주석
"""
여러줄
주석
"""
# if var >= 5:
if var >= 100:
# print("var =",var) <- if 이하의 블럭은 동일한 들여쓰기 개수로 작성해야함
    print("var =", var)
    print("var는 5보다 크다.")
    print("조건이 참인 경우 실행")
else:
    print("조건이 거짓인 경우 실행")

print("항상 실행")