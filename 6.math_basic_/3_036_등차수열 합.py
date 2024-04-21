inputN1 = int(input('a1 입력 : '))
inputD = int(input('공차 입력 : '))
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

    valueN += inputD
    sumN += valueN
    n += 1

print(f'{inputN}번째 항의 값 : {valueN}')
print(f'{inputN}번째 항까지의 합 : {sumN}')

# 등차수열의 일반항 공식 : an = a1 + (n -1) * d
valueN = inputN1 + (inputN - 1) * inputD
print(f'{inputN}번째 항의 값 : {valueN}')
# 등차수열의 합 공식 : Sn = n(a1 + an) / 2
sumN = inputN1 * (inputN1 + valueN) / 2
print(f'{inputN}번째 항까지의 합 : {sumN}')
