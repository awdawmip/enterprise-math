#!/usr/bin/env python3
"""Regression for the BRC class-13 -> class-19 cancellation-debt theorem.

Finite computation is falsification only. The theorem is proved symbolically in
research_notes/brc_class13_cancellation_debt_transfer_20260924.md.
"""
from collections import Counter

BOUND = 5000

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0: return False
        d += 2
    return True

def primes_upto(n):
    return [p for p in range(2,n+1) if is_prime(p)]

TARGETS=[p for p in primes_upto(BOUND) if p%24 in (13,19)]
C13=[p for p in TARGETS if p%24==13]
C19=[p for p in TARGETS if p%24==19]

def vp(n,p):
    c=0
    while n and n%p==0:
        n//=p;c+=1
    return c

def factor(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d;e+=1
            out.append((d,e))
        d += 1 if d==2 else 2
    if n>1: out.append((n,1))
    return out

def order_mod(a,p):
    o=p-1
    for r,_ in factor(p-1):
        while o%r==0 and pow(a,o//r,p)==1:
            o//=r
    return o

def s13(p):
    o=order_mod(4,p)
    assert p%24==13 and o%2==0
    return o//2

def c13(p):
    s=s13(p)
    return vp(pow(4,s)+1,p)

def fv(n,p):
    z=0
    while n:
        n//=p; z+=n
    return z

def cancel_q(q,j):
    s=s13(q)
    return j%s==0 and (j//s)%2==1

def delta_single(p,j):
    h=(p-1)//2
    E=int(j%h==0)
    a=vp(j,p)
    if p%24==13:
        s=s13(p); c=c13(p)
        C=(j%s==0 and (j//s)%2==1)
        return E+a-((a+c) if C else 0)
    return E+a

def delta(p,m):
    return sum(mult*delta_single(p,j)+fv(mult,p) for j,mult in m.items())

def debt(q,r):
    sq=s13(q); hr=(r-1)//2
    return int(sq%hr==0)+vp(sq,r)

dirty_edges=[]
for q in C13:
    if q==13: continue
    for r in C19:
        if r>=q: break
        d=debt(q,r)
        if d:
            dirty_edges.append((q,r,d))

# Every q-cancellation singleton pays the edge debt, independently of the odd multiplier.
singleton_fail=[]
for q,r,d in dirty_edges:
    sq=s13(q); cq=c13(q)
    for u in range(1,200,2):
        j=sq*u
        if delta_single(q,j) != -cq:
            singleton_fail.append(("q",q,r,u,delta_single(q,j),-cq))
        if delta_single(r,j) < d:
            singleton_fail.append(("r",q,r,u,delta_single(r,j),d))
assert not singleton_fail, singleton_fail[:5]

# Exhaust deterministic multi-port clouds. Add arbitrary non-cancellation ports and
# multiplicities so factorial terms are exercised as well.
cloud_fail=[]
tested=0
for idx,(q,r,d) in enumerate(dirty_edges):
    sq=s13(q); cq=c13(q)
    for t in range(1,8):
        m=Counter()
        # t q-cancellation copies on distinct ports
        for k in range(t):
            u=2*k+1
            m[sq*u]+=1
        # extra arbitrary positive-channel ports
        m[q+idx+1] += (idx+t)%5
        m[r] += (idx+2*t)%4
        T=sum(mult for j,mult in m.items() if cancel_q(q,j))
        dq=delta(q,m); dr=delta(r,m)
        tested += 1
        if dq < -cq*T:
            cloud_fail.append(("qbound",q,r,t,dq,-cq*T,m))
        if dr < d*T:
            cloud_fail.append(("rbound",q,r,t,dr,d*T,m))
        if dq <= -1:
            need=(-dq + cq - 1)//cq
            if T < need or dr < d*need:
                cloud_fail.append(("combined",q,r,t,dq,dr,T,need,d,m))
assert not cloud_fail, cloud_fail[:5]

dirty_q=sorted({q for q,r,d in dirty_edges})
edge2=[e for e in dirty_edges if e[2]>=2]
assert (2053,19,2) in edge2
assert (3613,43,2) in edge2
assert (4789,19,2) in edge2

print({
    "target_primes_below_5000":len(TARGETS),
    "higher_class13_q":len([q for q in C13 if q>13]),
    "dirty_class13_q":len(dirty_q),
    "class19_debt_edges":len(dirty_edges),
    "max_edge_debt":max(d for q,r,d in dirty_edges),
    "double_debt_examples":edge2,
    "multiport_clouds_checked":tested,
    "failures":0,
})
