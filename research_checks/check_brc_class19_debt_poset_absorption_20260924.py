#!/usr/bin/env python3
"""Regression for class-19 debt monotonicity on the class-13 step poset."""
BOUND=5000

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

PR=[p for p in range(2,BOUND+1) if is_prime(p)]
TARGET=[p for p in PR if p%24 in (13,19)]
C13=[p for p in TARGET if p%24==13 and p>13]
C19=[p for p in TARGET if p%24==19]

def vp(n,p):
    z=0
    while n and n%p==0:
        n//=p;z+=1
    return z

def factor(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            while n%d==0:n//=d
            out.append(d)
        d += 1 if d==2 else 2
    if n>1:out.append(n)
    return out

def order4(p):
    o=p-1
    for r in factor(p-1):
        while o%r==0 and pow(4,o//r,p)==1:o//=r
    return o

def step(p):
    o=order4(p)
    assert o%2==0
    return o//2

def debt_at_step(s,r):
    h=(r-1)//2
    return int(s%h==0)+vp(s,r)

def debt_vec(q):
    s=step(q)
    return {r:debt_at_step(s,r) for r in C19 if r<q and debt_at_step(s,r)>0}

nested=[]
fail=[]
for q in C13:
    s=step(q); dq=debt_vec(q)
    for Q in C13:
        if Q<=q:continue
        S=step(Q)
        if S%s:continue
        nested.append((q,Q))
        dQ=debt_vec(Q)
        for r,d in dq.items():
            if dQ.get(r,0)<d:
                fail.append(("monotonic",q,Q,r,d,dQ.get(r,0)))
        if dq and not dQ:
            fail.append(("dirty_not_upward",q,Q))

assert not fail, fail[:5]

# Horizon-by-horizon clean steps form a divisor down-set among realized class-13 steps.
ideal_fail=[]
for p in C13:
    earlier=[q for q in C13 if q<p]
    dirty={q:bool(debt_vec(q)) for q in earlier}
    for q in earlier:
        for Q in earlier:
            if q==Q:continue
            if step(Q)%step(q)==0 and not dirty[Q] and dirty[q]:
                ideal_fail.append((p,q,Q,step(q),step(Q)))
assert not ideal_fail, ideal_fail[:5]

# A negative signature at row q requires step(q)|step(Q); therefore a dirty
# row cannot be negatively affected by a clean signature generator Q.
absorbing_fail=[]
checks=0
for p in C13:
    earlier=[q for q in C13 if q<p]
    for q in earlier:
        if not debt_vec(q):continue
        sq=step(q)
        for Q in earlier:
            if debt_vec(Q):continue
            checks+=1
            if step(Q)%sq==0:
                absorbing_fail.append((p,q,Q,sq,step(Q)))
assert not absorbing_fail, absorbing_fail[:5]

print({
    "higher_class13_below_5000":len(C13),
    "nested_step_pairs":len(nested),
    "dirty_q":sum(bool(debt_vec(q)) for q in C13),
    "clean_q":sum(not debt_vec(q) for q in C13),
    "clean_generator_vs_dirty_row_checks":checks,
    "failures":0,
})
