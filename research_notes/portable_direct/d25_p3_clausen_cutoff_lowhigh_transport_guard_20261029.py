#!/usr/bin/env python3
"""Exact p^3 original Clausen low/high provenance and weighted observer.

Computes original beta and gamma recurrences independently. External arithmetic:
NOT the pending native H0/B0 divided-power benchmark.
"""
from d25_legendre_p3_frobenius_fullcompanion_guard_20261029 import primes_below

def direct_ledger(p):
    M=p**3
    h1=next(i for i in range(p) if (8*i+1)%p==0)
    h3=next(i for i in range(p) if (8*i+3)%p==0)
    b=max(h1,h3)
    t=[1]
    for n in range(p-1):
        t.append(t[-1]*(8*n+1)*(8*n+3)*pow(576*(n+1)**2,-1,M)%M)
    K=t[:b+1]; T=t[b+1:]
    assert all(v%(p*p)==0 for v in T)
    low=high=0
    for i,a in enumerate(K):
        for j0,bt in enumerate(T):
            n=i+b+1+j0
            v=2*(8*n+1)*a*bt
            if n<p: low=(low+v)%M
            else: high=(high+v)%M
    kd=sum(i*v for i,v in enumerate(K))%M
    td=sum((j+b+1)*v for j,v in enumerate(T))%M
    kval=sum(K)%M; tval=sum(T)%M
    Uold=kval*(kval+16*kd)%M
    Ufull=(kval+tval)*(kval+tval+16*(kd+td))%M
    assert (low+high)%M==(Ufull-Uold)%M
    oldH=0
    for i,a in enumerate(K):
        for j,c in enumerate(K):
            n=i+j
            if n>=p: oldH=(oldH+(8*n+1)*a*c)%M
    fullH=0
    for i,a in enumerate(t):
        for j,c in enumerate(t):
            n=i+j
            if n>=p: fullH=(fullH+(8*n+1)*a*c)%M
    assert (fullH-oldH)%M==high
    # Independent hypergeometric 3F2 first-p term, never from a square.
    gamma=1; Bdirect=0
    for n in range(p):
        Bdirect=(Bdirect+(8*n+1)*gamma)%M
        if n<p-1:
            gamma=gamma*(4*n+1)*(2*n+1)*(4*n+3)*pow(288*(n+1)**3,-1,M)%M
    assert (Uold-oldH+low)%M==Bdirect, (p,'old',Uold,oldH,low,Bdirect)
    assert (Ufull-fullH)%M==Bdirect, (p,'full',Ufull,fullH,Bdirect)
    return dict(p=p,b=b,low=low,high=high,oldH=oldH,fullH=fullH,
                Uold=Uold,Ufull=Ufull,Bdirect=Bdirect,
                delta=(Ufull-Uold)%M)

samples=[p for p in primes_below(200) if p>=11 and p%8 in (5,7)]+[229,373]
for p in samples:
    a=direct_ledger(p)
    assert a['low']%(p*p)==0 and a['high']%(p*p)==0
    if p in (13,23,37,373):
        print('CLAUSEN_LOW_HIGH_CERT',a,'low_p2',a['low']//(p*p),'high_p2',a['high']//(p*p))
a=direct_ledger(373)
assert (a['low'],a['high'],a['Uold'],a['oldH'],a['Ufull'],a['fullH'],a['Bdirect']) == (
    16556351,15443319,49669053,14329914,29773606,29773233,373)
print('PASS_CLAUSEN_CUTOFF_LOW_HIGH_TRANSFER',len(samples),'primes')
