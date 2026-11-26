"""Independent small model suffix packing verification and node125 witness."""
from functools import lru_cache
from itertools import product
from collections import Counter
from random import Random
from math import comb
from gal_path_hall import Bound, bitlist
from suffix_pack import packing
import json


def reference(b,k,h):
    s=b.full;d=k-h
    @lru_cache(None)
    def feasible(r,t):
        if r.bit_count()<=1:return {0,r}
        if not t:return {0}
        return {0}|{u|v for a in b.splits(r) for u in feasible(a,t-1) for v in feasible(r^a,t-1)}
    groups=[set() for _ in range(d+1)]
    # Explicit individual answer words and query selections; virtual padding (q=None).
    @lru_cache(None)
    def visit(r,depth,j):
        if depth==d:
            groups[j].update(feasible(r,h));return
        visit(r,depth+1,j);visit(r,depth+1,j+1)
        for q in b.qs:
            a=r&q;c=r^a
            if a and c:visit(a,depth+1,j);visit(c,depth+1,j+1)
    visit(s,0,0)
    dp={0}
    for j,gs in enumerate(groups):
        for _ in range(comb(d,j)):
            dp|={a|g for a in dp for g in gs if not a&g}
    return dp


def main():
    rng=Random(169432);stats=Counter()
    for i in range(100):
        n=rng.randrange(2,9);k=rng.randrange(1,5);m=max(3,(n-1).bit_length());states=rng.sample(range(1<<m),n)
        b=Bound([(0,0)]*n);b.qs=tuple(sum(1<<i for i,x in enumerate(states) if x>>j&1) for j in range(m))
        old=None
        for h in range(1,k+1):
            cap,dp,_=packing(b,k,h);ref=reference(b,k,h)
            assert dp==sum(1<<a for a in ref)
            if old is not None:assert dp&~old==0
            old=dp;stats['families']+=1;stats['membership_checks']+=1<<n
        assert cap(b.full)==b.exact(b.full,k);stats['models']+=1;b.clear()
    front=json.load(open('recoverable_frontier.out'))['rows']
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])));s=b.full
        cap,dp,_=packing(b,k,k)
        want=0
        for m in front[i]['frontier']:
            g=s^m;t=g
            while True:
                want|=1<<t
                if not t:break
                t=(t-1)&g
        assert dp==want;stats['frozen_exact_families']+=1;stats['frozen_membership_checks']+=1<<n;b.clear()
    k,n,*a=map(int,open('ga_nodes.txt').readlines()[125].split());b=Bound(list(zip(a[::2],a[1::2])));s=b.full
    rows=[(a,b.exact(a,k-1),b.exact(s^a,k-1)) for a in b.splits(s)]
    @lru_cache(None)
    def feas(r,t):
        if r.bit_count()<=1:return {0,r}
        if not t:return {0}
        return {0}|{u|v for a in b.splits(r) for u in feas(a,t-1) for v in feas(r^a,t-1)}
    pos=[];neg=[]
    for q in b.qs:
        if q and q!=s:
            pos.extend((q,t) for t in sorted(feas(q,k-1)) if t.bit_count()==7)
            neg.extend((q,t) for t in sorted(feas(s^q,k-1)) if t.bit_count()==7)
    witness=next((q,a,r,c) for q,a in pos for r,c in neg if not a&c)
    assert witness[0]!=witness[2] and max(v+w for a,v,w in rows)==13
    print(json.dumps({'stats':dict(stats),'node125_splits':rows,'node125_disjoint_7_witness':witness},sort_keys=True))
if __name__=='__main__':main()
