import math
import numpy as np
import matplotlib.pyplot as plt

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

N = []
ferm = []

Np = []
fermp = []

for n in range (3,5001,2):
    p,q,a = Fermat(n)
    if p==1:
        Np.append(n)
        fermp.append(a)
    else:
        N.append(n)
        ferm.append(a)
        
plt.title("Fermat's Method")
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(Np, fermp, 'k^', label='Prime Numbers')
plt.plot(N, ferm, 'w^', label='Composite Numbers')

plt.legend(loc=0, borderaxespad=0.)

plt.savefig('Fresult1.png',bbox_inches='tight')

plt.clf()

plt.title("Fermat's Method without primes")
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(N, ferm, 'w^')

plt.plot(N, (3.0+np.asarray(N)/3.0)/2.0-np.sqrt(N), lw=2, c='red', label='p=3')
plt.plot(N, (5.0+np.asarray(N)/5.0)/2.0-np.sqrt(N), lw=2, c='orange', label='p=5')
plt.plot(N, (7.0+np.asarray(N)/7.0)/2.0-np.sqrt(N), lw=2, c='yellow', label='p=7')
plt.plot(N, (9.0+np.asarray(N)/9.0)/2.0-np.sqrt(N), lw=2, c='green', label='p=9')
plt.plot(N, (11.0+np.asarray(N)/11.0)/2.0-np.sqrt(N), lw=2, c='blue', label='p=11')
plt.plot(N, (13.0+np.asarray(N)/13.0)/2.0-np.sqrt(N), lw=2, c='indigo', label='p=13')
plt.plot(N, (15.0+np.asarray(N)/15.0)/2.0-np.sqrt(N), lw=2, c='violet', label='p=15')
plt.legend(loc=0, borderaxespad=0.)

plt.savefig('Fresult2.png',bbox_inches='tight')
plt.show()
