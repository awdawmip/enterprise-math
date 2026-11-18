# OAI7 r344 — Slope-tube avoidance and existence of exactly regular, entropy-minimal codebooks macroscopically far from every progression orbit

Date: 2026-11-19. Evidence: new exact finite-combinatorial author-side argument. It continues r339 and r341–r343 but does not certify the all-K small-list tail, native X6/Port/Link transport, independent Native Result review, Source/Activity admission or formal Task completion. Original researcher EM-EMF6D046-5A2844 and all prior contributors remain attributed. This Driver context shares author-side work and is not a clean independent reviewer.

## 1. Every fixed progression slope has a universal bad-test witness near its orbit

Let p be prime, 1<=u,n<p, n+u-1<p, and h>=0 an integer. Write I_v={0,...,v-1}, T=p^(3/4), B=p-(n+u-1), and
```
D=(h+1)*(B-T)/u,
A_(a,t)=t+a*I_n,  K_a=a*I_u,  a in F_p^*, t in F_p.
```
Assume B>T. For any probability distribution P on n-element subsets C of F_p, define its worst deterministic test-set failure
```
q(P)=max_(|K|=u) P_C{ V_C(K;h)>T }.
```
Then for **each fixed nonzero slope a**,
```
P_C{exists t in F_p with |C\A_(a,t)| < D} <= q(P).        (344.1)
```
In particular, no predetermined pairing between the random row C and its reference translation is necessary for the r343 obstruction. It is a bound on the entire *union of p translation tubes* for one given slope, witnessed by the **single same deterministic test set** K_a.

**Proof.** For every t, K_a-A_(a,t) is an affine image of the n+u-1 consecutive-residue interval, so its complement has B points. Apply the r343 multiplicity bound to W=A_(a,t) and K=K_a. If |C\A_(a,t)|<D then V_C(K_a;h)>=B-u|C\A_(a,t)|/(h+1)>T. This implication holds for all t with the same K_a. Thus the union over t is a subset of the one fixed-K_a failure event; take probabilities and then the maximum over deterministic K. QED.

Averaging (344.1) over all a also yields
```
E_C[ (1/(p-1))*#{a!=0: exists t, |C\A_(a,t)|<D} ] <= q(P).  (344.2)
```
The order is important: this average-slope conclusion does not say that a row has no close progression of **any** slope. It supplies the correct quantitative interface for selecting a potentially pseudorandom candidate.

## 2. Uniform random n-sets are exponentially unlikely to lie near any length-n progression

For any 0<rho<1, take integer
```
m=floor((1-rho)*n)+1,
```
and assume m<=n. Let U be uniformly random among all n-element subsets of F_p. Then
```
P_U{exists a!=0, t: |U\A_(a,t)| < rho*n}
  <= p*(p-1)*binom(n,m)*(n/p)^m.                            (344.3)
```
**Proof.** Fix A=A_(a,t), an n-set. The event |U\A|<rho*n forces |U intersect A|>n-rho*n, hence at least m elements of A. If S is an m-element subset of A, then
```
P(S subset U) = (n)_m/(p)_m <= (n/p)^m.
```
Take a union over the binom(n,m) possible S and then the p(p-1) affine progressions. QED.

At n=c_*sqrt(p)(log p-2log log p+d)+O(1), for fixed d and c_*>0, the right side in (344.3) has logarithm at most
```
-((1-rho)*c_*/2+o(1))*sqrt(p)*(log p)^2.                   (344.4)
```
In particular, a uniform n-set is far, by an arbitrary fixed fractional replacement radius rho<1, from **every** nonzero-slope length-n arithmetic progression with probability tending to one extremely rapidly. The estimate uses only a union bound and exact uniform-subset containment; it makes no claim about the all-K tail.

## 3. Exactly n-regular p-row codebook, deterministic equal marginals and H(H)=log p, with all rows far from every progression

For each prime p and 1<=n<p, begin with the interval-translation incidence design R_t=t+I_n, t in F_p. Select one common permutation sigma of the p field symbols and define
```
C_t=sigma(R_t),  t in F_p,
H^(t)=( [sigma(t+j)]_p : j=0,...,n-1 ),
```
where [.]_p denotes an integer representative and t is uniformly random from F_p. This does **not** assume sigma is an additive homomorphism.

For any sigma, the p rows are pairwise distinct n-sets and each symbol occurs in exactly n rows. Each position H_j is individually uniform on the same p integers, hence all complete integer displacement marginal laws are equal; the joint vector identifies t from its first entry and
```
H(H)=log p.                                                 (344.5)
```
The same equality holds after embedding each H_j diagonally in Z^k. For independent lattice Y, all full-lattice Y+H_j marginal laws agree. All signed modular terminal coordinate marginals are uniform, although the r307 small-list tail is an *additional* property.

