"""Independent common-prefix support recursion and small-instance packing replay."""
from functools import lru_cache
from itertools import combinations
from math import comb
from random import Random
from collections import Counter
import json
from gal_path_hall import Bound, bitlist
from sibling_packing import pair_support, packing


def direct_pair(b,s,p,d):
    @lru_cache(None)
    def rec(s,a,c):
        if s==p:return True
        for q in b.qs:
            if q&p==p and a and s&q!=s and rec(s&q,a-1,c):return True
            if not q&p and c and s&~q!=s and rec(s&~q,a,c-1):return True
        return False
    if not any(q&p and p&~q for q in b.qs):return 0
    return sum(1<<j for j in range(d+1) if rec(s,d-j,j))


def naive(b,k):
    s=b.full; groups=[[] for j in range(k)]
    for x,o in b.opts(s,k):
        for j in range(k):
            if o&(3<<j):groups[j].append(x)
    for x,y in combinations(bitlist(s),2):
        p=x|y;o=direct_pair(b,s,p,k-1)
        for j in range(k):
            if o>>j&1:groups[j].append(p)
    dp={0}
    for j,gs in enumerate(groups):
        for _ in range(comb(k-1,j)):
            dp|={t|g for t in dp for g in gs if not t&g}
    return dp


def main():
    old=json.load(open('sibling_packing.json'))['rows']; stats=Counter();rng=Random(169431)
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])));s=b.full
        for d in (k,k+1):
            actual=[]
            for x,y in combinations(bitlist(s),2):
                p=x|y;v=direct_pair(b,s,p,d-1);assert v==pair_support(b,s,p,d-1)
                stats['pair_class_checks']+=d;stats['pair_checks']+=1
                if v:actual.append([p,v])
            if d==k:assert actual==old[i]['pairs']
            r=old[i]['budgets'][d-k];assert r[1]<=r[5]<=r[2]
        b.clear()
    for i in range(100):
        n=rng.randrange(2,9);k=rng.randrange(1,5);m=max(3,(n-1).bit_length());states=rng.sample(range(1<<m),n)
        # generic fixed binary queries, all states distinguishable
        b=Bound([(0,0)]*n);b.qs=tuple(sum(1<<i for i,x in enumerate(states) if x>>j&1) for j in range(m));dp=naive(b,k);cap,_,count=packing(b,b.full,k)
        assert len(dp)==count
        for t in range(1<<n):
            assert cap(t)==max((t&u).bit_count() for u in dp)
            stats['packing_target_checks']+=1
        stats['synthetic_models']+=1;b.clear();cap.cache_clear()
    print(json.dumps(dict(stats),sort_keys=True))
if __name__=='__main__':main()
