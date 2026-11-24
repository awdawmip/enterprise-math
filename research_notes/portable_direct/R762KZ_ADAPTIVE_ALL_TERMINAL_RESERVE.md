# R762KZ — Adaptive reserve for every terminal boundary

2026-11-24. AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable continuation of R762KY at e76e535585202b38e2733feb472e8a798f3136b9:research_notes/portable_direct/R762KY_ADAPTIVE_ZERO_TERMINAL_RESERVE.md (blob bfcbad700af48981d9f090d911c5a97b1d4fa4c0). Frozen P000 and joint relation companion read at a72226e2430ffa4786321ac86e7f0c599d5f0389; ACTIVE worldview and current portable protocol read. Original registration r3-20261124-0124-own-research-registration-v1 SUCCEEDED, EM-DIRECT-82A007, RA-708BCC309CE076D8BB599B91. Recovery r3-20261124-1120-own-recovery-read-v1 confirmed no own RUN, execution_authorized=false; owner inventory r3-20261124-1120-owner-read-v1 RUNNING at readback. No shared task adopted.

## Theorem and observer

Keep the same unsigned auxiliary cube support model as KY: eight triples s=(i,j,k) in {0,1}^3; ports (i,j),(i,k),(j,k) in three separate groups of four; the three event masks M_s are the three pairwise XORs of the associated port unit vectors. H_s=M_s union {0} is a binary rank-two space. E is the even-weight subspace of the twelve-port boundary, |E|=2048. For arbitrary nonnegative integer stock p, P(p) is the set of boundaries of all ordered words with this fixed inventory (ignore mixedness). Define k_p(b) as the minimum number of suffix events in a fixed suffix stock t, independently of the actual prefix word, such that every prefix word can be completed to boundary b in E. The suffix word can depend on the prefix. As in KY, P(p)=P(min(p,2)) and a minimum is attained by t in {0,1,2}^8. This is reachability of the declared terminal observer, not source counts, history, mixedness or native signed BRC/slice dynamics.

New finite classification, extended to all unbounded p by clipping:
* For every p and b, k_p(0) <= k_p(b) <= 11. Thus a nonzero terminal never improves on the zero-terminal minimum.
* Of the 6561 clipped prefix types, 1407 have a constant k_p over all 2048 b. For the others the largest extra cost ranges from one to six; the only type with maximum extra cost six is the empty prefix.
* For subspace prefixes (all occupied supports used at least twice), every type with at least five occupied supports has constant k_p over E. So do the eight four-support stars (one cube vertex and its three neighbors), at cost eight. A four-support face instead has 128 terminals of cost seven, 1792 of cost eight, and 128 of cost nine. These are exact minima across all suffix stocks, including outside supports.

## Exact erosion theorem and proof

For a suffix reachability set X=P(t), define the operator D_s(X)=intersection over e in M_s of (X XOR e). It is a backward universal branch operator (NOT positive BRC mass): b lies in D_s(X) iff all three possible one-event choices lead to a boundary in X. For a stock p, the feasible-terminal set F_t(p) equals the successive composition of D_s with multiplicities p_s, because intersections commute with XOR translations. Equivalently F_t(p)={b: b XOR P(p) subset P(t)}. D_s^2 is intersection over H_s of translates, since M_s+M_s=H_s. D_s^n=D_s^2 for n>=2, since H_s+M_s=H_s. For a doubled coordinate the four translations can be computed by two intersections with translations by two independent generators. This gives exact feasible terminal sets without scanning individual prefix words or individual terminal targets.

For increasing suffix event costs, assign all as-yet unassigned b in F_t(p) to cost |t|. Every earlier smaller-cost suffix has already been tested, proving minimality; ties can use any suffix. Skip a suffix only if |P(t)|<|P(p)|, which makes translated containment impossible. For finite completeness, enumerate all 3^8 suffix stocks and reduce prefix stocks by the 48 cube automorphisms (coordinate permutations and bit flips). They induce a permutation of the 12 ports preserving the event mask family, E, zero, stock size and the containment relation. Thus k_{gp}(gb)=k_p(b), and the histogram of costs over b is invariant. Enumerate all prefix types and take the lexicographic minimum of the 48 images; this yields 267 reps, of which 22 are stable/subspace prefixes. Weight each rep by its actual distinct orbit size. The following executed exact computation verifies the statements for 6561*2048=13,436,928 prefix-terminal pairs. All zeros reproduce KY's histogram. It is a finite exhaustive proof with an unbounded-stock extension, not an analytic proof of zero optimality independent of the cube census.

## Reproducible Python (executed with exact integers)

