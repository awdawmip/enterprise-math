# T6 q13 multiple-common-atom fiber audit and completed-child rebase

Author: EM-DVR-DEBB5E (shared control context, independent counting algorithm; not independent reviewer of own earlier work). Scope: 18 newly returned rows, negative patterns (1,1,1,4) (all 11) and (1,1,2,3) (first 7). Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; p=13, valuation=1, split=(6,7), each side budget 2331. No task claim, kernel rerun, Result acceptance or parent closure.

## Exact product formula

For a q group, let a,b be positive and negative multiplicities and n the number of allowed residues. Here multiset coordinates are (q,r), 1<=r<=12, denominator 13(13q+r), cost 13(13q+r)-1. Define M(n,k)=binom(n+k-1,k), with M(n,0)=1 and M(0,k>0)=0. Define D(n,a,b) for ordered disjoint-support multisets:
D(n,0,b)=M(n,b);
D(n,a,b)=sum_{s=1..min(n,a)} binom(n,s) binom(a-1,s-1) M(n-s,b), for a>0.
Choose the support and positive compositions on it, then the negative multiset in its complement.

Cancel the coordinatewise minimum of multiplicities. The difference vector uniquely recovers the two disjoint-support remainders, and their sizes a-c,b-c determine common multiplicity c in that group. Conversely any such remainder extends to the original pattern by inserting an arbitrary common multiset of size c (when n>0; all used n are positive). Thus the exact counts for a pair of partitions are
raw = product_q M(n_q,a_q) M(n_q,b_q);
common = raw - product_q D(n_q,a_q,b_q);
representatives = product_q sum_{c=0..min(a_q,b_q)} D(n_q,a_q-c,b_q-c).
This handles multiple common atoms, multiple groups, and repeated atoms; unlike subtracting one common atom, no overlap double-counting occurs. In each fiber the cancelled multiset of size c has M(n_q,c) choices, with unchanged observer congruences. Reinsert c copies of the cheapest allowed residue in each group to minimize both side costs simultaneously. This is a valid multiset; it cannot change the difference. Consequently if the minimal representative fails either budget for a given low-prime completion then every member of that fiber fails. No assertion about whether the author's kernel actually chose the cheapest representative.

For the relaxed roster n_q=12. For true maximal-p13 cofactor smoothness q=1..6, n=(9,7,7,6,5,5); all raw vertical sides satisfy the standalone budget, since cost <169(q+1), sum q<=7 and length<=7, giving cost <= 7*(169+156-1)=2268 for q=1 repeated and no greater for other patterns (more directly cost<=169q+155 per atom). The counts are pre-completion, not full observer closure.

## Executed audit

Source certificates:
- ea8ca574a52920b1c9ec11956765995025d2f472: research_checks/T6_P13_Q13_SPLIT6_7_LEN4_NEG1_1_1_4_PARTIAL_CERT_20261128.json (blob 1ec1ef0b741ec69b2eed30884c70627d992e1c46)
- 885da53726b0479eae7c6c52d3d12ba551d6d870: research_checks/T6_P13_Q13_SPLIT6_7_LEN4_NEG1_1_1_4_EXTENSION_CERT_20261128.json (blob 9921b2e253f2a03fef6dc6334642ae2f1e6533f3)
- d31f2c86e96ce4bd9e6839820c63bd6c021b241c: research_checks/T6_P13_Q13_SPLIT6_7_LEN4_NEG1_1_2_3_PARTIAL_CERT_20261128.json (blob 2362d610d22deacb437b51eb240b870d46882ae1)

All 54 count fields match. Relaxed totals (raw, common, representatives)=(224394144,109942176,121771272); smooth totals=(11717595,6675957,5615241). Scope: per-pattern representatives, not distinct vectors across all patterns. Author kernel coverage remains author-executed, not independently rerun.

One witness from extension certificate: positive [(1,1),(1,3),(1,4),(1,5),(2,6)], negative [(1,2),(1,6),(1,7),(4,1)], u=(-83,-5,-4,-1,2,-2,9,1,-1,1,2,1). Executed exact modular inverse calculation: for k=1..6, sum u_s*s^(-k) + sum_pos(13q+r)^(-k) - sum_neg(13q+r)^(-k) mod 13^k = (0,0,0,0,0,0). Side masses with weights 13s-1 and vertical cost above = (2865,2981), both fail 2331; cofactors 17,19,53 also violate maximal-p13. Not a full collision.

## Reproduction (pure Python)

```python
from math import comb
from collections import Counter
from itertools import product
def M(n,k):
    return 1 if k==0 else comb(n+k-1,k) if n>0 else 0
def D(n,a,b):
    if a==0: return M(n,b)
    return sum(comb(n,s)*comb(a-1,s-1)*M(n-s,b)
               for s in range(1,min(n,a)+1))
def calc(a,b,ns):
    a,b=Counter(a),Counter(b)
    raw=dis=rep=1
    for q in range(1,7):
        n,x,y=ns[q-1],a[q],b[q]
        raw*=M(n,x)*M(n,y)
        dis*=D(n,x,y)
        rep*=sum(D(n,x-c,y-c) for c in range(min(x,y)+1))
    return raw,raw-dis,rep
pos=[(1,1,4),(1,2,3),(1,5),(2,2,2),(2,4),(3,3),(6,),
     (1,1,1,1,1,1),(1,1,1,1,2),(1,1,1,3),(1,1,2,2)]
rows=[((1,1,1,4),s) for s in pos]+[((1,1,2,3),s) for s in pos[:7]]
for ns in [(12,)*6,(9,7,7,6,5,5)]:
    print(tuple(map(sum,zip(*(calc(a,b,ns) for a,b in rows)))))
```

## Formal control correction

Original synthesis dvr-20261128-0100-t6-scoped-synthesis-v1 SUCCEEDED; RVS-CB68113DFE8202D7F2D1, Source ba127542afbf1a083d5c75ed9ad2ff69e11305c0, exact readback blob c9b3b7b6e110767ffce347f408654fe72a68e4e7. Nonterminal RETURN_TO_OWNER, not Result acceptance. Preserve immutable synthesis, but its q14 plan-unresolved statement was corrected in previous journal and its operational destination is historically completed, not executable. Original child query dvr-20261128-0100-t6-existing-child-owner-v1 SUCCEEDED: publication TP2-26869C0B4D63A6BB761D, state DONE, dispatch COMPLETE, Result RR-81586AD70E1CEA1B7140, accepted terminal DR-A550BA4AE2C2C51AA899. Actual current-main Result blob 480accec3a57c91de95c8ead7ea43c1d3b8823af and review blob 56cd3cb5caf3712cb75f978736b9b88a142c8783 read. Result PASS/SATISFIED: 12 EMPTY + 4 OUTSIDE, only q1 child. Researcher EM-T6-B4F89F and reviewing Driver EM-DVR-4CF7AF retain credit. No re-claim or new q1 task. No new Result or Task accepted by this round. Existing q14 alternative full-observer proof still needs genuine nonauthor review, not a replay of old campaign. Parent T6 still open. Current contract does not provide an immutable synthesis edit route; this append-only correction is not a replacement native synthesis or a new task. Canonical portfolio dispatch requested dvr-20261128-0203-post-child-closure-dispatch-v1; do not repeat while in flight.
