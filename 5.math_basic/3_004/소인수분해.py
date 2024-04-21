inputNum = int(input('1보다 큰 정수 : '))

n=2

while n <= inputNum:
    if inputNum % n == 0:
        print(f'소인수 : {n}')
        inputNum /= n # inputNum = inputNum / n

    else:
        n += 1