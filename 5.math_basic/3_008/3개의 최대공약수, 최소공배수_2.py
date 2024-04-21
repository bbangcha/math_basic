fruit = 3; fish = 4; vegetable = 5

maxNum = 0

for i in range(1, fruit + 1):
    if fruit % i == 0 and fish % i == 0:
        maxNum = i

print(f'최소공배수 : {maxNum}')
minNum = (fruit * fish) // maxNum
print(f'최대공약수 : {minNum}')

newNum = minNum

for i in range(1, newNum + 1):
    if newNum % i == 0 and vegetable % i ==0:
        maxNum = i

print(f'{fruit}, {fish}, {vegetable}의 최대공약수 : {maxNum}')
minNum = (newNum * vegetable) // maxNum
print(f'{fruit}, {fish}, {vegetable}의 최소공배수 : {minNum}')
print('60일마다 모든 선박이 도착')