Moreover, if sigma is itself uniformly random among all p! label permutations, every fixed C_t is uniformly distributed over n-subsets of F_p. Thus a union bound over all p rows and all p(p-1) progressions gives
```
P_sigma{exists row t, slope a!=0, translate s:
          |C_t\(s+a*I_n)| < rho*n}
 <= p^2*(p-1)*binom(n,m)*(n/p)^m.                          (344.6)
```
At the sharp OAI7 length n=ceil(c_*sqrt(p)(log p-2log log p+d)), the RHS tends to zero with the same leading negative exponent (344.4), since the extra factor p only adds log p. Therefore, for all sufficiently large primes, **one fixed common permutation sigma exists** such that all p rows simultaneously satisfy
```
min_(a!=0,s) |C_t\(s+a*I_n)| >= rho*n  for every t in F_p.  (344.7)
```
This codebook has *exactly n-regular incidence, distinct rows, no auxiliary ordering seed, full-position marginal equality, and random-vector entropy exactly log p*, even while every row is macroscopically far from all arithmetic-progression orbits.

**Proof.** Each preimage symbol appears in exactly n translates R_t; relabeling preserves every incidence count and distinctness. For fixed j, t+j ranges uniformly over F_p; applying sigma preserves uniformity, proving the position marginals. The full vector identifies t via its first entry because sigma is injective. For uniform sigma, sigma(R_t) is a uniform n-set for each fixed t; no row independence is needed for the union bound (344.6). The asymptotics imply a choice of sigma avoiding all listed events. QED.

## 4. Scientific discrimination and exact open remainder

r343 shows that at the OAI7 threshold any q=o(1) codebook must be far from a *designated* interval orbit, with relative edit distance at least b-o(1), b=17/64. Equation (344.1) strengthens this to proximity to **any translated progression of each fixed slope**. Equations (344.3)–(344.7) independently show that regularity, exact entropy log p, complete position marginal equality, and even distance >=rho*n from *every* progression (for any fixed rho<1) are simultaneously realizable.

Thus the unexplored decisive property is the *additive all-fixed-K small-list tail* of a genuinely nonlinear relabeling sigma; ordinary incidence regularity, row separation and entropy are already achieved in this family. An arbitrary label permutation does not commute with the additive start x and is not known to preserve r307's V_C(K;h). Neither positive nor negative all-K attainment is asserted here. A useful next experiment is to evaluate V_(sigma(t+I_n))(K) across K families and random sigma, while retaining the exact row/position constraints.

Provenance: r307 integrated tail transfer (baaaabaacaf8543f62a45a00cdfcf03e95389075), r329 phase threshold (f1f35331daf48fbbbe01d8cf0cd43342dff85c01), r330 existential codebook (67f57ab662493b6744df560c8358a293a08d1165), r339 p-row degree/entropy saturation (b7bd6de6e1381fd04b0b37c16a56f14cea3b92f2), r341 near orbit regular witness (df916dc0b6f453c9cc87df3f67c75d8e8e16ee9b), r342 sharp edit-Lipschitz (b8790284f7e1ee102b5de27d2060004518e52912), r343 threshold-multiplicity barrier (4d77356d854c26066f745ce1ee94c3257ca14ad8). Original Task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19, parent OBJ-OAI7-RESEARCH-TRANSFER-20261007. The actual Source runtime/CLAIM, independent Native reviewer and Activity association remain separate.


## 5. Finite all-slope certificate at p=101 (separate from the asymptotic theorem)

A deterministic Python 3 check of the nonlinear common-permutation construction at p=101, n=8, random.Random(20261119).shuffle(permutation) found 101 pairwise-distinct rows with every field symbol incident to exactly 8 rows. Exhaustively comparing each of the 101 rows against all 101*100 nonzero-slope, translated 8-term arithmetic progressions gives **minimum swap distance 3**. Rowwise minimum-distance multiplicities are 3:4 rows, 4:85 rows and 5:12 rows. This is a genuine finite exactly 8-regular, `H(H)=log 101`, equal-position-marginal design, all of whose rows are >=3 swaps from *every* arithmetic progression. It is not a check of the all-K tail.

Python 3 reproducibility:
```python
import random
p,n=101,8
sigma=list(range(p))
random.Random(20261119).shuffle(sigma)
progressions=[sum(1<<((s+a*j)%p) for j in range(n))
              for a in range(1,p) for s in range(p)]
rows=[sum(1<<sigma[(t+j)%p] for j in range(n)) for t in range(p)]
assert len(set(rows))==p
assert all(sum((row>>v)&1 for row in rows)==n for v in range(p))
d=[min(n-(row&ap).bit_count() for ap in progressions) for row in rows]
assert min(d)==3
assert {k:d.count(k) for k in set(d)}=={3:4,4:85,5:12}
```
