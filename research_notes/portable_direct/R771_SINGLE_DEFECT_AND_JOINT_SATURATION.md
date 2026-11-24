# R771 — Exact single-defect reserve and joint saturation quotient criterion

2026-11-24. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R770 / EXACT_PYTHON_CHECKED / NOT_REVIEWED.

Predecessor: 7603a5655b287391d5a91c90508dd93ab7dabbec:research_notes/portable_direct/R770_ALL_RANK_GRAPHIC_SHARP_SAVING.md (actual full read, blob 20b025a11bff94faef90417b8fb2b144942f3ad2). Retain scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 as inherited from R770. Exact Source blobs re-read: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-relation contract 3923890d77a02d84b772f789e6912dd14f220d14, weighted substrate f375a059fa4af8c6eefaddb4d4a8689a0c063674. Generated foundation package was unavailable in predecessor; no repinning or claim of full package verification. Current global canonical snapshot f277e516eb1e805d0c5700290d66a3c2141f22ac: entries, ACTIVE worldview, P000 projection matching canonical V4, math/output policies, project router, BRC and residual-first policies. Current Source continuation/portable/method protocols read. Own session recovery r3-20261124-2020-own-recovery-v1 confirms original registration SUCCEEDED and no runs, execution_authorized=false. Owner inventory r3-20261124-2020-owner-read-v1 last observed QUEUED at research. Independent portable work, no shared task or protected execution write. This is the Boolean auxiliary observer only.

## 1. Setting and main theorem

Use exactly R770's loop-free subcubic multigraph G (parallel edges, isolated vertices allowed), n support vertices, cycle space K in V=product V_i, V_i=F2^2 representing even local Port triples with private unused ports, r=dim K, q:V->V/K. S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i; p and t truncated at 2. Feasibility is forall x in P_raw(p)=product S(p_i), exists z in K with x+w+z in P_raw(t), where q(w) is terminal. k_p(q(w)) is min sum t_i. R770 proves the universal saturated cost U=2n-r, for all terminals. We explicitly depend on that author theorem, not on its independent admission.

Let exactly one vertex i have p_i=a in {0,1}, with every other vertex saturated. Put D=projection_i K, d=dim D. Then

* d=2: k_p(q(w))=U for both a and all w.
* d=1,a=1: k_p(q(w))=U for all w.
* d=1,a=0: k_p(q(w))=U-1 for all w.
* d=0: k_p(q(w))=U-2+a+1_{w_i !=0}.

The final indicator is well-defined on the quotient when d=0. Consequently zero-terminal optimality holds for arbitrary graph size and cycle rank with at most one deficient support. A rank-one zero-stock support reduces the universally saturated cost by exactly one, whereas reducing a rank-two support even to zero does not reduce that cost. This is an inventory-sensitive distinction from R770's sharp bound.

## 2. Proof: orbit invariance, then the rank-one exception

Write X=product of all other V_j. Fix t and w. Define F subset V_i as the local input values y for which every x_other in X has a correction z in K satisfying y+z_i in S(t_i) and x_j+w_j+z_j in S(t_j) for j!=i. This is independent of w_other by saturation. For h in D take c in K lifting h; replacing the other independent inputs by x_other+c_other and the correction by z+c proves F+h=F. The original feasibility condition is S(a)+w_i subset F. A union of D-cosets containing a set meeting every coset must be V_i.

For d=2 all nonempty S(a) meet the sole coset; for d=1,a=1 the three-element S(1) meets both cosets of size two, under every translation. Thus every feasible t is also a saturated feasible t. Conversely any universal t suffices, so R770 gives U.

For d=0 the cycle relation has zero at i and is exactly the cycle space of G-i, with removed incidences replaced by private ports. Hence the other saturated problem costs 2(n-1)-r by R770. Locally the minimum is a at w_i=0, and a+1 for w_i!=0, since S(0)+nonzero is a nonzero singleton, and S(1)+nonzero is a three-set containing zero. This proves the last row.

