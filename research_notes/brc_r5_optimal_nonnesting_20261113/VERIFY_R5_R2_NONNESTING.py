#!/usr/bin/env python3
"""Exact frozen R5 rederivation and sharp radius-2 non-nesting witness."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
qs=(3,12,15)
pools={q:set() for q in qs}
n=k=mask=0
for step in range(1,1<<15):
    bit=1<<((step & -step).bit_length()-1)
    mask ^= bit
    i=bit.bit_length()-1
    if mask & bit:
        n += W[i]
        k += K0[i]
    else:
        n -= W[i]
        k -= K0[i]
    assert mask == (step ^ (step>>1))
    if n>=3 and k%36==0 and k//36 in pools:
        pools[k//36].add(n)
assert tuple(len(pools[q]) for q in qs)==(538,298,229)
thresholds=Counter(Fraction(p,q) for q,ints in pools.items() for p in ints)
assert len(thresholds)==953
assert Counter(thresholds.values())=={1:869,2:56,3:28}
x=[0]
for wall in sorted(thresholds):
    x.append(x[-1]+thresholds[wall])
assert len(x)==954 and x[-1]==1065
N=len(x); R=2

# Independent DP uses explicit intermediate nearest-distance sums and feasibility.
incoming=[[] for _ in x]
for p in range(N):
    for q in range(p+1,min(N,p+2*R+2)):
        middle=[min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q)]
        if any(d>R for d in middle):
            continue
        incoming[q].append((p,sum(middle)))
assert sum(map(len,incoming))==4383
prev=[None]*N
for p in range(N):
    if x[p]-x[0]<=R:
        prev[p]=sum(x[p]-x[b] for b in range(p))
frontier={}
for budget in range(1,N+1):
    options=[
        v+sum(x[b]-x[p] for b in range(p+1,N))
        for p,v in enumerate(prev)
        if v is not None and x[-1]-x[p]<=R
    ]
    if options:
        frontier[budget]=min(options)
    current=[None]*N
    for q,links in enumerate(incoming):
        values=[prev[p]+w for p,w in links if prev[p] is not None]
        if values:
            current[q]=min(values)
    prev=current
assert set(frontier)==set(range(213,N+1))
assert [frontier[k] for k in range(213,224)]==[
    1070,1064,1059,1054,1049,1044,1039,1034,1029,1024,1020
]
assert all(frontier[k]>=frontier[k+1] for k in range(213,N))

# All center subsets are exhausted for the independent 7-coordinate counterexample.
small=(0,1,3,4,6,7,8)
witness={}
for budget in (2,3):
    best=10**9
    opt=[]
    for S in combinations(small,budget):
        ds=[min(abs(y-z) for z in S) for y in small]
        if max(ds)>R:
            continue
        total=sum(ds)
        if total<best:
            best=total
            opt=[]
        if total==best:
            opt.append(list(S))
    witness[budget]={"minimum":best,"optimal_sets":opt}
assert witness[2]=={"minimum":8,"optimal_sets":[[1,6]]}
assert witness[3]=={"minimum":4,"optimal_sets":[
    [0,3,7],[0,4,7],[1,3,7],[1,4,7]
]}

gain_hist=Counter(frontier[k]-frontier[k+1] for k in range(213,N))
non_nested=[
    [k,k+1,frontier[k]-frontier[k+1]]
    for k in range(213,N)
    if frontier[k]-frontier[k+1]>3
]
assert dict(gain_hist)=={6:1,5:8,4:70,3:23,2:36,1:603}
assert len(non_nested)==79
assert sum(frontier.values())==292961
assert sum(k*v for k,v in frontier.items())==130909193

result={
    "status":"PASS_EXACT",
    "scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
    "N":N,
    "walls":len(thresholds),
    "events":x[-1],
    "edges":sum(map(len,incoming)),
    "feasible_budgets":[213,954],
    "cost_samples":{str(i):frontier[i] for i in [213,214,215,216,217,218,219,220,221,222,223,350,351,954]},
    "sum_costs":sum(frontier.values()),
    "sum_k_costs":sum(k*v for k,v in frontier.items()),
    "gain_histogram":{str(key):gain_hist[key] for key in sorted(gain_hist)},
    "sharp_insertion_bound_R2":3,
    "non_nesting_certified_count":len(non_nested),
    "non_nesting_certified_transitions":non_nested,
    "small_exact_witness":{str(key):val for key,val in witness.items()},
    "verification":"exact Fraction/integer reconstruction; full-budget DP; direct subset enumeration on seven coordinates"
}
print(json.dumps({
    **result,
    "non_nesting_certified_transitions":non_nested[:12]
},indent=2))
with (Path(__file__).parent/"EXACT_OUTPUT.json").open("w",encoding="utf-8") as f:
    json.dump(result,f,indent=2,ensure_ascii=False)
    f.write("\n")
