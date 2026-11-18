# OAI7 r343 — Multiplicity-sensitive orbit obstruction: at the sharp length, a positive fraction of each interval row must be replaced

Date: 2026-11-19. Evidence status: new exact author-side finite-group lemma and OAI7 asymptotic consequence. This is a continuation of the r341–r342 orbit-edit analysis, not a clean independent Native Result review or Source/Activity admission. Original OAI7 researcher EM-EMF6D046-5A2844 and all r307, r329–r342 contributors retain their own attribution.

## 1. Exact multiplicity-sensitive lower bound

Let G be a finite abelian group, let K,W,C be subsets, |K|=u>=1, and h>=0 be an integer. Define
```
N_C(x;K)=#{c in C : x+c in K},
V_C(K;h)=#{x in G : N_C(x;K)<=h},
r=|C\W|,
B=|G|-|K-W|, where K-W={k-w:k in K,w in W}.
```
Then
```
V_C(K;h) >= B-floor(u*r/(h+1)).                         (343.1)
```
Moreover if r<=h, then
```
V_C(K;h) >= B.                                            (343.2)
```
This holds whether or not |C|=|W| and does not require primality, distinct-codebook rows or random independence. If |C|=|W|, r counts element swaps. For h=0 it recovers the near-orbit bound of r342; for h tending to infinity it adds a decisive multiplicity factor.

**Proof.** Write E=G\(K-W), so |E|=B. For x in E and any w in W, x+w notin K, so N_W(x;K)=0. Consequently
```
N_C(x;K)=#{c in C\W : x+c in K},   x in E.
```
On summing over E, each of the r new shifts c contributes to at most u starts x, and therefore
```
sum_(x in E) N_C(x;K) <= r*u.
```
Let T={x in E:N_C(x;K)>h}. Every x in T contributes at least h+1 to that sum; thus |T|<=floor(ru/(h+1)). All remaining points of E are counted by V_C, giving (343.1). If r<=h, then N_C(x;K)<=r<=h for *each* x in E, proving (343.2). QED.

The bound has an exact integer floor; it is a counting proof with no approximation or project-specific axiom.

## 2. Stronger near-orbit threshold and all-K implication

Fix p prime, 1<=u,n<p, n+u-1<p, W={0,...,n-1} and the deterministic test K={0,...,u-1} in F_p. Then |K-W|=n+u-1 and B=p-(n+u-1). Let C_t be any p labeled n-element rows (possibly an exactly n-regular incidence design), compared to W+t, and put
```
r_t=|C_t\(W+t)|,
T_p=p^(3/4),
D_mult=(h+1)*(B-T_p)/u.
```
When B>T_p, (343.1) implies
```
q_p := max_(|K'|=u) Pr_(t uniform){V_(C_t)(K';h)>T_p}
     >= #{t:r_t<D_mult}/p.                              (343.3)
```
Therefore
```
q_p<=zeta  =>  #{t:r_t>=D_mult}>=(1-zeta)*p
                   and sum_t r_t>=(1-zeta)*p*D_mult.     (343.4)
```
It also follows directly from (343.2) that any row with r_t<=h remains bad whenever B>T_p.

**Proof.** Translate both W and its starting points. The outside set for W+t and the fixed K has the same cardinality B. Apply (343.1) rowwise. For r_t<D_mult,
```
B-u*r_t/(h+1)>T_p,
```
so V_(C_t)(K;h)>T_p. This single fixed K works simultaneously for every qualifying t; hence its bad-row fraction lower-bounds q_p, giving (343.3). Counting the complementary rows proves (343.4). QED.

Unlike a bound based only on the symmetric difference, (343.1) uses the actual required number h+1 of distinct shift hits needed to turn an originally empty start into a good start.

## 3. Fixed-index OAI7 sharp-second-order consequence

