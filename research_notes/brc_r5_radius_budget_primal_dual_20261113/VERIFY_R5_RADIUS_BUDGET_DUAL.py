#!/usr/bin/env python3
"""Exact greedy-cover / dual-packing certificates for frozen R5 checkpoint budgets.
Scientific input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551.
Python standard library; exact fractions and integers, no float decisions.
"""
import json
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
WEIGHTS = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD56 = 'd500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'

def frozen_r5_events():
    pools = {3:set(), 12:set(), 15:set()}
    for mask in range(1, 1 << 15):
        n = -sum(v for j,v in enumerate(WEIGHTS) if mask >> j & 1)
        k = -sum(v for j,v in enumerate(K0) if mask >> j & 1)
        if n >= 3 and k % 36 == 0 and k // 36 in pools:
            pools[k // 36].add(n)
    assert {q:len(a) for q,a in pools.items()} == {3:538,12:298,15:229}
    h = Counter((1 - Fraction(36*q,n))/23 for q,ns in pools.items() for n in ns)
    assert len(h)==953 and Counter(h.values())=={1:869,2:56,3:28}
    x=[0]
    for t in sorted(h):
        x.append(x[-1]+h[t])
    assert len(x)==954 and x[-1]==1065
    return x

def optimal_cover_and_dual(x,r):
    assert r>=0 and x==sorted(set(x)) and x
    n=len(x)
    L=[bisect_left(x,v-r) for v in x]
    U=[bisect_right(x,v+r)-1 for v in x]
    centers=[];witness=[];first=0
    while first<n:
        p=bisect_right(L,first)-1
        assert p>=first and L[p]<=first<=U[p]
        centers.append(p);witness.append(first)
        first=U[p]+1
    assert len(centers)==len(witness)
    assert all(min(abs(v-x[p]) for p in centers)<=r for v in x)
    assert all(not (L[p]<=witness[i] and witness[i+1]<=U[p])
               for p in range(n) for i in range(len(witness)-1))
    return centers,witness

def legacy_centers():
    raw=bytes.fromhex(OLD56)
    assert len(raw)==56
    assert sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little')
    ans=[bits&3];bits >>=2
    for _ in range(212):
        d=bits&3;bits>>=2
        assert d<=2
        ans.append(ans[-1]+3+d)
    assert not bits and len(ans)==213 and ans[0]==1 and ans[-1]==952
    return ans

def exhaustive_small():
    cases=0;subsets=0;dual_checks=0
    for n in range(1,8):
        for increments in product((1,2,3),repeat=n-1):
            x=[0]
            for d in increments:x.append(x[-1]+d)
            for r in range(6):
                centers,witness=optimal_cover_and_dual(x,r)
                kbest=n+1
                for k in range(1,n+1):
                    if any(all(min(abs(x[b]-x[s]) for s in subset)<=r
                               for b in range(n))
                           for subset in combinations(range(n),k)):
                        kbest=k;break
                assert len(centers)==kbest
                cases+=1;dual_checks+=len(witness)
                subsets+=(1<<n)-1
    return {'cases':cases,'dual_witness_points':dual_checks,
            'subset_search_spaces_upper_bound':subsets}

def main():
    x=frozen_r5_events()
    selected={}
    for r in range(0,37):
        c,w=optimal_cover_and_dual(x,r)
        if r in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,35,36):
            selected[str(r)]={'min_centers':len(c),'greedy_centers':c if r in (1,2,9,35,36) else None,
                              'dual_witness_indices':w if r in (1,2,9,35,36) else None}
    for k, r, prev in ((213,2,1),(57,9,8),(15,36,35)):
        assert selected[str(r)]['min_centers']==k
        assert selected[str(prev)]['min_centers']>k
    orig=legacy_centers()
    assert max(min(abs(v-x[p]) for p in orig) for v in x)==2
    assert sum(min(abs(v-x[p]) for p in orig) for v in x)==1070
    assert len(orig)==selected['2']['min_centers']
    g2,_=optimal_cover_and_dual(x,2)
    assert sum(min(abs(v-x[p]) for p in g2) for v in x)==1104
    small=exhaustive_small()
    summary={'status':'PASS_EXACT_R5_RADIUS_BUDGET_PRIMAL_DUAL',
      'frozen_pin':PIN,'boundaries':len(x),'events':x[-1],
      'histogram':{'single':869,'double':56,'triple':28},
      'budget_radius_thresholds':[
         {'budget':k,'minimal_radius':r,'minimum_centers_at_previous_radius':selected[str(p)]['min_centers'],
           'minimum_centers_at_radius':selected[str(r)]['min_centers']}
         for k,r,p in ((213,2,1),(57,9,8),(15,36,35))],
      'kmin_by_radius':{s:z['min_centers'] for s,z in selected.items()},
      'greedy_radius2_mean_cost':1104,
      'legacy_radius2_mean_cost':1070,
      'legacy_center_count':len(orig),
      'greedy_radius2_first_12':g2[:12],
      'greedy_radius2_last_12':g2[-12:],
      'exhaustive_small':small,
      'proof_certificate':'for every r, greedy centers cover all x and witnesses pairwise cannot share any radius-r center; matching cardinalities prove Kmin exactly'}
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
