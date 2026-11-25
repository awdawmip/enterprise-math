# EC49GAC — Exact weighted fiber-slot capacity
2026-11-26, independent informed portable continuation of EC49GAB. Parent: 2b65c2553fce835d245a8021d39cec9648ed5f5d:research_notes/portable_direct/EC49GAB_FIBER_SLOT_PROFILE.md; artifact head 61c02ae73901132cbc8a4e82ff97577a80d2495c. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Parent archive verified with SHA256SUMS. Finite binary support-hole observation model W(r,j)=1_{r in U}1_{j notin H}, 10 rows, 25 columns, h=14; no claim about physical dynamics, no P000 modification. Topic read r4-20261126-0129-rs-ec49as-read SUCCEEDED at Source 8546618187d5ef61830279f0f469321c26c9ec68: NO_CANONICAL_PUBLICATION_DIRECTORY; no native owner projection or shared CLAIM. Historical EM-DIRECT-23537B provenance; current private binding and Activity association unconfirmed.

## Theorem
Let S be finite, nonempty and distinguishable by fixed binary unit-cost queries Q, partitioned into nonempty blocks B_i. As in GAB, discard constant queries and orient each informative query so one answer side A_q lies entirely in a single block. Let w_x>=0, k>=0. V_d(P;w) is GAA's maximum weight of states identified within d queries in a full identifying tree on the conditional population P. The singleton has weight w_x at any nonnegative depth; nonsingleton has value zero at depth zero. No competitors with weight zero are removed.

For each block choose a chain of local queries along the complement-answer spine, assigned strictly increasing absolute slots t<=k. Starting at C=B_i, a query peels nonempty P=C intersect A_q and replaces C by C minus P. Credit V_{k-t}(P;w). A chain can stop with any residual C, categorized by c=min(2,|C|). Store for each used slot mask M and category c the maximum summed credit. In the singleton-terminal mode add w_x for a residual singleton {x}; in the unresolved-terminal mode no bonus. Merge one profile per block with pairwise disjoint slot masks. In singleton mode accept only total residual count exactly one; in unresolved mode accept count at least two, using capped addition. The maximum of both modes is exactly V_k(S;w). For an indicator weight w=1_T this gives D(S,T)<=k iff the merged value equals |T|.

Proof: Take an optimal full decision tree and truncate it at depth k. Remove constant queries without reducing its credited weight. Follow the oriented complement answer to the truncated terminal. Each peeled branch P is entirely in its block and contributes at most V_{k-t}(P;w). The spine's slots in each block give valid chains since queries from other blocks cannot change that local residual on the complement path. The terminal is nonempty. If singleton it contributes its weight; otherwise contributes zero. Thus the profile optimum is at least the true optimum. Conversely choose actual chains attaining the profiles and interleave them in increasing assigned slot order. The final residual is nonempty, so every nonempty peel is informative on the actual current population. Attach a conditional tree attaining V_{k-t} to its peeled branch. Skip unused slots so actual depth is no larger than t; all credits are achieved or exceeded. A singleton terminal is identified and an unresolved terminal may be completed by any separating full tree. The credited states are disjoint; nonnegative weights ensure any extra early leaves do not reduce credit. Therefore the merged optimum is at most the true optimum. This proves equality.

Local recursion: at residual C and earliest next slot s, insert the stop record (mask=0,c=min(2,|C|)) with zero credit, or singleton weight in bonus mode. For each nonempty local peel P and t in [s,k], take a tail record at (C minus P,t+1), add bit t-1 and V_{k-t}(P;w). Maximize equal mask/category records. At each fixed residual/earliest slot/bonus mode, record (M,c,z) is dominated by (M',c,z') if M' subset M and z'>=z. Removing dominated records is exact: external masks disjoint from M are disjoint from M', both have the same terminal category and their value does not decrease. All states (including zero weight) remain in the true conditional population. Counts saturated at two are sufficient only for this terminal test. Unlike full recovery GAB, stopping with multiple competitors is allowed, and no singleton weight is credited if the global terminal contains other states.

