import random
rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'rNum1 : {rNum1}')
print(f'rNum2 : {rNum2}')

maxNum = 0

for i in range(1 , min(rNum1, rNum2)):
    if rNum1 % i == 0 and rNum2 % i == 0:
        print(f'공약수 : {i}')
        maxNum = i

print(f'최대공약수 : {maxNum}')

minNum = (rNum1 * rNum2) // maxNum

print(f'최소공배수 : {minNum}')
