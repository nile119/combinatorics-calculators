import numpy as np
import matplotlib.pyplot as plt
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from math import factorial
    
'''
body=tk()
body.title('Биномиальное распределение')
'''

vkladka1=tk.Tk()
vkladka1.title('Биномиальное распределение')

# Отображение формулы.

ramka_formula1=tk.LabelFrame(vkladka1,
                             text='Биномиальное распределение',
                             labelanchor=tk.N)
ramka_formula1.grid(row=1,
                    column=1,
                    columnspan=2,
                    padx=20,
                    pady=20)

formula1=tk.PhotoImage(file='pic1.png')
pic1=tk.Label(ramka_formula1,
              image=formula1)
pic1.grid()

# Ввод данных

ramka_dano1=tk.Frame(vkladka1)                    
ramka_dano1.grid(column=1,
                 columnspan=2,
                 row=2,
                 padx=20)

tk.Label(ramka_dano1,
         text='Где:',
         justify=tk.LEFT).grid(row=1,
                               column=1,
                               columnspan=2)
k1=tk.StringVar()
n1=tk.StringVar()
p1=tk.StringVar()
na_ekrane=0

# Поля ввода

def vvod(frame,a,b,c,d):
    
    tk.Label(frame,
             text=str(a),
             justify=tk.LEFT).grid(row=d+1,
                                   column=1,
                                   sticky=tk.W,
                                   padx=3)
    tk.Label(frame,
             text='=',
             justify=tk.LEFT).grid(row=d+1,
                                   column=2,
                                   sticky=tk.W,
                                   padx=3)
    if (a=='q')|(a=='k'):
        tk.Label(frame,
                 text=str(b),
                 justify=tk.LEFT).grid(row=d+1,
                                       column=3,
                                       sticky=tk.W,
                                       padx=3)
    else:
        tk.Entry(frame,
                 textvariable=b,
                 width=10).grid(row=d+1,
                                column=3,
                                sticky=tk.W,
                                padx=3)
    tk.Label(frame,
             text='-',
             justify=tk.LEFT).grid(row=d+1,
                                   column=4,
                                   sticky=tk.W,
                                   padx=3)
    tk.Label(frame,
             text=str(c),
             justify=tk.LEFT).grid(row=d+1,
                                   column=5,
                                   sticky=tk.W,
                                   padx=3)


vvod(ramka_dano1,'k','0...n','количество успешных событий в выборке,',1)
vvod(ramka_dano1,'n',n1,'величина выборки,',2)
vvod(ramka_dano1,'p',p1,'вероятность успеха,',3)
vvod(ramka_dano1,'q','1 - p','вероятность провала.',4)

# Сбор значений из полей ввода


def n_entry(a):
    try:
        n=int(a.get())
        if (n<=0):
            return 'Число n не должно быть меньше 1,'
        else:
            return n
    except ValueError:
        return 'Число n должно быть целым,'

def p_entry(a):
    try:
        p=float(a.get())
        if not 0<=p<=1:
            return 'Вероятность p должна быть от 0 до 1.'
        else:
            return p  
    except ValueError:
        return 'Вероятность p должна быть десятичной дробью.'

"""
def debug():
    print (str(k_entry(k1))+'\n'+str(n_entry(n1,k1))+'\n'+str(p_entry(p1)))
"""

def bin_coef(n,k):
    i=n-(k-1)
    summa=1
    while i<=n:
        summa=summa*i
        i+=1
    summa=int(summa/factorial(k))
    return summa
    
#  График.

def vivod():
    
    global n1,p1
    
    n=n_entry(n1)
    p=p_entry(p1)

    if (type(n)==type(1))&(type(p)==type(.1)):        
        k_1=np.linspace(0,n,n+1,dtype=np.int8)
        p_1=[]
        for i in k_1:
            p_1.append(bin_coef(int(n),i)*(p**i)*((1-p)**(int(n)-i)))
            print (p_1)

        global grafik1,grafik,ax,na_ekrane
        plt.delaxes(ax)
        grafik=plt.figure(1)
        ax=grafik.add_subplot()
        ax.plot(k_1,p_1)
        plt.savefig('fig1.png')

        ramka_resultat1.delete(na_ekrane)
        grafik1=tk.PhotoImage(file='fig1.png')
        ramka_resultat1.config(height=480,
                               width=640)
        na_ekrane= ramka_resultat1.create_image(320,
                                                240,
                                                image=grafik1)
    else:
        ramka_resultat1.delete(na_ekrane)
        ramka_resultat1.config(height=480,width=640)
        na_ekrane=ramka_resultat1.create_text(320,
                                              240,
                                              text='n: '+str(n)+'\np: '+str(p))
        

def vivod_okno():
    plt.show()
    

ramka_resultat1=tk.Canvas(vkladka1)                             
ramka_resultat1.grid(row=1,
                     column=3,
                     rowspan=3,
                     padx=15,
                     pady=15)

grafik1=tk.PhotoImage(file='fig1.png')
ramka_resultat1.config(height=480,width=640)


grafik=plt.figure(1)
ax=grafik.add_subplot()

tk.Button(vkladka1,
          text='Посчитать результат,\nпостроить график',
          command=vivod,
          height=3).grid(row=3,
                         column=1,
                         padx=20,
                         pady=20)

tk.Button(vkladka1,
          text='Открыть график в\nинтерактивном окне',
          command=vivod_okno,
          height=3).grid(row=3,
                         column=2,
                         padx=20,
                         pady=20)


vkladka1.mainloop()
