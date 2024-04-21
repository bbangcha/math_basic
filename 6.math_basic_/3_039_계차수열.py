inputAN1 = int(input('a1 입력 : '))
inputAN = int(input('an 입력 : '))
inputBN1 = int(input('b1 입력 : '))
inputBD = int(input('bn 공차 입력 : '))

valueAN = 0
valueBN = 0

n = 1

while n <= inputAN:

    if n == 1:
        valueAN = inputAN1
        valueBN = inputBN1
        n += 1
        continue

    valueAN = valueAN + valueBN
    valueBN = valueBN + inputBD
    n += 1

print(f'an의 {inputAN}항의 값 : {valueAN}')
print(f'bn의 {inputAN}항의 값 : {valueBN}')