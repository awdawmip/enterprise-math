"""All 11-message partitions with exactly five 13-sets, modulo affine equivalence.

Python 3.10+, a C++17 compiler. The prior all-class inventory proves there
are 250 possible 13-sets. The accompanying six13.py handles six 13-sets.
"""
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from itertools import combinations,product,permutations
import json
import os
from pathlib import Path
import subprocess
import tempfile
from cyclic11 import P,index,setbits,observations
from six13 import enumerate_classes,is_legal

HERE=Path(__file__).resolve().parent
FULL=(1<<125)-1

def packings(bad, nlarge):
    a={0}
    for u,v in product((1,-1),repeat=2):
        a.update([index((0,2*u%5,v%5)),index((u%5,0,2*v%5)),index((2*u%5,v%5,0))])
    base=sum(1<<i for i in a)
    def image(row,t):
        return sum(1<<t[i] for i in setbits(row))
    def shift(p,d):
        return index(tuple((v+w)%5 for v,w in zip(p,d)))
    linear={tuple(index(tuple(sg[j]*k*p[per[j]]%5 for j in range(3))) for p in P)
            for per in permutations(range(3)) for sg in product((-1,1),repeat=3) for k in (1,2)}
    orient={image(base,t)for t in linear}
    bank={sum(1<<shift(P[i],d)for i in setbits(row))for row in orient for d in P}
    assert len(bank)==250 and all(is_legal(s,bad)for s in bank)
    stab=[t for t in linear if image(base,t)==base]
    maps=[{s:image(s,t) for s in bank}for t in stab]
    # Each admissible packing can be moved so that one of its five rows is base.
    pointed=[]
    def choose(ch,pool):
        if len(ch)==nlarge:
            pointed.append(tuple(sorted(ch)))
            return
        for j,s in enumerate(pool):
            choose(ch+[s],[w for w in pool[j+1:] if not w&s])
    choose([base],[s for s in sorted(bank)if not s&base])
    seen=set(); representatives=[]
    for p in pointed:
        if p not in seen:
            seen.update(tuple(sorted(m[s] for s in p))for m in maps)
            representatives.append(p)
    # Repoint to each of the five rows, then normalize by the stabilizer.
    maps_to_base={}
    for row in bank:
        xyz=[P[i] for i in setbits(row)]
        center=tuple(Counter(p[j]for p in xyz).most_common(1)[0][0] for j in range(3))
        shiftback=tuple(shift(p,tuple(-v for v in center))for p in P)
        centered=image(row,shiftback)
        t=next(t for t in linear if image(base,t)==centered)
        inv=tuple(t.index(i)for i in range(125))
        to=tuple(inv[w]for w in shiftback)
        assert image(row,to)==base
        maps_to_base[row]=to
    def canonical(p):
        variants=[]
        for m in p:
            based=[image(s,maps_to_base[m]) for s in p]
            variants.extend(tuple(sorted(h[s]for s in based))for h in maps)
        return min(variants)
    key=[canonical(p)for p in representatives]
    groups=[[i for i,c in enumerate(key)if c==k]for k in sorted(set(key))]
    return pointed,representatives,groups

