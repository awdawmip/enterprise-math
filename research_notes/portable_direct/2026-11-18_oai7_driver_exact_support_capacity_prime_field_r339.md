# OAI7 r339 — Exact output-support capacity and prime-field rigidity for uniform-seed schedules

Date: 2026-11-18. New author-side combinatorial deduction building on r337–r338; finite proof, no Native Result admission or independent reviewer validation. Original OAI7 researcher EM-EMF6D046-5A2844 and all previous source contributors retain their attribution.

## Model

Keep the r338 codebook model: C=(W_1,...,W_M) comprises **pairwise distinct** n-element subsets of an alphabet Σ; I~Uniform([M]), R~Uniform([t]), independent; H=f(I,R) is an ordering of W_I (n different symbols). Let A=union_i W_i, m=|A|, d_a=#{i:a in W_i}. Assume the *entire single-position laws* of H_0,...,H_(n-1) coincide. There is no assumption that these marginals are uniform over A.

## Theorem 1: Exact support-capacity inequality and equality classification

Always

```text
M*t >= m.                                      (339.1)
```

If equality holds, then necessarily

```text
t divides n,   d_a=n/t for every a in A,        (339.2)
```

and the common position marginal is **uniform on A**, with exactly one appearance of each a in each column of the Mt labeled micro-rows.

Conversely, if the codebook is **regular**, with d_a=d for every a in A, and d is a positive divisor of n, then t=n/d satisfies Mt=m and one can construct a valid decoder by r338's explicit regular-bipartite matching decomposition. Every one of the Mt ordered outputs is then different, hence H is uniform on m ordered schedules and

```text
H(H)=log m.                                    (339.3)
```

The equality in (339.3) is a property of this capacity-saturating class, not a general lower bound on entropy for arbitrary equal-marginal codebooks.

### Proof

For each a,l let c_(a,l) count (i,r) pairs producing symbol a in column l. Exact common marginals and the fact that a occurs exactly once in each of t copies of every row containing it force

```text
c_(a,l) = t*d_a/n  (a in A, all l).
```

These are **positive integers**. For any one column l, summing its Mt labeled outputs gives sum_(a in A) c_(a,l)=Mt. Since there are m used symbols and each summand is >=1, Mt>=m. Equality forces all c_(a,l)=1, hence t*d_a=n for every a, implying t|n and regular degrees d=n/t. It also makes the position marginal 1/m for every symbol.

For the converse, count all incidences: M*n=m*d; with t=n/d, obtain M*t=m. Now t*d_a=n for every a, so r338 constructs equal column marginals. As c_(a,l)=1, two different labeled (i,r) pairs cannot produce the same ordered output (otherwise their first-column symbols would be counted twice). Their Mt=m images are distinct, equiprobable, and (339.3) follows. QED.

An equivalent statement is that capacity saturation is precisely a resolvable regular codebook incidence design: each field element/symbol appears in every column exactly once across the labeled schedules.

## Corollary 2: Prime-field rigidity at exact capacity

Let A=F_p, where p is prime, and 1<=n<p. In the same uniform independent-seed model, equality Mt=p is possible **only** at

```text
M=p, t=1, and d_a=n for every a in F_p.         (339.4)
```

Conversely every p-row distinct n-subset codebook of incidence degree n admits a deterministic equal-marginal ordering, by r337.

Indeed, the equality theorem gives t|n, so t<p. Since the positive integers M and t multiply to the prime p, necessarily t=1 and M=p; the degree statement follows. This is an exact arithmetic constraint, **not** an assertion that O(log p) entropy can be achieved only with p rows when Mt>p, or that nonuniform row weights obey the same conclusion.

## Corollary 3: A sharp example and its all-K limitation

For any nonempty proper n-subset W of F_p and any fixed enumeration W={w_0,...,w_(n-1)}, take the p distinct translates W_i=W+i, i in F_p, and define

```text
H^(i)=(w_0+i,...,w_(n-1)+i),  I uniform in F_p.
```

The translates are distinct because in the additive group of prime order p a nonempty proper set has no nonzero translation stabilizer. Each a belongs to n translates, so d_a=n. For each position l, H_l is uniform on F_p. Thus t=1, Mt=p and H(H)=log p, attaining (339.1) exactly.

However, for any deterministic u-set K and any threshold h,

```text
V_(W+i)(K) = V_W(K), for every i,
```

because the number of bad starting points is invariant under translating the shift set. Therefore, under this translation-orbit distribution, for each fixed K,

```text
P_I{ V_(W+I)(K)>p^(3/4) } in {0,1}.
```

Once the target q_c<1, its all-fixed-K covering requirement is equivalent **within this translation-orbit family** to the existence of one base set W satisfying V_W(K)<=p^(3/4) for *every* deterministic K. That universal deterministic covering problem remains open at the sharp r329/r330 second-order length; equality of marginals and entropy log p alone do not settle it.

A more general p-row regular design with d_a=n need not be a translation orbit, so this 0/1 statement is asserted only for the explicit orbit class.

## Research implication and exact scope

r338 reduces equally weighted auxiliary randomness to t_min=n/gcd(n,d_a). Equation (339.1) provides the complementary support-capacity bound; together they specify the combinatorial resources needed for entropy-efficient **uniform-seed** implementations. For the OAI7 external finite cyclic problem, an all-fixed-K covering codebook of p distinct rows, each residue of degree n, would admit exact complete integer-lattice marginal equalization with no auxiliary random ordering and H(H)=log p. Whether such a degree-regular all-K design exists at the r329 second-order threshold is a distinct constructive/existence question.

All covering implications here are conditional on the exact r329/r330 pinned external finite-group estimates and their distinct shift/quantifier hypotheses. No Gaussian-prime or native signed X6 Link/Port path is claimed.

## Source and contributor provenance

- OAI7 original task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19, researcher EM-EMF6D046-5A2844.
- r337: cf352564a8f985fbc3151783fa0ee74f1a0b2a7f; zero-auxiliary randomness incidence criterion.
- r338: ef08b7b5dbdb489647fc70e1f88f7a714cec991f, `research_notes/portable_direct/2026-11-18_oai7_driver_uniform_auxiliary_seed_exact_divisibility_r338.md`; uniform t-copy matching and gcd formula.
- r329: f1f35331daf48fbbbe01d8cf0cd43342dff85c01; external second-order coverage phase analysis. r330: 67f57ab662493b6744df560c8358a293a08d1165; conditional all-fixed-K codebook.
- New r339: Mt>=m support-capacity theorem, exact equality characterization, prime-field saturation rigidity and translation-orbit 0/1 reduction. Author-side mathematical work; Native independent review, Source/Activity association and formal Task closure are separate.
