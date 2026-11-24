# R772 — Induced-support exact reserve and completion lower bound

2026-11-24. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R770 / EXACT_PYTHON_CHECKED / NOT_REVIEWED.
Continuation of R771, 41db7251a5be828c7891bb7e7499b685b874a1a7:research_notes/portable_direct/R771_SINGLE_DEFECT_AND_JOINT_SATURATION.md (full read, blob 38f3cac2a5339099e21ed17c87554ceaaab4beb1), and R770, 7603a5655b287391d5a91c90508dd93ab7dabbec:research_notes/portable_direct/R770_ALL_RANK_GRAPHIC_SHARP_SAVING.md. Frozen science pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5, joint-relation and weighted substrate at that pin re-read, blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447, 3923890d77a02d84b772f789e6912dd14f220d14, f375a059fa4af8c6eefaddb4d4a8689a0c063674. Current account entry snapshot c62f14064e52559271fd28ea642464333861852d, ACTIVE worldview and applicable rules read, current portable, continuation and research method read. Historical generated foundation package not fully verified. Own session recovery r3-20261124-2120-own-recovery-v1 verified original registration, researcher EM-DIRECT-82A007, activity RA-708BCC309CE076D8BB599B91, no RUN, execution_authorized=false. Owner inventory r3-20261124-2120-owner-read-v1 last observed RUNNING; independent portable derivation, no shared CLAIM/PROGRESS.

## Model

Use exactly R771's Boolean auxiliary observer: a finite loop-free subcubic multigraph G, private unused Ports, local V_i=F2^2, cycle relation K subset product V_i, quotient q, S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i, P(p)=product S(p_i), p_i in {0,1,2}. Suffix t feasible for terminal w iff q(P(p))+q(w) subset q(P(t)). Minimum cost k_p(q(w))=min sum t_i. We use R770's author theorem: any suffix covering full quotient costs at least 2n-r, and a suffix of that cost exists, for any such graph, r=dim K. No independent admission claimed.

## Theorem 1 (completion bound)

If an augmentation a satisfies q(P(p))+q(P(a))=V/K, then for every w, k_p(q(w)) >= 2n-r-sum a_i. Indeed for a feasible t, adding q(P(a)) to its inclusion gives q(P(t))+q(P(a))=V/K, since the left translates the full group. Local sum S(t_i)+S(a_i)=S(min(t_i+a_i,2)) (in particular two nonzero choices sum to all four elements). Thus the resulting full-cover suffix costs at most sum t_i+sum a_i; apply R770. This bound is uniform across terminals, with no assumption on optimal t.

For any linear D subset product of m copies of F2^2, an inventory of cost 2m-dim D covers the full quotient by D. Order coordinates; let D_i be the subspace of D with preceding coordinates zero and let d_i be its projection rank at i. Choose inventory 2-d_i. Every affine coset of the projection meets S(2-d_i): a singleton meets the full local space, a two-element affine line meets the three nonzero values, and the full space meets {0}. Equivalently for d_i=0,1,2 respectively the suffix inventory is 2,1,0. Sequentially choose a correction, fixing earlier coordinates, then adjust by D_i. Telescoping ranks sum to dim D. This construction only asserts an upper bound for arbitrary D; no graphic lower bound is imported into a nongraphic kernel.

## Theorem 2 (induced-support formula)

Let U={i:p_i>0}, J={i:p_i=1}, K_U=K intersect V_U (outside U zero); this is the cycle space of the induced graph G[U], replacing deleted edges by private ports. Set r_U=dim K_U and H=q(V_U). The quotient restriction has dimension h=2|U|-r_U. Let J0 consist of the singleton vertices with zero projection of K_U, J1=J minus J0. Define D1=projection_J1 K_U. Assume the joint saturation test
    product_{i in J1} S(1) + D1 = product_{i in J1} V_i.
Empty product convention applies. Then
    k_p(0) = 2|U|-r_U-|J0| <= k_p(q(w)) for every w.
This includes every 0/2 inventory, every inventory with at most one singleton and arbitrary many zeros, and the mixed case of arbitrarily many singletons meeting the stated joint condition. For a single singleton of nonzero rank its three-element set meets every coset of the projected local kernel (rank one or two).

Proof. Because the K_U projection on J0 is zero, the quotient V_U/K_U factors into independent V_i for i in J0 and the quotient on U minus J0 by the same K_U. By R771's projection criterion, on the latter factor the prefix is full: its only deficient indices are J1, satisfying the assumption. Thus the prefix support in H is exactly a product of a saturated quotient and one S(1) in each independent J0 factor. This is an observer identity, not an identification of weighted or ordered fibers.

For upper bound at zero: on G[U minus J0] use R770's full-cover suffix of cost 2(|U|-|J0|)-r_U; cycles unchanged because K_U vanishes on J0. At J0 choose suffix inventory one, and outside U choose zero. Its quotient contains the prefix, total cost h-|J0|.

For lower bound at every terminal: add a single event at each J0, filling those S(1) factors since S(1)+S(1)=V_i. On A=V(G) minus U, the quotient Q/H is isomorphic to V_A/projection_A K, whose dimension is 2|A|-(r-r_U)=2n-r-h. Apply the ordered rank-release construction above on A to cover Q/H at that cost. These two augmentation inventories are disjoint. Adding them to the prefix covers all of Q: first fill H, then meet every coset. Theorem 1 now gives k_p(w) >= 2n-r-(|J0|+2n-r-h)=h-|J0|. This proves both exact zero cost and zero-terminal optimality, with all zero/empty graph boundary cases included.

