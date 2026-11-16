#!/usr/bin/env python3
"""R663 independent group-factor cross-check, index pullback rather than slot inheritance."""
from itertools import combinations
from collections import Counter

triads=tuple(combinations(range(6),3))
base=(0,1,2)
def neighbor(x,y):
    return len(set(x).intersection(y))==2
def pullback(x,y):
    assert neighbor(x,y)
    leaving=next(iter(set(x)-set(y)))
    entering=next(iter(set(y)-set(x)))
    # New sorted-position j pulls its slot from old sorted-position pullback[j].
    return tuple(x.index(leaving if z==entering else z) for z in y)
def compose(f,g):
    return tuple(f[g[j]] for j in range(3))
counts=Counter()
for a in triads:
    if not neighbor(base,a): continue
    for b in triads:
        if not neighbor(a,b): continue
        for c in triads:
            if not (neighbor(b,c) and neighbor(c,base)): continue
            path=(base,a,b,c,base)
            h=(0,1,2)
            for x,y in zip(path,path[1:]):
                h=compose(h,pullback(x,y))
            counts[h]+=1
expected={(0,1,2):207,(0,2,1):48,(2,1,0):48,
          (2,0,1):9,(1,2,0):9,(1,0,2):48}
assert dict(counts)==expected and sum(counts.values())==369
print("R663_INDEPENDENT_GROUP_FACTOR_CROSSCHECK_PASS",dict(counts))
