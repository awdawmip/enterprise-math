# EC49GAB — Exact zero-spine fiber slot-profile scheduling
2026-11-26. Informed independent portable continuation of EC49GAA at 59e27a6a0edb03535b13d3e23b1de57ede2a70a3:research_notes/portable_direct/EC49GAA_WEIGHTED_CAPACITY_AND_RANK_FIVE.md. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; captured ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Local inherited archive SHA256SUMS verified. Exact binary support-hole model W(r,j)=1_{r in U}1_{j notin H}, 10 rows, 25 columns, h=14. This is a finite observation model, not physical dynamics. P000 unchanged. Topic receipt r4-20261126-0030-ec49as-read SUCCEEDED at Source 4472cd8be587a1532fa8fb80a7d134cf9b7d2708 with NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection or shared CLAIM. Historical EM-DIRECT-23537B provenance; current private research binding unconfirmed; Activity pending.

## 1. Exact partition-local slot theorem
Let S be a finite nonempty distinguishable state population with a fixed finite binary unit-cost query family Q. Discard queries constant on S. Let S be partitioned into nonempty blocks B_i. Assume each informative query has at least one answer side contained entirely in one block. Fix an orientation for each query so its local side A_q is contained in that block (the local side can be the original negative side). Orientation is a relabeling of both answers, not an extra physical query. Let d(P)=D(P,P) be exact full identification depth on the conditional population P using all original queries, with singleton depth zero.

For budget k, let F_i(C,l) be the inclusion-minimal masks of slots in {1,...,k} for a chain of oriented local queries, starting at C subset B_i, ending with exactly l residual states, l in {0,1}. At slot t peel P=C intersect A_q nonempty; require t+d(P)<=k, then replace C by C minus P. The slots are strictly increasing. The base is {empty mask} if |C|=l, and empty family if |C|<l. Otherwise the exact recursion is the inclusion-minimal family of {t} union M for every local q with nonempty P, M in F_i(C minus P,l), 1<=t<=k-d(P), and t<min(M) when M is nonempty. A query peeling all of C is allowed.

The full recovery decision D(S,S)<=k is equivalent to existence of one mask M_i in F_i(B_i,l_i) per block with pairwise disjoint masks and sum_i l_i=1.

Proof (necessity): remove constant queries from a complete bounded-depth decision tree. Starting at the root follow the nonlocal answer (complement of the oriented local side) until reaching a singleton. Every traversed query is informative on the current population, so both answers exist. Each peeled positive-side population P belongs to exactly one block and its conditional subtree identifies P at cost at least d(P). Its depth t on the spine therefore obeys the deadline. Other blocks are untouched, and each block's projection of the spine is a valid local chain. The terminal singleton gives sum l_i=1. Actual masks may be reduced to inclusion-minimal feasible masks, retaining disjointness.
Sufficiency: choose local chains realizing the masks. Interleave them in increasing slot order, deleting unused absolute slots (actual depths only decrease). Each peeled population belongs to a single block and is exactly the corresponding local residual intersection, since other blocks' queries cannot modify it on the nonlocal spine. Attach an optimal identifying tree for P to the local answer. Its depth is at most the original assigned slot plus d(P)<=k. The unique terminal residual is a singleton, and ensures no peeled query is constant on the global remaining population. All states are recovered. No target-only projection or lost competitors. The proof allows more than two blocks and any orientation satisfying the hypothesis.

Dominance justification in recursion: if tail mask M' subset M is feasible for the same C and l, min(M')>=min(M) (empty tail imposes no constraint). Any prefix placement feasible before M remains feasible before M'. Thus inclusion pruning is exact, both internally and across disjoint-block merge. Store actual physical representatives for oriented masks when constructing trees; the experiment computes only the optimum feasibility.

