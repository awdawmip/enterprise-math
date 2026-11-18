# OAI7 r338 — Exact equal-weight auxiliary-seed criterion for shared-shift codebooks

Date: 2026-11-18. Evidence class: new author-side finite combinatorial proof (an extension of r337), with a reproducible small witness. This is not an independent Native review, a frozen Native Result, formal Source/Activity association, canonical Task completion, or a native X6 transfer. Preserve original researcher EM-EMF6D046-5A2844 and the authorship of r307, r329–r337.

## Exact model and theorem

Let Σ be a finite alphabet and let C=(W_1,...,W_M) be **pairwise distinct** n-element subsets of Σ, with 1<=n<=|Σ| and M>=1. Set d_a=#{i:a in W_i}; zero-degree symbols are allowed. Independently draw I uniformly from [M] and R uniformly from [t], where t is a positive integer. A deterministic decoder f(i,r) must output a permutation H=(H_0,...,H_{n-1}) of the n distinct symbols of W_i. We allow two seed values to give the same permutation. Require **exact equality of the complete marginal laws** L(H_l) for all l.

**Theorem (uniform auxiliary seed).** Such a deterministic decoder exists if and only if

```text
n divides t*d_a for every symbol a.
```

Writing g=gcd(n,{d_a:a in Σ}), the **least feasible number of equally likely auxiliary seed slots** is

```text
t_min = n/g.
```

Here gcd includes zero degrees in the usual way; n>=1 makes g>=1. For this t_min there is a finite, explicit matching-based construction. In particular,

```text
H(H) = log M + H(H|I) <= log(M*t_min).
```

Logs are natural. The bound concerns Shannon entropy of the sampled vector, not public codebook-description bits. **t_min is a cardinality optimum for an independent *uniform* auxiliary seed**. It is not a lower bound for Shannon entropy under nonuniform or row-dependent randomization.

### Necessity

For each a and column l, let c_(a,l) be the integer count of pairs (i,r) for which the l-th symbol of f(i,r) is a. Uniform (I,R) gives P(H_l=a)=c_(a,l)/(Mt). Since every one of the t orderings for row i uses a exactly once if a in W_i, the total over columns is sum_l c_(a,l)=t*d_a. Equality of full column marginals forces c_(a,l)=t*d_a/n for every l. These counts are integers; hence n|t*d_a for each a.

The simultaneous divisibility conditions are equivalent to n/g | t: for any prime-power q^e dividing n, the largest power of q that divides every d_a is q^f (capped at e); n|t*d_a for all a then requires q^(e-f)|t. Equivalently use Bezout on g=gcd(n,d_a for all a).

### Sufficiency and constructive algorithm

Make Mt labeled left vertices (i,r), one for each row/seed pair, each carrying all n incidences to the symbols in W_i. Symbol a appears in exactly t*d_a incidences. As n|t*d_a, split these incidences arbitrarily into groups of size n, giving (t*d_a)/n separate right-side clones of a. Left degree and right degree are both exactly n, and there are exactly

```text
sum_a (t*d_a/n) = Mt
```

right vertices. The graph is an n-regular bipartite multigraph (in fact there is at most one incidence from a fixed labeled row to a fixed clone). Its edges admit a decomposition into n perfect matchings. For each column l, the l-th matching selects the unique edge at each left vertex (i,r), and we put that edge's original symbol in position l of f(i,r).

Each left vertex uses its n *distinct* symbols once; every right clone supplies one appearance in every position; hence c_(a,l)=t*d_a/n for all a,l. Thus all position distributions are identical exactly, with no approximation or asymptotics. A standard bipartite matching algorithm repeated n times constructs the orderings.

Pairwise distinct unordered rows ensure that I can be recovered from H, so H(H)=log M+H(H|I). As H is a function of (I,R), H(H|I)<=log t.

### Explicit finite witness where the improvement is strict

