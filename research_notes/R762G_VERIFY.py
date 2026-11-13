#!/usr/bin/env python3
"""R762G: independent exact port DP and Pareto erosion certificate.
Native TRIADIC_CLOSURE_E and V29/V39 mapping are not assumed.
"""
import json
from itertools import product

N = 6
E = tuple(range(N))
SUPPORTS = ((0, 1, 2), (0, 3, 4), (1, 3, 5))
F = ((1,4,6),(1,5,5),(1,7,4),(2,3,4),(3,2,4),(3,3,3),
     (4,1,5),(4,2,3),(4,3,2),(4,7,1),(5,1,4),(5,5,1),(6,4,1))
EXPECTED = {
 0: F,
 1: ((2,4,6),(2,5,5),(3,3,4),(4,2,5),(4,3,3),(5,2,4),(5,5,2),(6,4,2)),
 2: ((3,4,6),(3,5,5),(4,3,5),(4,4,4),(5,3,4),(5,5,3),(6,4,3)),
 3: ((4,4,6),(4,5,5),(5,4,5),(5,5,4),(6,4,4)),
 4: ((5,5,5),)
}
def le(a,b):
    return all(x<=y for x,y in zip(a,b))
def pareto(xs):
    xs=set(xs)
    return tuple(sorted(x for x in xs if not any(y!=x and le(y,x) for y in xs)))
def C(k):
    return tuple((i,j,k-i-j) for i in range(k+1) for j in range(k-i+1))
def certify_erosion(k):
    basis=((0,0,0),)
    for c in C(k):
        shifted=tuple(tuple(f[i]+c[i] for i in range(3)) for f in F)
        basis=pareto(tuple(max(x[i],y[i]) for i in range(3)) for x in basis for y in shifted)
    return basis
def cycle(s):
    p=list(E)
    a,b,c=s
    p[a],p[b],p[c]=b,c,a
    return tuple(p)
def mul(p,q):
    return tuple(p[q[i]] for i in E)
G=tuple(cycle(s) for s in SUPPORTS)
B=8
Q={(0,0,0):{E}}
R={(0,0,0):{E}}
for b in product(range(B+1),repeat=3):
    if b==(0,0,0):
        continue
    words=set()
    for i in range(3):
        if b[i]:
            prev=tuple(b[j]-(j==i) for j in range(3))
            words.update(mul(p,G[i]) for p in Q[prev])
    Q[b]=words
    R[b]=words|set().union(*(R[tuple(b[j]-(j==i) for j in range(3))] for i in range(3) if b[i]))
assert len(R[(8,8,8)]) == 360
assert all((len(R[b]) == 360) == any(le(f,b) for f in F) for b in R)
report={'schema':'R762G_ADVERSARIAL_PREFIX_BUDGET_CERTIFICATE_V1',
        'parent_task':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
        'frozen_scientific_input':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'observer':'all 360 final port placements re-reachable after any length-k prefix, right group action',
        'budget_box':[9,9,9], 'budget_box_cases':len(R),
        'independent_exact_count_dp':'Q[b]=union_i Q[b-e_i]*g_i; R[b]=Q[b] union_i R[b-e_i]',
        'results':{}}
for k in range(5):
    minima=certify_erosion(k)
    assert minima == EXPECTED[k], (k,minima)
    robust={}
    for b in product(range(B+1),repeat=3):
        if min(b)<k:
            ok=False
        else:
            ok=all(len(R[tuple(b[i]-c[i] for i in range(3))])==360 for c in C(k))
        assert ok == any(le(m,b) for m in minima),(k,b)
        robust[b]=ok
    local=pareto(b for b,x in robust.items() if x)
    assert local==minima, (k,local)
    witnesses=[]
    for m in minima:
        for i in range(3):
            if not m[i]: continue
            lower=tuple(m[j]-(j==i) for j in range(3))
            sample=None
            for c in C(k):
                if not le(c,lower):
                    sample={'prefix_counts':list(c),'reason':'not every length-k prefix legal'}
                    break
                residual=tuple(lower[j]-c[j] for j in range(3))
                miss=sorted(R[(8,8,8)]-R[residual])
                if miss:
                    sample={'prefix_counts':list(c),'residual_budget':list(residual),
                            'missing_port_image':list(miss[0]),'missing_port_count':len(miss)}
                    break
            assert sample,(k,m,i)
            witnesses.append({'minimal_budget':list(m),'decrement_axis':i,'witness':sample})
    report['results'][str(k)]={
        'minima':[list(x) for x in minima],
        'minima_count':len(minima),
        'min_total_budget':min(map(sum,minima)),
        'full_budget_cases_in_box':sum(robust.values()),
        'minimality_witnesses':witnesses}
assert report['results']['4']['minima']==[[5,5,5]]
print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
