#
# - Расчёт биномиальных коэффициентов
#
#  1. Упорядоченный, с возвращением. (Возведение в степень).
#

from string import digits
from random import randrange

cond1=0
print('\n * Введи целое положительное число "M":')
while (cond1==0):
    M=input(' M = ')
    if ((set(M)<=(set(digits)|{'-'}))==False)|(len(M)==0):
        net=('Нет,','Да нет же,', 'Неправильно,')
        print(net[randrange(len(net))],'введи целое число.\n')
    elif {'-'}<(set(M)):
        print('Введи ПОЛОЖИТЕЛЬНОЕ целое число.\n')
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
    else:
        cond2=1
if int(M)==0:
    print('\nНе имеет смысла при M=0.\n')
else:
    print('\nM в степени n = ', int(M)**int(n),'\n')
del n,M
