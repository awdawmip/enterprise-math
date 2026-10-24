#!/usr/bin/env python3
"""Author-side exact rational tests, NOT the native Source benchmark."""
from fractions import Fraction as F
from math import comb, factorial

def v_p(n,p):
    if n==0:return 10**9
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v

def mod_q(x,p,k):
    x=F(x);a,b=x.numerator,x.denominator
    va,vb=v_p(a,p),v_p(b,p)
    assert va>=vb,(p,x)
    a//=p**va;b//=p**vb;mod=p**k
    return pow(p,va-vb,mod)*(a%mod)*pow(b,-1,mod)%mod

def isprime(n):
    return n>1 and all(n%d for d in range(2,int(n**0.5)+1))

def original_jet(p):
    m=(p-1)//6
    A=F(factorial(6*m),3**(6*m)*factorial(2*m)**3)
    B=comb(4*m,2*m)
    b=(3**(p-1)-1)//p
    q2=(2**(p-1)-1)//p
    R,S=F(1),F(0);D,E=F(0),F(0);low=[];high=[]
    for n in range(4*m+1):
        if n<=m:
            C=F((-1)**n*comb(m,n),2**n)
        else:
            C=F((-1)**m*factorial(m)*factorial(n-m-1),
                2**(n+1)*3**int(n>2*m)*factorial(n))
        (low if n<=m else high).append((n,C,D,E))
        S+=A*(6*n+2*p-1)*R
        if n<4*m:
            R*=F((4*m+2*n+1)*(3*n+1)*(3*n+2),
                 36*(n+1)*(2*m+n+1)*(4*m+n+1))
            if n!=m:
                D+=F(1,2*(n-m));E+=F(1,4*(n-m)**2)
            if n!=2*m:
                D-=F(2,3*(n-2*m));E-=F(8,9*(n-2*m)**2)
            D-=F(1,3*n+2);E-=F(1,(3*n+2)**2)
    J0=(F(1,2**m)+sum((6*n-1)*C*D for n,C,D,E in low)
        +sum((6*n-1)*C for n,C,D,E in high))
    J1=(sum(C*(2*D+F(6*n-1,2)*(D*D-E)) for n,C,D,E in low)
        +sum(C*(2+(6*n-1)*D) for n,C,D,E in high))
    P=F(1,3**(p-1))
    for j in range(1,2*m+1):P*=1-F(p,j)
    assert A/B==P
    assert mod_q(A/B-(1+F(p*b,2)),p,2)==0
    assert mod_q(A*(J0+p*J1)-B*(J0+p*(J1+F(b,2)*J0)),p,2)==0
    assert mod_q(S-p*A*(J0+p*J1),p,3)==0
    # The following are finite regressions, NOT universal results.
    assert mod_q(B*J0-1,p,1)==0
    assert mod_q(B*(J0+p*(J1+F(b,2)*J0))-(1+p*(2*q2-b)),p,2)==0
    assert mod_q(S-p*F(4,3)**(p-1),p,3)==0
    return p,m,mod_q(S/p,p,2)

if __name__=="__main__":
    for m in range(1,12):
        p=6*m+1
        A=F(factorial(6*m),3**(6*m)*factorial(2*m)**3)
        B=comb(4*m,2*m);P=F(1,3**(p-1))
        for j in range(1,2*m+1):P*=1-F(p,j)
        assert A/B==P
    rows=[original_jet(p) for p in range(7,242,6) if isprime(p)]
    assert len(rows)==25,len(rows)
    print("PASS: exact A/B product for m=1..11 including composite p")
    print("PASS: full original two-jet and binomial bridge for 25 primes <=241")
    for p,m,d in rows:
        if p in (7,13,19,31,37,211):print(p,m,d)
