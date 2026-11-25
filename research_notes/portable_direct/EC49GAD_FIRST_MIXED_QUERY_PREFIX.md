# EC49GAD — First mixed-query interruption of exact fiber-slot profiles

2026-11-26, independent informed portable continuation of EC49GAC. Parent note d2bad72b03489fee74f404db1810bc5449a72838:research_notes/portable_direct/EC49GAC_WEIGHTED_FIBER_SLOT_CAPACITY.md; parent artifact commit dba0019d55987affcc59f926b6ed9c3811bea8df. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Parent GAC archive SHA256SUMS verified. Same finite support-hole model W(r,j)=1_{r in U}1_{j notin H}, 10 rows, 25 columns, h=14. P000 unchanged. Topic read r4-20261126-0229-rs-ec49as-read SUCCEEDED at Source 859ea23cc674a817937582d8a7298a7122eca3d6: NO_CANONICAL_PUBLICATION_DIRECTORY (not an owner projection). Historical EM-DIRECT-23537B; current private binding and Activity association unconfirmed. No shared CLAIM.

## Theorem

S finite nonempty distinguishable by fixed binary unit-cost queries Q, partition B_i, nonnegative weights w and horizon k. V_d(C) is the GAA/GAC optimum short-leaf weight on full conditional population C, using all physical queries. Classify each nonconstant q at S as local if an answer side A_q lies in a single B_i, and choose one such orientation once; otherwise q is mixed. Classification fixed at S (even if a mixed query becomes local later). Follow complement answers of oriented local queries until the first initially mixed query, or stop. A local peel P=C_i intersect A_q at absolute slot t credits V_{k-t}(P) and changes C_i to C_i minus P. Store the full terminal residual C_i and occupied slot mask M_i, not merely its cardinality. Let Z_i(M_i,C_i) be the largest summed credit attainable by a chain starting at B_i with these exact slot and residual data, including empty chain. Merge pairwise disjoint masks M_i; retain union residual C and union mask M. Only nonempty C and contiguous M={1,...,ell} are needed. Z=sum Z_i. Set terminal bonus b(C)=w_x for C={x}, zero otherwise. Define H_d(C)=max over initially mixed q informative on C of V_{d-1}(C intersect q)+V_{d-1}(C minus q) for d>=1; omit this option if no such q or d=0. Then

V_k(S;w) = max_{merged profiles} [ Z + max(b(C), H_{k-ell}(C)) ].

Proof: Take any optimal full tree truncated at k, remove constant queries, and follow the oriented complement path until its first initially mixed query or truncated terminal. Each local peel is confined to a block and contributes at most V_{k-t}(P), even when its branch itself uses mixed queries. The block subsequences produce valid profiles whose masks form a contiguous prefix and whose union is the actual nonempty conditional population. The mixed query splits that population into both full conditional populations; their best possible short-leaf credits are exactly the two terms of H. At a terminal its contribution is precisely b(C). This bounds the optimum above by the profile formula. Conversely interleave any realizing local chains in mask order. Each peel nonempty and final residual nonempty imply every query is informative on the current union population. Attach trees attaining V_{k-t} to peeled branches. At the interruption attach the selected mixed query and two optimal conditional trees, or complete the terminal arbitrarily. Credits are disjoint and nonnegative, so the realized total is at least the formula. Equality follows. All zero-weight competitors remain. No constant query or empty complement is required; actual early singleton may terminate immediately. A contiguous prefix suffices by the optimal-tree construction; no need to assume arbitrary mask gaps are harmless at fixed interruption time.

Local recursion starts with (M=0,C=current residual,Z=0); for each nonempty peel a and slot t >= earliest, extend a tail on residual minus a at earliest t+1, adding V_{k-t}(a) and bit t-1. Equal exact (mask,residual) keys retain maximum credit. Merge similarly. Retaining only capped residual cardinality as in GAC is not sufficient for this formula because the mixed query acts on the actual members. A safe optional compression would need preservation of all later continuation values; not asserted here.

This is an exact separation of the local prefix, not a complexity improvement claim. Local profiles have at most 2^k * 2^{|B_i|} keys per recursion state, at most (k+1)*2^{|B_i|} recursion states per block, naive merge at most 2^k*2^{|S|} keys and quadratic pairing. Conditional V evaluation still needs its own exact subset-depth recurrence. The implementation uses that recurrence for conditional continuations and the reference; the prefix equality is a distinct decomposition but shares that primitive. Can recursively invoke the hybrid method after interruption, with a new conditional partition; cost/benefit of such recursion remains open.

## Actual finite evidence

