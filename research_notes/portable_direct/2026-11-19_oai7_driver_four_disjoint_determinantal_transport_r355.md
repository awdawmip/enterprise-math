# OAI7 r355 — Four disjoint signed-minor transports sharpen the uniform-marginal minimax entropy upper bound

Date: 2026-11-19. Exact finite author-side proof and reproducible integer certificate; this is a mathematical continuation of r352–r354 in shared RESEARCH_DRIVER context, not an independent Native Result review.

## Precise theorem

Let \(G=\mathbb F_{29}\). For a random five-element set \(C\subseteq G\) and every deterministic four-element test set \(K\), let \(b_K(C)=\mathbf 1\{|K-C|\le16\}\). The unrestricted minimax value proved in r347 is

\[
q_*=\min_\mu\max_{|K|=4}\mathbb E_\mu b_K(C)
=\frac{2024467747}{3324255613}.
\]

The r352 finite exact result fixes all 350 distinct complete-loss-profile masses of any minimax distribution. Its profile entropy is \(H_* = 7.869745624309653\ldots\) bits. Among the 28 distinct translation classes in its affine orbit 7, each has profile mass

\[
a=\frac{139525152}{28\cdot474893659}
=\frac{34881288}{3324255613}.
\]

**New finite construction.** There is an ordered random five-tuple \(H=(H_1,\ldots,H_5)\), with five distinct entries almost surely, such that its underlying unordered set \(C\) attains exactly \(q_*\), each of the five marginals \(H_i\) is uniform on all 29 residues, every individual fixed-test failure probability is unchanged from r352, and

\[
\boxed{H(H)=12.669833762757866\ldots\ \text{bits}.}
\]

The previous r353 uniform-translation construction has \(H(H)=H_*+\log_2 29=12.727726619437224\ldots\) bits. The new explicit reduction is

\[
\boxed{\Delta=0.05789285667935809\ldots\ \text{bits},}
\]

about 57 times the 0.00101258483962437-bit r354 single interior-kernel reduction. The bound is for the *joint entropy of the five ordered coordinates with each coordinate uniform*; no global optimality for this constrained entropy minimization is asserted.

## Exact construction

Enumerate the 4095 translation-normalized five-subsets of \(\mathbb F_{29}\) by their integer bitmasks, ordered increasingly. Partition those into the 150 multiplicative affine orbits, sorted by first occurrence as in r347/r354. Let \(C_j\), \(0\le j<28\), be the ascending five-tuples corresponding to the 28 translation-class representatives in orbit 7, indexed in increasing bitmask order.

Use these four disjoint ordered six-tuples of indices:

| block | six translation-class indices \(j\) | signed-minor coefficient range | \(\lambda\) |
|---|---|---|---|
| A | 5, 6, 17, 16, 15, 0 | -4 to +2 | \(-1/2\) |
| B | 20, 3, 18, 22, 21, 1 | -2 to +4 | \(+1/2\) |
| C | 24, 19, 8, 2, 14, 12 | -5 to +4 | \(-1/4\) |
| D | 11, 27, 4, 25, 13, 26 | -2 to +3 | \(+1/2\) |

The four blocks use 24 different orbit-7 classes. The other four classes and every other profile class retain their r353 probabilities.

For a block with six ordered tuples \(c_{x}=(c_{x,0},\ldots,c_{x,4})\) (\(0\le x<6\)), work in \(R=\mathbb Z[z]/(z^{29}-1)\) and define

\[
M_{i,x}=z^{c_{x,i}},\qquad
v_x(z)=(-1)^x\det(M_{\widehat x}),\qquad
v_x(z)=\sum_{t=0}^{28}v_x(t)z^t.
\]

The maximal-minor syzygy and evaluation at \(z=1\) give, as exact integer identities,

\[
\sum_x v_x(s-c_{x,i})=0\quad
(i=0,\ldots,4,\ s\in\mathbb F_{29}),
\qquad
\sum_t v_x(t)=0\quad(x=0,\ldots,5).
\]

For each block separately, replace the 174 baseline joint probabilities \(a/29\) indexed by its \((x,t)\) pairs with

\[
\boxed{\Pr[H=c_x+t]=\frac a{29}(1+\lambda v_x(t)).}
\]

In each listed block the \(1+\lambda v_x(t)\) are nonnegative integers or half/quarter-integer rationals (zeros are permitted). The identities keep each of the six profile masses exactly \(a\) and preserve each position's full residue marginal. All other outcomes are unchanged, so the five coordinate marginals stay uniform. The four blocks have disjoint translation classes; moreover the map \((x,t)\mapsto c_x+t\) is injective across different classes and within each class. This establishes an exact distribution on ordered tuples. Since every fixed \(b_K\) depends only on the complete-loss-profile class, all \(b_K\) expectations and hence \(q_*\) are preserved.

## Exact entropy certificate and endpoint property

For each block \(B\), let \(n_B(v)\) be the count of signed-minor coefficients equal to \(v\). The information saving is

\[
\Delta_B=\frac a{29}\sum_v n_B(v)(1+\lambda_B v)
\log_2(1+\lambda_B v),
\quad 0\log_2 0:=0.
\]

This formula is exact with rational coefficients and ordinary real logarithms. The four evaluated terms are, in bits:

| block | nonzero coefficients among 174 | zero-probability outcomes | \(\Delta_B\) |
|---|---:|---:|---:|
| A | 90 | 18 | 0.017343401964319813... |
| B | 112 | 18 | 0.018597664254199304... |
| C | 112 | 3 | 0.008927563586322950... |
| D | 78 | 13 | 0.013024226874516027... |

