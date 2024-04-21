inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n번째 입력 : '))

# 등비수열의 일반항 공식 : an = a1 * r ^ (n - 1)
valueN = inputN1 * inputR ** (inputN - 1)
print(f'{inputN}번째 항의 값 : {valueN}')