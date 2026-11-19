#!/usr/bin/env python3
"""R762GE: exact integer-only DP for signed X6 primitive coordinate paths.
No external dependencies. No native TRIADIC_CLOSURE_E transition is assumed.
"""
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path

N_AXES=6
MAX_M=8
STARS=((0,1,2),(0,3,4),(1,3,5),(2,4,5))

def canon(z):
    low=min(z)
    return tuple(x-low for x in z),low

def star_obs(z, chosen=(0,1,2)):
    return tuple(tuple(z[e]-min(z[i] for i in STARS[v]) for e in STARS[v]) for v in chosen)

def reconstruct_relative_from_three_stars(z, chosen=(0,1,2)):
    # Exact shared-edge graph-offset recovery: return r, not full Cell.
    star_values={v:tuple(z[e]-min(z[i] for i in STARS[v]) for e in STARS[v]) for v in chosen}
    ref=chosen[0]
    offsets={ref:0}
    for v in chosen[1:]:
        common=set(STARS[ref]) & set(STARS[v]); assert len(common)==1
        e=next(iter(common))
        offsets[v]=star_values[ref][STARS[ref].index(e)]-star_values[v][STARS[v].index(e)]
    out=[None]*6
    for v in chosen:
        for i,e in enumerate(STARS[v]):
            val=star_values[v][i]+offsets[v]
            assert out[e] is None or out[e]==val
            out[e]=val
    assert all(x is not None for x in out)
    return canon(tuple(out))[0]

def f(r,h):
    return sum(abs(v+h) for v in r)

def possible_depths(r,m):
    if (m-sum(r))%2:
        return ()
    return tuple(h for h in range(-m,m+1) if f(r,h)<=m)

def advance(dp):
    nxt=defaultdict(int)
    for z,n in dp.items():
        for i in range(N_AXES):
            plus=list(z); plus[i]+=1
            minus=list(z); minus[i]-=1
            nxt[tuple(plus)]+=n
            nxt[tuple(minus)]+=n
    return dict(nxt)

def verify():
    dp={(0,)*N_AXES:1}
    rows=[]
    for m in range(MAX_M+1):
        fibers=defaultdict(dict)
        for z,n in dp.items():
            r,h=canon(z)
            fibers[r][h]=n
            for chosen in combinations(range(4),3):
                assert reconstruct_relative_from_three_stars(z,chosen)==r
            p=(m+sum(z))//2
            assert 2*p-m==sum(z) and 0<=p<=m
            assert (2*p-m-sum(r))%6==0
            assert (2*p-m-sum(r))//6==h
        max_fiber=max(map(len,fibers.values()))
        assert max_fiber==m//3+1, (m,max_fiber)
        for r,depth_counts in fibers.items():
            assert tuple(sorted(depth_counts))==possible_depths(r,m)
            assert sum(depth_counts.values())==sum(dp[tuple(x+h for x in r)] for h in depth_counts)
        a,b=divmod(m,3)
        witness=(0,0,0,a,a,a+b)
        assert len(fibers[witness])==a+1
        assert set(fibers[witness])==set(range(-a,1))
        assert sum(dp.values())==12**m
        rows.append({'m':m,'reachable_endpoints':len(dp),'relative_classes':len(fibers),
                     'max_depth_fiber':max_fiber,'sharp_witness_r':list(witness),
                     'witness_depths':list(range(-a,1)),'source_words':sum(dp.values())})
        dp=advance(dp)
    return {
        'schema':'R762GE_SIGNED_X6_REPAIR_EXACT_VERIFICATION_V1',
        'science_scope':'signed unit-axis coordinate adjacency on a charted Z^6 Cell torsor, NOT an admitted TRIADIC_CLOSURE_E rule',
        'method':'exact integer DP 12 signed steps; independent convex/triangle-inequality proof in companion note',
        'max_checked_length':MAX_M,
        'star_subsets_checked_per_endpoint':4,
        'checks':['all reachable endpoints','all relative-depth fibers','parity/l1 reachability formula',
                  'optimal worst-fiber count floor(m/3)+1','sharp witness construction',
                  '4 triple-STAR reconstructions for each endpoint','p/m integer common-depth repair',
                  'total ordered source count 12**m'],
        'rows':rows,
        'result':'PASS',
        'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    result=verify()
    dest=Path(__file__).with_name('R762GE_EVIDENCE.json')
    dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    for row in result['rows']:
        print(row['m'],row['reachable_endpoints'],row['relative_classes'],row['max_depth_fiber'],row['source_words'])
    print('PASS:',dest)
