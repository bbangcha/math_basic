inputN = int(input('n 입력 : '))

valueN = 0
sumN = 0

valuePreN2 = 0
valuePreN1 = 0

n = 1
while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valuePreN2 = valueN
        valuePreN1 = valueN
        sumN += valueN
        n += 1

    else:
        valueN = valuePreN2 + valuePreN1
        valuePreN2 = valuePreN1
        valuePreN1 = valueN
        sumN += valueN
        n += 1

print(f'{inputN}번째 항의 값 : {valueN}')
print(f'{inputN}번째 항까지의 값 : {sumN}')