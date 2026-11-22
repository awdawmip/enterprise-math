#!/usr/bin/env python3
"""Independent cone-rational F_p phase checks for R5 primitive 29/32 masks.
Uses root-evaluation and a direct six-cone rational expansion, NOT the
original seven-subset joint dynamic programming. Finite-field zeros do
NOT by themselves prove characteristic-zero zeros.
"""
from itertools import permutations

PRIMES=(929,5569,8353)
ORDERS=(29,32)

def factor_primes(n):
    out=[]; k=2
    while k*k<=n:
        if n%k==0:
            out.append(k)
            while n%k==0:n//=k
        k+=1
    if n>1:out.append(n)
    return out

def primitive_root(p):
    fs=factor_primes(p-1)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//x,p)!=1 for x in fs))

def linear(vec,c,p):
    out=[0]*len(vec)
    out[0]=vec[0]
    for k in range(1,len(vec)):
        out[k]=(vec[k]+c*out[k-1])%p
    return out

def quadratic(vec,c,p):
    out=vec.copy()
    for k in range(2,len(vec)):
        out[k]=(out[k]+c*out[k-2])%p
    return out

def calc(p,d):
    M=4*d
    z=pow(primitive_root(p),(p-1)//d,p)
    assert pow(z,d,p)==1 and all(pow(z,d//f,p)!=1 for f in factor_primes(d))
    one=[1]+[0]*(M-1)
    Du=1
    for v in range(214,222):Du=Du*(1-pow(z,v,p))%p
    hu=linear(one,1,p)
    for v in (216,217,218):hu=linear(hu,pow(z,v,p),p)
    A=[0]*M
    for r in (219,220,221):
        beta=1
        for r2 in (219,220,221):
            if r2!=r:
                beta=beta*pow((1-pow(z,r2-r,p))%p,-1,p)%p
        for a,b,c in permutations((214,215,r)):
            d1=int(a>b); d2=int(b>c)
            pref=Du*beta*pow(1-pow(z,a,p),-1,p)%p
            pref=pref*pow(z,a*d1+(a+b)*d2,p)%p
            h=linear(hu,pow(z,a+b,p),p)
            h=quadratic(h,pow(z,214+215+r,p),p)
            for k in range(d2,M):
                A[k]=(A[k]+pref*h[k-d2])%p
    Cz=linear(one,1,p)
    Dz=1
    for v in range(296,313):
        Dz=Dz*(1-pow(z,v,p))%p
        Cz=linear(Cz,pow(z,v,p),p)
    C=[Dz*x%p for x in Cz]
    R=[(A[k]+C[k]-A[k]*C[k])%p for k in range(M)]
    return z,A,C,R

if __name__=="__main__":
    for p in PRIMES:
        for d in ORDERS:
            z,A,C,R=calc(p,d)
            zero=[m for m in range(1,4*d+1) if R[m-1]==0]
            expected=(list(range(54 if d==29 else 60,2*d+1))
                      +list(range((54 if d==29 else 60)+2*d,4*d+1)))
            assert zero==expected,(p,d,zero)
            assert A[:2*d]==A[2*d:] and C[:2*d]==C[2*d:] and R[:2*d]==R[2*d:],(p,d,"period")
            print("prime",p,"d",d,"root",z,"zero",zero,"nonzero",4*d-len(zero))
    print("PASS: 3 primes x 2 orders, exact finite-field cone-series masks and 2d phase duplication")