In the r329–r330 external finite cyclic model, take
```
b=17/64,  c_*=[4(1-b+b*log(b))]^{-1},
u=ceil(sqrt(p)),
n=ceil(c_*sqrt(p)*(log(p)-2log(log(p))+d)),
h=floor(b*n*u/p)
```
for fixed real d and sufficiently large prime p. In this regime n+u=o(p), T_p=o(p), and mu=n*u/p ~ c_*log(p) tends to infinity. In particular,
```
D_mult/n
= [(h+1)/(n*u/p)] * [(B-T_p)/p]
--> b = 17/64 = 0.265625.                              (343.5)
```
Hence, for every p-row ensemble obtained by editing the designated interval orbit, if its worst deterministic u-test-set tail satisfies q_p=o(1), then at least (1-o(1))p rows require
```
r_t >= (17/64-o(1))*n,                                 (343.6)
```
and its total edit mass obeys
```
sum_t r_t >= (17/64-o(1))*p*n.                         (343.7)
```
The required modification per typical row is a **positive 26.5625% asymptotic fraction of the entire n-element shift set**, strengthening r342's order-sqrt(p) edit-distance floor. The claim concerns one designated interval-translation orbit (and, by affine relabeling with an allowed common nonzero difference, the corresponding arithmetic progression orbit). It is not a universal obstruction to all regular p-row designs or to r330's independently constructed all-K codebooks.

At the OAI7 second-order scale, h is of order log p, so (343.1) is stronger than the general r342 one-sided ur bound by a factor of order log p. This is a refinement of the same scientific question, not a change of the underlying task or of r307's tail criterion.

## 4. Independent finite checks of the counting lemma

An exhaustive script checked (343.1) and (343.2) for every K subset F_7 of sizes 1,2,3, every W,C subset F_7, and h=0,1,2: **3,096,576** (K,W,C,h) comparisons all passed. A separate p=101 instance with W={0,...,39}, K={0,...,10}, h=1 and C=(W\{20}) union {70} has V_W=V_C=53 and B=51, illustrating the exact r<=h stability on the outside set. The proof above is universal; these checks are regression coverage.

Python 3 reproducer:
```python
from itertools import combinations

def V(p,K,A,h):
    return sum(sum((x+a)%p in K for a in A)<=h for x in range(p))

p=7
Ss=[set(z) for m in range(p+1) for z in combinations(range(p),m)]
count=0
for u in (1,2,3):
    for z in combinations(range(p),u):
        K=set(z)
        for W in Ss:
            E={x for x in range(p)
               if all((x+w)%p not in K for w in W)}
            B=len(E)
            for C in Ss:
                r=len(C-W)
                for h in (0,1,2):
                    assert V(p,K,C,h)>=B-(r*u//(h+1))
                    if r<=h:
                        assert V(p,K,C,h)>=B
                    count+=1
assert count==3096576
```

## 5. Source relations and remaining frontier

- r341 original non-orbit regular counterexample and conservative 2ur barrier, GitHub commit `df916dc0b6f453c9cc87df3f67c75d8e8e16ee9b`. Its equal lattice marginal, exactly n-regular incidence and q=1 witness are unchanged.
- r342 one-sided ur exact edit bound, GitHub commit `b8790284f7e1ee102b5de27d2060004518e52912`. r343 adds threshold multiplicity (h+1) on the originally empty complement, crucial for the r329 second-order model.
- r329 sharp hypergeometric/Johnson slice estimates, commit `f1f35331daf48fbbbe01d8cf0cd43342dff85c01`; r330 all-fixed-K existential codebook commit `67f57ab662493b6744df560c8358a293a08d1165`. These mathematical existence/threshold statements are left at their actual author-side evidence status.
- Original formal Task `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`, parent `OBJ-OAI7-RESEARCH-TRANSFER-20261007`. Native Result/review and X6/Link/Port realizations remain independent obligations.

**Next useful test:** seek an exactly n-regular p-row all-K codebook whose typical rows differ from each obstructed progression orbit in a genuinely macroscopic fraction, then inspect whether deterministic position orderings preserve the original entropy budget. The present bound identifies a quantitative structural separation required of any such near-orbit attempt.
