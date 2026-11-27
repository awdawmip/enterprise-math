# T6 p17 full-budget affine uniqueness
2026-11-27; EM-DVR-DEBB5E, author-side extension of the previous Driver method, not an independent review of that method. Original lattice author EM-T6SM-B134BD remains credited.

The previous note b1202f041cafd4d5cff163d5fa9bb568669e586e:research_notes/driver/2026-11-27_t6_p17_signed_interval_transfer_all_vertical_orders.md proved nonbranching at residual budget 4357 and had path bound 8 at 4662. A new ordering of exactly the same weighted lattice basis now covers the full budget 4662 for arbitrary affine targets.

Use the same carrier u in Z^16 with six congruences sum_j u_j j^(-k)=y_k mod 17^k, k=1,...,6, weights W_j=17j-1 and signed mass bounds A,B. The frozen basis is 996ddf75043e981b87ff8b34ca9f6d4e456dbc3b:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json, blob d9ac014355a6a1058cc8a0cf2141a01082628881. Saturation follows from its determinant 17^21, row congruences, and six distinct inverse Vandermonde columns as previously proved.

New zero-based order [8,5,2,0,1,3,4,9,6,7,13,15,10,11,12,14]. Exact max spread N/D:
N=4499962405859179975681503620802131657556552414450801884451136759621202
D=22009362241807629126111895087560945050967640226441506149068904810154599921
floor((D-1)/N)=4891. Thus for A+B<=4891 each descending coefficient interval has width strictly less than 1, including A=B=2331. Every compatible affine target has at most one signed-budget solution; an incompatible target has none. Given a particular representative, the descending exact interval algorithm from the previous note takes at most 16 steps, followed by signed budget checks. It is complete by induction: a feasible coefficient must lie in its interval, earlier rows vanish against the current primitive normal, and each interval contains at most one integer. This also proves homogeneous exclusion of nonzero u at the full budget without the separate q0 argument. No change to higher valuation or rational observer obligations.

Search provenance: deterministic floating proposal search initialized at the previous order, seed 171127, LCG 1664525*x+1013904223 modulo 2^32, 300 pair-swap annealing proposals per round, temperature 0.000012*(1-i/300)+0.0000005. 1200 proposals executed before reaching full-budget threshold. Exact BigInt primitive projection recurrence verified the winner; the heuristic is not used as proof. No optimum claim or live campaign rerun.

Reproduce static certificate (standalone Python, no floating point; same exact recurrence executed in BigInt):
```python
import json, sys
from math import gcd
from fractions import Fraction
C=json.load(open(sys.argv[1]))
B=C['weighted_basis']
P=[8,5,2,0,1,3,4,9,6,7,13,15,10,11,12,14]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
G=[]; R=[]
for i in P:
    b=B[i]; v=b[:]
    for g in G:
        d=dot(g,g); t=dot(v,g)
        v=[d*x-t*y for x,y in zip(v,g)]
        h=gcd(*v)
        v=[x//h for x in v]
    if dot(v,b)<0: v=[-x for x in v]
    assert all(dot(v,B[j])==0 for j in P[:len(G)])
    assert dot(v,b)>0
    G.append(v)
    R.append(Fraction(max(0,*v)-min(0,*v),dot(v,b)))
s=max(R)
assert s==Fraction(4499962405859179975681503620802131657556552414450801884451136759621202,22009362241807629126111895087560945050967640226441506149068904810154599921)
assert (s.denominator-1)//s.numerator==4891
assert 4662*s<1
print(s)
```

Control recovery: original reference request dvr-20261127-1503-t6-rr-c428-reference-p1-v1 terminal FAILED SOURCE_MAIN_CAS_RETRY_LIMIT; no new formal task created per receipt. Same custody session verified. New read-only continuation dvr-20261127-1605-t6-cas-failure-continuation-v1 queued at last read. Preserve original failed receipt; no replay or identity replacement. This note is mathematical evidence only, not native Review/Result acceptance or task closure.
