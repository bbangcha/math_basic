inputN1 = int(input('a1 입력 : '))
inputD = int(input('공차 입력 : '))
inputN = int(input('n번째 입력 : '))

valueN = 0

n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        print(f'{n}번쨰 항의 값 : {valueN}')
        n += 1
        continue

    valueN += inputD
    print(f'{n}번쨰 항의 값 : {valueN}')
    n += 1

print(f'{inputN}번쨰 항의 값 : {valueN}')
