"""Exact checks for conditional relational PF-10 trace model, not native physical Cell event law."""
from collections import Counter, defaultdict
from itertools import product
from math import factorial
P=tuple(product(range(6), repeat=2))
for n in (2,3):
    fibers=defaultdict(Counter)
    for w in product(P,repeat=n):
        c=Counter(w); m=tuple(c.get(p,0) for p in P)
        fibers[m][w[-1]]+=1
    assert sum(sum(v.values()) for v in fibers.values())==36**n
    assert len(fibers)=={2:666,3:8436}[n]
    assert Counter(sum(v.values()) for v in fibers.values())==({1:36,2:630} if n==2 else {1:36,3:1260,6:7140})
    assert max(max(v.values()) for v in fibers.values())==({2:1,3:2}[n])
    for m,v in fibers.items():
        count=factorial(n)
        for k in m: count//=1 if not k else 1
        denom=1
        for k in m: denom*=factorial(k)
        assert sum(v.values())==factorial(n)//denom
print("PASS: N=2 and N=3 exact PF10 formal passage-trace enumeration")