All 131 previously nonlocal GAA failure-conditioned records, unchanged frozen inputs. For each: full indicator, saved deletion-minimal witness indicator, every one-target deletion, seeded integer weights 0..5. 727 comparisons against unrestricted value recurrence, plus 120 seeded synthetic comparisons; all agree. 26,460 local profile subproblems, 59,895 contiguous merged records, 179,498 mixed continuation evaluations (frozen cases); max intermediate merge size 1,037. Second execution byte-identical. All 107 rank-two and 24 rank-five recorded witnesses have value rank-1; every deletion value rank-1. Not an independent new witness search. 105 frozen weighted cases have lower value if initially mixed queries are prohibited on the complement spine (peeled subtrees remain unrestricted). 7 cases have lower value even if first mixed query is allowed at root, in addition to all no-mixed-spine strategies. Cases (index, test index, exact, restricted): (74,0,14,13), (87,7,38,36), (89,7,49,47), (93,0,14,13), (93,7,40,37), (136,0,10,9), (136,4,25,24). Three are full-indicator cases. These establish that requiring a mixed query first or never along the local complement spine is not exact even in this frozen input. No claim of global root classification or faster search.

Representative index 74: k=4, n=16, blocks masks [15,16,65504], physical signatures [14,16,27,29,31,43872,52640,61888,65024,65504,65520]. Oriented local signatures [14,15,16,43872,52640,61888,65024,65504], mixed signatures [27,29]. Full weights 1. First peel local 65024 contributes 7 in budget 3, complement residual 511. Next query 29 (initially mixed), splitting 511 into 29 and 482; remaining budget 2 gives capacities 4 and 3. Hence 14. Mixed first at root gives only 8 for either mixed query, no-mixed-spine optimum 13, full optimum 14. Exact states: [[101,33529344],[101,33512960],[101,33504768],[101,33496576],[613,33529344],[753,33552384],[753,33551360],[753,33550848],[753,33550336],[753,33549312],[753,33548800],[753,33548288],[753,33547776],[753,33547264],[753,33546752],[753,33546240]].

Compact lossless value evidence for all 727 frozen test records: decode base64 then zlib; bytes in original row/test order are quadruples (exact,reference,no_mixed,mixed_first_or_none), SHA256 e21262eb7cece9d24771146095de52edad65e26f6552ca5803e2ef353ca591be. The frozen row/test ordering and weight vectors are generated by exact source below. Full original JSON output (177634 bytes) SHA256 45231749cdc9f1ac8c9a75efa4314b9361504a2be00f97b56f7f5b3a5fd81d3b; full output retained in the local reproduction package.

eNqVlutu2zAMhRs0GBznsnXdWt9lWfEtTtv1/V+uh0iHOUeM6n1A/pyIIkVSlKMoilYzfoENmGu/wTcw1xIQKbasZWAP1jcYQej/M+A9C8BaCrbbzXauVVVRsVYUacHaOPYjn09i0vzyugfA63IQOpPkhHP8CFgrwW632c21pikb1qapmdhW6sNaBUJxvQLe+3y2Z9ZOJ3uK4018HWteLtGeAcelaZLrpevYhzGl4Zg1raqySut1re6Hw/5wna37z9963XVtp+WaNak7989PwP6kRkv67Ku7NQEtXzjLTRsHQntqd++rvmqA39t5qeVsSX4M8OvxD2tryzayj25zqWPXuSPHc9vmwvv721tozyPQeiCU/2FoW63vOS8yL/iMsi7Up9M0TqF42/bYxnEUX/dLot5DXmdMZvge/gBsK28Er0vTJPXnxNPzEluZ8UtnxxK/0lvazGJN5oQ2c30fqefD2sr6fiuz5I39Dnid5JnXPQGuUZI8Jpgs+9XqbvX359yDY1uZNRyf1m8XH9c5QE4Tju8AtDdSe8NDc0TyEfr/BbBvyZcWN6/bAS3XIX890OZMyKYF/P1R16Zmre9dz+/VMNiB1w1D42kyW9m2rrOa+1VqoM28UPwW/G9OpG6cb6m1VpfQ3vI+8FmdM047f2ifP4Bt8jzx+lG+v/y9M0/T7q7coQ80wVn5

No new fourth-layer root determinations; inherited GAC counts 1895 YES / 27 NO / 471 OPEN of 2393, ordered 3831/46/818 of 4695, 25<=M14<=27. Next: compare recursive hybrid against unrestricted recursion including preprocessing cost, explore exact coarsenings or retained mixed-query signature profiles. Continue remaining root computations without replaying completed ones. AUTHOR_PROVED / EXACT_FINITE_MIXED_PREFIX_CHECK / NOT_REVIEWED.

## Reproduction

Save the code below as mixed_prefix.py in verified EC49GAC archive directory; run python mixed_prefix.py > mixed_prefix.out. Script SHA256 0baac56fa72cef4e23cbb08f82113995f2590834f8b825c625162f201a16ad3d. Dependencies are existing multi_target.py, capacity_rank.out, ga_nodes.txt and inherited imports.

