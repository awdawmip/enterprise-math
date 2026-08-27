#!/usr/bin/env python3
import math, json, sys

def A_recurrence(n: int) -> int:
    a=1
    if n==0: return a
    for k in range(n):
        num=a*6*(2*k+1)*(3*k+1)*(3*k+2)
        den=(k+1)**3
        assert num%den==0
        a=num//den
    return a

def blind_prefix_mod(N:int,L:int)->int:
    assert math.gcd(N,6)==1 and L>=1
    inv216=pow(216,-1,N)
    s=0
    a=1
    powinv=1
    for k in range(L):
        if k>0:
            j=k-1
            num=a*6*(2*j+1)*(3*j+1)*(3*j+2)
            den=(j+1)**3
            assert num%den==0
            a=num//den
            powinv=(powinv*inv216)%N
        s=(s+(6*k+1)*(a%N)*powinv)%N
    return s

def F_recurrence(L:int)->int:
    assert L>=1
    f=0
    a=1
    p216=216**(L-1)
    for k in range(L):
        if k>0:
            j=k-1
            num=a*6*(2*j+1)*(3*j+1)*(3*j+2)
            den=(j+1)**3
            assert num%den==0
            a=num//den
            p216//=216
        f += (6*k+1)*a*p216
    return f

def primes_upto(n):
    ps=[]
    for x in range(2,n+1):
        if all(x%p for p in ps if p*p<=x):
            ps.append(x)
    return ps

def check():
    Ns=[35,55,65,77,85,91,143,187,221,247,299,323]
    for N in Ns:
        for L in range(1,18):
            g=blind_prefix_mod(N,L)
            f=F_recurrence(L)
            assert math.gcd(g,N)==math.gcd(f,N), (N,L,g,f)
            assert g == (f*pow(pow(216,L-1,N),-1,N))%N

    ps=[p for p in primes_upto(499) if p>3]
    weak=[]
    for p in ps:
        sp=blind_prefix_mod(p,p)
        weak.append((p,sp))
        assert sp%p==0

    comp=[]
    small=[p for p in primes_upto(43) if p>3]
    for i,p in enumerate(small):
        for q in small[i+1:]:
            N=p*q
            sN=blind_prefix_mod(N,N)
            comp.append((p,q,sN))
            assert sN%N==0

    divpat=[]
    for L in range(1,101):
        f=F_recurrence(L)
        d=(3*L-2) if L%2 else (3*L-1)
        divpat.append((L,d,f%d))
        assert f%d==0

    print(f"PCF4_CHECK_A_PASS gcd_cases={len(Ns)*17} weak_primes={len(weak)} "
          f"composite_sync={len(comp)} d_pattern=100")

if __name__=="__main__":
    check()