For d=1,a=0, if t_i=0 is feasible it forces z_i=w_i in D. Fix a lift c in K; the remaining correction coset c+ker(projection_i) is the cycle space of G-i shifted by c. Its rank is r-1, and the remaining prefix is saturated, so cost is at least 2(n-1)-(r-1)=U-1. If t_i>=1, replacing t_i by 2 makes the reserve feasible for the fully saturated prefix (the other constraints unchanged); R770 implies sum t >= U-(2-t_i)>=U-1. For the upper bound when w_i in D, use t_i=0 and the optimal saturated reserve on G-i at the shifted terminal. When w_i outside D, every w_i+z_i is nonzero, so t_i=1 suffices with no restriction on corrections at other vertices. Use R770's ordered rank-release construction with i last. The final conditional local projection rank is zero: any cycle supported only on i must vanish because every nonprivate edge has a distinct opposite endpoint, and private ports have zero cycle bits. Thus the universal reserve has t_i=2. Lower it to 1; all other constraints still satisfied, and the local one is automatic. Cost U-1. This completes the proof for every terminal, including rank-one vertices attached to parallel edges and disconnected graphs.

## 3. Joint saturation criterion for arbitrarily many defects

Let A={i:p_i<2}, V_A=product V_i over A, D_A=projection_A K, P_A=product S(p_i) over A. The following exact equivalence holds for any linear kernel K:
q(P_raw(p))=V/K iff P_A+D_A=V_A.
Proof: the quotient image is full iff P_raw(p)+K=V. Projecting gives necessity. For any y in V, if its A coordinates belong to P_A+D_A, choose c in K matching the difference on A; on the complement choose y_j+c_j in V_j freely, so y lies in P_raw(p)+K. Thus sufficiency. This is a Boolean support identity at the specified observer, not an equality of weighted or ordered fibers.

Under the condition, every t feasible for p must cover all quotient boundaries, independently of target; R770 therefore gives k_p(q(w))=U for all w. It is a sufficient condition for this cost formula, not asserted necessary. It includes joint effects where no independent local reduction suffices.

Graph-only readily testable sufficient subcondition: each p_i=0 in A has d_i=2, each p_i=1 has d_i>=1, and r(G)-r(G-A)=sum_{i in A} d_i. Indeed the kernel of projection_A is the cycle space of G-A with replaced private ports, so the left side is dim D_A. D_A lies inside product D_i; dimension equality forces equality, and each local S(p_i)+D_i is V_i. The dimension condition retains joint information: for two vertices joined by three parallel edges, each d_i=2 but D_A is diagonal (up to local coordinate relabeling), dimension 2 not 4. If both p_i=0, P_A+D_A is proper, and k_p(0)=0. Conversely for both p_i=1 the joint coverage is full because sums of two nonzero elements in F2^2 cover all four elements. Hence actual joint coverage is more general than independent projection. No blanket collapse of local coordinates is warranted.

## 4. Independent exact computation

Executed Python using exact integer XOR, explicitly enumerated every even edge mask, built a binary quotient by Gaussian elimination, and independently enumerated all suffix inventories in increasing cost. For each prefix, intersect the suffix's translated reachable bitsets across all quotient prefix values, assign first cost to each terminal. Checks cover all raw terminal lifts (repeated quotient representatives intentionally counted) for every single-defect prefix in nine explicit graphs, n=1..6, ranks 0..4. Also for every multi-defect prefix type satisfying the joint criterion on these graphs, independently check all quotient terminal costs. Observed per-graph counts (n,r,single raw lift checks,joint qualifying prefix types): (1,0,8,0),(2,0,64,0),(2,1,64,0),(2,2,64,1),(3,1,384,0),(4,1,2048,0),(4,3,2048,22),(5,3,10240,34),(6,4,49152,146). Totals: 64,072 raw-lift comparisons, 203 multi-defect prefix types, zero assertion failures. Not an enumeration of all graphs. The verification does not invoke R770 to compute optima.

Reproducer (same algorithm and fixed inputs executed; explanatory comments omitted):

