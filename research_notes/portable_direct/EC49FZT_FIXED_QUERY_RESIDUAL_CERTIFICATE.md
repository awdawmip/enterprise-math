# EC49FZT — Fixed-first-query exact residual certificate

2026-11-25. Parent EC49FZS @5349bb6b103a15620ad9866bdcd812efa3ed7635:research_notes/portable_direct/EC49FZS_TIGHT_UNSATURATED_FIRST_QUERY.md. Frozen BRC16943, m=25, h=14, fourth-level budget 15. Parent EC49FZS reproduction archive SHA256SUMS checked; 2393 roots, 1848 YES, 14 NO, 531 open. Topic read r4-20261125-1630-ec49as-read SUCCEEDED at 96ddac0387d0c0dfd6c99aedc14612d143927f47, NO_CANONICAL_PUBLICATION_DIRECTORY, not an owner projection. Historical researcher EM-DIRECT-23537B, current private binding unconfirmed; independent portable work, no shared CLAIM/Result/Review or new identity. P000 unchanged.

## Exact theorem
Let X be any finite family of pairs x=(U,H) with common active anchor row r0 and common normal anchor column j0. Query W(r,j)=1_{r in U}1_{j not in H}. For fixed target x and rivals Y subset X minus {x}, let R_r be rivals differing from x on the anchor-column query (r,j0); L_j be rivals differing on the anchor-row query (r0,j). For row set T and column set S, define
c_x(T,S)=|T minus U|+|S intersect H|+max(|T intersect U|,|S minus H|).
Define K_x(Y)=min c_x(T,S) subject to Y subset (union of R_r for r in T) union (union of L_j for j in S). Empty Y costs zero. This equals the minimum number of arbitrary physical queries needed to distinguish x from Y, with queries selected for the x path (not the optimal adaptive depth for all x).
Proof: Realize chosen negative row/column features singly using anchors, and pair positive rows with positive columns; remaining positive features use anchors. The paired AND has positive target outcome, and excludes the union of the paired row and column disagreement sets. This uses at most c_x queries. Conversely, any positive target query covers exactly the union of its two features; any negative target query is dominated by one negative feature (if both factors are zero, either negative feature suffices). Normalize every query in a certificate this way. Counting distinct features gives c_x at most the original certificate length. These inequalities establish equality, independently of a fiber interval hypothesis.

For physical query q let D_x(q)={y in X minus {x}:W_q(y) differs from W_q(x)}. The exact minimum x-path certificate length with prescribed first query q is 1+K_x((X minus {x}) minus D_x(q)). Indeed, after q, exactly those rivals remain; the common anchor survives. This gives an exact necessary first-query set for budget k:
P_k(x)={q:K_x((X minus {x}) minus D_x(q))<=k-1}.
Any depth-k adaptive strategy must choose q in intersection over x of P_k(x). This is not sufficient for an adaptive tree. In particular a saturated target can use the FZO optimizer on its q-conditioned fiber (not just the unconditioned fiber), with actual forced holes and active supports updated. Retain physical q and its joint disagreement set before doing the quotient; negative AND queries with both target factors zero may exclude a joint subset not represented by a single equality. Thus the theorem extends FZS to saturated and arbitrary anchored targets without discarding that joint observation.

Further necessary rule: for a tight x (K_x(X minus {x})=k), if a doubly negative q=(r,j), r notin U, j in H, belongs to P_k(x), then both anchor replacements (r,j0) and (r0,j) belong to P_k(x). Each excludes a superset of D_x(q), so each yields a certificate of length at most k by replacing the first query. If j is a free missing column in the target fiber (H minus B_U, with the interval fiber hypothesis), q is impossible in a tight certificate: the rival (U,H minus {j}) requires another query (s,j) with s in U; replace that other query by the stronger anchor-row query (r0,j) and drop q. This yields a certificate of length at most k-1, contradiction. Applies to saturated as well as unsaturated states. For arbitrary anchored subsets a blanket exclusion of doubly negative q is false: X={(U={0},H={1}),(U={0,1},H=empty)} with anchor (0,0); q=(1,1) alone distinguishes the states. This two-state example is not asserted to be an attainable frozen history.

