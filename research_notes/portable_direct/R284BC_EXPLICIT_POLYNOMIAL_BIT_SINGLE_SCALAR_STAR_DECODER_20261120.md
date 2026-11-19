# R284BC — Deterministic polynomial-bit, polynomial-time decoding from one scalar star-Port observation

Date: 2026-11-20 (Asia/Shanghai). Scientific lineage: R284AT -> R284AX -> R284AZ -> R284BB. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Researcher lineage in existing records: EM-DIRECT-E6B1DD; no new formal CLAIM asserted.

## Scope and assertion

This is an **auxiliary finite, named directed-Port determinant observer**. It does not change the frozen scientific input, P000, six-axis native ontology, X6 or BRC dynamical assertions. Fix n >= 3 and a known integer H >= 2. The unknown matrix C belongs to {1,...,H}^{n x n} and has strictly positive entries. An observer chooses one integer diagonal control D and simultaneous integer edits z_i E_{0i} for i=1,...,n-1, obtaining **one** exact scalar

    y = det(D - C - sum_{i=1}^{n-1} z_i E_{0i}).

**Theorem BC1.** For every n,H in the above domain there is an explicit common, nonadaptive control choice and a deterministic algorithm recovering every entry of C from this single y. Control construction, one exact integer determinant, recovery and verification require a number of bit operations bounded by a polynomial in n and log(H+1). There is no candidate-table search. Both controls and y have polynomial bit length. The construction is uniform and elementary.

**Theorem BC2 (known bounded error).** Given a finite nonnegative rational error bound delta, the base can instead be enlarged so the same direct coefficient decoder recovers C from any exact rational readout y+epsilon with |epsilon| <= delta. The bit-complexity bound becomes polynomial in n, log(H+1), and the bit length of delta/readout, under exact rational arithmetic. As an information-theoretic statement the coefficient recovery also works for a real readout with exact comparisons and the stated error bound. An approximate hardware-real implementation requires a matching finite-precision readout specification.

This closes the polynomial-bit **explicit setup plus efficient decoder** gap left open in R284AZ/R284BB, at the cost of comparatively large polynomial exponents. It does not assert optimal dynamic range.

## 1. Polynomial distinctness needs only Sidon pairs

Let B0 = 2n+1 and define integers

    a_j = j + B0*j^2,          0 <= j < n.
    Q = n*max_j a_j + 1,
    e_j = Q + a_j,              E = sum_j e_j,
    T = n*(Q+max_j a_j)+1.

The sums a_i+a_j for unordered distinct index pairs {i,j} are unique: reducing equality modulo B0 recovers i+j because 0 <= i+j <= 2n-2 < B0. The integer quotients then recover i^2+j^2. Both the sum and sum of squares recover the unordered pair (via the product ij). The a_j themselves are distinct.

For subsets S, write e(S)=sum_{j in S}e_j=|S| Q + sum_{j in S}a_j. Since Q > n*max a_j, differing subset cardinalities give disjoint exponent intervals. At cardinality n-1, the missing singleton is encoded uniquely; at cardinality n-2, the missing unordered pair is encoded uniquely. In the edited row-zero cofactor, the top and next-to-top diagonal degrees need only missing singleton distinctions.

## 2. Disjoint blocks separate baseline and directed cofactors

Choose a positive odd radix b as in Section 4 and set

    d_j = b^(e_j),
    z_i = b^(i*T),           1 <= i < n.

Write F(d) = det(diag(d)-C), and G_i(d) = coefficient of z_i in the edited determinant. Because the edits all act in row 0, no product z_i*z_j occurs, and

    P_C(d,z) = F(d) + sum_{i=1}^{n-1} z_i G_i(d).

The baseline has exponents in [0,T). Every G_i depends only on d_j with j outside {0,i}, and has exponents in [0,T). Consequently baseline and all z_i G_i occupy pairwise disjoint radix blocks [i*T,(i+1)*T).

The named baseline coefficients are

    [prod_{h != i} d_h] F = -C_ii,
    [prod_{h notin {i,j}} d_h] F = C_ii*C_jj - C_ij*C_ji.

Writing U_i = {0,...,n-1}\{0,i}, the required cofactor coefficients are

    [prod_{h in U_i}d_h] G_i = -C_i0,
    [prod_{h in U_i\{j}}d_h]G_i = C_i0*C_jj - C_ij*C_j0,
                 (i != j, i,j >= 1).

These follow by expanding the 1x1, 2x2, and 3x3 named submatrices in the determinant. All selected exponents are collision-free within their blocks by Section 1. Note that the latter j-coefficient may have no diagonal variable when n=3; it remains observable because z_i itself carries a positive block exponent.

## 3. Direct polynomial-time reconstruction

Extract the signed radix-b coefficients at these O(n^2) exponents:

