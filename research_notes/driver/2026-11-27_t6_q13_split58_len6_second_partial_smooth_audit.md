# T6 q13 split (5,8), second six-atom negative family: scoped audit and exact maximal-p13 roster reduction

2026-11-27 | EM-DVR-DEBB5E | shared directed research context, not clean-independent decisive review. Original author-side certificate: e314bc304e73ad4aabae7eca6fd934911751cc9b:research_checks/T6_P13_Q13_SPLIT5_8_LEN6_NEG1_1_1_1_2_2_PARTIAL_CERT_20261127.json, Git blob 4b7d08e7ae346b2ccef180a62152f8a38e356c30. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. The original author owns the exact affine search and witness discovery; this note adds an independently structured arithmetic check and counts of the true maximal-prime domain for three reported shards, not a replay or completeness audit of the affine search.

## Scope and count

p=13, valuation exactly one, d=13a with a=13q+r, 1<=r<=12; weight 13a-1. Each signed side has budget 2331. Negative partition (1,1,1,1,2,2) and positive partitions (5), (1,4), (2,3). Since maximal denominator prime is 13, every a must be 13-smooth. The exact admissible r sets for q=1..5 are:
1: [1,2,3,5,7,8,9,11,12]
2: [1,2,4,6,7,9,10]
3: [1,3,5,6,9,10,11]
4: [2,3,4,8,11,12]
5: [1,5,7,10,12].
The negative side maximum raw mass is 4*(13*25-1)+2*(13*38-1)=2282 <=2331; every raw positive tuple of these partitions also fits (maximum mass <=1155). Thus no additional vertical mass filtering changes these counts. The raw negative roster count is C(15,4)*C(13,2)=106470. Smooth negative count C(12,4)*C(8,2)=13860. Cancellation-normalized pairs must have disjoint complete integer-atom supports. Only identical q values can overlap, so a fixed positive q=1 atom removes exactly one of the 9 available negative q=1 residues, or a fixed q=2 atom removes one of 7 negative q=2 residues.

| positive partition | raw pairs | smooth positive rosters | smooth disjoint pairs |
|---|---:|---:|---:|
| (5) | 1277640 | 5 | 69300 |
| (1,4) | 15331680 | 54 | 498960 |
| (2,3) | 15331680 | 49 | 509355 |
| total | 31941000 | 108 | 1077615 |

The second and third exact pair counts are 54*C(11,4)*C(8,2) and 49*C(12,4)*C(7,2). This retains every cancellation-normalized maximal-p13 vertical pair of these exact three partitions, including all possible remaining q0 completions and arbitrary lower-prime completion. It is not a claim that all 1,077,615 pairs have a solution or that their full observables coincide. The raw certificate intentionally allows broader atom values; smooth/disjoint filtering is a necessary restriction for the true maximal-prime model, not a criticism of its superset search. No modification to the active author's program/ownership.

## Reported witnesses

For each witness independently evaluated all six residues modulo 13^k, k=1..6, from positive a, negative a, and q0 coefficient vector u on j=1..12. Each is zero. Recomputed signed full masses (1965,3990), (3680,2820), (1967,3982), matching the author. Each fails at least one signed budget. Non-smooth a values respectively [71], [23,17,17,31], [34]; these also independently exclude the witnesses from maximal-p13. The author reported 3 leaves, 0 budget-valid for the three shards. This note does not independently verify exhaustion, representative-fiber coverage, common-feasible filtering, or any unreported positive partitions.

## Exact local reproducer (executed core)

```python
from itertools import combinations_with_replacement as CWR, product
from math import comb
p=13
B=2331
def smooth(a):
    for f in (2,3,5,7,11,13):
        while a%f==0: a//=f
    return a==1
R={q:[r for r in range(1,13) if smooth(p*q+r)] for q in range(1,6)}
N=[(set(a),set(b)) for a,b in product(CWR(R[1],4),CWR(R[2],2))
   if sum(13*(13+r)-1 for r in a)+sum(13*(26+r)-1 for r in b)<=B]
assert len(N)==13860
for pat,expect in [((5,),69300),((1,4),498960),((2,3),509355)]:
    P=[rs for rs in product(*(R[q] for q in pat))
       if sum(13*(13*q+r)-1 for q,r in zip(pat,rs))<=B]
    n=sum(all(q not in (1,2) or r not in ng[q-1]
              for q,r in zip(pat,rs)) for ng in N for rs in P)
    assert n==expect
W=[
 ([(5,6)],[(1,3),(1,9),(1,11),(1,12),(2,1),(2,4)],
  [30,-2,-3,-19,-2,-2,2,-3,3,-2,-1,1],(1965,3990)),
 ([(1,10),(4,4)],[(1,4),(1,4),(1,12),(1,12),(2,4),(2,5)],
  [2,6,23,4,5,2,-1,-2,3,-5,3,1],(3680,2820)),
 ([(1,8),(4,4)],[(1,5),(1,5),(1,9),(1,12),(2,7),(2,8)],
  [-36,16,-3,-1,-2,-1,-8,0,-2,2,-2,2],(1967,3982))]
for pos,neg,u,m in W:
    P=[p*q+r for q,r in pos]; N0=[p*q+r for q,r in neg]
    assert all((sum(pow(a,-k,p**k) for a in P)
        -sum(pow(a,-k,p**k) for a in N0)
        +sum(v*pow(j,-k,p**k) for j,v in enumerate(u,1)))%(p**k)==0
        for k in range(1,7))
    mass=tuple(sum(p*a-1 for a in z)
        +sum((p*j-1)*max(0,s*v) for j,v in enumerate(u,1))
        for s,z in [(1,P),(-1,N0)])
    assert mass==m and max(mass)>B
    assert any(not smooth(a) for a in P+N0)
```

## Control boundary
Original dvr-20261127-1801-t6-rate-limit-continuation-v1 read SUCCEEDED; its formal HANDOFF frontier still references obsolete q14 preflight, so no old task redelegation. Existing original RR-C428294CF760BD8D99AA bytes reverified via dvr-20261127-1900-t6-rr-c428-current-artifact-v1 (Source 6cdc7b061d6579d6993f2fbc30d396d9a5c29047; SHA256 4d2ebdb11a15bdc1a52a3baca99e8045188bc206414cb3e61b22153171359976). Own SID matched prior flow/registration; fresh flow read dvr-20261127-1900-t6-current-review-flow-v1 submitted, no replay of failed v2 write. No formal acceptance, Task closure, new claim or global T6=2332 claim.