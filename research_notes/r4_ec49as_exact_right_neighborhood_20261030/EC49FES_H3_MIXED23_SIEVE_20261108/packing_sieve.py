"""Provably conservative EC49FEQ 23-word H3-B depthwise native prefix packing lower bound.
Every group is universally at least its shortest native microstep length; a subset of groups
whose sets of possible d-prefixes are pairwise disjoint and avoid free early prefixes
forces one new prefix per group at depth d. Exact clique search on 16 groups.
"""
import sys,json,time
from collections import Counter
from functools import lru_cache
from itertools import combinations
from EC49FEQ_H3_MIXED23 import enumerate_type_B
from EC49FEQ_DEPTH_SIEVE import EARLY_FREE
from EC49FEJ_SIEVE import pool
from EC49FEJ_CONSTRUCT import native
FREE_BY_DEPTH={d:frozenset(p for p in EARLY_FREE if len(p)==d) for d in range(1,40)}
@lru_cache(None)
def g(h,s,k):
    a=[native(w) for w,t in pool(h,k) if t==s]
    if not a:return None
    return min(map(len,a)),tuple(frozenset(w[:d] for w in a if len(w)>=d) for d in range(1,max(map(len,a))+1))
@lru_cache(maxsize=12)
def group(h,s,ks):
    z=[g(h,s,k) for k in ks];z=[i for i in z if i]
    if not z:return None
    return min(i[0] for i in z),tuple(frozenset().union(*(i[1][d-1] for i in z if len(i[1])>=d)) for d in range(1,max(len(i[1]) for i in z)+1))
@lru_cache(maxsize=8000)
def independent(adjs):
    n=len(adjs)
    @lru_cache(None)
    def f(mask):
        if not mask:return 0
        bit=mask & -mask
        i=bit.bit_length()-1
        return max(f(mask^bit),1+f(mask & ~bit & ~adjs[i]))
    return f((1<<n)-1)

def bound(K,high,cap=94):
    grp=[group(h,s,K) for h in range(4,10) for s in ((16,32) if h in high else (1,2,4,8))]
    if any(q is None for q in grp):return None
    b=39
    for d in range(1,max(len(q[1]) for q in grp)+1):
        free=FREE_BY_DEPTH[d]
        psets=[q[1][d-1] for q in grp if q[0]>=d and not (q[1][d-1]&free)]
        adjacency=tuple(sum(1<<j for j,b in enumerate(psets) if i!=j and bool(a&b)) for i,a in enumerate(psets))
        b+=independent(adjacency)
        if b>=cap:return b
    return b

if __name__=="__main__":
    start=int(sys.argv[1]) if len(sys.argv)>1 else 0
    end=int(sys.argv[2]) if len(sys.argv)>2 else 100
    output=sys.argv[3] if len(sys.argv)>3 else 'packing_report.json'
    _,inventories=enumerate_type_B(); counts=Counter();unresolved=[]
    t=time.time()
    for i in range(start,end):
        high,K=inventories[i];b=bound(K,high);counts[b]+=1
        if b<94:unresolved.append({'index':i,'high':list(high),'keys':list(map(list,K)),'lower':b})
    rep={'domain':'EC49FEQ type B feasible inventories; ordered enumeration as in EC49FEQ_H3_MIXED23.py', 'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','range':[start,end], 'tested':end-start, 'packing_lower_distribution':dict(sorted(counts.items())), 'excluded_le93':end-start-len(unresolved),'not_excluded_le93':len(unresolved),'unresolved_cases':unresolved, 'runtime_s':round(time.time()-t,3), 'method':'39 early mandatory cost; 113 early free prefixes; for each depth exact maximum packing of groups with pairwise disjoint full candidate prefix sets and no early-free intersection; exact graph DP'}
    with open(output,'w') as f:json.dump(rep,f,indent=2)
    print({k:v for k,v in rep.items() if k not in ('unresolved_cases',)})