#!/usr/bin/env python3
"""R749SA: exact 8:1 unsigned-support quotient and two-layer residual."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json

ports=[(a,s) for a in range(6) for s in (-1,1)]
V=[frozenset((x,y)) for x,y in combinations(ports,2) if x[0]!=y[0]]
index={v:i for i,v in enumerate(V)}
axes=[frozenset(x) for x in combinations(range(6),2)]
axis_index={a:i for i,a in enumerate(axes)}
def proj(v):return axis_index[frozenset(a for a,s in V[v])]
def adj(u,v):return len(u&v)==1 and len({a for a,s in u|v})==3
N=[[j for j,w in enumerate(V) if adj(v,w)] for v in V]
D=[(u,v) for u in range(60) for v in N[u]]
Nu=[[j for j,y in enumerate(axes) if len(x&y)==1] for x in axes]
Du={(proj(u),proj(v)) for u,v in D}
assert len(V)==60 and len(D)==960 and len(axes)==15 and len(Du)==120
assert {len(n) for n in N}=={16} and {len(n) for n in Nu}=={8}
assert Counter((proj(u),proj(v)) for u,v in D)==Counter({e:8 for e in Du})
cat=Counter()
for u,v in D:
    f=index[frozenset(V[u]^V[v])]
    fu=axis_index[frozenset(axes[proj(u)]^axes[proj(v)])]
    assert proj(f)==fu
    labels=[]
    for w in N[v]:
        label="full_signed_C1" if w==f else ("unsigned_C1_only" if proj(w)==fu else "unsigned_deviation")
        labels.append(label)
        cat[label]+=1
    assert Counter(labels)=={"full_signed_C1":1,"unsigned_C1_only":1,"unsigned_deviation":14}
    assert Counter(proj(w) for w in N[v])==Counter({z:2 for z in Nu[proj(v)]})
assert cat=={"full_signed_C1":960,"unsigned_C1_only":960,"unsigned_deviation":13440}
assert {len(set(Nu[u])&set(Nu[v])) for u,v in Du}=={4}
# Complete m=2 unsigned block histogram, from 120 starts and 8 moves at each step.
hist=Counter()
for u,v in Du:
    f=lambda x,y:axis_index[frozenset(axes[x]^axes[y])]
    for w in Nu[v]:
        for z in Nu[w]:
            hist[int(w==f(u,v))+int(z==f(v,w))]+=1
assert dict(hist)=={0:5880,1:1680,2:120},hist
result={
 "schema":"EM_R749SA_EXACT_UNSIGNED_QUOTIENT_V1",
 "status":"PASS",
 "signed_vertices":60,"signed_directed_edges":960,
 "unsigned_vertices":15,"unsigned_directed_edges":120,
 "directed_edge_fibre":8,"signed_degree":16,"unsigned_degree":8,
 "transition_category_counts_across_all_signed_edges":dict(sorted(cat.items())),
 "unsigned_n4_K_histogram":{str(k):v for k,v in sorted(hist.items())},
 "unsigned_3step_common_neighbors":4,
 "unsigned_return_source_posterior_p_half":str(Fraction(9**3,9**3+3)),
 "new_primitive_event_permission":False,
 "canonical_task_claim":False
}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
