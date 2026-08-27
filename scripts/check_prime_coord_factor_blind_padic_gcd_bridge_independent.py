#!/usr/bin/env python3
import math

def A_direct(n:int)->int:
    return math.comb(2*n,n)**2 * math.comb(3*n,n)

def prefix_direct_mod(N:int,L:int)->int:
    assert math.gcd(N,6)==1 and L>=1
    inv216=pow(216,-1,N)
    s=0
    z=1
    for k in range(L):
        if k:
            z=(z*inv216)%N
        s=(s+(6*k+1)*(A_direct(k)%N)*z)%N
    return s

def F_direct(L:int)->int:
    return sum((6*k+1)*A_direct(k)*216**(L-1-k) for k in range(L))

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        ok=True
        for d in range(2,int(math.isqrt(x))+1):
            if x%d==0:
                ok=False;break
        if ok: out.append(x)
    return out

def check():
    Ns=[35,55,77,91,143,187,221,323]
    for N in Ns:
        for L in range(1,15):
            g=prefix_direct_mod(N,L)
            f=F_direct(L)
            assert math.gcd(g,N)==math.gcd(f,N)
    weak=0
    for p in primes_upto(257):
        if p<=3: continue
        assert prefix_direct_mod(p,p)==0
        weak+=1
    sync=0
    ps=[p for p in primes_upto(31) if p>3]
    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            N=p*q
            assert prefix_direct_mod(N,N)==0
            sync+=1
    print(f"PCF4_CHECK_B_PASS gcd_cases={len(Ns)*14} weak_primes={weak} composite_sync={sync}")

if __name__=="__main__":
    check()