Complexity accounting: local profile state count at most 2(k+1) sum_i 2^|B_i| plus the final earliest-slot boundary; more precisely 2(k+1) is replaced by 2(k+1) for k>=1 with start=1..k+1 (k+1 values). Each state has <=3*2^k mask/category entries, each transition uses at most k|Q| tail choices times that bound, naive dominance quadratic in number of entries. Conditional V evaluation costs its own subset-depth DP; branch signatures and weights are input, not free preprocessing. Merge at most 3*2^k states and naive quadratic pairing. No general speedup claimed; implementation computes the optimum and not a materialized tree. This extends GAB from full feasibility to arbitrary nonnegative weighted capacity, and hence to designated-target obstructions without losing competitors.

## Actual exact computation
All 49 eligible GAB node records (from 180 failure-conditioned records) tested at their recorded k. For each: full indicator, GAA deletion-minimal witness indicator, every one-target deletion of that witness, and a seeded integer weight vector in [0,5]. 290 frozen checks, including 241 direct designated-target checks against FZY's independent all-informative-query recursion. All capacity checks compare against the unrestricted GAA value recurrence. All 34 rank-two and 15 rank-five witness records have capacity exactly rank-1 on witness weights and full capacity on every proper one-target deletion. Rank-five eligible indices: 3,5,6,7,15,17,21,25,76,132,133,135,164,171,176. This is a different decomposition of existing obstructions, not new root classifications. Node index 3 (n=15,k=4,blocks 15 and 32752): full indicator capacity 13; witness mask 13448, target indices 3,7,10,12,13, capacity 4; each of five deletion indicators capacity 4. Random weight vector [1,2,0,0,5,1,4,5,5,5,3,5,1,3,1] capacity 41. 100 seeded synthetic local-query systems, 299 comparisons at budgets near exact depth. Total 589 capacity checks, 50,373 profile subproblems, zero mismatches. Separate second execution output byte-identical. Frozen full-indicator capacity count by (n,k,value): (10,4,8):17; (8,3,6):13; (15,4,13):13; (11,4,9):3; (16,4,13):2; (15,4,9):1.

No new fourth-layer root determinations; retain GAB 1895 YES / 27 NO / 471 OPEN of 2393, ordered 3831/46/818 of 4695, 25<=M14<=27. No independent review or canonical integration. Next: exact mixed-query separator extension or coarsened partition, and targeted call-cost measurement on the 131 nonlocal records. Do not re-run completed roots. AUTHOR_PROVED / EXACT_FINITE_WEIGHTED_SLOT_CHECK / NOT_REVIEWED.

## Reproduction
Save code below as weighted_slots.py in the verified EC49GAB archive directory, execute python weighted_slots.py > weighted_slots.out. Dependencies and inputs are the unchanged inherited multi_target.py, ga_nodes.txt, capacity_rank.out and their dependencies. Exact script SHA256 85226f6d52b4aadac44a09cd87d65b5d49641f4606cd91864350b0f5f68d1cc9; output SHA256 a089c92e4f25cf914c06ec03fe50dcba386e791e515422cc5327249d0877cad5 (16616 bytes). Output contains the weights and exact values for all 49 node records.

