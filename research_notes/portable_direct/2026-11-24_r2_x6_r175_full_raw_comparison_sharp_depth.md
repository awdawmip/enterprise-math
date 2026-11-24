# X6 R175 — Seven is sharp even for all 884 raw comparison predicates

Date: 2026-11-24. AUTHOR ANALYTIC REDUCTION / EXACT FINITE OBSTRUCTION / NOT_REVIEWED. Independent informed portable static BRC research. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, no repinning. P000 V5 and ACTIVE worldview retained. This is an auxiliary weight parameter calculation, not a change to native X6 or a formal Task Result.

## Theorem

For Port 10 and weights (17t,B,22t,D), t,B,D>0, use the four heights and all six pair capacities as in R121. For every sign-reduced feasible nonzero integer direction v let F_v=max_j g_j(v)/s_j, eta=min_v F_v and N={v:2F_v<3eta}. Use the ten R162 rows V, six R163 optimizer rows W, fifteen R164 candidate terms T and thirty nonzero raw terms H of R170/R171. A leaf must return a term i in T equal to eta (any tied term legal) and the complete strict near mask N. Allow all ordered strict comparisons of raw terms a,b in H at ratios 1 and 3/2 and both orientations, i.e. the 884 nonconstant signed linear predicates constructed from the 442 primitive comparison forms in R171. Constant tests cannot improve the tree.

The minimum worst-case depth in this model is exactly 7.

Upper bound: the R168 depth-seven tree is already valid on the full positive cone, and its predicate family is a subset of this enlarged family. Its bank-coverage and face-coverage proofs are inherited at their original scope.

Lower bound: combine two independent necessary conditions for the first predicate. R174's 63-point convex-hull obstruction graph excludes 543 of the 884 first predicates (each child of a depth-six tree has capacity 32 leaves). The complete 341 surviving predicate indices were independently recomputed from the pinned R174 endpoint arrays using exact BigInt sign-crossing segment tests and graph partition DP: 17 edges, total necessary leaf count 44, 341 surviving roots. No triple edge is required for this filter. Reconstruct the exact R171 799-point refined CEGIS sample from its archived arrangement and first failed tree. On this sample, every one of those 341 remaining root predicates has at least one child that cannot be solved at depth five. This proves no root is possible, hence no depth-six tree can solve the full domain. The finite sample lower bound needs no continuum coverage argument and its outputs were checked directly against all 1935 directions.

## Exact finite recursion

For nonempty subset S of sample points, label each input by (M,N) where M is the mask of all terms in T equal to eta. A common leaf is possible iff N is constant and the intersection of M masks is nonempty. For each near group, select all distinct singleton masks present, then greedily add any present mask disjoint from the union already selected. Each pair of selected masks is disjoint, so each forces a separate leaf. Sum the counts across near groups (different near groups cannot share leaves). This is a safe lower bound L(S) even for ties. It need not be optimal. Prune only when L(S)>2^d. Otherwise enumerate every distinct nontrivial cut by the 884 predicates, modulo swapping children. A node is feasible at depth d iff it is already a legal leaf or some cut has two feasible children at depth d-1. Induction on d proves completeness of this recursion on the sample. Caching (S,d) and reordering the cuts by lower bounds do not change feasibility. Complementary cuts can be merged because both children must succeed.

## Actual execution

- Reconstructed R171's 117903 exact sign states and its 799 refined points; first depth-six sample tree reproduced 57 leaves, 18142 failures over 41 failed leaves. Reconstructed seed count 505 then 799, as in the pinned seed source.
- All 799 points compared against every one of 1935 integer directions: 1546065 exact direction scores checked, full eta masks and strict near sets match the bank. Max bound for the integer cross-products including factor 3: 5424571929420 < 2^63.
- 799-point sample admits 707 distinct nonconstant cuts up to branch exchange. Initial leaf lower bound 35; initial capacity filter alone excludes 276 roots.
- First bounded pass: 55 completed recursive root exclusions, 17000 recursive calls before budget interruption; 331 excluded counting the initial capacity filter.
- Second run: 71 completed recursive root exclusions including the original 55 before host timeout; retain only fully returned False roots, no inference for interrupted roots. Combined 347 distinct roots excluded (276 capacity plus 71 recursion). Of R174's 341 survivors, 71 excluded.
- Targeted pass over the remaining 270 R174 survivors: 125 completed recursive exclusions, 10000 calls before timeout. 145 remained.
- Final targeted pass: all 145 remaining roots excluded, 1896 recursive calls, terminated normally; no budget hit. Across the completed passes, sample evidence excludes 617 distinct oriented roots, including ALL 341 R174 survivors. The union with R174's 543 root exclusions is exactly all 884. The interrupted calls were not used as negative evidence.

