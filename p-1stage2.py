import math
import numpy as np
from decimal import *
import bisect
import matplotlib.pyplot as plt

def ssq(p,x,n):
    b = bin(n)
    b = b[2:]
    b = [int(d) for d in str(b)]
    e = []
    for t in range(len(b)):
        e.insert(0,x)
        x = Decimal(x)*Decimal(x) % p
    r = np.multiply(b,e)
    rel = r[np.nonzero(r)]
    ss = 1
    for i in range (len(rel)):
        ss = ss*rel[i] % p
    return ss

def gcd(a,b):
    while not (b==0):
        a = a % b
        if (a == 0):
            break
        b = b % a
    return max(a,b)

def astage(a,i,inter,B):
    r=1
    p=1
    while p==1 and r < B:
        a=ssq(n,a,r)
        p=gcd(a-1,n)
        r=r+1
        i=i+1
    if r==B:
        A=a
        for v in range(len(inter)):
            q=inter[v]
            a=ssq(n,A,q)
            p=gcd(a-1,n)
            i=i+1
            if not p==1:
                return p,i
    return p,i
    

def Pollard(n,inter,B):
    i=0
    p,i=astage(2,i,inter,B)
    return p,i

def prime_gen(n):
    primes = range (2,n)
    for x in primes:
        if x<math.sqrt(n):
            i = primes.index(x)
            for y in primes[i+1:]:
                if y % x ==0:
                    primes.remove(y)
    return primes

N20 = []
poll20 = []
N50 = []
poll50 = []
note20 = []
notepoll20 = []
note50 = []
notepoll50 = []

primes = prime_gen(100001)

interval_primes20=primes[bisect.bisect(primes,20):bisect.bisect(primes,150)]
interval_primes50=primes[bisect.bisect(primes,50):bisect.bisect(primes,150)]
 
print interval_primes20

for n in range (3,100001,2):
    if not n in primes:
        p,a = Pollard(n,interval_primes20,20)
        if n==p:
            note20.append(n)
            notepoll20.append(a)
        else:
            N20.append(n)
            poll20.append(a)
        p,a = Pollard(n,interval_primes50,50)
        if n==p:
            note50.append(n)
            notepoll50.append(a)
        else:
            N50.append(n)
            poll50.append(a)

print list(set(note20)-set(note50))
print list(set(note50)-set(note20))

print max(poll20)
print max(poll50)

plt.subplot(1, 2, 1)
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(N50, poll50, 'mp')
plt.xticks(rotation=30)

plt.subplot(1, 2, 2)
plt.xlabel('Value of N')
plt.plot(N20, poll20, 'mp')
plt.xticks(rotation=30)
plt.ylim(0,70)

plt.suptitle("Pollard's p-1 Method Second Stage")
plt.savefig('p2ndnoa7.png')
plt.show()
