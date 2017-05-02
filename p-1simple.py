import math
import numpy as np
from decimal import *
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

def Pollard(n):
    a=2
    r=1
    p=1
    i=0
    while p==1:
        a=ssq(n,a,r)
        p=gcd(a-1,n)
        r=r+1
        i=i+1
    return p, i

def prime_gen(n):
    primes = range (2,n)
    for x in primes:
        if x<math.sqrt(n):
            i = primes.index(x)
            for y in primes[i+1:]:
                if y % x ==0:
                    primes.remove(y)
    return primes

N = []
p1 = []
poll = []
note = []
primes = prime_gen(250001)

print primes

for n in range (3,250001,2):
    if not n in primes:
        p,a= Pollard(n)
        N.append(n)
        p1.append(p)
        poll.append(a)
        if n==p:
            note.append(n)

print note
  
plt.title("Pollard's p-1 Method without Even or Prime Numbers")
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(N, poll, 'mp')

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig('ppppp2.png')
plt.show()