Take n=4, M=5, alphabet {A,B,C,D,E,F} and five unordered rows:

```
W1=BCDF  W2=ACDF  W3=ABDE  W4=ABCE  W5=ABCD.
```

Degrees are d_A=d_B=d_C=d_D=4 and d_E=d_F=2. Thus g=gcd(4,4,4,4,4,2,2)=2, and t_min=2. One explicit pair of permutations per row is:

```
row       R=0      R=1
W1        CDBF     BCFD
W2        DFCA     FADC
W3        DBAE     ADEB
W4        ECBA     CEAB
W5        BADC     ABCD
```

For **every** one of the four columns, among these ten ordered rows each of A,B,C,D appears exactly twice and each of E,F appears exactly once. Hence each column has exactly the same law (probability 1/5 for each of A,B,C,D and 1/10 for E,F). A single deterministic ordering per row is impossible because 4 does not divide d_E=2. The construction uses t=2 rather than the generic t=n=4 cyclic-rotation seed.

As checks: for the r335 codebook of all n+1 complements of one symbol, every used d_a=n and g=n; hence t_min=1, recovering r337. For n=2 and C=({a,b},{b,c}), degrees (1,2,1) give g=1 and t_min=2.

## Interface to OAI7 / r330 and research consequence

The decoder changes only the **order** of a chosen unordered n-shift set. Every indicator V_(W_i)(K) used in r329/r330/r333, the exact all-fixed-K quantifier order, and every signed-coordinate negative-shift symmetry therefore remain unchanged. Embedding each output symbol into its chosen integer representative and then the same diagonal integer displacement makes equality of the *complete integer-valued single-position displacement laws* immediate. Independent Y then preserves complete terminal lattice-marginal equality. This recycles the external finite-group covering certificate as a **conditional scientific input** rather than independently accepting it.

For any fixed r330-type uniform distinct-row codebook, the universal cyclic ordering uses t=n. The theorem sharpens the implementation question to the concrete arithmetic invariant g of that actual codebook: whenever g>1, one may replace the n-way independent uniform rotation by a t=n/g-way uniform auxiliary seed with unchanged all-K coverage, saving **log g** in the upper bound log(Mn/g). When g=1, the n-slot uniform auxiliary seed is already *branch-count optimal in this precise independent uniform-seed class*. More general nonuniform conditional orderings remain possible and are not excluded by the theorem.

No general claim is made that the specific r330 covering codebook has g>1, that a smaller Shannon entropy is impossible, or that the original Gaussian-prime/X6 transfer has been implemented. The useful next discriminating step is to calculate the incidence gcd and degree profile of a **verified actual** covering codebook (or construct a family with prescribed g), before claiming entropy savings.

## Provenance / original objects

- OAI7 formal task: RS-OAI7-028-C-20261007-6F2A81; immutable publication TP2-96FAC49786245691AE19. Historical researcher EM-EMF6D046-5A2844.
- r337 exact t=1 criterion and conditional r330 incidence application: cf352564a8f985fbc3151783fa0ee74f1a0b2a7f, `research_notes/portable_direct/2026-11-18_oai7_driver_zero_overhead_equal_marginal_codebook_criterion_r337.md`, blob e78dceae768b2af23d8e491a736f3994fcf46df6.
- r330 fixed-index conditional covering-codebook construction: 67f57ab662493b6744df560c8358a293a08d1165, `research_notes/portable_direct/2026-11-18_oai7_driver_fixed_index_nonuniform_codebook_sharp_loglog_r330.md`.
- New contribution r338: exact t-copy degree divisibility and its minimal uniform auxiliary-seed count, constructive matching reduction, and fully checkable n=4,t=2 witness.
- Review boundary: this continuation has access to author-side r329/r330/r337 inputs and is not an independent decisive Native review of their mathematical validity. No CLAIM, DA, Result acceptance, activity attribution or Task completion is inferred from this GitHub scientific preservation.
