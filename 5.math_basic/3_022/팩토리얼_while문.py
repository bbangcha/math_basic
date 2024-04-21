inputN = int(input('n입력 : '))

result = 1
n = 1

while n <= inputN:
    result *= n
    n += 1

print(f'{inputN} 팩토리얼 : {result}')