#!/usr/bin/env python3
"""Exact unordered-multiset M3 Port-Euler fibers; unsigned auxiliary model."""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product

ports = [p for p in combinations(range(6), 2) if p not in {(0,1),(2,3),(4,5)}]
bit = {p:1<<i for i,p in enumerate(ports)}
E=[]
for i,j,k in product(range(2), repeat=3):
    a,b,c=(i,2+j),(i,4+k),(2+j,4+k)
    E.append((bit[a]^bit[b],bit[a]^bit[c],bit[b]^bit[c]))
assert all(a^b^c==0 for a,b,c in E)
F={0}
forced=[]
for triple in combinations(range(6),3):
    pairs=[p for p in combinations(triple,2) if p in bit]
    if len(pairs)==2: forced.append(bit[pairs[0]]^bit[pairs[1]])
for e in forced: F |= {x^e for x in tuple(F)}
assert len(forced)==12 and len(F)==512

def ab(m):
    r=m//2
    return ((r*(r+1)//2,(r+1)*(r+2)//2) if m%2
            else ((r+1)*(r+2)//2,r*(r+1)//2))

def formula(ms):
    prod=delta=1
    for m in ms:
        a,b=ab(m)
        prod*=a+3*b
        delta*=a-b
    assert (prod+3*delta)%4==0
    return (prod+3*delta)//4-(3 if sum(ms)%2==0 else 0)

def fiber(ms):
    dp={0:1}
    for m,es in zip(ms,E):
        a,b=ab(m)
        nxt=defaultdict(int)
        for x,n in dp.items():
            nxt[x]+=a*n
            for e in es: nxt[x^e]+=b*n
        dp=nxt
    disconnected=Counter()
    for typ in range(3):
        x=0
        for m,es in zip(ms,E):
            if m%2: x^=es[typ]
        disconnected[x]+=1
    q={x:dp.get(x,0)-disconnected[x] for x in F
       if dp.get(x,0)>disconnected[x]}
    assert sum(q.values())==formula(ms)
    return q

# Independent local multiset parity classification for all m=1..10.
for m in range(1,11):
    a,b=ab(m)
    for es in E:
        observed=Counter()
        for choice in combinations_with_replacement(range(3),m):
            x=0
            for typ in choice:x^=es[typ]
            observed[x]+=1
        assert observed==Counter({0:a, es[0]:b, es[1]:b, es[2]:b})

# R762KM complete 256-subset regression.
for ms in product((1,2),repeat=8):
    q=fiber(ms)
    k=ms.count(2)
    assert len(q)==(465 if k==0 else 495 if k==1 else 508 if k==2 else 512)
    assert sum(q.values())==(2**k*(3**8+3)//4-3 if k%2==0 else 2**k*(3**8-3)//4)

# Separate exact 12-bit Walsh transform for arbitrary multiplicity patterns.
def spectral(ms):
    A=[]
    for chi in range(4096):
        val=1
        for m,es in zip(ms,E):
            a,b=ab(m)
            s=sum(-1 if (chi&e).bit_count()%2 else 1 for e in es)
            val*=a+b*s
        A.append(val)
    for k in range(12):
        step=1<<k
        for p in range(0,4096,step*2):
            for j in range(step):
                x,y=A[p+j],A[p+j+step]
                A[p+j],A[p+j+step]=x+y,x-y
    assert all(v%4096==0 for v in A)
    return {x:v//4096 for x,v in enumerate(A) if v}

for ms in [(1,)*8,(2,)*8,(3,)*8,(1,2,3,4,1,2,3,4)]:
    raw=spectral(ms)
    disconnected=Counter()
    for j in range(3):
        x=0
        for m,es in zip(ms,E):
            if m%2:x^=es[j]
        disconnected[x]+=1
    expected={x:raw.get(x,0)-disconnected[x] for x in F
              if raw.get(x,0)>disconnected[x]}
    assert expected==fiber(ms)

for m in range(1,13):
    q=fiber((m,)*8)
    maxi=max(q.values())
    print(m,formula((m,)*8),len(q),maxi,(maxi-1).bit_length())
print('PASS: all 256 upgrades; local m<=10; exact Walsh inversion; uniform m<=12')
