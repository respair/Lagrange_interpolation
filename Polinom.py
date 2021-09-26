import numpy as np
import pandas as pd
from numpy import linalg

n = 10

def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z
'''
#cols = ["1", "2", "3", "4"]
def Graph(knote):
   a = [0] * n  # будущие коэффициенты
   i=0
   j=0

   #matrix = np.array([n][n])
   matrix = np.zeros((n,n))
   #print(pd.DataFrame(matrix, columns=cols, index=cols))

   k=0
   while(i<2*n):              # заполнение матрицы
     while(j<n):
        if j!= n-1:
            matrix[k][j]=float(float(knote[i])**(n-j-1))
        else:
            matrix[k][j] = 1
        j+=1
     #matrix[i][j]=knote[i+1]
     i=i+2
     k+=1
     j=0
   #print(pd.DataFrame(matrix, columns=cols, index=cols))
   detM0=np.linalg.det(matrix)    # определитель начальной матрицы
   #print(detM0)
   detMt = [0]*n               # определители побочных матриц
   i=0
   j=0
   k=1
   matrix_time=np.array(matrix)
   while (j<n):
      while(i<n):
        matrix_time[i][j]=knote[k]
        i+=1
        k+=2
      detMt[j] = np.linalg.det(matrix_time)
      #print(pd.DataFrame(matrix_time, columns=cols, index=cols))
      #print(detMt[j])
      matrix_time = np.array(matrix)
      j+=1
      i=0
      k=1

   i=0
   while(i<n):
     if(detM0 != 0):
       a[i]= detMt[i]/detM0
       i+=1
     else:
         print("error: division by zero!!")
         exit(1)
       #print(a[i-1])
   return(a)
'''


