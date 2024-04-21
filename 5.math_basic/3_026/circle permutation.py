n = int(input('친구 수 입력 : '))

result = 1

for i in range(1, n):
    result *= i

print(f'result : {result}')