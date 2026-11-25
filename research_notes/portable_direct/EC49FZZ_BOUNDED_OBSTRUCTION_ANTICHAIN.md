# EC49FZZ — Exact bounded-rank obstruction antichain
2026-11-25; independent informed portable continuation of EC49FZY, 79b2c87301255a3473f41608c0c52308de7b9458:research_notes/portable_direct/EC49FZY_MULTI_TARGET_SPLIT_CERTIFICATE.md. The inherited 142-file archive was checked against SHA256SUMS and the frozen fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. This is the existing BRC16943 finite binary support-hole observer model; exact integer masks, not physical dynamics or new native arithmetic. Current exact topic read r4-20261125-2232-ec49as-read SUCCEEDED at Source dc79a0071b48d89f4e3ac00e5a294a938b39e075, NO_CANONICAL_PUBLICATION_DIRECTORY; no native owner projection or shared execution authority. Historical EM-DIRECT-23537B provenance only; current private binding unconfirmed, Activity pending. No new identity or CLAIM.

## Theorem
Let S be a finite nonempty population separated by a fixed finite binary unit-cost query family Q. Let D(S,T) be FZY's designated-target optimum on T subset S, retaining all competitors in S. For integer k>=0 and w>=1 define B_w(S,k) as the inclusion-minimal nonempty T subset S with |T|<=w and D(S,T)>k. If |S|=1, B_w=empty at every k. If |S|>1 and k=0, B_w consists of all singletons. For k>=1 and |S|>1 let Q_S be the nonconstant queries, quotienting identical *unordered* partitions only at this fixed population. For each q form F_q=B_w(S_0(q),k-1) union B_w(S_1(q),k-1). Then
B_w(S,k) = min_inclusion { union_{q in Q_S} E_q : E_q in F_q for each q, |union E_q|<=w }.
An empty F_q makes the result empty. Implementation folds the families in any order starting at {emptyset}, taking minimal feasible unions after each fold. It may skip adding a member when the accumulated set already contains one; the supersets produced by adding another member are dominated.

Proof. For any T, with D(S,empty)=0, D(S,T)<=k iff there is an informative first query with both child designated optima <=k-1. Constant queries never help, and all targets may lie in one child (other child unrestricted). The two subtrees can be assembled and unrestricted branches completed because Q separates S. Thus D(S,T)>k iff every informative first query has at least one child with designated set T intersect S_a exceeding k-1. D is monotone in the designated set by definition; on the finite subset lattice each failed set of size <=w contains a minimal failed set in the same size range. This yields exactly the stated family formula. Each partial union exceeding w cannot shrink, and a superset of another feasible partial union can always be replaced by the subset under any subsequent union. Thus all pruning is lossless for the bounded-rank family. Every recursive population strictly shrinks. The resulting antichain represents all failures of designated sets of size <=w, not the whole-state decision unless an obstruction is found or w>=|S|. In fact, any larger target containing a discovered obstruction also fails. A complete no-obstruction result for w<|S| cannot establish full feasibility.

This dual computation enumerates minimal witnesses rather than every possible designated subset, allowing extraction of all low-rank obstacles and exact reuse of common conditioned populations. It does not replace physical queries in an actual recovery tree or discard non-target competitors. Intermediate union antichains can still be exponentially large. No runtime gain or BRC-specific upper bound on obstruction rank is claimed.

## Executed evidence
Seed 16943. Against FZY's independent all-informative-query recurrence, compare every nonempty target subset of size <=4 and the entire minimal failure antichain at each tested population/budget. Two earlier witness populations (510 subsets), 80 small anchored population/budget instances (11,426 subsets), 49 frozen conditioned nodes (14,677 subsets); total 26,613 exact comparisons, no mismatch. 40 small instances yield 234 minimal obstructions. Anchored witness has eight minimal obstructions, one triple (2,4,8) plus seven quadruples (0,2,4,6), (0,4,5,6), (0,2,6,7), (0,5,6,7), (4,5,6,8), (2,6,7,8), (5,6,7,8); generic witness has two quadruples (1,4,5,8), (1,4,7,8), zero-based indices from FZY. All 49 frozen sampled nodes have no rank<=4 obstruction at their maximum singleton cost; no new frozen pruning claim. These nodes are small conditioned populations of 3..13 states, not all fourth-layer roots. Dual subproblems: frozen 1115, small 1674, witnesses 166; union candidates counted before minimization: 1740, 6605, 674 respectively.

Source script obstruction_antichain.py SHA256 4726faf227ac5c00d1b2656ec8879063ed3331959944cb041093d99c656003c5, actual raw output obstruction_antichain.out SHA256 697c39351d07fce5fedf2f15f3acbd5abbbe5fbaaa9f235a09f5bf327f596421. Run beside inherited FZY files (multi_target.py, forced_hole.py, fourth.py, fourth.json and dependencies). The full output, with actual frozen histories and witness families, is stored below as zlib/base64.

