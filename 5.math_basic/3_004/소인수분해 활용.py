inputNum = int(input('1보다 큰 정수 : '))

n=2
searchNumber = [] # [](리스트) 선언
while n <= inputNum:
    if inputNum % n == 0:
        print(f'소인수 : {n}')
        # count함수 : n(매개변수)의 개수가 searchNumber 리스트에 몇개가 있는지 알려주는 함수
        if searchNumber.count(n) == 0:
            # append함수: 새로 발견된 요소 추가
            searchNumber.append(n)
        elif searchNumber.count(n) == 1:
            # remove함수: 요소 삭제
            searchNumber.remove(n)
        inputNum /= n # inputNum = inputNum / n

    else:
        n += 1

print(f'searchNumber : {searchNumber}')