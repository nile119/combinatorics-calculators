#
# Возведение в степень целых чисел
#

from string import digits
from random import randrange
from os import name

cond1=0
print('\n * Введи целое положительное число "M":')
while (cond1==0):
    M=input(' M = ')
    if ((set(M)<=(set(digits)|{'-'}))==False)|(len(M)==0):
        net=('Нет,','Да нет же,', 'Неправильно,')
        print(net[randrange(len(net))],'введи целое число.\n')
    elif {'-'}<(set(M)):
        print('Введи ПОЛОЖИТЕЛЬНОЕ целое число.\n')
    elif (len(str(M))>4):
        print('Длина M - < 5 знаков')
    else:
        cond1=1
        
cond2=0
print('\n * Хорошо, теперь введи целое положительное число "M":')
while (cond2==0):
    n=input(' n = ')
    if ((set(n)<=(set(digits)|{'-'}))==False)|(len(n)==0):
        net=('Нет,','Да нет же,', 'Неправильно,')
        print(net[randrange(len(net))],'введи целое число.\n')
    elif {'-'}<(set(n)):
        print('Введи ПОЛОЖИТЕЛЬНОЕ целое число.\n')
    elif (len(str(n))>4):
        print('Длина n - < 5 знаков')
    else:
        cond2=1

r1=str(int(M)**int(n))

if int(M)==0:
    print('\nНе имеет смысла при M=0.\n')
elif len(r1)>10:
    print('\nM в степени n ~ %s,%s * 10^%s' % (r1[0],r1[1:3],len(r1)-1))
else:
    print('\nM в степени n = ', int(M)**int(n))
if name=='nt':
    input()
del n,M
