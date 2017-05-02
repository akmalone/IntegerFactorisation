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

def astage(a,i):
    r=1
    p=1
    while p==1:
        a=ssq(n,a,r)
        p=gcd(a-1,n)
        r=r+1
        i=i+1
        if i==150:
            return 1,i
    return p,i
    

def Pollard(n):
    a=2
    i=0
    p,i=astage(a,i)
    if p==n:
        a=3 
        p,i=astage(a,i)
    if p==n:
        a=5 
        p,i=astage(a,i) 
    if p==n:
        a=7 
        p,i=astage(a,i) 
    if p==n:
        a=11 
        p,i=astage(a,i)
    if p==n:
        a=13 
        p,i=astage(a,i)
    if p==n:
        a=17 
        p,i=astage(a,i)
    if p==n:
        a=19 
        p,i=astage(a,i)
    return p,i,a

def prime_gen(n):
    primes = range (2,n)
    for x in primes:
        if x<math.sqrt(n):
            i = primes.index(x)
            for y in primes[i+1:]:
                if y % x ==0:
                    primes.remove(y)
    return primes

N2 = []
poll2 = []
N3 = []
poll3 = []
N5 = []
poll5 = []
N7 = []
poll7 = []
N11 = []
poll11 = []
N13 = []
poll13 = []
N17 = []
poll17 = []
N19 = []
poll19 = []
note = []
notepoll = []

primes = prime_gen(100001)

for n in range (3,100001,2):
    if not n in primes:
        p,a,hi = Pollard(n)
        if n==p or 1==p:
            note.append(n)
            notepoll.append(a)
        elif hi==2:
            N2.append(n)
            poll2.append(a)
        elif hi==3:
            N3.append(n)
            poll3.append(a)
        elif hi==5:
            N5.append(n)
            poll5.append(a)
        elif hi==7:
            N7.append(n)
            poll7.append(a)
        elif hi==11:
            N11.append(n)
            poll11.append(a)
        elif hi==13:
            N13.append(n)
            poll13.append(a)
        elif hi==17:
            N17.append(n)
            poll17.append(a)
        elif hi==19:
            N19.append(n)
            poll19.append(a)

print float(len(note))/float(len(note)+len(N2)+len(N3)+len(N5)+len(N7)+len(N11)+len(N13)+len(N17)+len(N19))
  
plt.title("Pollard's p-1 Method varying a")
plt.ylabel('Number of Iterations')
plt.xlabel('Value of N')
plt.plot(N2, poll2, 'bp', label='Found when a=2')
plt.plot(N3, poll3, 'gp', label='Found when a=3')
plt.plot(N5, poll5, 'mp', label='Found when a=5')
plt.plot(N7, poll7, 'p', c='yellow', label='Found when a=7')
plt.plot(N11, poll11, 'wp', label='Found when a=11')
plt.plot(N13, poll13, 'cp', label='Found when a=13')
plt.plot(N17, poll17, 'p', c='orange', label='Found when a=17')
plt.plot(N19, poll19, 'kp', label='Found when a=19')

plt.legend(loc=2)
plt.savefig('p235791.png',bbox_inches='tight')
plt.show()
