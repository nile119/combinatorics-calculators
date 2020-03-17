#
# - Расчёт биномиальных коэффициентов
#

#TODO: исправить ошибку при вводе буквенных символов.


from math import factorial
from random import randrange

def u_b(): # 1. Упорядоченный. Без возвращения.

    cond1=-1
    print('\nВведи целое положительное число "n":')
    while (cond1==-1):
        n=eval(input(' n = '))
        if type(n)!=type(1):
            net=('Нет.','Да нет же.', 'Неправильно.')
            print(net[randrange(len(net))],'\n')
        elif n<0:
            print('Необходимо ПОЛОЖИТЕЛЬНОЕ целое число.\n')
        else:
            cond1=1

    cond2=-1
    print('\nВведи целое положительное число "M":')
    while (cond2==-1):
        M=eval(input(' M = '))
        if type(M)!=type(1):
            net=('Нет.','Да нет же.', 'Неправильно.')
            print(net[randrange(len(net))],'\n')
        elif M<0:
            print('Необходимо ПОЛОЖИТЕЛЬНОЕ целое число.\n')
        else:
            cond2=1
            

    print('\nM в степени n = ', M**n)
    del n,M
    
u_b()
