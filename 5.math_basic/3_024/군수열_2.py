inputN = int(input('n항 입력 : '))

n = 1; nCnt = 1; searchNC = 0; searchNP = 0

flag = True
while flag:

    for i in range(1, (n + 1)):
        if i == n :
            print(f'{i}/{n + 1 - i} ', end='')
        else:
            print(f'{i}/{n + 1 - i}, ', end='')
        nCnt += 1

        if nCnt > inputN:
            searchNC = i
            searchNP = n + 1 - i
            flag = False
            break

    print()
    n += 1

print(f'{inputN}항의 값 : {searchNC}/{searchNP}')