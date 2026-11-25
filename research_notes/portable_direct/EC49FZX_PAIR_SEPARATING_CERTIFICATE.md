# EC49FZX — Pair-separating certificate theorem
2026-11-25. Portable continuation of EC49FZW at da53ef2ec78cc76646a335c7244af44da864cbab. Frozen BRC16943, fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923 (local file and inherited reproduction manifest verified). This is a finite relational observation problem, not a new spatial ontology or physical dynamics claim. No formal Task ownership, acceptance or current private research identity is asserted. Source control receipt r4-20261125-2033-ec49as-read SUCCEEDED: publication directory absent at aff42839ab7fbc746afd6611e52f4570af4168ec; no native owner projection.

## Theorem: a separating query can be moved to the root for two targets
Let X be a finite set of distinguishable states with a fixed set of deterministic binary queries available at every node, each of cost one. For x in X let C(x;S) denote the minimum number of queries isolating x from a subset S containing x. Let S_x(q)={z in X:q(z)=q(x)} and F_x(q)=1+C(x;S_x(q)), the FZT fixed-first cost. Define D_2(x,y;X) as the minimum, over decision trees identifying every state in X, of the larger of the depths of the two designated distinct states x,y. Other states need not satisfy this depth bound. Then
D_2(x,y;X)=min_{q:q(x)!=q(y)} max(F_x(q),F_y(q)).
Proof: In any such tree the two paths have a first separating query q, appearing on both paths. Along either path all queried answers isolate the corresponding target. Reorder q to the root and use the remaining queries of that path in its respective branch (drop already redundant queries). This gives F_x(q)<=depth(x) and F_y(q)<=depth(y). Conversely, use any separating q at the root and in its disjoint branches use respective shortest fixed-target certificates; any off-target branch can be completed with the fixed separating query family, without increasing either designated depth. Taking the minimum proves equality. This depends on availability of the same physical queries after reordering, not just equality of scalar residual costs.
For A_k(x)={q:F_x(q)<=k}, all-state adaptive recovery of depth <=k therefore requires, for every distinct pair x,y,
A_k(x) intersect A_k(y) intersect {q:q(x)!=q(y)} != empty.
This pair test uses existing FZT/FZW first-query data, and is exact for the two designated paths, necessary (not claimed sufficient) for all-state recovery. It differs from the existing first intersection over targets: a common first query may fail to separate a difficult pair. Query-mask equality is safe only for the declared current state set and its descendants, with an actual query representative retained. Complexity with precomputed A masks: O(number of tested pairs * ceil(number of physical queries / word size)); computing A and selecting useful pairs are additional costs. No solver speedup claimed.

## Strict anchored counterexample
Use nr=4,nc=5,hmax=3; row and column indices zero-based, support masks [15,13,7,11,3,9], initial fibers (U,0,30) with common positive anchor (0,0), actual negative history (0,2),(1,1),(0,3). The exact ten states in order, (U,H), are:
[(15,14),(13,12),(13,14),(13,28),(7,14),(11,14),(3,14),(9,12),(9,14),(9,28)].
At k=3 the individual certificate costs are [3,2,3,2,2,3,2,3,3,2]. Encode a physical query by its positive-answer mask over this ordered state list. The all-target first intersection is {23,31}. For targets indices 5 and 7 (11,14) and (9,12), A_3(5)={23,31,113,423,943}, A_3(7)={10,23,31,423,503,650}. Their common masks {23,31,423} have identical answers on bits 5 and 7 (both zero for 23,31; both one for 423). Thus no feasible depth-3 tree. Exact pair depth is 4, independently checked by recursive adaptive optimization. This is a genuine anchored support/holes fiber counterexample to sufficiency of the first intersection, not a BRC16943 root counterexample. A second generic binary example is in the output.
 
## Reproduction and exact finite checks
Run the following pair_cover.py in the verified FZW reproduction directory containing fourth.json, forced_hole.py, fourth.py and dependencies. The comparison oracle recurses over all informative queries on the remaining labeled state set and only charges depths of selected targets. Query signatures preserve all binary outcomes on that state set. Seed 16943; 240 attempted small histories with 197 nontrivial nodes admitted (2..18 states), and every 31st frozen root (78 nodes) conditioned by actual informative queries until 2..18 states. Up to 32 randomly ordered distinct pairs per node. 2298 small and 2149 frozen pair comparisons, all exact equality; all sampled nodes passed individual first intersection at their maximum individual certificate cost. No strict pair obstruction was observed in these samples. The separate anchored counterexample below is a constructed fixed witness, not part of that sample. No native BRC arithmetic implementation is invoked here; these are exact integer observation masks on the frozen BRC16943-derived input.