Implementation bound: at most 2*sum_i 2^{|B_i|} residual/l subproblems, each with at most 2^k masks; naive transitions at most O(k |Q| 2^k) per subproblem before antichain filtering; naive dominance comparisons O(4^k). Local depth calculations have their own conditional DP cost. Block merge uses at most 2*2^k states, naive mask pairing O(4^k) per block. This is a decomposition, not an unconditional speedup or an asymptotic improvement claim.

## 2. Actual rank-five obstruction explained by scheduling collision
GAA captured observation index 3: 15 states, 2 blocks masks 15 and 32752 (U=23 and 86), k=4. All informative query masks 11,13,14,15,21936,26320,30944,32512,32752. All are raw local. Slot mask bit t-1 denotes absolute spine slot t. Exact minimal families:
- Block 23, leave 0: [1,6,10] = [{1},{2,3},{2,4}].
- Block 23, leave 1: [1,2] = [{1},{2}].
- Block 86, leave 0: [7,11] = [{1,2,3},{1,2,4}].
- Block 86, leave 1: [3] = [{1,2}].
If the terminal singleton is in block 23, every leave-one mask in that block meets every leave-zero mask in block 86. If in block 86, every leave-zero mask of block 23 meets {1,2}. Hence four observations impossible. This is an independent structural witness for the full-node failure (not a new proof of minimal target rank; GAA proved that separately). At k=5 the families are [[[1,2,12,20],[1,2,4]],[[1,14,22],[3,5,6]]], and e.g. block23 leave0 mask1 and block86 leave1 mask6 are disjoint. Exact full depth=5. Thus the obstruction is competition for specific early slots despite 15<=2^4, not just leaf count or independent per-fiber depth.

## 3. Computed scope
Used all 180 previously captured failure-conditioned node records, without re-running fourth-layer closed roots. 43 raw-local two-support nodes; 6 additional three-support nodes become local by answer orientation; 131 nodes do not satisfy this test for the support partition. 49 eligible records include 15 of GAA's rank-five records and 34 rank-two records (not deduplicated or prevalence estimates). Compared feasibility for budgets 0 through each recorded k+1, 281 exact checks, 3256 local profile residual/leave subproblems in total. 160 deterministic generic separable block-local populations with 2..4 blocks and sizes 1..4, including randomized answer orientations, tested at exact depth-1, depth, depth+1: 480 checks. All 761 comparisons matched GAA/FZY full informative-query recurrence. Exact depth of eligible record indices:
0:4,2:5,3:5,5:5,6:5,7:5,8:5,11:4,14:5,15:5,17:5,18:4,20:5,21:5,22:4,24:5,25:5,26:5,27:5,28:6,29:5,30:5,31:5,54:5,61:4,63:5,67:5,76:5,77:4,85:4,90:5,110:5,116:5,126:4,129:5,130:4,132:5,133:5,134:5,135:5,139:4,148:4,161:4,163:5,164:5,171:5,173:4,175:5,176:5.
No new root determinations. Fourth layer retains GAA 1895 YES/27 NO/471 OPEN of 2393, ordered 3831/46/818 of 4695; 25<=M14<=27 unchanged. No overall performance claim; use actual hard-node gating and efficient local depth computation next. Study a bounded separator extension for the 131 mixed-side cases, and adapt slot profiles to designated-target budget (retain all competitors even when targets absent). AUTHOR_PROVED / EXACT_FINITE_SLOT_CHECK / NOT_REVIEWED.

