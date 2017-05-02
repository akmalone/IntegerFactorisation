import math
import numpy as np
import matplotlib.pyplot as plt

def ssq(p,x,n):
    b = bin(n)
    b = b[2:]
    b = [int(d) for d in str(b)]
    e = []
    for t in range(len(b)):
        e.insert(0,x)
        x = x*x % p
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
Np = []
pollp = []
N2 = []
poll2 = []
note = []
primes = prime_gen(501)

for n in range (2,501):
    p,a = Pollard(n)
    if n==p:
        note.append(n)
    if n in primes:
        Np.append(n)
        pollp.append(a)
    elif p==2 or n/p==2:
        N2.append(n)
        poll2.append(a)
    else:
        N.append(n)
        p1.append(p)
        poll.append(a)

print list(set(note)-set(primes))
print list(set(primes)-set(note))
  
plt.title("Pollard's p-1 Method for all Integers")
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')

plt.plot(Np, pollp, 'kp', label = 'Prime Numbers')
plt.plot(N2, poll2, 'cp', label = 'Even Numbers')
plt.plot(N, poll, 'mp', label = 'Composite Numbers')

plt.legend(loc=0, borderaxespad=0.)
plt.savefig('p-1a.png',bbox_inches='tight')
plt.show()
