# R780 — Exact real-context quotient and genuine multiprefix collisions

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779 / EXACT_PYTHON_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared Task claim. Predecessor: 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 verified. Global P000 projection matched its canonical blob; ACTIVE worldview and current continuation/portable rules read. Generated foundation package at frozen pin returned 404. Own registration EM-DIRECT-82A007 / TASK_RESEARCH; recovery request r3-20261125-0520-own-metadata-v1 verified existing registration, no RUN; owner inventory r3-20261125-0520-owner-read-v1 observed RUNNING. No changes to shared owners.

## 1. Exact quotient theorem

The observer is the auxiliary unsigned Boolean feasibility observer of R777–R779. A loop-free subcubic port region has local even triples. For fixed prefix x_i, target w_i and reserve t_i, accepted lifts satisfy x_i XOR w_i XOR z_i in S(t_i), where S(0)={0}, S(1)={1,2,3}, S(2)={0,1,2,3} in two-bit local coordinates. Private ports have lift zero. A fixed reserve is tested universally over independent local prefixes x_i in S(p_i), existentially over complete lifts. The minimal family A of its extendible boundary sets is a nonempty inclusion-antichain of nonempty subsets of the even boundary labels Q, unless the reserve is infeasible.

For a connected four-cut let Q=(0,3,5,6,9,10,12,15), with labels represented by their indices as bits in an eight-bit mask. R779 establishes that the set V of nonempty real exterior tests consists exactly of the 147 masks with number of complete antipodal pairs not equal to 1. Necessity holds for disconnected exteriors too; all 147 are realized by connected zero-prefix gadgets. We use this source result, not an independent reproof of its gadget completeness.

Define F(A)={E in V: there exists a in A with a intersection E empty}, and H(A)=Max F(A), inclusion-maximal elements. Thus F(A) is the downset of H(A) in the induced inclusion poset V. Empty exterior tests always fail and can be ignored here. For every feasible A and B:

* H(A)=H(B) iff they are indistinguishable by every actual exterior fixed-prefix feasibility test.
* A is at least as compatible as B in all actual exterior tests iff for each e in H(A) there is f in H(B) containing e.
* If H(A) is empty, all real nonempty tests succeed.

Proof: a glued network at a specified exterior prefix can be completed for every interior prefix iff all members of A intersect its exterior boundary set E. Failure is exactly membership in F(A). Downward closure within V follows from disjointness. A finite downset uniquely determines, and is uniquely determined by, its maximal elements; this proves the formulas. If two signatures differ, an E in the symmetric difference of their failure downsets distinguishes them; R779 realizes that E as an actual connected zero-prefix exterior. Hence equality is exactly observational equivalence, not merely sufficient.

Compute H(A) without searching all 147 tests: for each a take C=Q\a. If C empty omit it. If C has exactly one complete antipodal pair {u,v}, its maximal real subsets are C\{u} and C\{v}; otherwise C itself is real. Take inclusion maxima over the resulting union of at most 2|A| masks. The claim for the exceptional C follows because any subset retaining both u and v still has exactly one full pair; removing either destroys that pair and leaves a real nonempty set. This is an exact finite representation, not a scalar score.

The quotient is safe for arbitrary finite future graph gluing across this same declared interface, provided no operation reads the hidden interior ports. Fix all future exterior prefixes and reserves; the entire future exterior, including any eventual boundary test, is another graph with an extendible set E on the original four-cut (or E empty). Applying the equality for each prefix independently preserves the universal-prefix/existential-lift quantifiers. Consequently two fixed local reserve candidates with equal signatures can be merged by retaining the cheaper one; dominance permits deleting the weaker one if it is no cheaper. Keep the selected reserve witness for reconstruction. This is not a quotient of lift counts, signed BRC, provenance, event order, or native slice depth. In particular it does not authorize a composition API that gives access to hidden internal ports or assumes a signature for a different boundary width.

## 2. Actual graph collision (not merely abstract families)

Use 0,1,2,3 for labeled boundary ports; internal edge IDs start at 4. Every row gives the three ports of one vertex, with first two bits encoded as u+2v and third fixed by parity. Parameters are (p,t,w).

Graph A (two vertices, one edge):
ports [(0,1,4),(2,3,4)], parameters [(0,1,0),(1,1,1)].
Graph B (four-cycle):
ports [(0,4,7),(1,5,4),(2,6,5),(3,7,6)], parameters [(0,1,0),(0,2,0),(1,1,3),(1,1,2)].

Exact direct enumeration of every prefix and internal lift:
A raw masks [62,142,188], minimal antichain (62,142,188).
B raw distinct masks [63,142,159,191,207,223,252,254], minimal antichain (63,142,252).
Both fail exactly 19 of the 147 real tests. Both have H=(3,113,192), so both succeed on the remaining 128. The abstract tests distinguishing them are precisely [66,67,129,193], all forbidden by R779 (exactly one complete antipodal pair). Thus different genuinely achievable multiprefix residual states may be merged in the physical Boolean continuation observer. This resolves the strictness question from R779: even equivalence, stronger than one-way improvement, is genuinely possible. A direct independent verifier follows.

## 3. Finite catalog experiment, not global completeness

Enumerate all local p,t in {0,1,2} and w in {0,1,2,3}; after local min reduction and eliminating families containing the empty set, there are 19 distinct local types. For each graph exhaust the Cartesian product of these types using full lift masks. Two-vertex graph: 199 feasible minimal antichains at fixed labels. Four-cycle graph: 3308 at fixed labels. Union after all 24 boundary permutations: 6675 distinct antichains, 4968 distinct exact physical signatures, 577 signature classes of size >1, 1707 redundant dictionary entries for these topologies. This is a finite catalog for these two exact graphs only; unbounded graph reachability remains open. No timing or general wall-clock speed claim. Full input enumeration is independent of the proof of the quotient; the fixed collision was verified again using explicit prefix products and internal assignments.