```python
from functools import lru_cache
from collections import Counter
from random import Random
import json
from multi_target import model, physical

def solve(n, qs, blocks, k, w):
    full=(1<<n)-1
    local=[]; mixed=[]
    for q in qs:
        sides=[a for a in (q,full^q) if any(a&b==a for b in blocks)]
        if sides: local.append(min(sides))
        else: mixed.append(q)
    local=tuple(sorted(set(local)))
    @lru_cache(None)
    def v(s,d):
        if not s:return 0
        if s.bit_count()==1:return w[s.bit_length()-1]
        if not d:return 0
        return max(v(s&q,d-1)+v(s&~q,d-1) for q in qs if s&q and s&~q)
    @lru_cache(None)
    def prof(s,start):
        out={(0,s):0}
        for q in local:
            a=s&q
            if not a:continue
            for t in range(start,k+1):
                gain=v(a,k-t)
                for (m,c),z in prof(s^a,t+1).items():
                    key=(m|1<<(t-1),c)
                    out[key]=max(out.get(key,-1),z+gain)
        return out
    dp={(0,0):0}; peak=1
    for b in blocks:
        nxt={}
        for (m,c),z in dp.items():
            for (u,r),y in prof(b,1).items():
                if m&u:continue
                key=(m|u,c|r)
                nxt[key]=max(nxt.get(key,-1),z+y)
        dp=nxt;peak=max(peak,len(dp))
    best=nomix=first=0; mixed_evals=0; contiguous=0
    for (m,c),z in dp.items():
        if not c or m&(m+1):continue
        contiguous+=1
        t=m.bit_count()
        stop=z+(w[c.bit_length()-1] if c.bit_count()==1 else 0)
        nomix=max(nomix,stop);best=max(best,stop)
        if t==k:continue
        for q in mixed:
            a=c&q;b=c&~q
            if not a or not b:continue
            score=z+v(a,k-t-1)+v(b,k-t-1)
            best=max(best,score);mixed_evals+=1
            if not m:first=max(first,score)
    return dict(value=best,reference=v(full,k),no_mixed=nomix,mixed_first_or_none=max(first,nomix),mixed=len(mixed),local=len(local),profile_states=prof.cache_info().currsize,peak_merge=peak,contiguous=contiguous,mixed_evals=mixed_evals)

def main():
    rng=Random(16943); rows=[];stats=Counter(); rank=json.load(open('capacity_rank.out'))['nodes'];examples=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*p=map(int,line.split());st=list(zip(p[::2],p[1::2]));full,qs,*_=model(n,physical(st,10,25))
        blocks=[sum(1<<j for j,(u,h) in enumerate(st) if u==b) for b in sorted({u for u,h in st})]
        if all(any(q&b==q or (full^q)&b==full^q for b in blocks) for q in qs):continue
        witness=rank[i]['greedy_witness'];masks=[full,witness]+[witness^(1<<j) for j in range(n) if witness>>j&1]
        tests=[tuple((t>>j)&1 for j in range(n)) for t in masks]+[tuple(rng.randrange(6) for _ in range(n))]
        vals=[]
        for w in tests:
            r=solve(n,qs,blocks,k,w);assert r['value']==r['reference'],(i,w,r)
            stats['frozen_checks']+=1;stats['mixed_first_misses']+=r['mixed_first_or_none']<r['value'];stats['no_mixed_misses']+=r['no_mixed']<r['value'];stats['mixed_evals']+=r['mixed_evals'];stats['profile_states']+=r['profile_states'];stats['contiguous']+=r['contiguous'];stats['peak_merge_max']=max(stats['peak_merge_max'],r['peak_merge']);vals.append(dict(weights=w,**r))
            if r['mixed_first_or_none']<r['value'] and len(examples)<3:examples.append(dict(index=i,k=k,n=n,states=st,qs=qs,blocks=blocks,weights=w,**r))
        rows.append(dict(index=i,n=n,k=k,blocks=blocks,witness=witness,values=vals))
    for i in range(120):
        n=rng.randrange(4,11);full=(1<<n)-1;cut=rng.randrange(1,n);blocks=[(1<<cut)-1,full^((1<<cut)-1)]
        qs=tuple(sorted({1<<j for j in range(n)}|{rng.randrange(1,full) for _ in range(5)}));w=tuple(rng.randrange(6) for _ in range(n));k=rng.randrange(0,5)
        r=solve(n,qs,blocks,k,w);assert r['value']==r['reference'],(i,w,r);stats['synthetic_checks']+=1;stats['synthetic_mixed_first_misses']+=r['mixed_first_or_none']<r['value']
    print(json.dumps(dict(stats=stats,examples=examples,rows=rows),sort_keys=True))
if __name__=='__main__':main()
```