```python
from functools import lru_cache
from collections import Counter
from random import Random
import json
from multi_target import model,physical

def capacity(n,qs,blocks,k,w):
    full=(1<<n)-1
    assert sum(blocks)==full and all(not a&b for i,a in enumerate(blocks) for b in blocks[i+1:])
    assert all(x>=0 for x in w)
    oriented=tuple(sorted({q if any(q&b==q for b in blocks) else full^q for q in qs}))
    assert all(any(q&b==q for b in blocks) for q in oriented)
    @lru_cache(None)
    def v(s,d):
        if not s:return 0
        if s.bit_count()==1:return w[s.bit_length()-1]
        if d==0:return 0
        return max(v(s&q,d-1)+v(s&~q,d-1) for q in qs if s&q and s&~q)
    @lru_cache(None)
    def profiles(s,start,bonus):
        c=min(2,s.bit_count())
        out={(0,c):w[s.bit_length()-1] if bonus and c==1 else 0}
        for q in oriented:
            a=s&q
            if not a:continue
            for t in range(start,k+1):
                gain=v(a,k-t)
                for mask,cost,val in profiles(s^a,t+1,bonus):
                    key=(mask|(1<<(t-1)),cost)
                    out[key]=max(out.get(key,-1),gain+val)
        # A subset mask with equal residual category and no lower value dominates.
        keep=[]
        for (mask,c),val in sorted(out.items(),key=lambda p:(p[0][0].bit_count(),p[0])):
            if not any(c==b and m&mask==m and z>=val for m,b,z in keep):keep.append((mask,c,val))
        return tuple(keep)
    best=0
    for bonus in (False,True):
        dp={(0,0):0}
        for b in blocks:
            nxt={}
            for (used,c),val in dp.items():
                for mask,e,z in profiles(b,1,bonus):
                    if used&mask:continue
                    count=min(2,c+e)
                    if bonus and count>1:continue
                    key=(used|mask,count)
                    nxt[key]=max(nxt.get(key,-1),val+z)
            dp=nxt
        best=max(best,max((val for (_,c),val in dp.items() if c==(1 if bonus else 2)),default=0))
    return best,v(full,k),profiles.cache_info().currsize

def main():
    rng=Random(16943); stats=Counter(); rows=[]
    rank=json.load(open('capacity_rank.out'))['nodes']
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*pairs=map(int,line.split());st=list(zip(pairs[::2],pairs[1::2]));full,qs,_,_,ref,_=model(n,physical(st,10,25))
        blocks=[sum(1<<j for j,(u,h) in enumerate(st) if u==v) for v in sorted({u for u,h in st})]
        if not all(any(q&b==q or (full^q)&b==full^q for b in blocks) for q in qs):continue
        witness=rank[i]['greedy_witness']; masks=[full,witness]+[witness^(1<<j) for j in range(n) if witness>>j&1]
        tests=[(tuple((t>>j)&1 for j in range(n)),t) for t in masks]+[(tuple(rng.randrange(6) for _ in range(n)),None)]
        vals=[]
        for w,t in tests:
            a,b,c=capacity(n,qs,blocks,k,w);assert a==b,(i,k,w,a,b)
            if t is not None:assert (a==sum(w))==(ref(full,t)<=k);stats['target_checks']+=1
            stats['frozen_checks']+=1;stats['profile_subproblems']+=c
            vals.append([list(w),a])
        assert vals[1][1]<witness.bit_count() and all(vals[j+2][1]==witness.bit_count()-1 for j in range(witness.bit_count()))
        stats['witnesses']+=1;stats['rank_'+str(witness.bit_count())]+=1
        rows.append(dict(index=i,k=k,n=n,blocks=blocks,witness=witness,values=vals))
    for i in range(100):
        sizes=[rng.randrange(1,5) for _ in range(rng.randrange(2,5))];n=sum(sizes);full=(1<<n)-1;blocks=[];off=0
        for size in sizes:blocks.append(((1<<size)-1)<<off);off+=size
        qs=set(blocks)
        for b in blocks:
            qs.update(1<<j for j in range(n) if b>>j&1)
            for _ in range(4):
                q=b&rng.randrange(1<<n)
                if q:qs.add(q)
        _,qs,_,_,ref,_=model(n,[q if rng.randrange(2) else full^q for q in sorted(qs)])
        d=ref(full,full)
        for k in range(max(0,d-2),d+1):
            w=tuple(rng.randrange(6) for _ in range(n));a,b,c=capacity(n,qs,blocks,k,w);assert a==b
            stats['generic_checks']+=1;stats['profile_subproblems']+=c
    print(json.dumps(dict(counts=stats,rows=rows),sort_keys=True))
if __name__=='__main__':main()
```
