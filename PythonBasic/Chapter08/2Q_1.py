def my_div(num1, num2):
    return num1 / num2, num1 // num2, num1 % num2

try:
    print(my_div(10, 2))

except:
    print("분모가 0 입니다.")