```python
from functools import lru_cache
from collections import Counter
from itertools import combinations
from random import Random
import json
from forced_hole import explicit,child,obs
from fourth import fibers

def model(st,nr,nc):
    return mask_model(len(st), [sum(1<<i for i,x in enumerate(st) if obs(x,r,j)) for r in range(nr) for j in range(nc)])

def mask_model(N,qs):
    full=(1<<N)-1
    masks=tuple(sorted(set(qs)-{0,full}))
    def side(q,i):return q if q>>i&1 else full^q
    @lru_cache(None)
    def cert(i,s):
        if s==1<<i:return 0
        return 1+min(cert(i,s&side(q,i)) for q in masks if s&side(q,i)!=s)
    def allowed(i,k):return {q for q in masks if 1+cert(i,side(q,i))<=k}
    def pair(i,j):
        return 1+min(max(cert(i,side(q,i)),cert(j,side(q,j))) for q in masks if (q>>i&1)!=(q>>j&1))
    @lru_cache(None)
    def reference(s,t):
        if not t or s.bit_count()==1:return 0
        return 1+min(max(reference(s&q,t&q),reference(s&~q,t&~q)) for q in masks if s&q and s&~q)
    return full,cert,allowed,pair,reference

def check(st,nr,nc,rng,c,tag):
    full,cert,allowed,pair,reference=model(st,nr,nc)
    k=max(cert(i,full) for i in range(len(st)))
    first=set.intersection(*(allowed(i,k) for i in range(len(st))))
    c[tag+'_nodes']+=1
    if first:c[tag+'_first_pass']+=1
    witness=None
    pairs=list(combinations(range(len(st)),2));rng.shuffle(pairs)
    for i,j in pairs[:32]:
        p=pair(i,j);assert p==reference(full,(1<<i)|(1<<j));c[tag+'_pairs']+=1
        if p>k and first:
            c[tag+'_strict_pairs']+=1
            if witness is None:witness={'states':st,'i':i,'j':j,'k':k,'pair':p,'first':sorted(first),'nr':nr,'nc':nc}
    return witness

def main():
    rng=Random(16943);c=Counter();examples={}
    for _ in range(240):
        nr,nc,hm=3,4,2
        f=[(u,0,14) for u in range(1,8,2)]
        x=rng.choice(explicit(f,hm))
        for _ in range(rng.randrange(1,10)):
            r,j=rng.randrange(nr),rng.randrange(nc);f=child(f,r,j,obs(x,r,j),hm)
        st=explicit(f,hm)
        if 2<=len(st)<=18:
            w=check(st,nr,nc,rng,c,'small')
            if w:examples.setdefault('small',w)
    roots=json.load(open('fourth.json'))
    for ix in range(0,len(roots),31):
        f=list(fibers(roots[ix][1]));x=rng.choice(explicit(f,14))
        hist=[]
        for _ in range(30):
            st=explicit(f,14)
            if 2<=len(st)<=18:
                w=check(st,10,25,rng,c,'frozen')
                if w:examples.setdefault('frozen',dict(w,root=ix,history=hist[:]))
                break
            if len(st)<2:break
            # Select an actual informative query with random tie breaks.
            opts=[(r,j) for r in range(10) for j in range(25) if any(obs(y,r,j)!=obs(x,r,j) for y in st)]
            r,j=rng.choice(opts);a=obs(x,r,j);hist.append((r,j,a));f=child(f,r,j,a,14)
    vals=[31,59,8,23,57,36,30,12]
    full,cert,allowed,pair,reference=mask_model(len(vals),[sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(6)])
    k=max(cert(i,full) for i in range(len(vals)))
    first=set.intersection(*(allowed(i,k) for i in range(len(vals))))
    assert k==3 and first=={50,215,233}
    assert pair(0,7)==reference(full,129)==4
    examples['generic']={'values':vals,'k':k,'first':sorted(first),'pair':[0,7],'pair_cost':4,'individual_costs':[cert(i,full) for i in range(len(vals))],'allowed0':sorted(allowed(0,k)),'allowed7':sorted(allowed(7,k))}
    us=[15,13,7,11,3,9];hist=[(0,2,False),(1,1,False),(0,3,False)]
    f=[(u,0,30) for u in us]
    for r,j,a in hist:f=child(f,r,j,a,3)
    st=explicit(f,3);full,cert,allowed,pair,reference=model(st,4,5)
    k=max(cert(i,full) for i in range(len(st)))
    first=set.intersection(*(allowed(i,k) for i in range(len(st))))
    assert k==3 and first=={23,31} and pair(5,7)==reference(full,(1<<5)|(1<<7))==4
    examples['anchored']={'supports':us,'history':hist,'states':st,'k':k,'first':sorted(first),'pair':[5,7],'pair_cost':4,'individual_costs':[cert(i,full) for i in range(len(st))],'allowed5':sorted(allowed(5,k)),'allowed7':sorted(allowed(7,k))}
    print(json.dumps({'counts':dict(c),'examples':examples},sort_keys=True))
if __name__=='__main__':main()
```
Raw output pair_cover.out:
```json
{"counts": {"frozen_first_pass": 78, "frozen_nodes": 78, "frozen_pairs": 2149, "small_first_pass": 197, "small_nodes": 197, "small_pairs": 2298}, "examples": {"anchored": {"allowed5": [23, 31, 113, 423, 943], "allowed7": [10, 23, 31, 423, 503, 650], "first": [23, 31], "history": [[0, 2, false], [1, 1, false], [0, 3, false]], "individual_costs": [3, 2, 3, 2, 2, 3, 2, 3, 3, 2], "k": 3, "pair": [5, 7], "pair_cost": 4, "states": [[15, 14], [13, 12], [13, 14], [13, 28], [7, 14], [11, 14], [3, 14], [9, 12], [9, 14], [9, 28]], "supports": [15, 13, 7, 11, 3, 9]}, "generic": {"allowed0": [27, 50, 215, 233], "allowed7": [50, 75, 91, 215, 233], "first": [50, 215, 233], "individual_costs": [3, 2, 2, 2, 2, 2, 2, 3], "k": 3, "pair": [0, 7], "pair_cost": 4, "values": [31, 59, 8, 23, 57, 36, 30, 12]}}}
```
Executed script SHA256 1699a64bcb507029dd1fa4bd83e003d758a327bb74fc7d4e4fb2a18297c21bd2, output SHA256 7c437c0eabef75095a3e191a90ed0a75e61b8e71dfd235011d3ab5af717a5080.

