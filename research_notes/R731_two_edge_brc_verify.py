#!/usr/bin/env python3
"""R731: exact two-new-port-edge BRC counts with independent labeled-ID recurrence."""
from functools import lru_cache
from itertools import combinations
from math import factorial, comb
import json

AX=tuple(range(6))
BASE=frozenset(t for t in combinations(AX,3) if not (0 in t and 1 in t))

@lru_cache(None)
def direct(a, k=-1, l=-1):
    if not any(a): return 1
    if sum(a)%3: return 0
    i=next(i for i,v in enumerate(a) if v)
    edges=BASE|({(0,1,k)} if k>=0 else set())|({(0,1,l)} if l>=0 else set())
    v=0
    for t in edges:
        if i not in t: continue
        j,h=(x for x in t if x!=i)
        if a[j] and a[h]:
            b=list(a);b[i]-=1;b[j]-=1;b[h]-=1
            v+=a[j]*a[h]*direct(tuple(b),k,l)
    return v

def falling(a,s):
    assert s<=a
    return factorial(a)//factorial(a-s)

def poly(a,k,l):
    m=sum(a)//3
    smax=min(a[k],m-a[l]);tmax=min(a[l],m-a[k])
    if smax<0 or tmax<0: return {}
    lower=max(0,a[0]+a[1]-m)
    upper=min(a[0],a[1],m,*(m-a[j] for j in AX if j not in (0,1,k,l)))
    out={}
    for s in range(max(0,smax)+1):
        for t in range(max(0,tmax)+1):
            q=s+t
            if not lower<=q<=upper:continue
            b=list(a)
            b[0]-=q;b[1]-=q;b[k]-=s;b[l]-=t
            val=(falling(a[0],q)*falling(a[1],q)*falling(a[k],s)*falling(a[l],t)//(factorial(s)*factorial(t)))*direct(tuple(b))
            assert val>0
            out[s,t]=val
    return out

def vectors(total,n=6):
    if n==1:
        yield (total,);return
    for i in range(total+1):
        for b in vectors(total-i,n-1):yield (i,)+b

def verify():
    stats={}
    pairs=list(combinations(range(2,6),2))
    for m in range(0,5):
        vcount=0;cases=0;nonempty=0;mixed_new=0;synergy=0;max_points=0;max_coeff=0
        for a in vectors(3*m):
            vcount+=1
            old=direct(a)
            for k,l in pairs:
                cases+=1
                P=poly(a,k,l)
                assert direct(a,k,l)==sum(P.values()),(a,k,l)
                feasible={(s,t) for s in range(m+1) for t in range(m+1)
                    if s+t<=min(a[0],a[1],m)
                    and s<=a[k] and t<=a[l]
                    and a[0]+a[1]-2*(s+t)<=m-(s+t)
                    and a[k]-s<=m-(s+t)
                    and a[l]-t<=m-(s+t)
                    and all(a[j]<=m-(s+t) for j in AX if j not in(0,1,k,l))}
                assert feasible==set(P), (a,k,l,feasible,set(P))
                if P:
                    nonempty+=1
                    max_points=max(max_points,len(P));max_coeff=max(max_coeff,max(P.values()))
                    if any(s and t for (s,t) in P):mixed_new+=1
                if direct(a,k,l)>0 and old==direct(a,k)==direct(a,l)==0:
                    synergy+=1
        stats[str(m)]={'vectors':vcount,'pair_cases':cases,'nonempty':nonempty,'with_both_edges':mixed_new,'strict_cooperation':synergy,'max_support_points':max_points,'max_coefficient':max_coeff}
    family=[]
    for m in range(2,9):
        for r in range(1,m):
            a=(m,m,r,m-r,0,0)
            P=poly(a,2,3)
            assert P=={(r,m-r):factorial(m)**2}
            if m<=5:
                assert direct(a,2)==direct(a,3)==0 and direct(a,2,3)==factorial(m)**2
            family.append((m,r))
    stats['family']={'tested_pairs':len(family),'m_range':[2,8], 'max_m_branch_count':factorial(8)**2}
    print(json.dumps(stats,indent=2,sort_keys=True))
    print('R731_TWO_EDGE_BRC_SUPPORT_AND_COOPERATION_EXACT_PASS')
    with open('R731_two_edge_brc_results.json','w') as f:
        json.dump({'verified':True,'marker':'R731_TWO_EDGE_BRC_SUPPORT_AND_COOPERATION_EXACT_PASS','source':'R728/R730 candidate port incidence, not native V29/V39', 'stats':stats},f,ensure_ascii=False,indent=2)

if __name__=='__main__':verify()
