# R284BF — Target-degree Sidon packing: cubic-exponent deterministic one-scalar Port decoding

Date: 2026-11-20 (Asia/Shanghai). State: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Parent result: R284BE shared-cofactor-block one-read decoder; original scientific scope and frozen inputs inherited from R284BD. Independent portable mathematics, with no new native Task CLAIM, Result, Review or P000/worldview edit.

## Theorem BF1: O(n³) maximum radix exponent

For every n≥3 and known H≥2, an unknown strictly positive integer matrix C∈{1,…,H}^{n×n} can be recovered exactly, in deterministic polynomial bit time, from one observation

```
y=det(diag(d_0,…,d_{n−1})−C−Σ_{i=1}^{n−1}z_i E_{0i}).
```

Choose p as the first odd prime ≥n and put

```
a_j=2pj+(j² mod p),  0≤j<n; A=max_j a_j;
Q=2A+1; e_j=Q+a_j; S=Σ_j e_j; K=S+1;
d_j=b^{e_j}; z_i=b^{K+2a_i}  (1≤i<n).
```

The same exact coefficient decoder as R284BE recovers all n² entries. Both the maximum exponent of a controlled parameter and every exponent occurring in the readout are **O(n³)**, and control/readout bit lengths are

```
O(n³ · (n log n+n log(H+1)+log(1+δ)))
```

when the single reading is an exact rational number perturbed by unknown |ε|≤δ, with δ≥0 specified in advance. In the noiseless case omit the last logarithmic term.

This strictly improves R284BE's sufficient O(n⁴) exponent and R284BD's O(n⁵) exponent while keeping the same single simultaneous star-Port read and direct polynomial-time reconstruction.

## Key proof: only target degrees need isolation

R284BE used Q=nA+1 so that *every* subset cardinality had a disjoint band. Its decoder, however, extracts only:

* baseline F(d)=det(diag(d)−C): the coefficients obtained by deleting exactly one or exactly two diagonal variables from the top monomial;
* cofactor G_i(d) of the row-zero edit z_i: the coefficient obtained by deleting zero or exactly one additional diagonal variable from its top monomial.

All other coefficient collisions are immaterial to reconstruction.

### Baseline targets

Since every e_j lies in [Q,Q+A], the positive exponent **missing-sum** of a baseline monomial that deletes m diagonal variables belongs to [mQ,m(Q+A)].

For Q>2A the intervals for m=1 and m=2 are disjoint, and the m=2 interval lies strictly below the first m≥3 interval, because

```
Q+A<2Q,    2(Q+A)<3Q.
```

The m=0 exponent S is separate. Thus the target missing-one/missing-two coefficients cannot collide with any other degree. Within m=1 the omitted index is unique because a_j are distinct; within m=2 the omitted unordered pair is unique because R284BE proved the *complete* pair-sum Sidon property of a_j, including repeated-index pairs.

The exact target coefficients remain

```
at S−e_i:        −C_ii,
at S−e_i−e_j:    C_ii C_jj−C_ij C_ji,   i<j.
```

### Shared cofactor targets

From row-zero multilinearity,

```
y=F(d)+Σ_{i≥1}b^{K+2a_i}G_i(d).
```

For G_i, an additional deletion set W among {1,…,n−1}\{i} produces exponent

```
K+S−e_0−Q + a_i−|W|Q−Σ_{j∈W}a_j.
```

For |W|=0, the variable part is a_i∈[0,A]; for |W|=1 it is −Q+a_i−a_j∈[−Q−A,−Q+A]; all |W|≥2 have variable part at most −2Q+A. The bands do not overlap because Q>2A. Within |W|=0, i uniquely identifies the coefficient; within |W|=1, the nonzero ordered differences a_i−a_j are unique by the *complete* Sidon property, so no cofactor index pair collides.

Further, every G_i term has exponent ≥K>S, and every baseline term has exponent ≤S. Consequently all needed targets in both portions are isolated.

The exact cofactor coefficients are

```
at t_i+S−e_0−e_i:          −C_i0,
at t_i+S−e_0−e_i−e_j:    C_i0 C_jj−C_ij C_j0,
where t_i=K+2a_i, i,j≥1, i≠j.
```

They give C_i0, and together with R_0i=C_0i C_i0 give C_0i. Each C_ij for i,j≥1, i≠j is then recovered by dividing (C_i0 C_jj−g_ij) by C_j0. Since entries are strictly positive, the divisors are nonzero.

### Coefficient size, noise and runtime

Use the same total absolute coefficient bound L=n·n!·(1+H)^n. Choose b=2L+1 for exact reading; choose b=4L+8⌈δ⌉+9 for any specified rational |ε|≤δ. The lower-address tail and bounded perturbation remain strictly inside the nearest-integer digit cell, so balanced radix extraction returns the required coefficient exactly.

The quadratic Sidon construction has A=O(n²), so Q=O(n²), e_j=O(n²), S=O(n³), K=O(n³). Every parameter exponent is at most max_j(e_j,K+2A)=O(n³), and the largest nonzero determinant monomial exponent is less than K+S=O(n³). Exact arithmetic and O(n²) coefficient extraction are polynomial in these bit lengths.

### Architecture-relative lower bound (BF2)

Within the explicitly described **uniform target-degree guard family**—namely e_j=Q+a_j with min a_j=0, a_j distinct, all nonzero ordered differences distinct, and the sufficient guard requirement Q>2A—the cubic exponent order is optimal.

Indeed n(n−1)/2 positive pair differences a_j−a_i (i<j) are distinct integers in [1,A]. Thus A≥n(n−1)/2. The chosen guard requires Q>2A and separating the whole cofactor family above F requires K>S=Σ_j(Q+a_j)≥nQ. Therefore the highest star edit exponent K+2a_i is Ω(n³). Together with the construction this is Θ(n³) **for this guard architecture**. The lower bound does not assert optimality among other deterministic decoders or unrestricted one-read observers.

## Exact author-side evidence

The reusable R284BE decoder is called by the companion R284BF checker with the single scientific change Q=2A+1 (the old Q=nA+1 is not reused). The checker runs an independent *full target-address source census* over every baseline and all star cofactor subsets for 3≤n≤12, alongside exact determinant/reconstruction comparisons.

* 562 reconstructed matrices PASS: complete {1,2}^{3×3} domain (512) and 50 fixed-seed cases at n=3,…,6.
* 128 rational/integer bounded-error reconstructions PASS for δ=7000.
* Target address census PASS for each n from 3 through 12.
* Max parameter bits for H=2, comparing same b and exact controls: n=3, R284BE 1658 → R284BF 1271; n=4, 9553 → 5765; n=5, 22202 → 11038; n=6, 68709 → 28595.
* Finite checks are author-side; generality rests on the displayed proof. Independent scientific review remains NOT_REVIEWED.

Code: `research_notes/portable_direct/R284BF_sparse_target_guard_checker.py`.
Evidence: `research_notes/portable_direct/R284BF_target_guard_verification.json`.
Reuse: `research_notes/portable_direct/R284BE_shared_sidon_cofactor_checker.py`.

## Source discipline / next question

This concerns a *finite named/directed Port matrix observer*, retaining all off-diagonal direction and pair relations under the declared reconstruction map. No BRC/X6 native physics or P000 promotion is inferred. R284BF preserves the same inherited scientific pin and continuation lineage as R284BE.

Research next: search for a genuinely new packing architecture bypassing the uniform Q>2A separation, or an information/complexity lower bound for deterministic polynomial-time one-read recovery beyond this restricted family; quantify actual actuator amplitude, communication bits and quantized/noisy readout costs.
