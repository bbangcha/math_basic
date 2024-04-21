inputN = int(input('n항 입력 : '))

n = 1; nCnt = 1; searchN = 0

flag = True
while flag:

    for i in range(1, (n + 1)):
        if i == n :
            print(f'{i} ', end='')
        else:
            print(f'{i}, ', end='')


        nCnt += 1
        if nCnt > inputN:
            searchN = i
            flag = False
            break

    print()
    n += 1

print(f'{inputN}항의 값 : {searchN}')