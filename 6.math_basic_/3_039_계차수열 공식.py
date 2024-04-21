# {2, 5, 11, 20, 32, 47, 65, 86, 110, 137, 167}
#   {3, 6, 9, 12, 15, 18..}
# an = (3n^2 - 3n + 4) / 2

inputAN = int(input('an 입력 : '))
inputAN1 = int(input('a1 입력 : '))

valueAN = ((3 * inputAN ** 2) -3 * inputAN + 4) / 2
print(f'{inputAN}항의 값 : {valueAN}')