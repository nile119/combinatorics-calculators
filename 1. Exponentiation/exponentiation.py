
# -*- encoding: UTF-8 -*-

#
# Возведение в степень целых чисел
#

from string import digits
from random import randrange
from os import name

cond1=0
print('\n * Введи целое положительное число "M":')
while (cond1==0):
    try:
        M=int(input(' M = '))
    except:
        net=('Нет,','Да нет же,', 'Неправильно,') 
        print(net[randrange(len(net))]+'введи целое число.\n')
    else:
        if M<0:
            print ('Введи ПОЛОЖИТЕЛЬНОЕ целое число.\n')
        elif (len(str(M))>4):
            print('Длина M - < 5 знаков')
        else:
            cond1=1
cond2=0
print('\n * Хорошо, теперь введи целое положительное число "M":')
while (cond2==0):
    try:
        n=int(input(' n = '))
    except:
        net=('Нет,','Да нет же,', 'Неправильно,') 
        print(net[randrange(len(net))]+'введи целое число.\n')
    else:
        if n<0:
            print ('Введи ПОЛОЖИТЕЛЬНОЕ целое число.\n')
        elif (len(str(n))>4):
            print('Длина n - < 5 знаков')
        else:
            cond2=1

r1=str(int(M)**int(n))

if int(M)==0:
    print('\nНе имеет смысла при M=0.\n')
elif len(r1)>10:
    print('\n%s в степени %s ~ %s,%s * 10^%s' % (M,n,r1[0],r1[1:3],len(r1)-1))
else:
    print('\n%s в степени %s = %d\n' % (M,n,int(M)**int(n)))
if name=='nt':
    input()
del n,M
