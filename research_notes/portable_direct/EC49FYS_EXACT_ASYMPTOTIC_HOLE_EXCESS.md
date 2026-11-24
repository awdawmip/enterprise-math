# EC49FYS — exact asymptotic hole-excess slope; counterexample to h+2

2026-11-24. Frozen auxiliary Boolean observer BRC16943, same 50 supports as EC49FYN at 0e4e800d1a3f3efa4f58950309aa5fcfb33e4733, research_notes/portable_direct/EC49FYN_TWO_HOLE_UNIFORM_OBSTRUCTION.md (read back). EC49FYQ at ce7abff378aa77006334656fd9396bf9f8666bdf established the stable three-hole law. Here m>h>=1, W(t,j)=1[t in U]1[j not in H], |H|<=h, U in F nonempty; exact labeled recovery, unit noiseless probes. This is an auxiliary support observation model, not a new native X6 attribution.

## New results

Define the integer row multicover number K_F(k)=min sum_t x_t over nonnegative integer x_t with sum_{t in U} x_t>=k for every U in F. For ANY finite family of distinct nonempty supports, Q_h(m)>=m+K_F(h)-h for all m>h. For this frozen family:
K_F(k)=ceil(26k/11) for every integer k>=0;
Q_h(m)>=m+ceil(15h/11) for every m>h>=1.
For m>=K_F(h+1), a constructive bound is Q_h(m)<=m+ceil(15(h+1)/11)+5. Combining with the prior fixed-h stabilization theorem (FYL), the exact asymptotic slope is lim_{h->infty} c_h/h=15/11, where c_h is the eventually constant Q_h(m)-m for fixed h.

The conjecture c_h=h+2 is FALSE for every h>=6: e.g. c_6>=9>8. The previous h=1,2,3 equalities remain unchanged; c_4=6 or larger and c_5=7 or larger remain open. This conclusion changes the scientific target; do not run a c_6=8 existence search. The prior FYN coefficient 15/26 applies to first-touch mismatch, whereas 15/11 is the exact asymptotic excess per allowed hole in the entire adaptive model.

## Proof of uniform lower bound (all-zero path)

Consider any correct decision tree of worst depth m+c. Follow the all-zero path, including the first impossible answer if a zero edge is absent. Let d be prefix length and b(U) the number of distinct columns with at least one queried row in U; these are exactly the forced holes for support U. If b(U)<h, the target (U, forced holes) is legal and compatible. Every one of its m-b(U) live columns needs a future positive query: making that single column an additional hole would otherwise give identical transcript. Thus d+m-b(U)<=m+c and d-b(U)<=c. At d=c+h this is impossible for b(U)<h. If the path ends before that depth, an impossible branch forces b(U)>h for all U, or a correct terminal leaf cannot have a compatible U with b(U)<h (the extra-hole competitor exists since m>h). Therefore some zero prefix of length d<=c+h has b(U)>=h for every U. Count the row multiplicities x_t of its queries; sum_{t in U} x_t>=b(U)>=h, even when queries revisit columns. Hence d>=K_F(h), giving c>=K_F(h)-h. No assumption of distinct queried columns, no finite m cutoff, and no relaxation of actual target identity.

## Exact multicover law

Reuse FYN's integer support weights W: total 26, every row weighted incidence <=11. Summing the constraints gives 26k<=11 sum x_t, hence K_F(k)>=ceil(26k/11). Conversely the table V below supplies exact feasible multisets for k=0..11 at this cost. Write k=11a+r, 0<=r<11. The vector a V[11]+V[r] covers k and has cost 26a+ceil(26r/11)=ceil(26k/11). This is an analytic unbounded construction from finite integer certificates.

## Constructive upper and sharp slope

