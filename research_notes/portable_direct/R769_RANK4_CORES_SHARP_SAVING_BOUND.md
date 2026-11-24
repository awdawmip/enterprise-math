# R769 — Five rank-four graphic cores and the sharp unbounded saving bound

2026-11-24. AUTHOR_PROOF_WITH_EXACT_FINITE_CORE_CERTIFICATE / NOT_REVIEWED. Independent continuation of R768 (379ffcdaaeab08e526bf830940c0415d153fce71:research_notes/portable_direct/R768_UNBOUNDED_RANK3_ZERO_TERMINAL_OPTIMALITY.md). Frozen science pin a72226e2430ffa4786321ac86e7f0c599d5f0389 retained. P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint relation contract blob 3923890d77a02d84b772f789e6912dd14f220d14, weighted substrate f375a059fa4af8c6eefaddb4d4a8689a0c063674 read at pin. Historical foundation startup and heartbeat companion return 404 at pin, no repin. ACTIVE worldview and current portable/continuation/method rules read. Own session MCP-ec17f2f30fb8409f8e664eb29ae6c08c recovered; original registration SUCCEEDED, no runs, execution_authorized=false. Owner inventory r3-20261124-1820-owner-read-v1 last RUNNING at derivation; no shared CLAIM/PROGRESS. Activity RA-708BCC309CE076D8BB599B91. Boolean auxiliary observer only, retaining distinct signed, weighted, order, source and common-depth observations.

## 1. Result
Let G be any finite loop-free subcubic Port graph with total cycle rank r=4 (parallel edges allowed). In the R768 model V_i=F2^2; S0={0}, S1={1,2,3}, S2={0,1,2,3}; p_i=min(raw p_i,2), B=sum p_i. For every terminal lift w and every feasible suffix t,
    sum t_i >= B-4.
Moreover for every such G there exists a saturated prefix p (all p_i=2) with k_p(0)=B-4. Thus the maximum saving, even allowing free nonzero terminals, is exactly four, for unbounded graph sizes. This uses R768's author-proved lower bound at rank <=3 as a dependency. Zero-terminal optimality for arbitrary rank-four subdivisions remains open.

For the five unsubdivided connected bridgeless cubic rank-four cores, exact computation additionally proves k_p(0)=min_w k_p(w) for all p, and max_w k_p(w)<=8, with equality at saturated p. Across all five cores the computation represents 933120 prefix/terminal pairs (extrema by simultaneous bitsets, not 933120 separately materialized costs).

## 2. Core classification
After removing bridges, factor independent cyclic components and rank-zero local coordinates. In a connected bridgeless rank-four block every vertex has degree two or three, with 6 degree-three vertices by the degree sum and r=E-V+1. Suppressing degree-two paths gives a connected bridgeless cubic multigraph on six vertices, nine edges. A loop in that core would leave exactly one other incident edge at its vertex, necessarily a bridge; hence there are no loops. Enumerate the 15 unordered vertex-pair multiplicities in 0..3 with all six degree sums 3. Check every nontrivial cut has at least two crossing edges. Quotient by all 720 permutations. The exact enumeration below gives 760 labeled cubic multigraphs, 550 connected bridgeless, five isomorphism classes. This exhausts the cores, not arbitrary subdivisions.

## 3. Rank-one vertex cut bound (simplifies group argument)
Feasibility means for every x in product S(p_i), there exists z in K=cycle space such that x_i+w_i+z_i in S(t_i) for every i, with all sums XOR. Take any feasible suffix. At a rank-one vertex i the local projection is {0,v}, v!=0, parametrized by f(z) in F2. For any local prefix x_i at least one of the two halves must be allowed, by global feasibility and independence of prefix choices.

If t_i<p_i, the only possible pair is (p_i,t_i)=(2,1): for t_i=0 and p_i>=1, S(p_i) has >=3 elements, whereas only two x_i can be corrected to zero by the two lifts. Thus t_i>=p_i-1. If there exists any rank-one vertex and a prefix value forcing exactly one half f(z)=b, fix that x_i. Translate by any z0 with f(z0)=b. For every combination of remaining prefixes a correcting lift now exists in ker f. Delete i and replace its lost incidences at neighboring vertices by distinct private ports. Cycles of the resulting graph are exactly the original cycles vanishing on the incident edges of i, since the local projection at i is injective in f. Thus the remaining kernel is ker f, of rank 3, and the remaining local spaces and prefix sets are unchanged. The residual terminal lifts are w_j+z0_j. R768 gives sum_{j!=i}t_j >= sum_{j!=i}p_j-3. Add t_i>=p_i-1, obtaining B-4.

