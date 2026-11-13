#!/usr/bin/env python3
"""R749 exact C1 retained-versus-resampled path-law verifier; Python stdlib."""
from itertools import combinations
import json

ports=[(i,s) for i in range(6) for s in (-1,1)]
V=[frozenset((a,b)) for a,b in combinations(ports,2) if a[0]!=b[0]]
assert len(V)==60

def adjacent(v,w):
    return len(v&w)==1 and len({p[0] for p in v|w})==3

neighbors={v:[w for w in V if adjacent(v,w)] for v in V}
assert all(len(z)==16 for z in neighbors.values())
assert sum(len(z) for z in neighbors.values())==960

def update(v,w):
    z=v^w
    assert adjacent(w,z) and adjacent(z,v)
    return z

for v in V:
    assert len({update(w,v) for w in neighbors[v]})==16

results={}
for n in (1,2,3,4):
    legal={(v,) for v in V}
    for _ in range(1,n):
        legal={p+(w,) for p in legal for w in neighbors[p[-1]]}
    c1=set()
    for v in V:
        if n==1:
            c1.add((v,))
            continue
        for w in neighbors[v]:
            p=[v,w]
            while len(p)<n:
                p.append(update(p[-2],p[-1]))
            c1.add(tuple(p))
    assert len(legal)==60*16**(n-1)
    assert len(c1)==(60 if n==1 else 960)
    assert c1<=legal
    denominator=1 if n<=2 else 16**(n-2)
    assert len(legal)//len(c1)==denominator
    results[str(n)]={
        "resampled_legal_blocks":len(legal),
        "retained_legal_blocks":len(c1),
        "resampled_acceptance":f"1/{denominator}",
        "total_variation":f"{denominator-1}/{denominator}",
        "equal_prior_bayes_error":f"1/{2*denominator}"
    }

print(json.dumps({"schema":"EM_R749_X6_C1_BLOCK_LAW_EXACT_V1",
    "result":"PASS","signed_ports":12,"visible_states":60,
    "directed_source_edges":960,"exact_horizons":[1,2,3,4],
    "checks":results,
    "all_horizon_proof":"n>=2: C1 blocks 960; resampled blocks 60*16^(n-1); TV=1-16^(-(n-2))",
    "fixed_current_four_bit_predictive_bound":16,
    "scope":"candidate finite C1; no native V29/V39 execution"},indent=2))
