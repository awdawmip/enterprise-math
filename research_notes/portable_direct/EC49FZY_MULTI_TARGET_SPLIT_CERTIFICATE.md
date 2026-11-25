# EC49FZY — Target-splitting normal form and strict triple obstruction
2026-11-25. Independent informed portable continuation of EC49FZX at 3085a6be00b91313ba61b1a8f62dbe08a880c96a, research_notes/portable_direct/EC49FZX_PAIR_SEPARATING_CERTIFICATE.md. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; inherited FZX reproduction archive and manifest checked locally. This is a finite relational binary-query model, not an assertion of physical dynamics or a change to P000. No native BRC arithmetic is invoked in the integer mask comparisons. Original read r4-20261125-2132-ec49as-read SUCCEEDED, Source 5ff459b01b369f2ed311b5ab141abbe50ef77e1b, absence of the canonical publication directory for RS-EC49AS only. No live owner projection, formal Task claim, current private researcher binding, or mathematical acceptance asserted. Historical lane provenance EM-DIRECT-23537B; activity association pending.

## Theorem (designated-target splitting normal form)
Let S be a finite set of states distinguishable by a fixed family of deterministic binary queries, all of unit cost and available in every branch. For T subset S let D(S,T) be the minimum over decision trees identifying every state of S of the maximum leaf depth among T only. Set D(S,empty)=0; for a singleton {x}, D(S,{x})=C(x;S), the exact single-target certificate cost of FZT. For |T|>=2,
D(S,T)=1+min_{q: T0(q) and T1(q) nonempty} max(D(S0(q),T0(q)), D(S1(q),T1(q))),
where Sa(q)={z in S:q(z)=a}, Ta=T intersect Sa.
Proof: In a feasible tree follow the common path of the targets to the first query q splitting T. Every target passes through that node; the query exists because the targets are distinct and must be individually identified. Move q to the root. In each root branch restrict the original tree to states agreeing with that answer and suppress repeats of q and redundant tests. On each designated path the original q is removed, and the added root q accounts for it, so depths do not increase. Other branches can be completed using the fixed separating family; their depths are unconstrained. The lower bound follows by restricting the reordered branches to their respective full populations Sa, not just Ta. The upper bound attaches optimal subtrees for the two target sets to q. This proves equality and terminates because each child has strictly fewer designated targets. Queries used before the first split may still be needed to exclude non-target competitors; the leaf certificate on the retained Sa pays that cost. Do not replace Sa by Ta or discard physical query identities in actual tree recovery. Exact signature deduplication is safe on a fixed population and its descendants with a physical representative.
For triples, every splitting query partitions T into a singleton {x} and a pair {y,z}; hence the cost is exactly 1+min over splitting q of max(C(x;Sx(q)), D_2(y,z;Sy(q))). The pair term is the FZX separating certificate applied to the conditional full population. This extends FZX to arbitrary designated subsets; it does not claim small subsets suffice to decide the full population. For any subset T, D(S,T)<=D(S,S). Also T subset T' implies D(S,T)<=D(S,T'). Thus strict subset obstructions can be used for exact lower-bound pruning. If first-query masks A_k are already available, only their intersection need be checked for splitting roots (necessary by FZT). A full implementation must account for conditional pair computations, preprocessing and selection cost; no global speedup asserted.

