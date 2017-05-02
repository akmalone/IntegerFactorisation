import math
import numpy as np
import matplotlib.pyplot as plt

def TrialDivision(n):
    a=0
    for x in range (2, int(math.sqrt(n))+1):
        a=a+1
        if n%x==0:
            return x,a
    return 'is prime',a

def Fermat(n):
    x = math.ceil(math.sqrt(n))
    a = 0
    if n%2==0:
        return 2,n/2,a
    while True:
        y = math.sqrt(math.pow(x,2)-n)
        a=a+1
        if y==int(y):
            p = x-y
            q = x+y
            return p,q,a
        else:
            x=x+1

NTD = []
TDsmaller = []
Fbigger = []
NF = []
Fsmaller = []
TDbigger = []

for n in range (1,20001,2):
    p,a = TrialDivision(n)
    q,r,b = Fermat(n)
    if not p=='is prime':
        if p==q and n/p==r:
            if a<b:
                NTD.append(n)
                TDsmaller.append(a)
                Fbigger.append(b)
            else:
                NF.append(n)
                Fsmaller.append(b)
                TDbigger.append(a)

plt.subplot(1, 3, 1)
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(NF, TDbigger, 'mx')
plt.plot(NTD, TDsmaller, 'cx')
plt.xticks(rotation=60)
plt.title("Trial Division")

plt.subplot(1, 3, 2)
plt.xlabel('Value of N')
plt.plot(NTD, Fbigger, 'cx', label='Trial Div')
plt.plot(NF, Fsmaller, 'mx', label="Fermat's")
plt.xticks(rotation=60)
plt.legend(loc=0, borderaxespad=0.)
plt.title("Fermat's Method")

plt.subplot(1, 3, 3)
plt.xlabel('Value of N')
plt.plot(NTD, Fbigger, 'cx')
plt.plot(NF, Fsmaller, 'mx')
plt.ylim(0,140)
plt.xticks(rotation=60)
plt.title("Fermat's Zoomed")

plt.tight_layout()
plt.savefig('TDorF2.png')
plt.show()
