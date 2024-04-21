inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n번째 입력 : '))

valueN = 0
sumN = 0

n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        print(f'{n}번쨰 항의 값 : {valueN}')
        n += 1
        continue

    valueN *= inputR
    sumN += valueN
    print(f'{n}번쨰 항까지의 합 : {valueN}')
    n += 1

print(f'{inputN}번쨰 항까지의 합 : {sumN}')