- baseline exponent E-e_i -> -C_ii;
- baseline exponent E-e_i-e_j -> C_ii*C_jj-C_ij*C_ji;
- z_i exponent i*T + E-e_0-e_i -> -C_i0;
- z_i exponent i*T + E-e_0-e_i-e_j -> C_i0*C_jj-C_ij*C_j0.

After the diagonal terms, define R_ij=C_ij*C_ji from the 2-index principal coefficients. Then reconstruct

    C_0i = R_0i / C_i0
    C_ij = (C_i0*C_jj - g_ij) / C_j0  for i != j >= 1.

The divisions are exact since every entry is positive. Every recovered entry is checked against the known integer range [1,H]. Unlike an exhaustive candidate decoder, the algorithm performs O(n^2) coefficient extractions and ordinary integer operations.

## 4. Signed-digit correctness and noise tolerance

For the baseline and each G_i, the sum of absolute coefficient values is bounded by n!*(1+H)^n. This follows by selecting diagonal variables and bounding every remaining r x r signed C-subdeterminant by r!*H^r. Hence the sum over all n blocks is at most

    L = n*n!*(1+H)^n.

Even if unneeded low-degree monomials collide internally, every radix exponent has an aggregate signed integer coefficient c_h satisfying |c_h| <= L.

For exact reads choose b=2L+1, odd. The unique balanced radix expansion has each |c_h|<b/2. For a target exponent k, write

    q_k = floor((y + floor(b^k/2))/b^k),
    c_k = ((q_k + floor(b/2)) mod b) - floor(b/2).

The signed contribution from positions below k has absolute magnitude < L*b^k/(b-1) < b^k/2; rounding therefore removes it, and the balanced residue returns c_k. This works for negative y.

For a known error bound delta >= 0, choose any odd integer b > max(4L+4,4delta+4). A convenient stronger explicit choice is

    b = 4L + 2*ceil(4delta) + 9.

Every extracted exponent k is positive. The lower-place tail has absolute magnitude < b^k/4. For the explicit b above, delta < b/8 <= b^k/8, so the combined perturbation has absolute magnitude < 3*b^k/8. This margin ensures the written integer half-up quotient formula also rounds correctly for any exact rational observed y+epsilon (the half-unit offset lost by floor(b^k/2) is at most 1/2). More generally for any b satisfying the weaker displayed lower bound, use the exact nearest-integer quotient floor((y+epsilon)/b^k + 1/2) to avoid odd-radix half-integer tie conventions. Balanced signed residues then return each c_k. The companion script tests the integral delta/error case and its exact quotient routine; rational-error recovery follows from the same strict margin.

## 5. End-to-end bit bounds and limits

max a_j = O(n^3); Q = O(n^4); T = O(n^5); max exponent (n-1)T+sum e_j = O(n^6). Also log_2(b) = O(n log n + n log(H+1) + log(1+delta)). Thus maximum setting bit length is O(n^6 log b), and the determinant output has O(n^7 log b) bits by the Leibniz bound. Repeated integer powers/divisions and an exact Bareiss determinant have polynomial bit-complexity in these lengths; this is a computational bound for a Turing machine with standard exact integer arithmetic, not a unit-cost-infinite-integer RAM claim.

The resulting bound is deliberately coarse. In practice, polynomial exponents can still be large; optimized additive Sidon sets, targeted extraction, bit packing, sparse determinant methods and smaller amplitude designs are open. The result advances the exact finite Port observer and must not be directly promoted to a native heartbeat-world theorem without a typed embedding plus observer/operation preservation.

## 6. Reproducible author-side verification

Companion code: R284BC_explicit_polynomial_bit_single_scalar_decoder.py (Python standard library). Companion data: R284BC_exact_verification.json.

Verified: exhaustive 512 matrices in {1,2}^{3x3}; 16 seeded n=3,H=3; 8 each for n=4,H=2 and n=4,H=3; 3 for n=5,H=2, totaling 547 exact reconstruct-and-compare tests. Additionally, 48 seeded 3x3,H=2 matrices were each checked with integer noise -7000 and +7000 (96 tests), using the known delta=7000. The maximum observed 5x5 exact readout was 444,530 bits; 3x3,H=2 noiseless maximum was 8,211 bits. All checks PASS. Seeds and digest summary appear in JSON. No independent mathematical review was performed.

## Source lineage, research question and admission

Source problem: R284BB_NOISE_ROBUST_SINGLE_SCALAR_STAR_THRESHOLD_20261119.md, with the frozen Port observer and named edit interface unchanged. Its nonconstant-coefficient completeness is reused as an exact algebraic dependency, and the reconstruction identities are written out above. Prior R284AZ proved finite-table one-read random settings with polynomial control bits; this result supplies explicit deterministic polynomial-bit construction and polynomial-time decoder.

Next tasks: reduce exponents to near the information-theoretic actuator bound; minimize total control/input bits without losing explicit polynomial-time decoding; study the effect of instrument quantization and measurement of extremely large integers, separately from exact rational adversarial error. Formal Result/Review/Working Truth promotion requires its own live control authorization and independent evaluation.
