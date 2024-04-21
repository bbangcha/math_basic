inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n번째 입력 : '))

# 등비수열의 일반항 공식 : an = a1 * r ^ (n - 1)
# N번쨰의 일반항 값 구하기
valueN = inputN1 * inputR ** (inputN - 1)
print(f'{inputN}번째 항의 값 : {valueN}')
# 등비수열의 합 공식 : Sn = a1 * (1 - r^n) / (1-r)
sumN = inputN1 * (1 - (inputR ** inputN)) / (1 - inputR)
print(f'{inputN}번째 항까지의 합 : {int(sumN)}')
