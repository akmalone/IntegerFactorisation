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

def factor_base(n,primes):
    FB=[2]
    for p in primes[1:]:
        if n%p==0:
            return p
        elif ssq(p,n%p,(p-1)/2)==1:
            FB.append(p)
    R=[]
    for p in FB:
        r=n%p
        if p%4==3:
            R.append(int(ssq(p,r,(p+1)/4)))
        elif p%8==5:
            if ssq(p,r,(p-1)/4)==1:
                R.append(int(ssq(p,r,(p+3)/8)))
            elif ssq(p,r,(p-1)/4)-p==-1:
                R.append(int(ssq(p,4*n,(p+3)/8)*(p+1)/2)%p)
            else:
                R.append(int(ssq(p,r,(p-1)/4)))
        else:
            for i in range(p):
                if i*i%p==r:
                    R.append(i)
                    break
    return FB,R

def SieveIt(i,FB,Q,ti,r,matrix):
    j=ti.index(r)
    while j<len(Q):
        matrix[j][i]=matrix[j][i]+1
        Q[j]=Q[j]/FB[i]
        j=j+FB[i]
    return matrix,Q

def sieve(n,R,t,Q,FB):
    matrix=np.zeros((len(t),len(FB)))
    Qi=list(Q)
    ti = np.asarray(t)%2
    ti = ti.tolist()
    if R[0] in ti:
        matrix,Qi=SieveIt(0,FB,Qi,ti,R[0],matrix)
    while len(Qi)-np.count_nonzero(np.asarray(Qi)%2)>0:
        J=np.where(np.asarray(Qi)%FB[0]==0)
        J=list(J[0])
        for j in J:
            matrix[j][0]=matrix[j][0]+1
            Qi[j]=Qi[j]/2
    for i in range(1,len(R)):
        ti = np.asarray(t)%FB[i]
        ti = ti.tolist()
        if R[i] in ti:
            matrix,Qi=SieveIt(i,FB,Qi,ti,R[i],matrix)
        if FB[i]-R[i] in ti:
            matrix,Qi=SieveIt(i,FB,Qi,ti,FB[i]-R[i],matrix)
        while len(Qi)-np.count_nonzero(np.asarray(Qi)%FB[i])>0:
            J=np.where(np.asarray(Qi)%FB[i]==0)
            J=list(J[0])
            for j in J:
                matrix[j][i]=matrix[j][i]+1
                Qi[j]=Qi[j]/FB[i]
    W=np.where(np.asarray(Qi)==1)
    W=list(W[0])
    mym=np.empty([len(W),len(FB)])
    Qq=[]
    tT=[]
    for w in range(len(W)):
        mym[w]=matrix[W[w]]%2
        Qq.append(Q[W[w]])
        tT.append(t[W[w]])
    return mym,Qq,tT

def Qx(n,A):
    t=[]
    Q=[]
    s=int(math.ceil(math.sqrt(n)))
    for x in range(s,s+A):
        t.append(x)
        Q.append(x*x-n)
    return Q,t


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
    
def QS(n,A,primesB):
    B=A
    TD=TrialDivision(n,primesB)
    if not TD==None:
        return 0,TD,n/TD
    FB,R=factor_base(n,primesB)
    if math.sqrt(n)==int(math.sqrt(n)):
        return 0,int(math.sqrt(n)),int(math.sqrt(n))
    Q,t=Qx(n,A)
    mym,Q,t=sieve(n,R,t,Q,FB)
    while not mym.size:
        A=A+B
        if A>=B*25:
            break
        Q,t=Qx(n,A)
        mym,Q,t=sieve(n,R,t,Q,FB)
    while mym.size:
        h,I=GE2(mym)
        if I.size and h.size:
            row=I[h[0]]
            y=prod(row,Q)
            x=prod(row,t)
            if not math.sqrt(y)==x%n:
                p=gcd(x+math.sqrt(y),n)
                q=gcd(x-math.sqrt(y),n)
                if not p==1:
                    if not q==1:
                        if p*q==n:
                            return A,p,q
            Q=np.delete(Q,h[0])
            t=np.delete(t,h[0])
            mym=np.delete(mym,h[0],axis=0)
        else:
            A=A+B
            if A>=B*25:
                break
            Q,t=Qx(n,A)
            mym,Q,t=sieve(n,R,t,Q,FB)
N=[]
N10 = []
A10 = []
note10=[]
N25 = []
A25 = []
note25=[]
N250 = []
A250 = []
note250=[]

primes250=prime_gen(250)
primes25=primes250[:bisect.bisect_left(primes250,25)]
primes10=primes25[:bisect.bisect_left(primes25,10)]

print primes250
print primes25
print primes10

while len(N)<500:
    n=random.randint(1,5000000)
    if TrialDivision(n,primes10)==None:
        if not n in N:
            print len(N)
            N.append(n)
            ans10=QS(n,10,primes10)
            ans25=QS(n,25,primes25)
            ans250=QS(n,250,primes250)
            if not ans10==None:
                A,p,q=ans10
                N10.append(n)
                A10.append(A)
            else:
                note10.append(n)
            if not ans25==None:
                A,p,q=ans25
                N25.append(n)
                A25.append(A)
            else:
                note25.append(n)
            if not ans250==None:
                A,p,q=ans250
                N250.append(n)
                A250.append(A)
            else:
                    note250.append(n)

print float(len(note10))/float(len(N))
print float(len(note25))/float(len(N))
print float(len(note250))/float(len(N))

plt.subplot(1, 3, 1)
plt.ylabel('Value of A')
plt.xticks(rotation=60)
plt.plot(N10, A10, 'b|')
plt.plot(note10, np.asarray(note10)*0, 'g|')
plt.title('B=10')

plt.subplot(1, 3, 2)
plt.xlabel('Value of N')
plt.xticks(rotation=60)
plt.plot(N25, A25, 'b|')
plt.plot(note25, np.asarray(note25)*0, 'g|')
plt.title('B=25')

plt.subplot(1, 3, 3)
plt.xticks(rotation=60)
plt.plot(N250, A250, 'b|')
plt.plot(note250, np.asarray(note250)*0, 'g|')
plt.title('B=250')

plt.tight_layout()
plt.savefig('QSresult.png')
plt.show()












