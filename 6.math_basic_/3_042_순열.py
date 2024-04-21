numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

resultP = 1

for n in range(numN, numN - numR, -1):
    resultP *= n
    print(f'n : {n}')

print(f'resultP : {resultP}')