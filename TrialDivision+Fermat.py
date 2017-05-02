import math
import numpy as np
import matplotlib.pyplot as plt

def TrialDivision_Fermat(n,h):
    a=0
    for x in range (2, h+1):
        a=a+1
        if n%x==0:
            return x,n/x,a
    x = math.ceil(math.sqrt(n))
    while True:
        y = math.sqrt(math.pow(x,2)-n)
        a=a+1
        if y==int(y):
            p = x-y
            q = x+y
            return p,q,a
        else:
            x=x+1

def TDFtogether(s): 
    N = []
    TDF = []
    Np = []
    TDFp = []

    for n in range (3,50001,2):
        p,q,a = TrialDivision_Fermat(n,s)
        if p==1 or p==n:
            Np.append(n)
            TDFp.append(a)
        else:
            N.append(n)
            TDF.append(a)
    return N, TDF

def TDFtogethersqrt(s): 
    N = []
    TDF = []
    Np = []
    TDFp = []

    for n in range (3,50001,2):
        p,q,a = TrialDivision_Fermat(n,int(math.sqrt(n)/s))
        if p==1 or p==n:
            Np.append(n)
            TDFp.append(a)
        else:
            N.append(n)
            TDF.append(a)
    return N, TDF

N1, TDF1, = TDFtogether(85)
N2, TDF2, = TDFtogether(115)
N3, TDF3, = TDFtogether(175)
N4, TDF4, = TDFtogethersqrt(2.5)
print max(TDF4)
N5, TDF5, = TDFtogethersqrt(1.85)
print max(TDF5)
N6, TDF6, = TDFtogethersqrt(1.25)
print max(TDF6)
        
plt.subplot(2, 3, 1)
plt.xticks(rotation=60)
plt.plot(N1, TDF1, 'm+')
plt.ylabel('Number of Iterations')

plt.subplot(2, 3, 2)
plt.plot(N2, TDF2, 'm+')
plt.xticks(rotation=60)
plt.ylim(0,200)
plt.title('Combined Algorithms')

plt.subplot(2, 3, 3)
plt.plot(N3, TDF3, 'm+')
plt.xticks(rotation=60)
plt.ylim(0,200)

plt.subplot(2, 3, 4)
plt.plot(N4, TDF4, 'm+')
plt.xticks(rotation=60)
plt.ylabel('Number of Iterations')

plt.subplot(2, 3, 5)
plt.xlabel('Value of N')
plt.plot(N5, TDF5, 'm+')
plt.xticks(rotation=60)
plt.ylim(0,200)

plt.subplot(2, 3, 6)
plt.plot(N6, TDF6, 'm+')
plt.xticks(rotation=60)

plt.tight_layout()
plt.savefig('TDF.png')
plt.show()
