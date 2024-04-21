inputN = int(input('n입력 : '))

def factorialFun(n):
    if n == 1:
        return 1

    return n * factorialFun(n - 1)

print(f'{inputN} 팩토리얼 : {factorialFun(inputN)}')