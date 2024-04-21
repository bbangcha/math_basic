num1 = int(input('factorial1 입력 : '))

result1 = 1

for i in range(num1, 0, -1):
    result1 *= i

print(f'factorial1 : {result1}')

num2 = int(input('factorial2 입력 : '))

result2 = 1

for i in range(num2, 0, -1):
    result2 *= i

print(f'factorial2 : {result2}')

probability = result1 * result2

print(f'probability : {probability}')