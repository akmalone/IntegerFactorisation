import math
import numpy as np
import matplotlib.pyplot as plt

def TrialDivision(n):
    a=0
    for p in range (2, int(math.sqrt(n))+1):
        a=a+1
        if n%p==0:
            return p,a 
    return 'is prime',a

def TrialDivision_odd(n):
    a=1
    if n%2==0:
        return 2,a
    else:
        for x in range (3, int(math.sqrt(n))+1,2):
            a=a+1
            if n%x==0:
                return x,a
    return 'is prime',a

def TrialDivision_6k1(n):
    a=1
    if n%2==0:
        return 2,a
    elif n%3==0:
        a=a+1
        return 3,a
    else:
        a=2
        x=5
        while x<=(int(math.sqrt(n))):
            a=a+1
            if n%x==0:
                return x,a
            x=x+2
            a=a+1
            if n%x==0:
                return x,a
            x=x+4
    return 'is prime',a

def TrialDivision_primes(n, primes):
    a=0
    for x in primes:
        if x<=(int(math.sqrt(n))):
            a=a+1
            if n%x==0:
                return x,a
        else:
            break
    return 'is prime',a


N = []
iter_norm = []
iter_odd = []
iter_6k1 = []
iter_prime = []
primes = [2,3]

for n in range (4,500001):
    p,a = TrialDivision(n)
    q,b = TrialDivision_odd(n)
    r,c = TrialDivision_6k1(n)
    s,d = TrialDivision_primes(n,primes)
    if not p==q==r==s:
        print 'ERROR'
    if not p == 'is prime':
        N.append(n)
        iter_norm.append(a)
        iter_odd.append(b)
        iter_6k1.append(c)
        iter_prime.append(d)
    else:
        primes.append(n)
  
plt.title('Trial Division Algorithm Results')
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(N, iter_norm, 'ro', label='Standard implementation')
plt.plot(N, iter_odd, 'bo', label='Improvement 2 (only odd)')
plt.plot(N, iter_6k1, 'go', label='Improvement 3 (only 6k+/-1)')

plt.plot(N, np.sqrt(N)-1, lw=5, c='red')
plt.plot(N, np.sqrt(N)/2.0+0.5, lw=5, c='blue')
plt.plot(N, np.sqrt(N)/3.0+5.0/3.0, lw=5, c='green')

B=1.08366

plt.plot(N, iter_prime, 'yo', label='Improvement 1 (only primes)')
plt.plot(N, np.sqrt(N)/(np.log(np.sqrt(N))-B), lw=5, c='yellow')

plt.plot([], [], lw=5, c='black', label='Corresponding Upper Bound')
plt.legend(loc=0, borderaxespad=0.)

plt.ylim(ymin=0)
plt.savefig('TDresult.png',bbox_inches='tight')
plt.show()
