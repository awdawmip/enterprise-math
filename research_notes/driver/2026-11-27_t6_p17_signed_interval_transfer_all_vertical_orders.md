# T6 p17: exact signed-interval transfer to every nonzero vertical order

2026-11-27. EM-DVR-DEBB5E; same lane, author-side method transfer. Original RR author EM-T6SM-B134BD and original p17 q0 certificate remain immutable. Shared context; this is not a nonauthor review of the Driver's prior method. No live campaign or historical finite census rerun.

## Statement and proof

For the valuation-one maximal-p17 carrier, write d=17(17q+r), 1<=r<=16, q>=0. After higher valuations have been separately cleared and common atoms canceled, define the residual q0 congruences sum_{j=1}^{16}u_j j^{-k}=y_k (mod 17^k), k=1,...,6, and signed budgets A,B<=2331 with weights W_j=17j-1. Each nonzero vertical roster uses at least one atom with q>=1, costing at least 17*18-1=305; hence A+B<=4357. For every arbitrary affine target with this residual cap, there is at most one feasible integer completion. The solution or certified absence is determined by at most 16 exact integer interval steps and the final two signed mass checks.

Use the frozen saturated basis from 996ddf75043e981b87ff8b34ca9f6d4e456dbc3b:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json, blob d9ac014355a6a1058cc8a0cf2141a01082628881. Independent BigInt Bareiss determinant and all 96 row congruences verified, det magnitude 69091933913008732880827217. Surjectivity to the mixed moduli follows by the six distinct nonzero inverse Vandermonde columns modulo 17, lifting to 17^6; hence the verified index proves saturation. Weighted rows match the frozen certificate exactly. Reorder by zero-based permutation [0,15,1,14,4,13,3,2,9,6,8,10,5,11,7,12]. A finite floating proposal search over 12000 permutations yielded this order; only the following exact certificate is used for the proof (no optimality claimed).

For the weighted rows b_i take a primitive integer normal g_i parallel to the exact Gram–Schmidt vector, with d_i=<g_i,b_i>>0. Set l_i=min(0,min g_i), h_i=max(0,max g_i). For v=Wu the signed budget gives A*l_i-B*h_i<=<g_i,v><=A*h_i-B*l_i. Descend from i=15, subtract the contribution of the particular weighted vector plus already fixed later rows. Earlier rows vanish against g_i. The permitted integer row coefficient interval is [ceil((A*l_i-B*h_i-<g_i,v>)/d_i), floor((A*h_i-B*l_i-<g_i,v>)/d_i)]. Its width is (A+B)(h_i-l_i)/d_i. Exact maximum spread s=19969401/91577936786, so 4357*s<1, and even A+B<=4585 suffices. Every step is forced or infeasible; induction plus final signed checks proves exact completeness. For q0 homogeneous target, the already frozen static GS exclusion remains applicable. Thus all actual valuation-one vertical orders admit either the earlier q0 proof or this new nonbranching solver. Arbitrary nonzero affine targets at the full 4662 cap may require branching: the path bound here is 8, not uniqueness. Higher valuation cancellation and all rational observers including H0 are separate obligations.

Original basis order strict integer cap 3829, path bound at full cap 16; new cap 4585, full-cap path bound 8. New bound at 4357: 1. No claim that any bound is attained.

## Executed checks

{
  "sourceBlob": "d9ac014355a6a1058cc8a0cf2141a01082628881",
  "determinant": "69091933913008732880827217",
  "rowCongruences": 96,
  "original": {
    "n": "96776889",
    "d": "370559959288",
    "strictIntegerCap": "3829",
    "paths4662": "16",
    "paths4357": "4"
  },
  "permutation": [
    0,
    15,
    1,
    14,
    4,
    13,
    3,
    2,
    9,
    6,
    8,
    10,
    5,
    11,
    7,
    12
  ],
  "optimized": {
    "n": "19969401",
    "d": "91577936786",
    "strictIntegerCap": "4585",
    "paths4662": "8",
    "paths4357": "1"
  },
  "tests": 512,
  "known": 256,
  "feasible": 256,
  "mismatch": 0
}

The 512 cases use deterministic seed 171127, both full and reduced budgets (A=2331 or 2026, B=2331); 256 generated feasible vectors plus 256 arbitrary representative vectors with coordinates in [-5000,5000], each shifted by an integer combination of the original kernel rows. Exact old-order branching and new-order interval enumeration returned identical sorted solutions. This is regression evidence; the universal assertion follows from the static proof. It is not a new census of vertical rosters.

## Reproduce exact static certificate

Use the frozen unweighted_basis matrix; this self-contained Python integer/Fraction certificate verifies the basis, normals and bound. The tested BigInt orthogonal construction uses the equivalent primitive integer projection recurrence. 
```python
from fractions import Fraction as F
from math import gcd, prod
from sympy import Matrix
import json, sys
C=json.load(open(sys.argv[1]))
U=C['unweighted_basis']
p=17; W=[17*j-1 for j in range(1,17)]
assert abs(Matrix(U).det())==17**21
assert all(sum(x*pow(j,-k,17**k) for j,x in enumerate(row,1))%17**k==0 for row in U for k in range(1,7))
B=[[x*w for x,w in zip(row,W)] for row in U]
assert B==C['weighted_basis']
def certificate(P):
    G=[]; R=[]
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    for i in P:
        b=B[i]; v=b[:]
        for g in G:
            d=dot(g,g); t=dot(v,g)
            v=[d*x-t*y for x,y in zip(v,g)]
            v=primitive(v)
        if dot(v,b)<0: v=[-x for x in v]
        assert all(dot(v,B[j])==0 for j in P[:len(G)])
        G.append(v)
        R.append(F(max(0,*v)-min(0,*v),dot(v,b)))
    s=max(R)
    return s, (s.denominator-1)//s.numerator, prod(int(4662*r)+1 for r in R)
def primitive(v):
    g=gcd(*v)
    return [x//g for x in v]
old=certificate(list(range(16)))
new=certificate([0,15,1,14,4,13,3,2,9,6,8,10,5,11,7,12])
assert new==(F(19969401,91577936786),4585,8)
assert 4357*new[0]<1
print(old,new)
```

## Scope and continuation
No new native Result, Task completion, or parent closure. This is a method reference for future eligible audit or lower-prime/vertical work, not an instruction to rerun completed p17 or interrupt a frozen active researcher. Prior p13 and lower-prime transfer remains at 996ddf75043e981b87ff8b34ca9f6d4e456dbc3b. Current p17 reference and p13 results retain actual contribution history.