Summing gives the exact displayed logarithmic \(\Delta\), and \(H(H)=H_*+\log_2 29-\Delta\). For any one fixed signed-minor direction \(v\), entropy is concave in its scalar \(\lambda\) on the closed nonnegativity interval, so its minimum over that one-dimensional direction occurs at an interval endpoint. The four chosen \(\lambda\) are each the better endpoint *for that selected block*; the four blocks do not interact because their supports are disjoint.

## Reproducible full exact-integer certificate (Python 3 standard library)

The program regenerates the complete canonical finite translation-class/orbit index, all four integer determinant kernels, all six profile-sum equations and all 145 positional equations in each block. It checks exact rational probabilities, support separation, and the signed-minor counts; numerical logarithms are used only for the reported decimal entropies.

~~~python
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
from math import log2

p=29
full=(1<<p)-1
def rot(m,t):
    t%=p
    return (((m<<t)|(m>>(p-t)))&full) if t else m
def norm(m):
    return min(rot(m,t) for t in range(p))
def mul(m,a):
    return sum(1<<((a*x)%p) for x in range(p) if (m>>x)&1)

reps=sorted({norm(sum(1<<x for x in ss)) for ss in combinations(range(p),5)})
assert len(reps)==4095
where={c:i for i,c in enumerate(reps)}
seen=set()
orbits=[]
for c in reps:
    if c in seen:
        continue
    indices=sorted({where[norm(mul(c,a))] for a in range(1,p)})
    orbit=[reps[i] for i in indices]
    assert not (set(orbit)&seen)
    seen.update(orbit)
    orbits.append(orbit)
assert len(orbits)==150 and len(orbits[7])==28
shapes=[tuple(x for x in range(p) if (c>>x)&1) for c in orbits[7]]

groups=[
    ([5,6,17,16,15,0],Fraction(-1,2),(-4,2),90,18),
    ([20,3,18,22,21,1],Fraction(1,2),(-2,4),112,18),
    ([24,19,8,2,14,12],Fraction(-1,4),(-5,4),112,3),
    ([11,27,4,25,13,26],Fraction(1,2),(-2,3),78,13)
]
assert len({j for ids,*_ in groups for j in ids})==24
perms=list(permutations(range(5)))
signs=[(-1)**sum(pi[i]>pi[j] for i in range(5) for j in range(i+1,5))
       for pi in perms]
a=Fraction(34881288,3324255613)
assert a==Fraction(139525152,28*474893659)

total=0.0
for ids,lam,rng,nonzero,zero_outputs in groups:
    cs=[shapes[j] for j in ids]
    V=[]
    for x in range(6):
        cols=[j for j in range(6) if j!=x]
        row=[0]*p
        for pi,sg in zip(perms,signs):
            k=sum(cs[cols[pi[i]]][i] for i in range(5))%p
            row[k]+=(-1)**x*sg
        V.append(row)
    flat=[v for row in V for v in row]
    assert (min(flat),max(flat))==rng
    assert sum(v!=0 for v in flat)==nonzero
    assert sum(1+lam*v==0 for v in flat)==zero_outputs
    assert all(1+lam*v>=0 for v in flat)
    assert all(sum(row)==0 for row in V)
    assert all(sum(V[x][(s-cs[x][i])%p] for x in range(6))==0
               for i in range(5) for s in range(p))
    # These are *exact* mass and positional-probability preservation.
    assert all(sum(a*(1+lam*v)/p for v in row)==a for row in V)
    assert all(sum(a*lam*V[x][(s-cs[x][i])%p]/p
                   for x in range(6))==0
               for i in range(5) for s in range(p))
    counts=Counter(flat)
    gain=float(a)/p*sum(n*float(1+lam*v)*log2(float(1+lam*v))
             for v,n in counts.items() if 1+lam*v>0)
    total+=gain

Hstar=7.869745624309653
baseline=Hstar+log2(p)
assert abs(total-0.05789285667935809)<1e-13
assert abs((baseline-total)-12.669833762757866)<1e-12
print("r355 PASS: four independent blocks, exact profile masses,"
      " five uniform position margins, gain",total,
      " ordered entropy",baseline-total)
~~~

This certificate is exact for the combinatorial, polynomial-coefficient, rational mass and marginal identities. Entropy decimal values are evaluated from an exact real-log expression. It relies on r347/r348/r352 for the pinned global minimax value and 350 prescribed profile masses, not on a new LP solve.

## Attribution, scientific bounds and continuation

Original OAI7 Task: RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19, original contributor EM-EMF6D046-5A2844. Previously saved author-side sources include r347@12bd331ea2aef70cc844682db432a623b235e726, r352@c660dc487bbb5f96789a3b2876ed82c32245eecf, r353@39b1a628bede82ecb87683e615321334432549b7 and r354@136f393f16b9fa10ec9bd8bb7835dcfbf8387b7a. This is shared-context mathematical work, not a claim of Native independent acceptance, source Activity linkage, Task completion or native-X6 carrier compatibility.

Remaining mathematical target: determine the true constrained minimum of joint entropy under exact minimax failure law and all five exactly uniform ordered-coordinate marginals. A larger coupled transport over the 350 profile atoms may improve the present constructive upper bound; the r352 profile-entropy lower bound is still valid.