If no rank-one vertex has any forcing prefix, both halves are allowed for every local x_i; in particular t_i>=p_i since (2,1) excludes one half for x_i=w_i. Rank-zero local projections likewise require t_i>=p_i by cardinality. In a connected rank-four bridgeless block ignore these neutral constraints and retain only its six rank-two vertices: suppressing the degree-two paths induces an isomorphism of cycle spaces preserving the local projections at all six endpoints. Their suffix is feasible in the corresponding core, so the exact core lower bound (section 4) gives sum_core t>=sum_core p-4. Add the neutral vertices. If rank 4 is split among cyclic blocks of lower rank, apply R768 separately and sum. Bridges carry zero cycle coordinates; the kernel factors across blocks, which also makes feasibility and additive minimum costs factor, by independence of local prefixes and terminal lifts. Isolated/rank-zero vertices have no saving. This proves the bound.

Sharpness: each of the five cores has k_p(0)=8 for all-six saturated p (baseline 12). Extend its attaining suffix to any subdivision by setting p_i=t_i=2 at each new rank-one vertex; every local prefix there is automatically feasible for every z, so the core feasible correction extends. Add all rank-zero coordinates with p=t=2. If the rank splits among lower-rank blocks, use their R768 saturated sharpness constructions and add. Lower bound gives equality.

A further analytic elimination for the remaining zero-optimality question: if any rank-one vertex with p_i<=1 forces a half for some prefix in a free optimum, t_i>=p_i. The reduced graph has rank three, so R768 replaces the translated remainder by a zero-terminal solution of no greater cost. Restore vertex i with t_i=p_i, z_i=0, which accommodates all its local prefixes. Therefore such a free optimum cannot be a strict counterexample. A minimal counterexample must have every low-stock rank-one vertex neutral in the chosen free optimum. This is a single-vertex proof, no repeated group accounting needed.

## 4. Exact certificate
Use physical edge parity as the quotient representation. Each local nonzero even triple is a pair of incident edges. XOR sums over vertices; the kernel is precisely the cycle space: zero boundary forces shared incidences to agree and the local triples are even. All boundary vectors have even total parity, and the connected graph yields rank 8 (12-4), so the image is the entire even subspace of F2^9. Dropping the ninth coordinate is a bijection on even parity vectors. Hence each terminal is an 8-bit number. A 256-bit integer X is its support set. Suffix composition uses XOR-shift unions; robust prefix composition uses XOR-shift intersections. D0(X)=X, D1(X)=intersection of the three nonzero shifts, D2(X)=X intersect D1(X). These implement exactly the universal prefix quantifier, commuting across vertices. Iterate every suffix stock in nondecreasing cost, then all 3^6 prefix stocks via recursion; first nonempty set is free optimum, first set containing bit 0 is zero optimum. Accumulated union first reaching full set gives max_w k_p(w). Empty subtrees have no feasible terminal. These extrema suffice to check all w without storing a table of individual costs.

Executed Python exact integer bitsets, no floating arithmetic. Five representatives and output histograms, in lexicographic canonical order (zero and free saving histograms identical):
1 edges 04 05 05 13 14 15 23 23 24; saving counts [540,152,30,6,1]; max-minus-zero spread counts [157,267,206,79,20].
2 edges 04 05 05 13 14 14 23 23 25; saving [504,188,30,6,1]; spread [152,282,217,68,10].
3 edges 04 05 05 12 13 15 23 24 34; saving [576,122,24,6,1]; spread [188,263,193,71,14].
4 edges 03 04 05 13 14 15 23 24 25 (K3,3); saving [642,59,21,6,1]; spread [246,224,190,62,7].
5 edges 03 04 05 12 14 15 23 25 34 (triangular prism); saving [628,73,21,6,1]; spread [228,242,190,62,7].
All five: 729 prefix stocks each, no free<zero, max_worst=8. Only one stock has saving four in each core; since cost baseline 12 at full stock, and all terminal costs <=8, it is necessarily the full stock. 5*729*256=933120 prefix/terminal pairs covered by extrema; 5*729^2=2657205 possible prefix/suffix pairs before empty pruning.