## Strict anchored triple obstruction
Take nr=4, nc=5, hmax=3; supports [7,9,15], initial fibers (U,0,30), zero-based row/column indices, common positive anchor (0,0). Apply actual history [(3,2,0),(0,0,1),(1,4,0),(2,2,0),(1,4,0),(1,1,0),(0,2,0),(1,4,0)]. The ordered states (support bitmask, hole bitmask) are
[(7,22),(9,4),(9,6),(9,12),(9,20),(9,14),(9,22),(9,28),(15,22)].
The six nonconstant physical positive-answer signatures are [46,154,257,342,343,510]. At budget k=3, the individual costs are [1,3,3,3,3,2,3,2,2], the common first intersection is {46,154}, and every one of the 36 pairs has D_2<=3. The full pair matrix (diagonal omitted) is:
```
- 3 3 3 3 2 3 2 2
3 - 3 3 3 3 3 3 3
3 3 - 3 3 3 3 3 3
3 3 3 - 3 3 3 3 3
3 3 3 3 - 3 3 3 3
2 3 3 3 3 - 3 3 3
3 3 3 3 3 3 - 3 3
2 3 3 3 3 3 3 - 3
2 3 3 3 3 3 3 3 -
```
But the designated triple indices (2,4,8), i.e. (9,6),(9,20),(15,22), has precisely three splitting signatures. Conditional costs (positive branch, negative branch) are (46,2,3), (154,2,3), (257,1,3). Each root therefore costs 4. This proves D(S,T)=4>3, independently checked by all-informative-query adaptive recursion. The all-state optimum is also 4. This is a strict obstruction not recognized by all-target first intersection or even the complete set of FZX pair tests. It is a small genuine history in the same support-hole observation class, not a counterexample at a BRC16943 root.
A separate generic binary example in the raw output has all pair tests passing at k=3 but a minimal designated obstruction of size four (all triples pass). The script enumerates target subset sizes in increasing order and returns the first obstruction; this demonstrates that fixed-size tests should not be presumed sufficient even for generic binary queries.

