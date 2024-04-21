inputN1 = int(input('a1 입력 : '))
inputD = int(input('공차 입력 : '))
inputN = int(input('n번째 입력 : '))

# 등차수열의 일반항 공식 : an = a1 + (n -1) * d
# N번쨰의 일반항 값 구하기
valueN = inputN1 + (inputN -1) * inputD
print(f'{inputN}번째 항의 값 : {valueN}')
# 등차수열의 합 공식 : Sn = n(a1 + an) / 2
sumN = inputN * (inputN1 + valueN) / 2
print(f'{inputN}번째 항까지의 합 : {int(sumN)}')