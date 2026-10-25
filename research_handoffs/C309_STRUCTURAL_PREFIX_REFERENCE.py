#!/usr/bin/env python3
"""C309: exact Z[t] structural content and Newton-prefix certificates.
Standalone author-level arithmetic kernel. No native BRC/X6 transfer."""
from math import gcd, comb, factorial
from random import Random

def content(a):
    g=0
    for v in a:g=gcd(g,v)
    return g

def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def poly_add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]

def at(a,t):
    y=0
    for v in reversed(a):y=y*t+v
    return y

def H(n,s):
    h=1
    while (v:=gcd(n,s))>1:
        n//=v;h*=v
    return h

def prefix_moduli(s,K):
    hh=[H(factorial(j),s) for j in range(K+1)]
    return [s*hh[j]*hh[K-j] for j in range(K+1)]

def prefix_gcd(s,residues):
    K=len(residues)-1
    if s==1:return 1
    g=s
    for k in range(K+1):
        h=H(factorial(k),s)
        D=sum((-1)**(k-j)*comb(k,j)*residues[j]
              for j in range(k+1))%(s*h)
        assert D%h==0
        b=factorial(k)//h
        B=(D//h)*pow(b,-1,s)%s
        g=gcd(g,B)
    return g

def falling(T,k):
    q=[1]
    for j in range(k):q=poly_mul(q,[-T-j,1])
    return q

def newton_coeff(a,T):
    row=[at(a,T+j) for j in range(len(a))]
    ans=[]
    for k in range(len(a)):
        assert row[0]%factorial(k)==0
        ans.append(row[0]//factorial(k))
        row=[row[j+1]-row[j] for j in range(len(row)-1)]
    return ans

def test(cases=2200,seed=30920261026):
    rng=Random(seed)
    prefixes=witnesses=0
    for z in range(cases):
        d=z%12
        s=[1,2,4,6,8,10,12,18,25,27,64,121,250][(z//12)%13]
        T=rng.randint(-9,9)
        P=[rng.randint(-200,200) for _ in range(d+1)]
        if z%23==0:P=[0]*(d+1)
        C=[rng.randint(-5,5),rng.choice([-5,-3,-1,1,3,5])]
        while content(C)!=1:C[0]+=1
        A=poly_mul(C,P)
        U=[rng.randint(-100,100) for _ in range(d+3)]
        L=gcd(s,content(poly_add(A,U)),content(U))
        G=gcd(s,content(P))
        assert G%L==0
        Bs=newton_coeff(P,T)
        for K in range(d+1):
            N=prefix_moduli(s,K)
            r=[at(P,T+j)%N[j] for j in range(K+1)]
            g=prefix_gcd(s,r)
            assert g==gcd(s,*Bs[:K+1]) and g%L==0
            if g==L:assert G==L
            if K<d and g>L:
                Q0=[0]*(d+1)
                for k in range(K+1):
                    Q0=poly_add(Q0,poly_mul([Bs[k]],falling(T,k)))
                Q1=poly_add(Q0,poly_mul([L],falling(T,K+1)))
                assert all(at(Q0,T+j)==at(Q1,T+j)
                           for j in range(K+1))
                assert gcd(s,content(Q0))==g
                assert gcd(s,content(Q1))==L
                witnesses+=1
            prefixes+=1
    assert content([2,-1,1])==1
    assert all((t*(t-1)+2)%2==0 for t in range(-40,41))
    return {'polynomials':cases,'prefixes':prefixes,
            'sharpness_witnesses':witnesses,'status':'PASS'}

if __name__=='__main__':
    print('C309_EXACT_PASS',test())