In the 0/2 case, h alone is the exact optimum, even when global cycles cross the zero-stock vertices. Compared to B-r, the bound improves by r-r_U, exactly the rank of cycles that cannot be supported on the occupied region. General singletons give saving B-k_p(0)=r_U-|J1| under the hypothesis. The result does not claim equality for arbitrary nonzero targets, nor for nonsaturating J1. The complement rank-release argument preserves the joint quotient rather than discarding exterior cycles.

## Independent finite check

Executed Python integer XOR/bitsets, computing quotient from explicitly enumerated even edge masks, then independently enumerating suffix inventories. For qualifying p, every t cheaper than the formula was checked to cover no terminal; at the predicted cost a zero-terminal witness was found. Counts per graph (n,r,qualifying prefixes,quotient prefix-terminal pairs,0/2 prefixes,exactly one singleton):
(1,0,3,12,2,1)
(2,0,9,144,4,4)
(2,1,8,64,4,4)
(2,2,9,36,4,4)
(3,1,23,736,8,12)
(4,1,69,8832,16,32)
(4,3,64,2048,16,32)
(5,3,186,23808,32,80)
(6,4,527,134912,64,192)
Totals: 898 prefixes, 170592 prefix-terminal lower-bound checks, 150 binary prefixes, 361 exactly one singleton, no assertion failures. These are nine specified graphs, not an all-graph enumeration. Code follows (same algorithm and fixed inputs executed).

```python
from itertools import product
S=((0,),(1,2,3),(0,1,2,3))
def check(n,E):
    inc=[[] for _ in range(n)]
    for j,(u,v) in enumerate(E): inc[u].append(j);inc[v].append(j)
    K=[]
    for z in range(1<<len(E)):
        a=[sum(((z>>e)&1)<<i for i,e in enumerate(es)) for es in inc]
        if not any(x.bit_count()%2 for x in a):K.append(sum((x&3)<<(2*i) for i,x in enumerate(a)))
    piv={}
    for z in K:
        for b,v in sorted(piv.items(),reverse=True):
            if z>>b&1:z^=v
        if z:piv[z.bit_length()-1]=z
    free=[i for i in range(2*n) if i not in piv]; Q=1<<len(free);full=(1<<Q)-1
    def q(x):
        for b,v in sorted(piv.items(),reverse=True):
            if x>>b&1:x^=v
        return sum(((x>>b)&1)<<j for j,b in enumerate(free))
    masks=[sum(1<<x for x in range(Q) if not(x>>b&1)) for b in range(len(free))]
    def shift(s,x):
        while x:
            k=x&-x;m=masks[k.bit_length()-1];s=((s&m)<<k)|((s&~m)>>k);x^=k
        return s
    types=list(product(range(3),repeat=n));costs=sorted(types,key=sum);P={}
    for p in types:
        s=1
        for i,a in enumerate(p):
            v=0
            for x in S[a]:v|=shift(s,q(x<<(2*i)))
            s=v
        P[p]=s
    counts=[0,0,0,0]
    for p in types:
        U=[i for i in range(n) if p[i]];J=[i for i in U if p[i]==1];outside=sum(3<<(2*i) for i in range(n) if not p[i]);KU=[z for z in K if not z&outside];rU=len(KU).bit_length()-1
        J0=[i for i in J if all(not ((z>>(2*i))&3) for z in KU)];J1=[i for i in J if i not in J0]
        def proj(z):return sum(((z>>(2*i))&3)<<(2*j) for j,i in enumerate(J1))
        D={proj(z) for z in KU};A={sum(x<<(2*j) for j,x in enumerate(xs)) for xs in product(*([S[1]]*len(J1)))}
        if len({a^d for a in A for d in D})!=4**len(J1):continue
        want=2*len(U)-rU-len(J0);xs=[x for x in range(Q) if P[p]>>x&1];zero=None
        for t in costs:
            c=sum(t)
            if c>want:break
            cand=full
            for x in xs:
                cand &= shift(P[t],x)
                if not cand:break
            if c<want:assert not cand,(n,E,p,t,want)
            if cand&1:zero=c;break
        assert zero==want,(n,E,p,zero,want)
        counts[0]+=1;counts[1]+=Q;counts[2]+=not J;counts[3]+=len(J)==1
    return (n,len(K).bit_length()-1,*counts)
if __name__=='__main__':
    graphs=[(1,[]),(2,[(0,1)]),(2,[(0,1)]*2),(2,[(0,1)]*3),(3,[(0,1),(1,2),(2,0)]),(4,[(0,1),(1,2),(2,0),(2,3)]),(4,[(i,j) for i in range(4) for j in range(i+1,4)]),(5,[(0,4),(4,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),(6,[(i,j) for i in range(3) for j in range(3,6)])]
    results=[check(n,E) for n,E in graphs];print(*results,sep='\n');print('totals',tuple(sum(row[i] for row in results) for i in range(2,6)))
```

## Next question

Nonzero-rank singleton groups failing joint saturation in the induced graph remain open. Study minimal completion cost of their coset pattern, and whether it gives a sharp lower bound matched by a zero-target suffix, or a genuine graphic nonzero-target advantage. No native signed/weighted/ordered/provenance/common-depth lift is claimed. Retain full original carriers outside this specific Boolean observation.
