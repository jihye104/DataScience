# import os
# print(os.getcwd())
#
# life = open("life.txt", mode="r")
# print(life.read())

import os
print(os.getcwd())

try:
    w_test = open("test.txt",mode="w")
    w_test.write("Life is too short")
    w_test.close()

    r_test = open("test.txt",mode="r")
    print(r_test.read())
    r_test.close()

except Exception as e:
    print(f"Error 발생 : {e}")


