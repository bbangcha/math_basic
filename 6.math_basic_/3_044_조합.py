def proFun():

    numN = int(input('numN 입력 : '))
    numR = int(input('numR 입력 : '))

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(numN, (numN - numR), -1):
        resultP *= n

    for n in range(numR, 0, -1):
        resultR *= n

    resultC = int(resultP / resultR)
    return resultC

sample = proFun()
print(f'sample : {sample}')
event1 = proFun()
print(f'event1 : {event1}')
event2 = proFun()
print(f'event2 : {event2}')

print(f'probability : {round(event1 * event2 / sample * 100, 2)}')

