# R284BE — Shared Sidon cofactor block: an O(n^4)-exponent one-scalar Port decoder

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Research lineage: R284AT → R284AX → R284BC → R284BD → R284BE. This is an independent, typed finite directed-Port observer construction; P000, native world dynamics, and formal task claims are unchanged.

## Proposition BE1 (deterministic shared-block packing)

For every integer n≥3, known H≥2 and unknown strictly positive integer matrix C∈{1,…,H}^{n×n}, consider exactly one scalar measurement

```
y = det(diag(d_0,…,d_{n−1}) − C − Σ_{i=1}^{n−1} z_i E_{0i}).
```

There is an explicit choice of nonnegative integer d_i,z_i and a deterministic exact decoder reconstructing every C_ij in time polynomial in n and the full binary input/output length. **The maximum control and readout bit length is O(n^4 log b)** where

```
log b = O(n log n + n log(H+1))
```

for exact readings. If the measurement is an exact rational `y+ε` with known finite bound |ε|≤δ, the same conclusion holds with an additional O(log(1+δ)) inside log b. This reduces R284BD's O(n^5 log b) maximum packing exponent to O(n^4), retaining one scalar observation, deterministic decoding and a specified worst-case error guarantee.

### 1. Complete two-sum Sidon property

Let p be the smallest odd prime p≥n; write a_j=2pj+(j² mod p), 0≤j<n, A=max_j a_j. In fact the a_j have **all unordered pair sums unique, including the pairs (i,i)**:

```
a_i+a_j = a_s+a_t,  i≤j, s≤t   ⇒   (i,j)=(s,t).
```

The quotient/remainder on division by 2p gives i+j=s+t and r_i+r_j=r_s+r_t because both residue sums lie in [0,2p). Modulo p we have i²+j²=s²+t², hence ij≡st mod p since p is odd. The two index multisets are the roots of the same quadratic over F_p. All indices are <p, proving equality as integer multisets. This strengthens the distinct-index pair statement used in R284BD.

Consequently **all ordered nonzero differences are distinct**:

```
a_i−a_j=a_s−a_t,  i≠j, s≠t   ⇒   (i,j)=(s,t).
```

Indeed a_i+a_t=a_s+a_j and the just-proved full Sidon property excludes the alternative i=j. A=O(n²), using p<2n.

### 2. One baseline block and one shared cofactor block

Put

```
Q=nA+1,   e_j=Q+a_j,   S=Σ_j e_j,   K=S+1,
d_j=b^{e_j},   z_i=b^{K+2a_i}  (1≤i<n).
```

Because the edits occupy only row zero, the determinant is affine in the z_i:

```
y=F(d)+Σ_{i=1}^{n−1}b^{K+2a_i}G_i(d),
F(d)=det(diag(d)−C).
```

Every monomial in F has exponent Σ_{j∈U}e_j ∈[0,S]. Every monomial in the cofactor term is at least K, so the two portions cannot collide.

The F coefficients at addresses

```
S−e_i:          −C_ii
S−e_i−e_j:      C_ii C_jj−C_ij C_ji  (i<j)
```

are isolated from every other monomial. For different cardinalities of U, the base offset Q exceeds any possible variation in the a_j sums; for cardinality n−1 the missing index is unique, and for n−2 the missing unordered pair is unique by the Sidon property.

The monomial support in G_i consists of subsets of the diagonal variables indexed by {1,…,n−1}\{i}. Its exponents have the form

```
K+S−e_0−Q + a_i − |W|Q − Σ_{j∈W} a_j,
W⊆{1,…,n−1}\{i}.
```

The different deletion cardinalities |W| are separated by Q>nA. At |W|=0 the address contains the unique a_i; at |W|=1 it contains a_i−a_j, unique among all ordered i≠j by the full Sidon difference property. Thus **all n−1 cofactor responses share one block** with no collisions at the required addresses. Specifically,

```
K+2a_i+S−e_0−e_i:            −C_i0
K+2a_i+S−e_0−e_i−e_j:       C_i0 C_jj−C_ij C_j0
                                    (i,j≥1, i≠j).
```

Other coefficient collisions, at addresses unused by the decoder, are permitted.

### 3. Bounded coefficients and exact decoding

Let L=n·n!·(1+H)^n. Direct determinant expansion bounds the **sum of absolute algebraic coefficients** of all baseline and edited cofactor monomials by L, including possible collisions after exponent packing.

