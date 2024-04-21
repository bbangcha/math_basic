inputN = int(input('n입력 : '))

result = 1

for n in range(1, inputN + 1):
    result *= n

print(f'{inputN} 팩토리얼 : {result}')