## Executed experiment
Use the verified FZX reproduction archive; run the following multi_target.py beside forced_hole.py, fourth.py, fourth.json and their inherited dependencies. Seed 16943. Independent reference considers all informative queries on the full population S; the new recurrence considers only queries that split designated targets, using single-target certificate at singleton leaves. Compare up to 16 subsets of each size 2,3,4 for small and frozen histories, and up to 3 for the targeted witness searches. 7,311 exact comparisons, no assertion failure. Frozen sample: 78 conditioned roots at stride 31, 1,244 pair, 1,248 triple, 1,244 quadruple checks; 77 of 78 nodes pass every pair test at their maximum individual cost; no pair-passing full failure in this frozen sample. Targeted anchored search found the witness after 17 admitted nodes. Generic search found a minimal size-four witness after three nodes. The sample is not exhaustive over frozen roots or histories; the strict anchored example is separately generated. Source code SHA256 abf40e5fef2469268d5d8838bd8f1edbf6e3ac622a12220b8c023dac950d1011; raw output SHA256 e2616f6416974c01c0ad0c7bc1a758a66036c03e69b8b7defe6210c30d255b9d.
```python
from functools import lru_cache
from itertools import combinations
from random import Random
from collections import Counter
import json
from forced_hole import explicit,child,obs
from fourth import fibers

def model(n,queries):
    full=(1<<n)-1
    qs=tuple(sorted(set(queries)-{0,full}))
    @lru_cache(None)
    def cert(s,t):
        if s==t:return 0
        return 1+min(cert(s&q if t&q else s&~q,t) for q in qs if s&q and s&~q)
    @lru_cache(None)
    def split(s,t):
        if not t:return 0
        if t.bit_count()==1:return cert(s,t)
        return 1+min(max(split(s&q,t&q),split(s&~q,t&~q)) for q in qs if t&q and t&~q)
    @lru_cache(None)
    def ref(s,t):
        if not t or s.bit_count()==1:return 0
        return 1+min(max(ref(s&q,t&q),ref(s&~q,t&~q)) for q in qs if s&q and s&~q)
    def allowed(s,t,k):
        return [q for q in qs if 1+cert(s&q if t&q else s&~q,t)<=k]
    return full,qs,cert,split,ref,allowed

def physical(st,nr,nc):return [sum(1<<i for i,x in enumerate(st) if obs(x,r,j)) for r in range(nr) for j in range(nc)]

def check(st,qs,c,tag,rng,meta,examples,search=False):
    n=len(st); full,qs,cert,split,ref,allowed=model(n,qs)
    c[tag+'_nodes']+=1
    k=max(cert(full,1<<i) for i in range(n))
    first=set.intersection(*(set(allowed(full,1<<i,k)) for i in range(n)))
    for size in (2,3,4):
        if n<size:continue
        ts=list(combinations(range(n),size));rng.shuffle(ts)
        for inds in ts[:(16 if not search else 3)]:
            t=sum(1<<i for i in inds);a=split(full,t);b=ref(full,t);assert a==b
            c[tag+'_size'+str(size)]+=1
    if not first:return
    c[tag+'_first_pass']+=1
    if any(split(full,(1<<i)|(1<<j))>k for i,j in combinations(range(n),2)):return
    c[tag+'_all_pair_pass']+=1
    if split(full,full)<=k:return
    c[tag+'_pair_pass_but_full_fail']+=1
    if tag in examples:return
    for size in range(3,n+1):
        found=False
        for inds in combinations(range(n),size):
            t=sum(1<<i for i in inds)
            if split(full,t)>k:
                examples[tag]=dict(meta,states=st,masks=qs,k=k,first=sorted(first),targets=inds,target_cost=split(full,t),full_cost=split(full,full),all_pair_max=max(split(full,(1<<i)|(1<<j)) for i,j in combinations(range(n),2)),individual=[cert(full,1<<i) for i in range(n)],root_split_costs={q:1+max(split(full&q,t&q),split(full&~q,t&~q)) for q in qs if t&q and t&~q});found=True;break
        if found:break

def main():
    rng=Random(16943); c=Counter();examples={}
    for _ in range(180):
        nr,nc,hm=3,4,2;f=[(u,0,14) for u in range(1,8,2)]
        x=rng.choice(explicit(f,hm));hist=[]
        for _ in range(rng.randrange(1,10)):
            r,j=rng.randrange(nr),rng.randrange(nc);a=obs(x,r,j);f=child(f,r,j,a,hm);hist.append((r,j,a))
        st=explicit(f,hm)
        if 3<=len(st)<=18:check(st,physical(st,nr,nc),c,'small',rng,dict(history=hist,nr=nr,nc=nc),examples)
    roots=json.load(open('fourth.json'))
    for ix in range(0,len(roots),31):
        f=list(fibers(roots[ix][1]));x=rng.choice(explicit(f,14));hist=[]
        for _ in range(30):
            st=explicit(f,14)
            if 3<=len(st)<=18:
                check(st,physical(st,10,25),c,'frozen',rng,dict(root=ix,history=hist),examples);break
            if len(st)<3:break
            opts=[(r,j) for r in range(10) for j in range(25) if any(obs(y,r,j)!=obs(x,r,j) for y in st)]
            r,j=rng.choice(opts);a=obs(x,r,j);hist.append((r,j,a));f=child(f,r,j,a,14)
    for _ in range(3000):
        nr,nc,hm=4,5,3;us=sorted(rng.sample(list(range(1,16,2)),rng.randrange(3,9)));f=[(u,0,30) for u in us]
        x=rng.choice(explicit(f,hm));hist=[]
        for _ in range(rng.randrange(2,12)):
            r,j=rng.randrange(nr),rng.randrange(nc);a=obs(x,r,j);f=child(f,r,j,a,hm);hist.append((r,j,a))
        st=explicit(f,hm)
        if 4<=len(st)<=18:check(st,physical(st,nr,nc),c,'anchored',rng,dict(supports=us,history=hist,nr=nr,nc=nc,hmax=hm),examples,True)
        if 'anchored' in examples:break
    for _ in range(3000):
        n=rng.randrange(5,12); m=rng.randrange(4,9); vals=rng.sample(range(1<<m),n)
        check(vals,[sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(m)],c,'generic',rng,dict(m=m),examples,True)
        if 'generic' in examples:break
    print(json.dumps(dict(counts=dict(c),examples=examples),sort_keys=True))
if __name__=='__main__':main()
```
Raw output (multi_target.out):
```json
{"counts": {"anchored_all_pair_pass": 17, "anchored_first_pass": 17, "anchored_nodes": 17, "anchored_pair_pass_but_full_fail": 1, "anchored_size2": 51, "anchored_size3": 51, "anchored_size4": 49, "frozen_all_pair_pass": 77, "frozen_first_pass": 78, "frozen_nodes": 78, "frozen_size2": 1244, "frozen_size3": 1248, "frozen_size4": 1244, "generic_all_pair_pass": 1, "generic_first_pass": 1, "generic_nodes": 3, "generic_pair_pass_but_full_fail": 1, "generic_size2": 9, "generic_size3": 9, "generic_size4": 9, "small_all_pair_pass": 104, "small_first_pass": 104, "small_nodes": 106, "small_size2": 1223, "small_size3": 1156, "small_size4": 1018}, "examples": {"anchored": {"all_pair_max": 3, "first": [46, 154], "full_cost": 4, "history": [[3, 2, false], [0, 0, true], [1, 4, false], [2, 2, false], [1, 4, false], [1, 1, false], [0, 2, false], [1, 4, false]], "hmax": 3, "individual": [1, 3, 3, 3, 3, 2, 3, 2, 2], "k": 3, "masks": [46, 154, 257, 342, 343, 510], "nc": 5, "nr": 4, "root_split_costs": {"46": 4, "154": 4, "257": 4}, "states": [[7, 22], [9, 4], [9, 6], [9, 12], [9, 20], [9, 14], [9, 22], [9, 28], [15, 22]], "supports": [7, 9, 15], "target_cost": 4, "targets": [2, 4, 8]}, "generic": {"all_pair_max": 3, "first": [89, 325, 398, 433], "full_cost": 4, "individual": [2, 3, 3, 2, 3, 2, 1, 2, 3], "k": 3, "m": 7, "masks": [56, 64, 89, 325, 398, 433, 452], "root_split_costs": {"56": 4, "89": 4, "325": 4, "398": 4, "433": 4, "452": 4}, "states": [38, 1, 13, 97, 98, 66, 60, 11, 15], "target_cost": 4, "targets": [1, 4, 5, 8]}}}
```

