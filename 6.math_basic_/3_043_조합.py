numN = int(input('numN 입력 : '))
numR = int(input('numN 입력 : '))

resultP = 1
resultR = 1
resultC = 1

for n in range(numN, numN - numR, -1):
    resultP *= n

for n in range(numR, 0, -1):
    resultR *= n

resultC = int(resultP / resultR)
print(f'reslutC : {resultC}')

result = (1 / resultC) * 100
print(f'result : {round(result, 2)}')