For noiseless readings, choose odd b=2L+1. For a specified rational error bound δ≥0, choose odd

```
b = 4L + 8⌈δ⌉ + 9.
```

For each required address k, the lower-address tail after division by b^k is strictly bounded by L/(b−1); in the noisy case |ε|/b^k≤δ/b. Thus nearest-integer extraction at y/b^k (or (y+ε)/b^k) followed by taking the balanced residue modulo b returns exactly the algebraic coefficient at k. All required addresses are positive, and the error bound gives a strict margin from the half-integer boundary.

Read the n diagonal coefficients and the n(n−1)/2 two-index principal coefficients. Then read the n−1 leading cofactor coefficients and the (n−1)(n−2) singly deleted cofactor coefficients. Set

```
R_ij = C_ii C_jj − coeff_F(S−e_i−e_j) = C_ij C_ji
C_i0 = −coeff_G(i,leading)
C_0i = R_0i / C_i0
C_ij = (C_i0 C_jj − coeff_G(i,j)) / C_j0,   i,j≥1, i≠j.
```

Every division is exact and its denominator is positive. Hence all n² entries are recovered.

### 4. Size and complexity

The same explicit p yields A=O(n²), Q=O(n³), every e_j=O(n³), S=O(n⁴), and K=S+1=O(n⁴). Every diagonal control exponent is O(n³) and every star edit exponent is K+2a_i=O(n⁴). Every determinant monomial exponent is at most K+S−e_0−Q+A=O(n⁴). The coefficient norm bound gives log b=O(n log n+n log(H+1)+log(1+δ)).

Thus each control and the single readout require O(n⁴ log b) bits. Standard exact integer/rational arithmetic, the Bareiss determinant, the O(n²) direct coefficient decoder and primality trial division all have polynomial bit complexity. This is a bit-complexity theorem, not a statement about the cost of physical actuation.

## Exact author-side verification

Accompanying executable: `research_notes/portable_direct/R284BE_shared_sidon_cofactor_checker.py`.
Evidence file: `research_notes/portable_direct/R284BE_shared_sidon_exact_verification.json`.

* 562 exact matrix reconstructions PASS, including every one of the 512 matrices in {1,2}^{3×3}, plus seeded samples at (n,H)=(3,3),(4,2),(4,3),(5,2),(6,2).
* 128 exact bounded-error reconstructions PASS, using δ=7000, positive and negative integer and rational perturbations.
* Complete monomial-address census for 3≤n≤12 checks that every targeted exponent has exactly one permitted source monomial.
* Explicit comparison of maximum **actual** control bit lengths, same radix in both constructions: (3,2) R284BD 3177 → R284BE 1658; (4,2) 28616 → 9553; (5,2) 89752 → 22202; (6,2) 351787 → 68709.
* Exact Python integers, Fractions and Bareiss elimination were used. Finite computations verify these tested domains, while the general proposition relies on the algebraic proof. Independent review: NOT_REVIEWED.

## Source, residual fidelity, and continuation

Inputs are the inherited R284BD bounded positive-integer, labelled star-Port observer and its unmodified frozen scientific pin. The detector retains named/directed pairs and the jointly edited row; it is not a general all-operation Port quotient. The reduction in packing length preserves all entries under the declared future reconstruction operation; no erasure of residual differences is claimed beyond this observer model. This work does not alter the protected P000, ACTIVE worldview, native BRC/X6 mechanics, original shared Task Result, review or CLAIM.

Next research: determine whether one can shrink the O(n⁴) exponent by avoiding the Q-sized cardinality guard while still preventing target-address collisions, or prove a lower bound for this constrained monomial-address architecture; evaluate total control output bits and rational-error scale, not merely read count. Before any claim of asymptotic optimality, separate unrestricted one-read information bounds from this explicit polynomial-time coefficient decoder.

Main predecessors: R284BD_PRIME_SIDON_COMPACT_SINGLE_SCALAR_PORT_DECODER_20261120.md and R284BC_EXPLICIT_POLYNOMIAL_BIT_SINGLE_SCALAR_STAR_DECODER_20261120.md, and the R284AT observer identifiability theorem. Status: AUTHOR_PROVED, EXACT_FINITE_CHECK_PASSED, NOT_REVIEWED.