```python
from functools import lru_cache
from itertools import combinations
from collections import Counter
from random import Random
import json
from multi_target import model,physical
from forced_hole import explicit,child,obs
from fourth import fibers

def minimal(xs):
    out=[]
    for x in sorted(set(xs),key=lambda x:(x.bit_count(),x)):
        if not any(y&x==y for y in out):out.append(x)
    return tuple(out)

def dual(n,qs,w):
    full=(1<<n)-1; stats=Counter()
    @lru_cache(None)
    def bad(s,k):
        stats['subproblems']+=1
        if s.bit_count()<=1:return ()
        if k==0:return tuple(1<<i for i in range(n) if s>>i&1)
        partitions=sorted({min(s&q,s&~q) for q in qs if s&q and s&~q})
        families=[]
        for a in partitions:
            b=s^a
            # The two child families have disjoint nonempty supports.
            f=bad(a,k-1)+bad(b,k-1)
            if not f:
                stats['empty_root']+=1
                return ()
            families.append(f)
        assert families
        frontier=(0,)
        for f in sorted(families,key=len):
            # One witness must defeat every candidate root.
            candidates=set()
            for x in frontier:
                if any(x&y==y for y in f):candidates.add(x)
                else:
                    for y in f:
                        z=x|y
                        if z.bit_count()<=w:candidates.add(z)
            stats['union_candidates']+=len(candidates)
            frontier=minimal(candidates)
            if not frontier:break
        return frontier
    return full,bad,stats

def check(st,qs,k,w,c,tag):
    n=len(st);full,qs,cert,split,ref,allowed=model(n,qs)
    _,bad,stats=dual(n,qs,w)
    a=bad(full,k);fail=[]
    for r in range(1,min(n,w)+1):
        for inds in combinations(range(n),r):
            t=sum(1<<i for i in inds);v=ref(full,t)>k
            assert v==any(t&x==x for x in a)
            if v:fail.append(t)
            c[tag+'_subsets']+=1
    assert minimal(fail)==a
    c[tag+'_nodes']+=1;c[tag+'_obstructions']+=len(a)
    c[tag+'_nodes_with_obstruction']+=bool(a)
    c[tag+'_dual_subproblems']+=stats['subproblems']
    c[tag+'_union_candidates']+=stats['union_candidates']
    c[tag+'_empty_root']+=stats['empty_root']
    return a

def main():
    rng=Random(16943);c=Counter(); witnesses={}
    for name,a in json.load(open('multi_target.out'))['examples'].items():
        out=check(a['states'],a['masks'],a['k'],4,c,'witness')
        witnesses[name]=[list(i for i in range(len(a['states'])) if t>>i&1) for t in out]
    for _ in range(80):
        nr,nc,hm=3,4,2;f=[(u,0,14) for u in range(1,8,2)]
        x=rng.choice(explicit(f,hm))
        for _ in range(rng.randrange(2,10)):
            r,j=rng.randrange(nr),rng.randrange(nc);f=child(f,r,j,obs(x,r,j),hm)
        st=explicit(f,hm)
        if 3<=len(st)<=13:
            qs=physical(st,nr,nc);full,_,cert,_,_,_=model(len(st),qs)
            k=max(cert(full,1<<i) for i in range(len(st)))
            for z in sorted({max(0,k-1),k}):check(st,qs,z,4,c,'small')
    roots=json.load(open('fourth.json'))
    frozen=[]
    for ix in range(0,len(roots),47):
        f=list(fibers(roots[ix][1]));x=rng.choice(explicit(f,14));history=[]
        for _ in range(35):
            st=explicit(f,14)
            if 3<=len(st)<=13:
                qs=physical(st,10,25);full,_,cert,_,_,_=model(len(st),qs)
                k=max(cert(full,1<<i) for i in range(len(st)))
                a=check(st,qs,k,4,c,'frozen')
                frozen.append(dict(root=ix,history=history,n=len(st),budget=k,obstructions=list(a)))
                break
            if len(st)<3:break
            opts=[(r,j) for r in range(10) for j in range(25) if any(obs(y,r,j)!=obs(x,r,j) for y in st)]
            r,j=rng.choice(opts);v=obs(x,r,j);history.append((r,j,v));f=child(f,r,j,v,14)
    print(json.dumps(dict(counts=dict(c),witnesses=witnesses,frozen=frozen),sort_keys=True))
if __name__=='__main__':main()
```

Raw output: decode the following single line using zlib.decompress(base64.b64decode(line)); check SHA256 as above (11965 bytes).
```text
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
```

## Separate branch continuation using unchanged FZV solver
Generate retry_z.py by replacing "'x2.csv'" with "'x2.csv','y.csv','y2.csv'" and "len(ids)==483" with "len(ids)==476" in inherited retry_y.py.
```sh
python retry_z.py 7 10 250000 > z.in
g++ -O3 -std=c++17 sat_token.cpp -o sat_token
./sat_token < z.in > z.csv
```
Exact raw z.csv (id,n,status,calls,envelopePrunes,satChecks,satPrunes):
```csv
1871,1580,1,132449,1902,66,0
1872,1580,1,132449,1902,66,0
1873,1581,1,52964,967,43,0
```
Hashes: retry_z.py d6c583ed40b02f33f13212da54d986591feb31871c083b5f8cea0d183644889f, z.in 6926c111a0a43b9f38862d41474a2355fb675f0af26acda60efc206ed74c6737, z.csv 794b32f0db26715bc4f8e396d605a64cf493340124dd12307af07230d2b70f28. 317862 recursive calls and 4741 labeled state replays, all three YES; nine ordered histories newly YES. Frontier 1893 YES / 27 NO / 473 UNKNOWN of 2393; ordered 3829 / 46 / 820 of 4695. 25<=M14<=27 unchanged. No new strict NO. No dual integration into full solver yet.

## Next
Target low-budget full-search internal populations where cheaper single-target tests pass; test the dual family as a bounded rank witness finder against FZY conditional-pair checks, measure incremental prune count and wall time, and continue the 473 unresolved roots. Preserve all closed statuses, no cap rerun at equal/lower budget without new method. AUTHOR_PROVED / EXACT_FINITE_ANTICHAIN_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