For m>=K_F(h+1), select a multicover of strength h+1 and order all row-0 copies first. Assign each listed probe to a distinct fresh column. Read until the first positive. A positive must occur, since for the actual U at least h+1 listed probes lie in U, on distinct columns, and at most h are holes. With a known-live column and its positive row t, identify U by an optimal ordinary row decision tree in that same column. The exact finite recursion below gives depth 6 for t=0 and 5 for every other t. Then infer the b forced holes from the prior negative rows that lie in U. Probe one known-positive row in every remaining column except the already-confirmed live column and the b forced holes. This recovers every physical label. If d negatives preceded the first positive, cost is d+1+q_t+(m-1-b)=m+d-b+q_t. For t!=0, the number d-b of misses is at most the total number of scheduled rows outside U, bounded by K_F(h+1)-(h+1); q_t<=5. For t=0, d-b=0 because row-0 probes are first and all preceding row-0 answers are genuine forced holes; q_t<=6. For h>=1 the former upper bound is at least 6. Thus Q_h(m)<=m+ceil(15(h+1)/11)+5. Combined with the uniform lower bound, dividing the stable excess by h gives the exact limit 15/11. For fixed h this does not claim the upper bound is sharp; the additive interval remains to be resolved. It also does not assume a joint limit where m is smaller than K_F(h+1).

## Exact reproducible integer evidence (Python 3)

```python
from functools import lru_cache
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
W=[[86,3],[101,4],[281,2],[394,5],[460,1],[602,3],[673,5],[788,3]]
V=[[0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,1,0],[1,1,1,0,0,0,0,0,1,1],[1,1,0,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,2,1],[2,2,1,0,1,1,1,1,2,1],[2,2,2,0,1,1,1,1,3,2],[3,3,2,0,1,1,1,1,3,2],[4,3,2,0,1,0,2,2,3,2],[3,3,2,0,2,2,2,2,4,2],[4,4,2,0,2,2,2,2,4,2],[6,5,4,1,1,0,1,2,3,3]]
assert len(set(F))==50 and all(0<u<1024 for u in F)
assert all(u in F for u,w in W) and sum(w for u,w in W)==26
hits=[sum(w for u,w in W if u>>t&1) for t in range(10)]
assert max(hits)==11
checks=[]
for k,v in enumerate(V):
    a=sum(v); b=min(sum(v[t] for t in range(10) if u>>t&1) for u in F)
    assert a==(26*k+10)//11 and b>=k
    checks.append((k,a,b))
R=[sum(1<<i for i,u in enumerate(F) if u>>t&1) for t in range(10)]
@lru_cache(None)
def q(a):
    if a.bit_count()<=1: return 0
    return 1+min(max(q(a&r),q(a^ (a&r))) for r in R if a&r and a^ (a&r))
depths=[q(r) for r in R]
assert depths==[6]+[5]*9
print(hits,checks,depths)
```

Executed exact certificate checks in JavaScript BigInt (same recurrence); output hits=[11,11,11,11,11,9,11,11,11,11], checks=[[0,0,0],[1,3,1],[2,5,2],[3,8,3],[4,10,4],[5,12,5],[6,15,6],[7,17,7],[8,19,8],[9,22,9],[10,24,10],[11,26,11]], depths=[6,5,5,5,5,5,5,5,5,5]. The row decision recursion is exhaustive over the 10 row tests and strictly decreases support count on both nonempty branches; integer-only certificate checks cover all 50 frozen masks. Python independent calculation of the row depths also gave [6,5,5,5,5,5,5,5,5,5]. Discovery used a numerical LP/MILP only to locate certificates; no optimizer output is needed for the proof.

## Continuation and provenance

Historical researcher EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76. Current exact topic read r4-20261124-1330-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at 4299fcf0db83ee3332112662b25f5854c078e508; directory observation only, no formal claim. Own recovery metadata confirms historical session not closed/revoked; no new write authority asserted. Previous FYR finite-column result has separate local evidence; this theorem does not depend on its unpublished code or 10-column witness. The 9-column search was rerun locally for 28 seconds; it finished the abstract phase (4,744,482 calls, 886,971 memo entries) but not the finite phase. No new finite-m classification. Next: tighten additive gap by incorporating order-sensitive prefix miss profiles and saturated terminal recovery; solve h=4,5 individually and investigate c_h-ceil(15h/11), periodicity and possible exact bounded corrections. AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
