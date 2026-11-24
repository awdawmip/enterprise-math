# EC49FYX — packed multicover transport and near-sharp phase-5 onset

2026-11-24. Frozen BRC16943 auxiliary Boolean observer, 50 nonempty supports on ten rows, state (U,H), |H|<=h<m, probe W(t,j)=1[t in U]1[j not in H], noiseless unit-cost adaptive queries, exact recovery of both support and labeled hole set. No new native X6 attribution. Parent pins read this turn: b4b38aaa894b6e6906d6037f92b747a7a0dea182:research_notes/portable_direct/EC49FYW_EXACT_STABLE_HOLE_LAW.md (Q4(9)=15, stable law); 1c89f8f765926749601fdcb739fe74b66aefa2c6:research_notes/portable_direct/EC49FYV_TIGHT_PHASE5_PREFIX_CLASSIFICATION.md (phase-5 lower); 438163ba045e2d3ea8d27bbb81004694f5069ae0:research_notes/portable_direct/EC49FYT_EVENTUAL_PERIODIC_EXCESS.md (multicover vectors and q_t). These are author-proved parent-dependent results, not independently reviewed.

## Packed block transport theorem

Let S_1,...,S_N be nonempty row masks placed on N distinct physical columns, with L=sum |S_j| queries. Require b(U)=#{j:S_j intersects U}>=k for every support U. Probe the distinct row/column pairs in an order with all row-0 probes first, stopping at first positive. Suppose on n=m-N>h untouched columns a base h-hole strategy has depth n+c, c>=5. For the frozen family the conditional support identification depth after a positive in a known live column is q_0=6, q_t<=5 for t!=0 (FYT). Then

Q_(h+k)(m) <= m+c+L-k.

Proof: if the first positive is at query i, let b count DISTINCT physical columns hit by rows in U in the preceding zero prefix. They are known holes, and the positive column is distinct from them. Recover U by at most q_t additional probes in the known live column (reuse already known bits if needed). One live and b holes are known; one probe in a row in U on each of the other m-1-b columns recovers all remaining labels. Depth <= m+(i-1-b)+q_t. Since at least k distinct columns are hit in the entire scheduled block and at most L-i+1 further distinct hits can occur, k<=b+L-i+1, hence i-1-b<=L-k. When the positive is row 0, all preceding probes were row 0 on distinct columns, so i-1-b=0. Thus the positive branch costs <=m+max(6,L-k+5), at most m+c+L-k provided L-k>=1 or c>=6. The theorem as used here has c=6; the more general precise bound is m+max(6,L-k+5,c+L-k). If the entire block is zero, at least b(U)>=k of its physical columns are holes. Apply the old strategy on the n untouched columns (at most h holes), obtaining U and all their labels. Recover the remaining block labels by one probe per column not hit by U, count N-b(U). Total <=L+n+c+N-b(U)=m+c+L-b(U)<=m+c+L-k. This proof preserves label and joint observation relations; counting probes instead of distinct hit columns would invalidate it. The construction never invokes the base on a column touched by the block.

## Period block, optimal static packing at minimum query cost

For k=11a, a>=1, take a copies of the FYT multicover vector x=(6,5,4,1,1,0,1,2,3,3), with L=26a. Form 3a shared columns, each with rows {0,1}; put all other row copies on distinct columns. For each U containing both rows the unmerged surplus over 11 is at least 3, attained by 91 and 123 (see code/check table); others lose nothing when packed. Thus all 50 distinct-hit counts >=11a, on exactly 23a physical columns.

This packing is optimal among ALL static blocks of 26a probes meeting distinct-column strength 11a, not merely this vector. FYU dual weights on supports W=(86,101,281,394,460,602,673,788) are (3,4,2,5,1,3,5,3), sum 26; each row load <=11, with row 5 strictly lower. At L=26a the inequalities sandwich the weighted row hit total between 26*11a and 11*26a, so equality forces x5=0, row totals on every weighted support exactly 11a, and no double hit on a weighted support in the same column. Solving the eight equations and x5=0 as in FYV, with free z=x8, gives (6a,5a,7a-z,4a-z,a,0,z-2a,2a,z,3a). The extra nonweighted supports 346,412 have surpluses z-3a and 3a-z; both nonnegative force z=3a. Tight support set is W plus 346 and 412. Every used row occurs in a tight support and every pair of used distinct rows except (0,1) co-occurs in one. Thus no repeated row within a column and no other merging pair or triple. Support 91 has slack 3a; at most 3a pairs allowed. Minimum N=L-3a=23a. This is a statement about static cover blocks at prescribed query cost, not about globally optimal adaptive trees.

Apply the transport theorem with base Q4(9)=15, c=6. For h=4+11a, m>=23a+9 (a>=0), Q_h(m)<=m+6+15a, matching FYU/FYW. Combined with FYV necessary inventory, for a>=1:
23a+8 <= M_(4+11a) <= 23a+9.
Previously upper 26a+9. At a=0 M4=9. In particular M15 in {31,32}, M26 in {54,55}, M114 in {238,239}. The asymptotic minimum physical inventory per hole on this phase is exactly 23/11. The remaining gap of ONE physical column is not resolved. Distinct optimal static terminal prefix of FYV has one further merge available; existence of that prefix does not prove a winning tree.