```python
from itertools import product
from collections import Counter

def analyze(n, edges):
    incid=[[] for _ in range(n)]
    for j,(u,v) in enumerate(edges):
        incid[u].append(j); incid[v].append(j)
    assert all(len(a)<=3 for a in incid)
    K=[]
    for z in range(1<<len(edges)):
        loc=[sum(((z>>e)&1)<<i for i,e in enumerate(a)) for a in incid]
        if any(x.bit_count()%2 for x in loc): continue
        K.append(sum((x&3)<<(2*i) for i,x in enumerate(loc)))
    assert len(K)==len(set(K))
    r=len(K).bit_length()-1; assert len(K)==1<<r
    piv={}
    for z in K:
        for b,v in sorted(piv.items(),reverse=True):
            if z>>b&1:z^=v
        if z:piv[z.bit_length()-1]=z
    free=[i for i in range(2*n) if i not in piv]
    def q(x):
        for b,v in sorted(piv.items(),reverse=True):
            if x>>b&1:x^=v
        return sum(((x>>b)&1)<<j for j,b in enumerate(free))
    Q=1<<len(free); full=(1<<Q)-1
    masks=[sum(1<<x for x in range(Q) if not(x>>b&1)) for b in range(len(free))]
    def shift(s,x):
        while x:
            k=x&-x;b=k.bit_length()-1; m=masks[b]
            s=((s&m)<<k)|((s&~m)>>k); x^=k
        return s
    S=((0,),(1,2,3),(0,1,2,3)); local=[[q(x<<(2*i)) for x in range(4)] for i in range(n)]
    types=list(product(range(3),repeat=n))
    P={}
    for t in types:
        s=1
        for i,a in enumerate(t):
            s0=s;s=0
            for x in S[a]:s|=shift(s0,local[i][x])
        P[t]=s
    costs=sorted(types,key=sum)
    def opt(p):
        remain=full; out=[None]*Q; xs=[i for i in range(Q) if P[p]>>i&1]
        for t in costs:
            cand=P[t]&remain if 0 in xs else remain
            for x in xs:
                cand &= shift(P[t],x)
                if not cand:break
            while cand:
                b=cand&-cand;out[b.bit_length()-1]=sum(t);remain^=b;cand^=b
            if not remain:return out
        raise AssertionError('uncovered')
    checked=0;multi=0;defects=Counter()
    U=2*n-r
    for i in range(n):
        D={(z>>(2*i))&3 for z in K};d=len(D).bit_length()-1
        for a in (0,1):
            p=tuple(a if j==i else 2 for j in range(n));o=opt(p)
            for w in range(4):
                expected=U if d==2 or (d==1 and a==1) else U-1 if d==1 else U-2+a+int(w!=0)
                for x in range(1<<(2*n)):
                    if (x>>(2*i))&3==w:
                        assert o[q(x)]==expected,(n,edges,i,a,w,o[q(x)],expected)
                        checked+=1
                defects[(d,a)]+=1
    for p in types:
        A=[i for i in range(n) if p[i]<2]
        if len(A)<2:continue
        proj=lambda z:sum(((z>>(2*i))&3)<<(2*j) for j,i in enumerate(A))
        D={proj(z) for z in K}
        PA={sum(x<<(2*j) for j,x in enumerate(xs)) for xs in product(*(S[p[i]] for i in A))}
        if len({x^z for x in PA for z in D})==4**len(A):
            assert P[p]==full
            assert all(v==U for v in opt(p))
            multi+=1
    return {'n':n,'r':r,'single_lift_checks':checked,'joint_prefix_types':multi,'rank_inventory_cases':dict(defects)}

if __name__=='__main__':
    graphs=[(1,[]),(2,[(0,1)]),(2,[(0,1),(0,1)]),(2,[(0,1)]*3),(3,[(0,1),(1,2),(2,0)]),(4,[(0,1),(1,2),(2,0),(2,3)]),(4,[(i,j) for i in range(4) for j in range(i+1,4)]),(5,[(0,4),(4,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),(6,[(i,j) for i in range(3) for j in range(3,6)])]
    for n,E in graphs: print(analyze(n,E),flush=True)
```

## 5. Next problem

For multiple deficient supports not satisfying P_A+D_A=V_A, characterize the exact minimum using the remaining coset pattern rather than raw local inventory alone. Seek a terminal-independent lower bound matching a zero-target construction, or a genuine graphic counterexample. The general nonsaturated all-rank zero-terminal question remains open. Preserve native signed/weighted/ordered/provenance/common-depth coordinates separately; no native lift is claimed.
