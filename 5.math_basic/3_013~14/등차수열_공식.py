inputN1 = int(input('a1 입력 : '))
inputD = int(input('공차 입력 : '))
inputN = int(input('n번째 입력 : '))

# 등차수열의 일반항 공식 : an = a1 + (n -1) * d
valueN = inputN1 + (inputN -1) * inputD
print(f'{inputN}번째 항의 값 : {valueN}')