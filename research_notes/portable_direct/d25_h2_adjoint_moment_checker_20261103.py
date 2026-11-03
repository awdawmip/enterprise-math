#!/usr/bin/env python3
"""D25 high-band adjoint: exact Fraction and mod-p regression, no native experiment."""
from fractions import Fraction as Q
from math import comb

def primes(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for k in range(2,int(n**.5)+1):
        if a[k]:a[k*k::k]=b'\0'*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def L(P):
    shifted=[Q(0)]*len(P)
    for i,a in enumerate(P):
        for j in range(i+1):shifted[j]+=a*comb(i,j)
    n=[x/9 for x in mul(mul([Q(1),Q(1)],[Q(5),Q(6)]),[Q(7),Q(6)])]
    a=mul(n,shifted);b=mul([Q(1),Q(6),Q(12),Q(8)],P)
    return [x-y for x,y in zip(a,b)]

def normal(W):
    W=list(map(Q,W));P=[Q(0)]*max(len(W)-3,1);R=W[:]
    for d in range(len(W)-1,2,-1):
        c=-R[d]/4;P[d-3]+=c
        a=L([Q(0)]*(d-3)+[c])
        for i,x in enumerate(a):R[i]-=x
    assert all(x==0 for x in R[3:])
    return P,R[:3]

def value(poly,s,p):
    return sum(a.numerator*pow(a.denominator,-1,p)*pow(s,j,p) for j,a in enumerate(poly))%p

def facunit(n,p):
    a=1
    for i in range(1,n+1):
        while i%p==0:i//=p
        a=a*i%p
    return a

def main():
    assert L([Q(1)])==[Q(26,9),Q(53,9),Q(0),Q(-4)]
    weights=[[0]*d+[1] for d in range(3,11)]+[[7,-3,13,1,2]]
    for W in weights:
        P,R=normal(W);a=L(P)
        assert all(a[i]+(R[i] if i<len(R) else 0)==W[i] for i in range(len(W)))
    ps=primes(2000);count=0;examples=[]
    for p in ps:
        r=(p-1)//6;T=[1]
        for s in range(r):
            q=(s+1)*(6*s+5)*(6*s+7)*pow(9*(2*s+3)**3,-1,p)%p
            T.append(T[-1]*q%p)
        assert T[r]==0;count+=r
        M=[sum(pow(s,j,p)*T[s] for s in range(r))%p for j in range(5)]
        assert (36*M[3]-53*M[1]-26*M[0]-9)%p==0
        assert (36*M[4]-36*M[3]-161*M[2]-133*M[1]-35*M[0])%p==0
        for W in weights:
            P,R=normal(W)
            lhs=sum(value(W,s,p)*T[s] for s in range(r))%p
            rhs=(sum(value(R,s,p)*T[s] for s in range(r))-value(P,0,p))%p
            assert lhs==rhs
        if p in (7,13,19,37,373,1999):
            chi=1 if pow(6,(p-1)//2,p)==1 else -1
            high=[]
            for s in range(r):
                k=(p+1)//2+s
                a=facunit(2*k,p)*facunit(3*k,p)%p
                b=pow(facunit(k,p),5,p)*pow(216,k,p)%p
                high.append(a*pow(b,-1,p)%p)
            assert high==[chi*pow(9,-1,p)*t%p for t in T[:r]]
            signed=sum((6*((p+1)//2+s)+1)*x for s,x in enumerate(high))%p
            assert signed==chi*pow(9,-1,p)*(6*M[1]+4*M[0])%p
            examples.append((p,r,M[:4],signed))
    print("PASS",len(ps),"primes;",count,"coefficients; 9 weights; 6 original factorial checks")
    print(examples)

if __name__=="__main__":main()
