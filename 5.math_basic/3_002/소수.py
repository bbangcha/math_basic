inputNumber = int(input('0보다 큰 정수 입력 : '))

for number in range(2, (inputNumber + 1)):
    flag = True

    for n in range(2, number):
        if number % n ==0:
            flag = False
            break

    if flag:
        print(f'{number} : 소수!')

    else:
        print(f'{number} : 합성수')