## All residues, explicit packed block witnesses

For k=11a+r, 0<=r<=10, concatenate a period blocks and one packed r-block; no column sharing between these blocks. The query cost stays ceil(26k/11) and physical columns N=23a+B_r, where B_r=(0,1,4,6,8,10,11,14,16,17,20). Each r-block uses the exact frozen FYT row vector; exact packing within that vector was optimized by enumerating non-singleton column masks and their multiplicities under all 50 slack and 10 row-inventory constraints. This is not claimed optimal across all possible row vectors. Every listed witness preserves row counts and checks every support's distinct-column strength. It gives, for h=4+11a+r, m>=9+23a+B_r:
Q_h(m)=m+ceil((15h+6)/11).
This improves FYW's sufficient inventory 9+ceil(26(h-4)/11), including M5<=10 (one column with rows 0,1,8, rather than three separate columns). It is an exact construction guarantee; individual onset values remain open unless separately bounded. For k=0 just use the base.

## Exact reproduction (Python 3; executed for fixed vectors)

```python
from functools import lru_cache
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
V=[[0]*10,[1,1,0,0,0,0,0,0,1,0],[1,1,1,0,0,0,0,0,1,1],[1,1,0,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,2,1],[2,2,1,0,1,1,1,1,2,1],[2,2,2,0,1,1,1,1,3,2],[3,3,2,0,1,1,1,1,3,2],[4,3,2,0,1,0,2,2,3,2],[3,3,2,0,2,2,2,2,4,2],[4,4,2,0,2,2,2,2,4,2],[6,5,4,1,1,0,1,2,3,3]]
def pack(k,x):
    slack=tuple(sum(x[i] for i in range(10) if u>>i&1)-k for u in F)
    assert min(slack)>=0
    cand=[]
    for s in range(1,1024):
        if s.bit_count()<2 or any(s>>i&1 and not x[i] for i in range(10)):continue
        loss=tuple(max(0,(s&u).bit_count()-1) for u in F)
        if all(a<=b for a,b in zip(loss,slack)):cand.append((s,loss))
    @lru_cache(None)
    def solve(j,r,b):
        if j==len(cand):return (0,())
        s,loss=cand[j]; best=solve(j+1,r,b)
        if all(r[i] for i in range(10) if s>>i&1) and all(a<=v for a,v in zip(loss,b)):
            sc,ms=solve(j,tuple(v-(s>>i&1) for i,v in enumerate(r)),tuple(v-a for v,a in zip(b,loss)))
            sc+=s.bit_count()-1
            if sc>best[0]:best=(sc,(s,)+ms)
        return best
    saved,ms=solve(0,tuple(x),slack)
    r=[x[i]-sum(s>>i&1 for s in ms) for i in range(10)]
    cols=list(ms)+[1<<i for i in range(10) for _ in range(r[i])]
    assert len(cols)==sum(x)-saved
    assert [sum(s>>i&1 for s in cols) for i in range(10)]==x
    assert min(sum(bool(s&u) for s in cols) for u in F)>=k
    return saved,ms,cols,solve.cache_info().currsize
for k,x in enumerate(V):
    if k==0:continue
    s,ms,cols,n=pack(k,x)
    assert sum(x)==(26*k+10)//11
    print(k,sum(x),s,len(cols),ms,n)
```

Actual output (k, query count, saved columns, physical columns, non-singleton column masks, DP states):

```
1 3 2 1 (259,) 19
2 5 1 4 (768,) 8
3 8 2 6 (160, 576) 48
4 10 2 8 (288, 768) 59
5 12 2 10 (3, 288) 28
6 15 4 11 (288, 320, 516, 768) 207
7 17 3 14 (3, 288, 768) 84
8 19 3 16 (3, 3, 320) 27
9 22 5 17 (3, 288, 288, 320, 768) 420
10 24 4 20 (3, 3, 288, 288) 90
11 26 3 23 (3, 3, 3) 8
```

The finite packing proof is exact: each physical column is a subset of distinct rows (repeating an identical query gives no new coverage and cannot occur in a minimum-query block), and its loss on U relative to singleton columns is max(0,|S intersect U|-1). The DP enumerates all feasible multisets of non-singleton masks in ascending index, allowing reuse only while row inventory and every slack remain nonnegative; remaining singleton columns reconstruct the vector. All 550 support/strength checks passed. Separate executed integer check: tight set of period vector [86,101,281,346,394,412,460,602,673,788]; only allowed pair (0,1); surplus among supports containing both is min 3. No new end-to-end large physical decision-tree replay asserted; transport is an analytic proof using the existing base replay.

## Control and next

AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Historical researcher registration EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76 verified original receipt r4-20261124-0240-ec49fyh-own-session-v1 SUCCEEDED. Exact topic query r4-20261124-1830-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at 4e1802f4b2da9eb21e8cc1a8815ad5da72f67152, observed 2026-11-24T10:31:03.807328Z; not a full native owner projection. No shared CLAIM or formal Result/Review. Next: decide whether the single additional cross-boundary (0,1) merge can be realized by a winning adaptive tree, particularly M15=31 vs 32; use joint residual of previously touched base column, not mere static hit counts. Also optimize small-r blocks across row vectors if informative.
