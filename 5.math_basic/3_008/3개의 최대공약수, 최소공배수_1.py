num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))
num3 = int(input('1보다 큰 정수 입력 : '))

maxNum = 0

for i in range(1, (num1 + 1)):
    if  num1 % i == 0 and num2 % i == 0:
        maxNum = i

print(f'최대공약수 : {maxNum}')

minNum = (num1 * num2 ) // maxNum
print(f'{num1}, {num2}의 최소공배수 : {minNum}')

newNum = minNum

for i in range(1, (newNum + 1)):
    if  newNum % i == 0 and num3 % i == 0:
        maxNum = i

print(f'최대공약수 : {maxNum}')

minNum = (newNum * num3) // maxNum
print(f'{num1}, {num2}, {num3}의 최소공배수 : {minNum}')