```python
from itertools import product, permutations
from collections import Counter
D=4096; ALL=(1<<D)-1
lo=[sum(1<<i for i in range(D) if not(i>>j&1)) for j in range(12)]
def tr(x,e):
    while e:
        q=e&-e;j=q.bit_length()-1;l=lo[j]
        x=((x&l)<<q)|((x&(ALL^l))>>q);e^=q
    return x
M=[]
for i,j,k in product(range(2),repeat=3):
    a=1<<(2*i+j); b=1<<(4+2*i+k); c=1<<(8+2*j+k)
    M.append((a|b,a|c,b|c))
E=sum(1<<i for i in range(D) if i.bit_count()%2==0)
R={(0,)*8:1}
for t in product(range(3),repeat=8):
    if not any(t):continue
    j=next(i for i,n in enumerate(t) if n)
    u=list(t);u[j]-=1;x=R[tuple(u)]
    R[t]=tr(x,M[j][0])|tr(x,M[j][1])|tr(x,M[j][2])
bycost=sorted(R,key=sum)
def spectrum(p):
    left=E;hist=Counter();zero=None;witness=None
    for t in bycost:
        x=R[t]
        if x.bit_count()<R[p].bit_count():continue
        for s,n in enumerate(p):
            if n==1:x=tr(x,M[s][0])&tr(x,M[s][1])&tr(x,M[s][2])
            if n==2:
                x &= tr(x,M[s][0]);x &= tr(x,M[s][1])
            if not x:break
        new=x&left
        if new:
            k=sum(t);hist[k]+=new.bit_count();left^=new
            if witness is None:witness=((new&-new).bit_length()-1,t)
            if new&1:zero=k
        if not left:break
    assert not left and zero is not None
    return sorted(hist.items()),zero,witness
V=list(product(range(2),repeat=3));perms=[]
for p in permutations(range(3)):
    for f in V:
        perms.append([V.index(tuple(v[p[j]]^f[j] for j in range(3))) for v in V])
def rep(p):return min(tuple(p[j] for j in perm) for perm in perms)
reps=sorted({rep(p) for p in product(range(3),repeat=8)},key=lambda p:(sum(p),p))
print('orbits',len(reps))
ct=Counter();zeros=Counter();gaps=Counter();full=Counter();stable=Counter()
for p in reps:
    h,z,w=spectrum(p);n=min(k for k,c in h);mx=max(k for k,c in h)
    orbit=len({tuple(p[j] for j in perm) for perm in perms})
    ct[n-z,mx-z]+=orbit
    zeros[sum(p),z]+=orbit
    for k,c in h:gaps[k-z]+=orbit*c;full[k]+=orbit*c
    if 1 not in p:stable[sum(x>0 for x in p),z,mx]+=orbit
    if n<z:print('improvement',p,h,z,w)
print('counts min/max relative to zero',sorted(ct.items()))
print('zero histogram',sorted(zeros.items()))
print('all pair gaps',sorted(gaps.items()))
print('all pair costs',sorted(full.items()))
print('stable min/max',sorted(stable.items()))
assert sum(full.values())==6561*2048
```

## Actual output

```text
orbits 267
counts min/max relative to zero [((0, 0), 1407), ((0, 1), 1512), ((0, 2), 1634), ((0, 3), 1321), ((0, 4), 588), ((0, 5), 98), ((0, 6), 1)]
zero histogram [((0, 0), 1), ((1, 1), 8), ((2, 2), 36), ((3, 3), 112), ((4, 4), 266), ((5, 5), 504), ((6, 6), 784), ((7, 7), 1016), ((8, 7), 6), ((8, 8), 1101), ((9, 8), 24), ((9, 9), 992), ((10, 9), 60), ((10, 10), 724), ((11, 10), 120), ((11, 11), 384), ((12, 10), 12), ((12, 11), 254), ((13, 11), 112), ((14, 11), 36), ((15, 11), 8), ((16, 11), 1)]
all pair gaps [(0, 3435520), (1, 4367936), (2, 3864000), (3, 1559219), (4, 208612), (5, 1640), (6, 1)]
all pair costs [(0, 1), (1, 32), (2, 486), (3, 4410), (4, 27370), (5, 120718), (6, 400065), (7, 1048844), (8, 2170081), (9, 3460370), (10, 3867106), (11, 2337445)]
stable min/max [((0, 0, 6), 1), ((1, 2, 6), 8), ((2, 4, 7), 28), ((3, 6, 8), 56), ((4, 7, 9), 6), ((4, 8, 8), 8), ((4, 8, 9), 56), ((5, 9, 9), 24), ((5, 10, 10), 32), ((6, 10, 10), 12), ((6, 11, 11), 16), ((7, 11, 11), 8), ((8, 11, 11), 1)]
```

Separate executed stable orbit scan gives face p=(0,0,0,0,2,2,2,2): [(7,128),(8,1792),(9,128)]; star p=(0,0,0,2,0,2,2,2): [(8,2048)]. It gives 22 reps and all stable minima above.

## Additional analytic consequences and next

For stable prefix p with U=P(p) a subspace, F_t(p) is a union of U-cosets, hence k_p(b+u)=k_p(b) for u in U. For general p, its actual translation stabilizer gives the same invariance. Define d(v) as the minimum event count reaching boundary v. Then |k_p(b)-k_p(c)| <= d(b XOR c): append a fixed word of that length to any optimal compensating suffix (or reverse roles); this does not require native arithmetic or a mixedness predicate. More sharply minimize d(b XOR c XOR u) over u in the stabilizer. These claims hold for arbitrary stocks in this declared unsigned observer. The terminal optimality result is a cube-specific exact theorem; whether a structural proof or generalization to other support hypergraphs exists is open. Next: derive zero-optimality without enumeration via cycle-space/affine obstructions, or isolate a different support system where it fails. Then study the separately typed native signed/time-dependent BRC operation correspondence and common depth. No original history quotient, native signed attribution or mixedness improvement asserted.
