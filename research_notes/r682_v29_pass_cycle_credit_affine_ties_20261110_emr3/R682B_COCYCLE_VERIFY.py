#!/usr/bin/env python3
"""R682-B: self-contained exact cycle-credit 2-cocycle validator."""
from itertools import product
from collections import Counter
import json

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))
def delta(m):
    a,b,c=m
    return a-c,b-a,c-b,0
def residual(d):
    x,y,z,t=d
    assert x+y+z==0 and t==0
    b=min(0,y,-x)
    v=(-b,y-b,-x-b)
    assert min(v)==0 and delta(v)==d
    return v
def credit(m):
    return min(m)
def kap(d,e):
    return min(add(residual(d),residual(e)))

zero=(0,0,0,0)
assert residual(zero)==(0,0,0)
V=list(product(range(4),repeat=3))
pairs=triples=0
dist=Counter()
for m in V:
    dm=delta(m)
    assert m==tuple(credit(m)+x for x in residual(dm))
    for n in V:
        dn=delta(n)
        k=kap(dm,dn)
        mn=add(m,n)
        assert credit(mn)==credit(m)+credit(n)+k
        assert residual(add(dm,dn))==tuple(x+y-k for x,y in zip(residual(dm),residual(dn)))
        dist[k]+=1
        pairs+=1
for m in V:
    d=delta(m)
    for n in V:
        e=delta(n)
        for p in V:
            f=delta(p)
            assert kap(d,e)+kap(add(d,e),f)==kap(e,f)+kap(d,add(e,f))
            triples+=1
assert pairs==4096 and triples==262144
assert dict(sorted(dist.items()))=={0:2416,1:1206,2:420,3:54}
assert kap(delta((3,0,0)),delta((0,3,3)))==3
out={
 'schema':'R682_B_CYCLE_CREDIT_COCYCLE_EXACT_V1',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'domain':'directed nonnegative triangle PASS counts; exact integer combinatorial model',
 'formula':'j(m+n)=j(m)+j(n)+kappa(delta(m),delta(n))',
 'cocycle':'kappa(d,e)+kappa(d+e,f)=kappa(e,f)+kappa(d,e+f)',
 'pairs_checked':pairs,'triples_checked':triples,
 'defect_histogram':dict(sorted(dist.items())),
 'unbounded_defect_family':'m=(r,0,0), n=(0,r,r), kappa=r for all integers r>0',
 'source_status':'author-only; no official V39 mapping or independent Driver acceptance'
}
with open('R682B_COCYCLE_EVIDENCE.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,sort_keys=True,indent=2)
    f.write('\n')
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
print('R682B_CYCLE_CREDIT_COCYCLE_EXACT_PASS')
