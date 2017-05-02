import math
import numpy as np
import matplotlib.pyplot as plt
import random
import bisect
from decimal import *

def prime_gen(n):
    primes = range (2,n)
    for x in primes:
        if x<math.sqrt(n):
            i = primes.index(x)
            for y in primes[i+1:]:
                if y % x ==0:
                    primes.remove(y)
    return primes

def TrialDivision(n, primes):
    for x in primes:
        if n%x==0:
            return x

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

def CF(n,k):
    q=[int(math.sqrt(n))]
    A=[q[0]]
    P=[0,q[0]]
    Q=[1,n-math.pow(q[0],2)]
    n=math.sqrt(n)-q[0]
    n=1/float(n)
    q.append(int(n))
    A.append(q[1]*A[0]+1)
    for x in range(2,k):
        P.append(q[x-1]*Q[x-1]-P[x-1])
        Q.append(Q[x-2]+(P[x-1]-P[x])*q[x-1])
        q.append(int((q[0]+P[x])/Q[x]))
        A.append(q[x]*A[x-1]+A[x-2])
    return q,A,Q

def factor_base(n,primes):
    FB=[-1,2]
    for p in primes[1:]:
        if n%p==0:
            return p
        elif ssq(p,n%p,(p-1)/2)==1:
            FB.append(p)
    return FB

def factorise(Q,FB):
    factors=[]
    if Q==1:
        return 1,0
    for f in FB:
        while Q%f==0:
            factors.append(f)
            Q=Q/f
        if Q==1:
            break
    return factors, Q

def iQA(n,k,FB):
    qi,Ai,Qi=CF(n,k)
    Q=[]
    A=[]
    I=[]
    for i in range(k):
        f,e=factorise(Qi[i],FB[1:])
        if e==1:
            I.append(i)
            Q.append(Qi[i])
            A.append(Ai[i-1]%n)
    return I,Q,A

def getmat(i,Q,FB):
    matrix=np.zeros((len(i),len(FB)))
    for y in range(len(i)):
        f,_=factorise(Q[y],FB[1:])
        if i[y]%2==1:
            matrix[y][0]=1
        for x in range(1,len(FB)):
            matrix[y][x]=f.count(FB[x])%2
    return matrix

def GE2(mym):
    rows=[]
    x,y=mym.shape
    a=np.copy(mym)
    I=np.identity(x)
    for j in range(y):
        loc=np.where(a[:,j])
        loc=np.setdiff1d(loc,rows)
        if loc.size:
            row=loc[0]
            rows=np.append(rows,row)
            for i in range(1,len(loc)):
                a[loc[i]] = (a[loc[i]]+a[loc[0]])%2
                I[loc[i]]=(I[loc[i]]+I[loc[0]])%2
        hi=np.where(~a.any(axis=1))[0]
    return hi,I

def prod(a,b):
    c=1
    r=np.multiply(a,b)
    rel = r[np.nonzero(r)]
    for i in range (len(rel)):
        c = c*rel[i]
    return c
    
def CFRAC(n,k,primesB):
    if math.sqrt(n)==int(math.sqrt(n)):
        return 0,int(math.sqrt(n)),int(math.sqrt(n))
    FB=factor_base(n,primesB)
    if not type(FB) is list:
        return 0,FB,n/FB
    i,Q,A=iQA(n,k,FB)
    while not i:
            k=k+10
            if k>=250:
                break
            i,Q,A=iQA(n,k,FB)
    mym= getmat(i,Q,FB)
    while mym.size:
        h,I=GE2(mym)
        if I.size and h.size:
            row=I[h[0]]
            y=prod(row,Q)
            x=prod(row,A)
            if not math.sqrt(y)==x%n:
                p=gcd(x+math.sqrt(y),n)
                q=gcd(x-math.sqrt(y),n)
                if not p==1:
                    if not q==1:
                        if p*q==n:
                            return k,p,q
            Q=np.delete(Q,h[0])
            A=np.delete(A,h[0])
            mym=np.delete(mym,h[0],axis=0)
        else:
            k=k+10
            if k>=250:
                break
            i,Q,A=iQA(n,k,FB)
            mym= getmat(i,Q,FB)
        
N=[]
N10 = []
K10 = []
note10=[]
N25 = []
K25 = []
note25=[]
N250 = []
K250 = []
note250=[]

primes250=prime_gen(250)
primes25=primes250[:bisect.bisect_left(primes250,25)]
primes10=primes25[:bisect.bisect_left(primes25,10)]

while len(N)<1000:
    n=random.randint(1,5000000)
    if TrialDivision(n,primes10)==None:
        if not n in N:
            N.append(n)
            ans10=CFRAC(n,10,primes10)
            ans25=CFRAC(n,10,primes25)
            ans250=CFRAC(n,10,primes250)
            if not ans10==None:
                k,p,q=ans10
                N10.append(n)
                K10.append(k)
            else:
                note10.append(n)
            if not ans25==None:
                k,p,q=ans25
                N25.append(n)
                K25.append(k)
            else:
                note25.append(n)
            if not ans250==None:
                k,p,q=ans250
                N250.append(n)
                K250.append(k)
            else:
                note250.append(n)

print float(len(note10))/float(len(N))
print float(len(note25))/float(len(N))
print float(len(note250))/float(len(N))

plt.subplot(1, 3, 1)
plt.ylabel('Value of k')
plt.xticks(rotation=60)
plt.plot(N10, K10, 'r|')
plt.plot(note10, np.asarray(note10)*0, 'k|')
plt.title('B=10')

plt.subplot(1, 3, 2)
plt.xlabel('Value of N')
plt.xticks(rotation=60)
plt.plot(N25, K25, 'r|')
plt.plot(note25, np.asarray(note25)*0, 'k|')
plt.title('B=25')
plt.yticks(visible=False)

plt.subplot(1, 3, 3)
plt.xticks(rotation=60)
plt.plot(N250, K250, 'r|')
plt.plot(note250, np.asarray(note250)*0, 'k|')
plt.title('B=250')
plt.yticks(visible=False)
plt.ylim(0,250)

plt.tight_layout()
plt.savefig('CFRACresult.png')
plt.show()