## Fourth-layer continuation (unchanged FZV solver)
The new pair criterion is not yet integrated in the adaptive solver. To avoid the redundant FZW first-query gate observed last turn, independently run the unchanged FZV sat_token.cpp on the first 16 still-unknown roots after FZW, cap 200000 each. Reproduce by replacing 'v2.csv' in retry_w.py's files list with 'v2.csv','w.csv','w2.csv' and expected count 507 with 495, saving as retry_x.py. Commands: python retry_x.py 0 8 200000 > x.in; python retry_x.py 8 16 200000 > x2.in; g++ -O3 -std=c++17 sat_token.cpp -o sat_token; ./sat_token < x.in > x.csv; ./sat_token < x2.in > x2.csv. For two NO roots (1856,1858), extract those complete input records from x2.in with header 2 into x_no.in and run unchanged FZW sat_first.cpp compiled with same flags. Each YES is replayed against every physical labeled state in the inherited solver.
Raw x.csv then x2.csv columns id,n,status,calls,envelopePrunes,satChecks,satPrunes, status 1 YES,-1 NO,0 cap:
```csv
1773,1451,0,200001,5744,176,0
1813,1495,0,200001,3401,174,0
1819,1511,1,195688,2095,138,0
1828,1526,0,200001,7351,44,0
1846,1546,1,68569,2151,77,0
1848,1555,1,48683,892,78,0
1849,1556,1,25837,199,28,0
1850,1556,1,69867,2272,63,0
1851,1557,1,41681,836,78,0
1852,1557,0,200001,1474,100,0
1853,1557,1,126582,670,123,0
1854,1557,1,18738,244,9,0
1855,1557,1,18738,244,9,0
1856,1559,-1,177687,2191,160,0
1857,1560,1,22187,336,22,0
1858,1567,-1,73478,1666,132,0
```
FZW crosscheck x_no.csv adds firstChecks,firstDrops,firstEmpty:
```csv
1856,1559,-1,177687,2191,160,0,3378,1764,0
1858,1567,-1,73478,1666,132,0,2743,1517,0
```
SHA256: x.csv 88ff615ce87273ab0c59ae489ce619e41dc224274207bb4fe815d61231dd7207; x2.csv 6933359b8976a110b9b99bc7ba25be75960fc35252615c0170faf56b33123257; x_no.csv 5443e502cf9ef5baaafa90d5a9974fcc5c0c9428faf214816e3bfd8dd37f82fd; retry_x.py ad13061eb51a5667194b2b98829ad9404e2342d51739eb26c5ed3264b7ef496c. Input x.in 9700c38f97a72a5dd4c13ce865594a3933706673d7129612c7dc41b588e57a31; x2.in 790dc096b024bcf27e2d2e34a2dff4d634067bed7c62da91d3230e475789de43; x_no.in 9e9ec8f2beccbb71c4ecebbf20b277e85ae1754db9c52c1fcc6b91ae977aea76.
1,687,739 calls, 15,512 actual labeled replay states, 10 YES, 2 NO crosschecked, 4 UNKNOWN. Frontier 1883 YES / 27 NO / 483 UNKNOWN out of 2393; ordered 3807 / 46 / 842 out of 4695. Bound 25<=M14<=27 unchanged.

## Next
Use the pair criterion at tight decision nodes after cheaper existing checks, prioritizing saturated witnesses where FZW can compute first masks cheaply, with explicit tests for pair obstruction not already excluded. A genuine anchored counterexample proves the additional criterion can strengthen individual first intersection; the frozen sample has not established incremental pruning. Continue the remaining 483 roots, preserve already resolved statuses. AUTHOR_PROVED / EXACT_FINITE_PAIR_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
