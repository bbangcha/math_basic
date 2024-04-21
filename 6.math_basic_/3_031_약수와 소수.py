import random

rNum1 = random.randint(100, 1000)
print(f'rNum1 : {rNum1}')

yaksuList = {}


for n in range(1, rNum1 + 1):

    soinsuflag = 0

    # 약수
    if rNum1 % n == 0:
        print(f'{rNum1}의 약수 : {n}')
        soinsuflag += 1

    # 소수
    if rNum1 !=1:
        flag = True
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break

        if(flag):
            print(f'{rNum1}의 소수 : {n}')
            soinsuflag += 1

    #소인수
    if soinsuflag >= 2:
        print(f'{rNum1}의 소인수 : {n}')

