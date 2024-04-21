flag = True

n = 1
nCnt = 1; searchNC = 0; searchNP = 0

sumN = 0
while flag:

    for i in range(1, (n + 1)):
        print(f'{i}/{n - i + 1} ', end='')

        sumN += i / (n - i + 1)
        nCnt += 1

        if sumN > 100:
            searchNC = i
            searchNP = n - i + 1
            flag = False
            break

    print()
    n += 1

searchNC = i
print(f'수열의 합이 최초 100을 초과하는 항 : {nCnt}, 값 :{searchNC}/{searchNP}, 합 : {round(sumN, 2)}')