## Independent finite check
The following exact Python program uses explicit rivalry masks and a separate exhaustive query-cover dynamic program, compared against row/column-feature enumeration after each possible prescribed query. Small complete anchored history populations (3x4 h=2, 4x4 h=2, 4x5 h=3), 100 seeded histories per shape, up to 3 targets/history. Output: 882 targets (541 unsaturated, 341 saturated), 14124 fixed-query comparisons, no assertion failures. No doubly-negative optimum observed in this sampled genuine-history population; this is not a universal exclusion theorem. The fixed-first-query oracle is not yet integrated into the BRC16943 adaptive solver.
```python
"""Exact anchored query-certificate oracle; independent finite check, not BRC16943 classification."""
from itertools import combinations
from functools import lru_cache
from random import Random
from collections import Counter

# Bits r0=j0=0 fixed to active and normal. Small anchored histories from complete states.
def obs(x,r,j): return bool(x[0]>>r&1) and not bool(x[1]>>j&1)
def submasks(n): return range(1<<n)
def oracle(states,x,nr,nc):
    rivals=[y for y in states if y!=x]; full=(1<<len(rivals))-1
    masks=[]
    for r in range(nr):
        for j in range(nc):
            masks.append(sum(1<<i for i,y in enumerate(rivals) if obs(y,r,j)!=obs(x,r,j)))
    @lru_cache(None)
    def brute(e):
        if not e:return 0
        bit=e&-e
        return min(1+brute(e&~m) for m in masks if m&bit)
    # Independent feature sets: row and column literal observations, then pair positive ones.
    rows=[masks[r*nc] for r in range(nr)]
    cols=masks[:nc]
    u,h=x; rm=(1<<nr)-1; cm=(1<<nc)-1
    configs=[]
    for t in submasks(nr):
        c=0
        for r in range(nr):
            if t>>r&1:c|=rows[r]
        for s in submasks(nc):
            cov=c
            for j in range(nc):
                if s>>j&1:cov|=cols[j]
            cost=(t&~u).bit_count()+(s&h).bit_count()+max((t&u).bit_count(),(s&~h).bit_count())
            configs.append((cost,cov))
    def feat(e):return min(c for c,v in configs if e&~v==0)
    assert brute(full)==feat(full)
    k=brute(full); allowed=[]
    for q,m in enumerate(masks):
        assert brute(full&~m)==feat(full&~m)
        if 1+feat(full&~m)==k: allowed.append(q)
    # A tight minimum cert containing a doubly negative q permits both stronger replacements.
    for q in allowed:
        r,j=divmod(q,nc)
        if not(u>>r&1) and h>>j&1:
            assert r*nc in allowed and j in allowed
    return k,allowed

def main():
    rng=Random(16943); totals=Counter(); example=None
    for nr,nc,hmax in [(3,4,2),(4,4,2),(4,5,3)]:
        allx=[(u,h) for u in range(1,1<<nr,2) for h in range(0,1<<nc,2) if h.bit_count()<=hmax]
        for trial in range(100):
            x=rng.choice(allx); states=allx[:]
            for _ in range(rng.randrange(0,6)):
                r,j=rng.randrange(nr),rng.randrange(nc)
                states=[y for y in states if obs(y,r,j)==obs(x,r,j)]
            if len(states)<2:continue
            for x in rng.sample(states,min(3,len(states))):
                k,a=oracle(states,x,nr,nc);totals['targets']+=1;totals['saturated' if x[1].bit_count()==hmax else 'unsaturated']+=1;totals['fixed_queries']+=nr*nc
                for q in a:
                    r,j=divmod(q,nc)
                    if not(x[0]>>r&1) and x[1]>>j&1:
                        totals['tight_double_zero']+=1
                        if example is None:example=(nr,nc,hmax,states,x,k,(r,j))
    print(dict(totals));print('first_double_zero_example',example)
if __name__=='__main__':main()
```

## Frozen fourth-level branch progress
Reused unchanged parent tight.cpp, compiled g++ -O3 -std=c++17. Extend retry_s.py files list after r3.csv by s.csv,s2.csv,s3.csv and change len(ids)==578 to len(ids)==531. Run python retry_t.py 0 12 200000 and feed solver; no already decided root revisited. Crosscheck four new NO roots using unchanged union.cpp at cap 250000, regenerate inputs from fourth.json and gen.physical. All four independently exhausted by predecessor implementation (cross-algorithm author check, not independent review).
New 6 YES, 4 NO, 2 open; 1,733,015 calls, 8,585 physical-label replays, 44,896 envelope prunes; elapsed 21.18 s for main batch. Totals 1854 YES,18 NO,521 open; ordered 3741 YES,34 NO,920 open. Inventory still 25<=M14<=27. No speed claim; new theorem not integrated. Raw data (root,n,status,calls,envelopePrunes):
```csv
1529,1237,0,200001,1109
1732,1401,-1,102950,3625
1744,1410,1,101291,2620
1745,1411,1,121941,1331
1758,1427,1,189172,2832
1760,1427,1,193940,6898
1761,1432,-1,116505,4840
1762,1432,-1,116505,4840
1763,1432,-1,184241,5213
1773,1451,0,200001,5744
1778,1453,1,100519,3167
1781,1457,1,105949,2677
```
Predecessor NO crosscheck:
```csv
1732,1401,-1,105767,6418
1761,1432,-1,120227,8451
1762,1432,-1,120227,8451
1763,1432,-1,186376,7329
```
Next: implement fixed-query certificate oracle for saturated targets using FZO after exact child transition; exploit free missing column exclusion and evaluate cost on small remaining-budget nodes. Preserve all 1872 classified roots, continue 521 open. Current Activity linkage pending actual own binding. AUTHOR_PROVED / EXACT_FINITE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
