inputN = int(input('n번째 항 입력 : '))

valueN = 0; sumN = 0

valuePre2 = 0
valuePre1 = 0

n = 1

while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valuePre2 = valueN
        valuePre1 = valueN
        sumN += valueN

        n += 1

    else:
        valueN = valuePre2 + valuePre1
        valuePre2 = valuePre1
        valuePre1 = valueN
        sumN += valueN

        n += 1

print(f'{inputN}번쨰 항의 값 : {valueN}')
print(f'{inputN}번쨰 항까지의 합 : {sumN}')