```python
from itertools import combinations, permutations, product
from collections import Counter
import json
n=6; pairs=list(combinations(range(n),2)); perms=list(permutations(range(n))); pi={e:i for i,e in enumerate(pairs)}
permids=[[pi[tuple(sorted((p[a],p[b])))] for a,b in pairs] for p in perms]
def graphs():
    def rec(i,ds,ms):
        if i==len(pairs):
            if not any(ds): yield tuple(ms)
            return
        a,b=pairs[i]
        for k in range(min(ds[a],ds[b])+1):
            d=ds[:]; d[a]-=k;d[b]-=k
            if any(d[v]>sum(d[w] for j,(u,w) in enumerate(pairs) if j>i and u==v)+sum(d[u] for j,(u,w) in enumerate(pairs) if j>i and w==v) for v in range(n)):continue
            yield from rec(i+1,d,ms+[k])
    def bridgeless(ms):
        return all(sum(k for k,(a,b) in zip(ms,pairs) if ((s>>a)^(s>>b))&1)>=2 for s in range(1,1<<n-1))
    allg=list(rec(0,[3]*n,[])); good=[m for m in allg if bridgeless(m)]
    reps=sorted(set(min(tuple(m[i] for i in ix) for ix in permids) for m in good))
    print('labeled',len(allg),'bridgeless',len(good),'cores',len(reps),flush=True)
    return reps

def solve(edges):
    assert len(edges)==9
    inc=[[j for j,e in enumerate(edges) if v in e] for v in range(n)]
    vals=[[((1<<a)^(1<<b))&255 for a,b in combinations(z,2)] for z in inc]
    masks=[sum(1<<x for x in range(256) if not (x>>j&1)) for j in range(8)]
    def shift(x,a):
        while a:
            z=a&-a;j=z.bit_length()-1;m=masks[j];x=((x&m)<<z)|((x>>z)&m);a^=z
        return x
    stocks=list(product(range(3),repeat=n)); cost=list(map(sum,stocks)); order=sorted(range(len(stocks)),key=lambda i:cost[i]); zero=[99]*len(stocks);free=zero[:]; allterm=[0]*len(stocks); worst=[99]*len(stocks)
    def getreach(t):
        X=1
        for q,v in zip(t,vals):
            if q:
                Y=shift(X,v[0])|shift(X,v[1])|shift(X,v[2]); X=Y if q==1 else X|Y
        return X
    FULL=(1<<256)-1
    for ix in order:
        c=cost[ix];X=getreach(stocks[ix])
        def walk(j,i,X):
            if not X:return
            if j==n:
                if free[i]==99:free[i]=c
                if X&1 and zero[i]==99:zero[i]=c
                if allterm[i]!=FULL:
                    allterm[i]|=X
                    if allterm[i]==FULL:worst[i]=c
                return
            v=vals[j];Y=shift(X,v[0])&shift(X,v[1])&shift(X,v[2]); i*=3
            walk(j+1,i,X);walk(j+1,i+1,Y);walk(j+1,i+2,X&Y)
        walk(0,0,X)
    assert max(worst)<99
    bad=[(p,z,f) for p,z,f in zip(stocks,zero,free) if f<z]
    row=dict(edges=edges,zero_saving=dict(sorted(Counter(b-z for b,z in zip(cost,zero)).items())),free_saving=dict(sorted(Counter(b-f for b,f in zip(cost,free)).items())),terminal_spread=dict(sorted(Counter(w-z for w,z in zip(worst,zero)).items())),bad=bad, max_worst=max(worst))
    print(json.dumps(row),flush=True);return row
if __name__=='__main__':
    out=[solve([e for e,k in zip(pairs,m) for _ in range(k)]) for m in graphs()]
    print('total',len(out)*729*256,'bad stocks',sum(len(x['bad']) for x in out))
```

## Next
Use the R768 categorical comparison on five rank-four cores; develop a compact endpoint state representation or an analytic comparison, focusing on neutral low rank-one groups and saturated adversarial half constraints. R769 establishes the sharp savings bound but not the universal rank-four zero optimum. The single-vertex cut proof also extends inductively to any higher rank once lower rank bounds and corresponding core bounds are established. No formal Result or acceptance requested.
