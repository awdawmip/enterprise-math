"""R252 exact positive unit-weight BRC author-side certificate; not native module execution.
A restricted six-axis affine g(z)=diag(eps,eps,1,1,1,1) z + k*e1
is faithfully encoded by (eps,k).
"""
from collections import Counter
from math import comb
import json
EDGES = {0: ((2,(-1,-1)), (2,(1,-1))),
         1: ((0,(-1,-1)), (0,(1,-1))),
         2: ((1,(1,1)), (2,(1,-1)))}

def compose(f,g):
    eps,k=f; eta,t=g
    return (eta*eps,eta*k+t)  # g after f

def step(cur,edges=EDGES):
    out=Counter()
    for (q,f),n in cur.items():
        for dest,g in edges[q]:
            out[(dest,compose(f,g))]+=n
    return out

def anchor(cur):
    out=Counter()
    for (_q,(eps,k)),n in cur.items():
        out[-eps*k]+=n  # F^{-1}(0) on first of 6 native axes
    return out

def full(cur):
    out=Counter()
    for (_q,f),n in cur.items(): out[f]+=n
    return out

cur={q:Counter({(q,(1,0)):1}) for q in (0,1)}
for m in range(41):
    target=Counter({m-2*j:comb(m,j) for j in range(m+1)})
    assert anchor(cur[0])==anchor(cur[1])==target
    assert sum(anchor(cur[0]).values())==2**m
    if m<=2: assert full(cur[0])==full(cur[1])
    if m==3:
        assert full(cur[0])==Counter({(-1,-3):1,(-1,-1):3,(1,-3):1,(1,-1):3})
        assert full(cur[1])==Counter({(-1,-3):1,(-1,-1):2,(-1,1):1,(1,-3):1,(1,-1):2,(1,1):1})
    cur={q:step(cur[q]) for q in cur}
changed={**EDGES,2:((1,(1,2)),(2,(1,-1)))}
c0=Counter({(0,(1,0)):1});c1=Counter({(1,(1,0)):1})
for _ in range(2):c0=step(c0,changed);c1=step(c1,changed)
assert anchor(c0)==Counter({-2:1,-1:1,1:1,2:1})
assert anchor(c1)==Counter({-2:1,0:2,2:1})
print(json.dumps({"status":"PASS","model":"author_side_six_axis_restricted_affine_BRC",
"depths":"0..40","max_positive_paths":str(2**40),"first_full_effect_difference":3,
"altered_kernel_first_anchor_difference":2,"native_module_run":False},sort_keys=True))
