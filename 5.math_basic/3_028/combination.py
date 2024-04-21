numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN - numR), -1):
    print(f'n : {n}')
    resultP *= n

print(f'resultP : {resultP}')

for n in range(numR, 0, -1):
    print(f'n : {n}')
    resultR *= n

print(f'resultR : {resultR}')

resultC = int(resultP / resultR)

print(f'resultC : {resultC}')

result = (1/resultC) * 100

print(f'{round(result, 2)}%')
