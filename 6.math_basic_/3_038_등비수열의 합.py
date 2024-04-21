inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n 입력 : '))

valueN = 0
sumN = 0

n = 1

while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        n += 1
        continue

    valueN *= inputR
    sumN += valueN
    n += 1

print(f'{inputN}번쨰 항의 값 : {valueN}')
print(f'{inputN}번쨰 항까지의 합 : {sumN}')


# 등비수열의 일반항 공식 : an = a1 * r ^ (n - 1)
valueN = inputN1 * inputR ** (inputN1 -1 )
print(f'{inputN}번쨰 항의 값 : {valueN}')
# 등비수열의 합 공식 : Sn = a1 * (1 - r^n) / (1-r)
sumN = inputN1 * (1 - (inputR ** inputN)) / (1 -inputR)
print(f'{inputN}번쨰 항까지의 합 : {sumN}')