## 4. Reproduction
From GAA reproduction archive (verified inherited SHA256SUMS), save the following exact script as fiber_schedule.py, run python fiber_schedule.py > fiber_schedule.out. Script SHA256 ac5d33593dba35e35eb0826fc9cf1189ecc26fe948461097ed4f47820c0a0452; output SHA256 3696930fe3ed40af2cc35f28f33ad7dbc635d35d3d2c2d06cfe77d55ee2c511d (9556 bytes). Output contains all 49 exact profile sets and reference depths. Uses prior multi_target.py and its physical observation functions, no new model generation for captured records.
```python
from functools import lru_cache
from collections import Counter
import json
from multi_target import model,physical

def schedule(n,qs,blocks,k):
    full=(1<<n)-1
    assert sum(blocks)==full and all(not (a&b) for i,a in enumerate(blocks) for b in blocks[i+1:])
    oriented=tuple(sorted({q if any(q&b==q for b in blocks) else full^q for q in qs}))
    assert all(any(q&b==q for b in blocks) for q in oriented)
    _,_,_,_,ref,_=model(n,qs)
    @lru_cache(None)
    def profiles(s,leave):
        # Profile is a bitmask of absolute slots used on the global zero spine.
        # Last remaining state need not receive a positive answer.
        if s.bit_count()==leave:return (0,)
        if s.bit_count()<leave:return ()
        out=set()
        for q in oriented:
            a=s&q
            if not a:continue
            d=ref(a,a)
            if d>=k:continue
            for tail in profiles(s^a,leave):
                # Put this job as late as feasible, or enumerate all slots.
                end=min(k-d, (tail&-tail).bit_length()-1 if tail else k+1)
                for t in range(1,end+1):
                    # slot t uses bit t-1; strictly precedes earliest tail slot.
                    if tail and (1<<(t-1)) >= (tail&-tail):continue
                    out.add(tail|(1<<(t-1)))
        # A subset slot set is at least as flexible for external interleaving.
        keep=[]
        for a in sorted(out,key=lambda a:(a.bit_count(),a)):
            if not any(b&a==b for b in keep):keep.append(a)
        return tuple(keep)
    p=[[profiles(b,l) for l in (0,1)] for b in blocks]
    # Merge disjoint slot sets, with exactly one terminal state.
    dp={(0,0)}
    for a in p:
        dp={(used|v,leave+l) for used,leave in dp for l in (0,1) if leave+l<=1 for v in a[l] if not used&v}
    return any(l==1 for _,l in dp),p,profiles.cache_info().currsize

def main():
    stats=Counter(); rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*pairs=map(int,line.split()); st=list(zip(pairs[::2],pairs[1::2])); full,qs,_,_,ref,_=model(n,physical(st,10,25))
        blocks=[sum(1<<j for j,(u,h) in enumerate(st) if u==v) for v in sorted({u for u,h in st})]
        raw=all(any(q&b==q for b in blocks) for q in qs)
        if not all(any(q&b==q or (full^q)&b==full^q for b in blocks) for q in qs):stats['nonlocal']+=1;continue
        stats['raw_local' if raw else 'orientation_only']+=1
        stats['local']+=1;stats['fibers_'+str(len(blocks))]+=1
        for budget in range(0,k+2):
            ans,p,c=schedule(n,qs,blocks,budget); expected=ref(full,full)<=budget
            assert ans==expected,(i,budget,ans,expected,p)
            stats['checks']+=1;stats['profile_subproblems']+=c
            if budget==k: rows.append(dict(index=i,k=k,n=n,blocks=blocks,qs=qs,profiles=p,answer=ans,depth=ref(full,full)))
    # Independent generic block-local systems, including feasible instances.
    from random import Random
    rng=Random(16943)
    for i in range(160):
        sizes=[rng.randrange(1,5) for _ in range(rng.randrange(2,5))];n=sum(sizes);full=(1<<n)-1
        blocks=[];off=0
        for size in sizes:blocks.append(((1<<size)-1)<<off);off+=size
        qs=set(blocks)
        for b in blocks:
            for bit in range(n):
                if b>>bit&1:qs.add(1<<bit)
            for _ in range(4):
                q=b&rng.randrange(1<<n)
                if q:qs.add(q)
        qs=tuple(sorted({q if rng.randrange(2) else full^q for q in qs}))
        _,qs,_,_,ref,_=model(n,qs)
        d=ref(full,full)
        for k in range(max(0,d-1),d+2):
            a,_,_=schedule(n,qs,blocks,k);assert a==(d<=k);stats['generic_checks']+=1
    print(json.dumps(dict(counts=stats,rows=rows),sort_keys=True))
if __name__=='__main__':main()
```
