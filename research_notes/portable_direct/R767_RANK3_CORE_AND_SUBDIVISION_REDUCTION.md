# R767 — Rank-three core classification and subdivision reduction

2026-11-24. AUTHOR_ANALYTIC_REDUCTION / EXACT_PYTHON_CHECKED / NOT_REVIEWED. Independent portable continuation of R766 at e93960b71a181a1ed5e9b42f668cdd3dc7e6a512:research_notes/portable_direct/R766_UNBOUNDED_THETA_RESERVE_THEOREM.md. Scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint relation contract read at that commit, ACTIVE worldview and current protocols read. Frozen generated foundation package returned 404 as in predecessor. Historical author/Activity EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; current Sites identity check did not confer execution authority and no shared task or protected write is claimed. Owner inventory r3-20261124-1620-owner-read-v1 last observed RUNNING. This is Boolean auxiliary boundary compensation, preserving the universal-prefix cost observer, not a native signed BRC or physical three-dimensional slice claim.

## Core classification (analytic)

For a loop-free subcubic incidence graph, remove bridges and split into connected nontrivial cyclic blocks. Distinct blocks have independent relation kernels; isolated rank-zero coordinates have minimum free and zero cost p_i (strictly increasing local attainable cardinalities). Quotient and costs factor over these independent blocks. A connected bridgeless block of cycle rank r=3 has exactly four degree-three vertices by the R765 degree identity. Suppress all degree-two paths. The connected cubic multigraph on four vertices cannot have a loop: a loop uses two incidences, leaving a single edge to the rest, which would be a bridge. If simple it is K4. If it has a doubled uv edge, u and v each have one remaining edge; these must attach to distinct other vertices (attachment to the same vertex leaves that vertex's sole remaining edge a bridge). The other two vertices then have two remaining incidences each, hence are joined by a double edge. Triple edges would disconnect the graph. Thus there are exactly two possible cores (K4 and a four-cycle with two opposite edges doubled). Every connected rank-three cyclic block is a subdivision of one of them. Disconnected cyclic blocks of total rank at most three with no rank-three block are covered by R763/R766.

## Unbounded reduction (analytic, NOT a completed rank-three zero-optimality proof)

Keep R765 local S0={0}, S1={1,2,3}, S2={0,1,2,3} with XOR and kernel K=F2^3. Each degree-two vertex has rank-one projection; along a suppressed path its nonzero functional f on K is constant. Rank-two endpoints remain explicit. Group all internal vertices sharing the same f, even from different paths (local basis changes preserve S0,S1,S2). There are at most six nonempty groups. Every local mask is now an eight-bit forbidden subset of K, with group H0/H1/A defined by the two complementary four-point halves of f. The R766 path proof uses only the fact that the two halves partition K; it therefore works unchanged for eight lifts and for grouped equal functionals. Explicitly, write a,b,c for numbers of clipped prefix stocks 0,1,2, and subtract the group baseline b+2c. In order N,H0,H1,A the exact zero-mode costs are (2a+b, 0 if a+b>0, a+b if a>0, 2a+b-1 if c>0); nonexistent options have infinite cost. The free-terminal dominating achievable table is (a+b, 0 if a+b>0, 0 if a+b>0, a+b-1 if c>0). Opposite deterministic half restrictions, or an adversarial half combined with any nonneutral half, permit full coverage of K and are infeasible. Repeated identical deterministic half restrictions are idempotent. At free terminal a p=1 adversarial half is dominated by a deterministic half at the same cost. Independent local lift choices induce an actual quotient terminal. This is sufficient for minimum over all terminals, not for the entire fixed-terminal spectrum.

Each of four endpoints can save at most two events relative to baseline, and each of at most six groups can save at most one. Total negative incremental contributions bounded by 14. Zero baseline is feasible with t=p, also for free mode. Thus any individual positive contribution >14 can be replaced by infinity without changing the optimum in either mode. Cap a,b at 16 and c at the indicator c>0: all changed finite positive costs are at least 15 at the cap, and already discarded. Consequently at most 17*17*2=578 profiles per functional suffice for an exact finite comparison of zero and free minima for every subdivision; compare the four endpoint local mask families and up to six group families by R765 union safety, with the full mask now 255. In particular the arbitrary-length problem reduces to two fixed cores and finite bounded inventory types. This is a sufficient cap, not a minimal one or a completed exhaustive certificate. Need a more efficient profile comparison or analytic domination proof to close all subdivision lengths. Do not conflate equality in the finite test below with the general statement.

## Exact finite computation (executed)

All labelled subdivisions of both cores with 0,1,2 added vertices: 1+6+21 per core, 56 graph instances (duplicates up to isomorphism deliberately retained). For each graph all 3^n clipped prefix stocks, all 3^n suffix stocks and all terminals in the full quotient image are covered. The direct image bitset algorithm starts at {0}, uses XOR translations for local sumsets, and applies intersection of translations for universal-prefix erosion. For each suffix, DFS across all prefixes computes the entire permissible terminal set, pruning only empty sets (further intersections of translates of empty remain empty). Search minimum zero and minimum free costs, then compare. 23,042,232 stock pairs in the full Cartesian domain, 4,459,520 nonempty erosion leaves actually visited, 16,054,848 prefix/terminal pairs represented simultaneously (not individually scored). No free terminal strictly improves zero. For each of the 56 graphs the maximum zero saving is exactly 3 over all prefixes (attained). Both unsubdivided cores independently cross-checked by explicit Python sets, 2592 prefix/terminal combinations per core: savings histogram for K4 {0:66,1:10,2:4,3:1}; doubled core {0:60,1:16,2:4,3:1}. Neither has a strict free improvement. No higher subdivision claim.

The following is the executed primary Python algorithm (minor omission of an unused global declaration and stop-on-witness, not of arithmetic). It prints the complete per-graph evidence. Integers and XOR are exact.

```python
from itertools import product,combinations_with_replacement
from collections import Counter

def solve(edges,n):
    inc=[[] for _ in range(n)]
    for j,(u,v) in enumerate(edges):inc[u].append(j);inc[v].append(j)
    m=len(edges)
    for a in inc:
        while len(a)<3:a.append(m);m+=1
    gen=[[(1<<a[0])^(1<<a[2]),(1<<a[1])^(1<<a[2])] for a in inc]
    basis={};g=[]
    for row in gen:
        tmp=[]
        for x in row:
            y=x;v=0
            while y:
                k=y.bit_length()-1
                if k not in basis:
                    basis[k]=(y,1<<len(basis));break
                z,b=basis[k];y^=z;v^=b
            if y:v^=basis[y.bit_length()-1][1]
            tmp.append(v)
        g.append(tmp)
    N=1<<len(basis);full=(1<<N)-1
    masks=[sum(1<<i for i in range(N) if not i&(1<<j)) for j in range(len(basis))]
    def shift(x,a):
        while a:
            b=a&-a;a^=b;mask=masks[b.bit_length()-1];x=((x&mask)<<b)|((x&(full^mask))>>b)
        return x
    stocks=list(product(range(3),repeat=n));costs=[sum(p) for p in stocks]
    def rec(x,i,p,erode):
        a,b=g[i];y,z,q=shift(x,a),shift(x,b),shift(x,a^b)
        if p==0:return x
        if erode:
            r=y&z&q;return r&x if p==2 else r
        r=y|z|q;return r|x if p==2 else r
    reach=[]
    def build(x,i):
        if i==n:reach.append(x);return
        for p in range(3):build(rec(x,i,p,False),i+1)
    build(1,0)
    order=sorted(range(len(stocks)),key=costs.__getitem__)
    zero=[next(costs[j] for j in order if x&~reach[j]==0) for x in reach]
    free=zero[:];witnesses={};checks=0
    for j in order:
        cost=costs[j]
        def dfs(x,i,index):
            nonlocal checks
            if not x:return
            if i==n:
                checks+=1
                if cost<free[index]:
                    free[index]=cost;witnesses[index]=(stocks[index],stocks[j],(x&-x).bit_length()-1,zero[index],cost)
                return
            for p in range(3):dfs(rec(x,i,p,True),i+1,index*3+p)
        dfs(reach[j],0,0)
    return dict(n=n,edges=edges,N=N,rank=2*n-len(basis),stocks=len(stocks),nonempty_pairs=checks,better=len(witnesses),maxgain=max(z-f for z,f in zip(zero,free)),witness=next(iter(witnesses.values()),None),savings=dict(Counter(sum(p)-k for p,k in zip(stocks,zero))),generators=g)

def sub(edges,seq):
    E=[];n=4
    for i,(u,v) in enumerate(edges):
        for _ in range(seq.count(i)):E.append((u,n));u=n;n+=1
        E.append((u,v))
    return E,n

cores=[[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],[(0,1),(0,1),(1,2),(2,3),(2,3),(3,0)]]
for core in cores:
    for d in range(3):
        for seq in combinations_with_replacement(range(6),d):
            E,n=sub(core,seq);r=solve(E,n);print(seq,r,flush=True)
```

Independent set oracle for each core: for each stock tuple build set D[p] by iteratively taking all XOR sums with [0,a,b,a^b] indexed by S[p_i]. For each prefix p and each w in range(32), take the first t ordered by sum(t) with {x^w for x in D[p]} <= D[t]. Compare min over w with w=0 and tally the zero savings histogram. This independent enumeration was executed and matched both core histograms.

## Next

Use the grouped half-profile reduction to search or prove arbitrary rank-three zero optimality, with the eight-lift endpoint constraints kept explicit; exploit graph symmetries and dominance rather than a naive Cartesian product of 578^6. Retain possible higher-rank and non-graphic counterexamples. No signed/ordered/weighted BRC transfer or common slice depth repair is inferred.