## 4. Reproduction code (Python 3.10+, exact integer masks)

```python
from itertools import product, permutations
Q=tuple(x for x in range(16) if x.bit_count()%2==0)
FULL=255
pairs=[(i,Q.index(q^15)) for i,q in enumerate(Q) if q<(q^15)]
def realizable(m):
    return bool(m) and sum(bool(m>>i&1 and m>>j&1) for i,j in pairs)!=1
V=tuple(m for m in range(1,256) if realizable(m))
def mn(a):
    out=[]
    for x in sorted(set(a),key=lambda x:(x.bit_count(),x)):
        if not any(y&x==y for y in out):out.append(x)
    return tuple(sorted(out))
def mx(a):
    return tuple(sorted(FULL^x for x in mn(FULL^x for x in a)))
def sig(a):
    return mx(e for e in V if any(not(e&x) for x in a))
S=((0,), (1,2,3), (0,1,2,3))
def local(p,t,w):
    return mn(sum(1<<z for z in range(4) if x^w^z in S[t]) for x in S[p])
T={}
for p,t,w in product(range(3),range(3),range(4)):
    a=local(p,t,w)
    if 0 not in a:T.setdefault(a,(p,t,w))
print('local types',len(T))
def catalog(ports):
    n=len(ports); e=max(max(row) for row in ports)-3
    lifts=[]
    for qi,q in enumerate(Q):
        for z in range(1<<e):
            bits=q|(z<<4); codes=[]
            for row in ports:
                u,v,w=(0 if k<0 else bits>>k&1 for k in row)
                if u^v^w:break
                codes.append(u+2*v)
            else:lifts.append((qi,codes))
    allmask=(1<<len(lifts))-1
    masks=[[sum(1<<i for i,(_,codes) in enumerate(lifts) if a>>codes[j]&1) for a in range(16)] for j in range(n)]
    bm=[sum(1<<i for i,(q,_) in enumerate(lifts) if q==j) for j in range(8)]
    def proj(x):return sum(1<<j for j,m in enumerate(bm) if x&m)
    d={}
    for ts in product(T,repeat=n):
        cur=(allmask,)
        for j,a in enumerate(ts):
            cur=mn(x&masks[j][y] for x in cur for y in a)
            if 0 in cur:break
        if 0 in cur:continue
        a=mn(proj(x) for x in cur)
        d.setdefault(a,tuple(T[x] for x in ts))
    return d
graphs=[[(0,1,4),(2,3,4)],[(0,4,7),(1,5,4),(2,6,5),(3,7,6)]]
cats={}
for j,g in enumerate(graphs):
    cat=catalog(g);print('graph',j,len(cat))
    for a,c in cat.items():cats.setdefault(a,(j,c))
orig=dict(cats)
for perm in permutations(range(4)):
    maps=[Q.index(sum(((q>>i)&1)<<perm[i] for i in range(4))) for q in Q]
    for a,(j,c) in orig.items():
        b=tuple(sorted(sum(1<<maps[i] for i in range(8) if x>>i&1) for x in a))
        cats.setdefault(b,(j,c,perm))
sigs={}
for a in cats:sigs.setdefault(sig(a),[]).append(a)
print('total',len(cats),'signatures',len(sigs),'collisions',sum(len(v)>1 for v in sigs.values()))
assert (len(T),len(cats),len(sigs),sum(len(v)>1 for v in sigs.values()))==(19,6675,4968,577)
# Independent direct multiprefix witness verification.
def verify(ports,params):
    sets=set()
    for xs in product(*(S[p] for p,t,w in params)):
        m=0
        for i,q in enumerate(Q):
            for z in range(1<<(max(map(max,ports))-3)):
                b=q|(z<<4)
                loc=[tuple(b>>k&1 for k in row) for row in ports]
                if all(u^v^s==0 and (u+2*v)^x^w in S[t] for (u,v,s),x,(p,t,w) in zip(loc,xs,params)):
                    m|=1<<i;break
        sets.add(m)
    a=tuple(sorted(m for m in sets if not any(k!=m and k&m==k for k in sets)))
    return sorted(sets),a
A=verify(graphs[0],[(0,1,0),(1,1,1)])
B=verify(graphs[1],[(0,1,0),(0,2,0),(1,1,3),(1,1,2)])
assert A[1]==(62,142,188) and B[1]==(63,142,252)
fa=[m for m in V if any(not(m&a) for a in A[1])]
fb=[m for m in V if any(not(m&a) for a in B[1])]
assert fa==fb
maxfail=tuple(m for m in fa if not any(m!=k and m&k==m for k in fa))
assert maxfail==(3,113,192)
abstract=[m for m in range(1,256) if all(m&a for a in A[1])!=all(m&a for a in B[1])]
print('Q',Q,'A',A,'B',B,'physical fail',len(fa),'maxfail',maxfail,'abstract differences',abstract)
```

Observed separate exact Python executions: local types 19; graph 0 199; graph 1 3308; total 6675; signatures 4968; collisions 577. Direct witness output: Q (0,3,5,6,9,10,12,15), A ([62,142,188],(62,142,188)), B ([63,142,159,191,207,223,252,254],(63,142,252)), physical fail 19, maxfail (3,113,192), abstract differences [66,67,129,193]. All witness assertions passed.

## 5. Next science

Determine full reachability of physical signatures on unbounded four-cut regions, and whether quotient transitions can be implemented directly at fixed-width interfaces without expanding representative antichains. Develop real exterior test catalogs at higher widths; paired exchange supplies necessary restrictions but not yet sufficiency. Preserve signed, weighted provenance and native BRC as distinct observers.
