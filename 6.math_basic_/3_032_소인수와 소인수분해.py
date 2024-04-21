import random

rNum1 = random.randint(100, 1000)
print(f'rNum1 : {rNum1}')


soinsuList = []

n = 2
while n <= rNum1:
    if rNum1 % n == 0:
        print(f'소인수 : {n}')
        soinsuList.append(n)
        rNum1 /= n
    else:
        n += 1

print(f'soinsuList : {soinsuList}')

tempNum = 0

for s in soinsuList:
    if tempNum != s:
       print(f'{s}\'s count : {soinsuList.count(s)}')
       tempNum = s


