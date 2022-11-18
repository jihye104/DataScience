import random

lotto = []

for i in range(6):
    num = random.randint(1,45)

    while num in lotto:
        num = random.randint(1,45)
        
    lotto.append(num)

print(lotto)
