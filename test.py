import numpy as np
from Polinom import lagranz
import math
# импортируем один из пакетов Matplotlib
import pylab
# импортируем пакет со вспомогательными функциями
from matplotlib import mlab
from prettytable import PrettyTable  # импортируем установленный модуль
n=10
a=[0]*n
knote = [0] * n * 2
xx=[0]*n
yy=[0]*n
print("введите конец интервала: ")
x = input()  # конец интервала ?

# интервал изменения переменной по оси X
xmin = 0.001
xmax = int(x)

def func0(z):
    return math.log10(z)*z*math.sin(z) # функция которая задается по умолчанию 1;0 10;10 100;200 0.1;-0.1

def main():
    i=0
    c=1
    b=0;
    while c <= n:  # ищем координаты узлов
       # if i%2==0:
         #print("введите координаты ",c," узла (всего 10)")
         #print("(сначала x, потом y (не забывайте нажимать enter после каждой координаты)): ")
         #c+=1
        #knote[i] = input()
            xx[b] = 0.5*(xmin+xmax)+0.5*(xmax-xmin)*math.cos((2*c-1)*math.pi/20) # Чебышев
       # else:
            yy[b]=func0(xx[i])
            c+=1
            b+=1
            i+=1
        #b+=1

    #a=
    #print(knote)
  #  return(a)

if __name__ == "__main__":
  main()
 # print(a)

'''def func(t):
    sum=0
    i=n-1
    j=0
    while(i>=0):
        sum=sum+a[j]*(t**i)
        i-=1
        j+=1
    return sum'''
# шаг между точками
dx = 0.1
xlist4=np.arange(xmin, 100, dx)
ylist4 = [lagranz(xx,yy,i) for i in xlist4]

def func(t):
    return ylist4[t];




# табличка
i = 1
th = [0] * 101
th[0] = "-"
count=xmin
while (i <= 100):
    th[i] = str(round(count,3))
    count=count+dx
    i+=1
table = PrettyTable(th)

i=1
td=[0]*303
td[0]="real y"
count=xmin
while (i <= 100):
    td[i] = round(func0(count),3)
    count = count + dx
    i+=1
i=102
td[101]="possible y'"
count=xmin
cc=0
while (i <= 201):
    td[i] = round(func(cc),3)
    #td[i] = round(func(count), 3)
    cc+=1
    count = count + dx
    i+=1
i=203
td[202]="y-y'"
count=xmin
cc=0
while (i <= 302):
    td[i] = round(func0(count)-func(cc),3)
    count = count + dx
    cc+=1
    i+=1

while td:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td[:101])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td = td[101:]

print(table)  # Печатаем таблицу

# создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = np.arange(xmin, xmax, dx)

# вычислим значение функции в заданных точках
#ylist = [func(t) for t in xlist]
ylist = [lagranz(xx,yy,i) for i in xlist]
ylist0 = [func0(t) for t in xlist]

i=0
j=0
k=0
xn=[0]*n
yn=[0]*n
while(i<n):
    if i%2==0:
        xn[j]=float(xx[i])
        yn[j]=float(yy[i])
        k+=1
    i+=1

# рисуем график 1
pylab.figure(1)
pylab.plot(xlist, ylist, label='polynomial', color='#88c999')
pylab.plot(xlist, ylist0, label='original function', color='blue')
pylab.grid(True)

pylab.scatter(xx, yy, label='nodal points', c='hotpink')
pylab.legend()
#pylab.show()

#def func2(r):
 #   return func0(r)-func(r)

ylist2=ylist;
for t in xlist:
    cc=0
    ylist2[cc]=func0(t)-func(k)
# график 2
pylab.figure(2)
#ylist2=[func2(t) for t in xlist]
pylab.plot(xlist, ylist2, label='delta', color='darkred')
pylab.grid(True)
pylab.legend()
pylab.show()

