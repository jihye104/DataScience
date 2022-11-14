# 5.	삼각형 출력 문제 ver2
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")