## Branch continuation using unchanged FZV solver
No multi-target pruning integrated yet. In retry_x.py (from FZX) replace "'w2.csv'" with "'w2.csv','x.csv','x2.csv'" and "len(ids)==495" with "len(ids)==483", save as retry_y.py. Run:
```sh
python retry_y.py 4 12 200000 > y2.in
g++ -O3 -std=c++17 sat_token.cpp -o sat_token
./sat_token < y2.in > y2.csv
```
Raw y2.csv columns id,n,status,calls,envelopePrunes,satChecks,satPrunes (1 YES, -1 NO, 0 cap):
```csv
1859,1568,1,44038,400,57,0
1860,1568,1,88306,1800,51,0
1861,1568,1,77345,3207,59,0
1862,1569,1,97178,2779,117,0
1863,1570,1,38944,51,55,0
1864,1570,1,176416,3504,52,0
1865,1575,0,200001,7572,160,0
1868,1578,1,89513,1533,51,0
```
8 previously unresolved roots, 7 YES with 10,991 actual labeled state replays, one cap, 811,741 calls. 13 ordered histories newly YES. A preliminary lower-cap run of three already capped roots (not included in the frontier update, no new information) is also preserved: python retry_y.py 0 3 100000 > y.in; ./sat_token < y.in > y.csv:
```csv
1773,1451,0,100001,2773,110,0
1813,1495,0,100001,1930,145,0
1828,1526,0,100001,3373,30,0
```
SHA256 retry_y.py 6647f7f99e34893387fd344443048a00a2de6f3c560f515cbfde030c2e5b65c2, y2.in 6bc75ad1df0a9d4d27eabde705f89e69098246148bcc2bb2fd573884f194ba0f, y2.csv b784e50603ed95b8ff00c1d2603e1d248468dabbf06d05cf114589e7b46f6fe1, y.in 8acd164b5497d4f613efe1a54ef9269337676107c8317308fc4ef8f17ff863a6, y.csv dc66574be99663d9903797912d10d0a12bc61b23f328eb933d7b22580d770c89.
Frontier 1890 YES / 27 NO / 476 UNKNOWN of 2393; ordered 3820 / 46 / 829 of 4695. Bound 25<=M14<=27 unchanged. Preserve all resolved statuses. Do not retry cap roots at equal/lower budget without a new method or discriminating comparison.

## Next
Use actual FZX pair obstruction masks to prioritize small designated sets, then test conditional pairs for triple obstructions after cheaper checks. Preserve full residual populations and physical labels. Measure incremental pruning (not just theoretical strength) and total overhead in the frozen model; continue the remaining 476 roots. AUTHOR_PROVED / EXACT_FINITE_MULTI_TARGET_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED. No task closure or review asserted.
