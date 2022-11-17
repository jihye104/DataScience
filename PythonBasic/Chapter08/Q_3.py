import os
print(os.getcwd())

try:
    life = open("life.txt",mode="r")
    update = life.read()
    life.close()

    update = update.replace("java","python")

    life = open("life.txt", mode="w")
    life.write(update)
    life.close()

except Exception as e:
    print(f"Error 발생 : {e}")