The first full-domain six-versus-seven question of R170–R174 is settled. Seven is a comparison-depth result, not a wall-clock benchmark or an unrestricted arithmetic lower bound. It applies to the declared raw-pair query family, and retains all original six observation relations. Independent review remains pending.

## Reproduction

Obtain the following exact immutable source files into one working directory (names unchanged):
- [x6_r171_exact_arrangement.py](https://github.com/awdawmip/enterprise-math/blob/15032218f2f7c4c1474c123c2e2cefd46d7e0030/research_notes/portable_direct/x6_r171_exact_arrangement.py), blob ea625c7fa545805934cbe3cdc4164447449f5f97.
- [x6_r171_cegis_seed.py](https://github.com/awdawmip/enterprise-math/blob/14f81ab27c16f8cdb3ffc2d7c41aea3b6edaa721/research_notes/portable_direct/x6_r171_cegis_seed.py), blob 88d6fdc71e098b0e24bc94f0f7429b5a1baa09d7.
- [x6_r174_convex_hypergraph_replay.cjs](https://github.com/awdawmip/enterprise-math/blob/96cabdf04977ec15f05e1a417fef75268ba09cf7/research_notes/portable_direct/x6_r174_convex_hypergraph_replay.cjs), blob 73f6d8c9638ddc2bd9646464b521e84a567c6395.

Run python x6_r171_exact_arrangement.py, python x6_r171_cegis_seed.py, and node x6_r174_convex_hypergraph_replay.cjs > root174.json. The exact core of the executed Python sample search is below, with an unbounded deterministic replay driver (rather than the original time-bounded multi-pass driver). It accepts the R174 JSON output, checks the full population and all 341 roots. The source arrangement was reconstructed locally from its pinned code; the source seed was copied verbatim except saving the selected indices instead of the selected points, which is equivalent.

```python
import numpy as np, functools, itertools as it, json
from x6_r171_exact_arrangement import V,W,M,E,G,T,H,L,labels,gaps
p=np.load('r171_refined_sample.npy')
assert p.shape==(799,3) and np.all(p>0)
lab=labels(p); S=p@E.T
full=[v for v in it.product(range(-10,11),repeat=3)
      if next((x for x in v if x),0)>0 and
      max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))<=10]
assert len(full)==1935
maxg=max(max(gaps(v)) for v in full)
assert 3*maxg*int(S.max())<2**63
nr=np.ones(len(p),dtype=np.int64); dr=np.zeros(len(p),dtype=np.int64)
vals=[]
for v in full:
    a=np.zeros(len(p),dtype=np.int64);b=np.ones(len(p),dtype=np.int64)
    for j,g in enumerate(gaps(v)):
        q=g*b>a*S[:,j];a=np.where(q,g,a);b=np.where(q,S[:,j],b)
    q=a*dr<nr*b;nr=np.where(q,a,nr);dr=np.where(q,b,dr)
    vals.append((v,a,b))
mask=np.zeros(len(p),dtype=np.int64);near=mask.copy()
for i,(j,g) in enumerate(T):mask|=((g*dr==nr*S[:,j]).astype(np.int64)<<i)
for v,a,b in vals:
    q=2*a*dr<3*nr*b
    if v not in V:assert not np.any(q)
    else:near|=q.astype(np.int64)<<V.index(v)
assert np.array_equal(np.stack([mask,near],1),lab)
print('full-direction checks',len(p)*len(full),'PASS')
L=np.array(L,dtype=np.int64);Q=np.concatenate([L,-L],axis=0)
assert len(Q)==884 and int(np.max(np.abs(Q)))*3*int(p.max())<2**63
n=len(p);ALL=(1<<n)-1
bits=lambda a:int.from_bytes(np.packbits(a,bitorder='little').tobytes(),'little')
qs=[bits(p@q>0) for q in Q]
qmap={}
for i,x in enumerate(qs):
    if x and x!=ALL:qmap.setdefault(min(x,ALL^x),i)
queries=[(qs[i],i) for i in qmap.values()]
assert len(queries)==707
groups=[(int(m),int(b),bits((lab[:,0]==m)&(lab[:,1]==b)))
        for m,b in sorted(set(map(tuple,lab)))]
near_groups=[(b,[(m,x) for m,c,x in groups if c==b])
             for b in sorted(set(lab[:,1]))]
@functools.lru_cache(maxsize=400000)
def lower(s):
    k=0
    for _,g in near_groups:
        chosen=0;rest=[]
        for m,x in g:
            if s&x:
                if m.bit_count()==1:chosen|=m
                else:rest.append(m)
        k+=chosen.bit_count()
        for m in sorted(rest,key=int.bit_count):
            if not (m&chosen):k+=1;chosen|=m
    return k
def out(s):
    m=(1<<15)-1;b=None
    for a,c,x in groups:
        if s&x:
            if b is not None and b!=c:return None
            b=c;m&=a
            if not m:return None
    return [int((m&-m).bit_length()-1),b] if b is not None else [0,0]
@functools.lru_cache(maxsize=300000)
def solve(s,d):
    k=lower(s)
    if k>1<<d:return False
    if k<=1:
        o=out(s)
        if o is not None:return True
    if not d:return False
    cand=[];seen=set();cap=1<<(d-1)
    for x,i in queries:
        a=s&x;b=s^a
        if not a or not b:continue
        key=min(a,b)
        if key in seen:continue
        seen.add(key)
        ka=lower(a)
        if ka>cap:continue
        kb=lower(b)
        if kb>cap:continue
        cand.append((max(ka,kb),abs(ka-kb),abs(a.bit_count()-b.bit_count()),i,a,b,ka,kb))
    cand.sort()
    for _,__,___,i,a,b,ka,kb in cand:
        if ka>=kb:
            if solve(a,d-1) and solve(b,d-1):return True
        else:
            if solve(b,d-1) and solve(a,d-1):return True
    return False
root=json.load(open('root174.json'))['root']
assert len(root)==341 and len(set(root))==341
assert lower(ALL)==35
order=[]
for i in root:
    a=qs[i];b=ALL^a;ka=lower(a);kb=lower(b)
    order.append((max(ka,kb),abs(ka-kb),abs(a.bit_count()-b.bit_count()),i,a,b,ka,kb))
for _,__,___,i,a,b,ka,kb in sorted(order):
    if ka>=kb:ok=solve(a,5) and solve(b,5)
    else:ok=solve(b,5) and solve(a,5)
    assert not ok, i
    print('root excluded',i,flush=True)
print('ALL 341 R174 SURVIVORS EXCLUDED; DEPTH SEVEN SHARP')
```

## Next

The 884-predicate comparison-depth classification is complete. A new scientific question is whether the same seven lower bound persists when arbitrary rational linear observations are allowed, or whether an additional non-raw predicate enables a six-level tree. Another direction is the variation of sharp observation cost with the fixed C/A ratio and Port. Do not re-solve the closed 884-predicate case. The next model must explicitly account for observation cost and preserve strict equality/tie compatibility.

## Control provenance

Read-only X6 request r2-20261124-2110-x6-current-read-v1 returned SUCCEEDED/error=null, source a25234629c24a8f87bbe564cfa9051f22abbf9c9, observed 2026-11-24T13:10:35.344737Z, NO_CANONICAL_PUBLICATION_DIRECTORY; native owner view not evaluated; execution_authorized=false. Native gateway identity-only read succeeded; current own Researcher SID/private binding not established. Historical lane provenance EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317, not claimed as current authenticated ownership. No new CLAIM or task mutation. Activity association pending current own identity verification. Independent informed source preservation.
