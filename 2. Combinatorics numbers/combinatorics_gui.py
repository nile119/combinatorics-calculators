#
# - Подсчёт комбинаторных чисел + ГПИ
#

from math import factorial

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    
    
root=tk.Tk()
root.title('Комбинаторные числа')
root1=tk.LabelFrame()
root1.grid(padx=5,pady=5)

#Основные фрэймы

t1=tk.LabelFrame(root1,text='Возведение в степень',padx=5, pady=5,labelanchor=tk.N)
t1.grid(row=2,column=2,padx=20,pady=20)

t2=tk.LabelFrame(root1,text='Сочетания (с возвращением)',padx=5, pady=5,labelanchor=tk.N)
t2.grid(row=2,column=3,padx=10,pady=10)

t3=tk.LabelFrame(root1,text='Размещения (неполный факториал)',padx=5, pady=5,labelanchor=tk.N)
t3.grid(row=3,column=2,padx=10,pady=10)

t4=tk.LabelFrame(root1,text='Сочетания (без возвращения)',padx=5, pady=5,labelanchor=tk.N)
t4.grid(row=3,column=3,padx=10,pady=10)

info1=tk.Label(root1,text='Выбор с возвращением:',wraplength=150)
info1.grid(row=2,column=1,padx=10,pady=10)

info2=tk.Label(root1,text='Выбор без возвращения:',wraplength=150)
info2.grid(row=3,column=1,padx=10,pady=10)

info3=tk.Label(root1,text='Упорядоченные выборки:',wraplength=200)
info3.grid(row=1,column=2,padx=10,pady=10)

info4=tk.Label(root1,text='Неупорядоченные выборки:',wraplength=200)
info4.grid(row=1,column=3,padx=10,pady=10)

# ------ Фрэйм t1 -------

n1=tk.StringVar()
M1=tk.StringVar()
res1=tk.StringVar()

def result1():
    try:
        a=int(n1.get())
        b=int(M1.get())
        if (a<=0)|(b<=0):
            res1.set('Введи M>0 и n>0')
        else:
            res1.set(str(b**a))
    except ValueError:
        res1.set('Введи целые числа')

formula1=tk.PhotoImage(file='Pic1.png',width=120,height=50)
img1=tk.Label(t1,image=formula1,height=69,width=150)
img1.grid(row=1,column=1,columnspan=4)
tk.Label(t1,text='=', width=2).grid(row=1,column=5)
tk.Label(t1,textvariable=res1,width=20,wraplength=150).grid(row=1,column=7)
tk.Label(t1,text='n =').grid(row=2,column=1)
tk.Entry(t1,textvariable=n1,width=10).grid(row=2,column=2,columnspan=5,padx=3)
tk.Label(t1,text='M =').grid(row=3,column=1)
tk.Entry(t1,textvariable=M1,width=10).grid(row=3,column=2,columnspan=5,padx=3)
tk.Button(t1, text='Результат',command=result1,height=2).grid(row=2,column=7,rowspan=2,pady=5)

# ------ Фрэйм t2 -------

n2=tk.StringVar()
M2=tk.StringVar()
res2=tk.StringVar()

def result2():
    try:
        n=int(n2.get())
        M=int(M2.get())
        if (M<=0)|(n<0):
            res2.set('Введи M>0')
        elif (n>M):
            res2.set('M не может быть меньше n')
        else:
            i=(M+n-1)-(n-1)
            summa=1
            while i<=(M+n-1):
                summa=summa*i
                i+=1
            summa=int(summa/factorial(n))
            res2.set(str(summa))
    except ValueError:
        res2.set('Введи целые числа')

formula2=tk.PhotoImage(file='Pic2.png',width=120,height=50)
img2=tk.Label(t2,image=formula2,height=69,width=150)
img2.grid(row=1,column=1,columnspan=4)
tk.Label(t2,text='=', width=2).grid(row=1,column=5)
tk.Label(t2,textvariable=res2,width=20,wraplength=150).grid(row=1,column=7)
tk.Label(t2,text='n =').grid(row=2,column=1)
tk.Entry(t2,textvariable=n2,width=10).grid(row=2,column=2,columnspan=5,padx=3)
tk.Label(t2,text='M =').grid(row=3,column=1)
tk.Entry(t2,textvariable=M2,width=10).grid(row=3,column=2,columnspan=5,padx=3)
tk.Button(t2, text='Результат',command=result2,height=2).grid(row=2,column=7,rowspan=2,pady=5)

# ------ Фрэйм t3 -------

n3=tk.StringVar()
M3=tk.StringVar()
res3=tk.StringVar()

def result3():
    try:
        n=int(n3.get())
        M=int(M3.get())
        if (M<=0)|(n<0):
            res3.set('Введи M>0')
        elif (n>M):
            res3.set('M не может быть меньше n')
        else:
            i=M-(n-1)
            summa=1
            while i<=M:
                summa=summa*i
                i+=1
            res3.set(str(summa))
    except ValueError:
        res3.set('Введи целые числа')
        
formula3=tk.PhotoImage(file='Pic3.png',width=120,height=50)
img3=tk.Label(t3,image=formula3,height=69,width=150)
img3.grid(row=1,column=1,columnspan=4)
tk.Label(t3,text='=', width=2).grid(row=1,column=5)
tk.Label(t3,textvariable=res3,width=20,wraplength=150).grid(row=1,column=7)
tk.Label(t3,text='M =').grid(row=2,column=1)
tk.Entry(t3,textvariable=M3,width=10).grid(row=2,column=2,columnspan=5,padx=3)
tk.Label(t3,text='n =').grid(row=3,column=1)
tk.Entry(t3,textvariable=n3,width=10).grid(row=3,column=2,columnspan=5,padx=3)
tk.Button(t3, text='Результат',command=result3,height=2).grid(row=2,column=7,rowspan=2,pady=5)

# ------ Фрэйм t4 -------

n4=tk.StringVar()
M4=tk.StringVar()
res4=tk.StringVar()

def result4():
    try:
        n=int(n4.get())
        M=int(M4.get())
        if (M<=0)|(n<0):
            res4.set('Введи M>0')
        elif (n>M):
            res4.set('M не может быть меньше n')
        else:
            i=M-(n-1)
            summa=1
            while i<=M:
                summa=summa*i
                i+=1
            summa=int(summa/factorial(n))
            res4.set(str(summa))
    except ValueError:
        res4.set('Введи целые числа')

formula4=tk.PhotoImage(file='Pic4.png',width=120,height=50)
img4=tk.Label(t4,image=formula4,height=69,width=150)
img4.grid(row=1,column=1,columnspan=4)
tk.Label(t4,text='=', width=2).grid(row=1,column=5)
tk.Label(t4,textvariable=res4,width=20,wraplength=150).grid(row=1,column=7)
tk.Label(t4,text='n =').grid(row=2,column=1)
tk.Entry(t4,textvariable=n4,width=10).grid(row=2,column=2,columnspan=5,padx=3)
tk.Label(t4,text='M =').grid(row=3,column=1)
tk.Entry(t4,textvariable=M4,width=10).grid(row=3,column=2,columnspan=5,padx=3)
tk.Button(t4, text='Результат',command=result4,height=2).grid(row=2,column=7,rowspan=2,pady=5)


root.mainloop()
