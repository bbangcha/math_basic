numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

result = 1

for n in range(numN, (numN - numR), -1):
    print(f'n : {n}')
    result *= n

print(f'result : {result}')
