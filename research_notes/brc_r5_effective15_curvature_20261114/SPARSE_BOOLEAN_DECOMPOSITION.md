# Frozen R5 — sparse four-cluster Boolean factorization

Date 2026-11-14. Status: author-side exact finite proof, NOT_REVIEWED. Frozen scientific input pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Predecessor within this PR: RESEARCH.md (15 effective cuts and unique curvature threshold). This theorem refers only to the 1D integer-event radius-2 **minimum center count** D, not native X6 geometry, the optimal-center witness set, or full BRC state.

## Exact theorem

Write x_i=1 when original gap i (zero based) is shortened from 3 to 2; otherwise x_i=0. The 13 cuts with zero exact all-background pivotal count have no effect on D. For every assignment of all 28 x_i, the following **four-cluster sum** is exact:

    D(x) = 213 - A(x) - B(x) - C(x) - E(x),

    A(x) = (x5 OR x6) + x2*x3*x4*(NOT x5 OR x6),
    B(x) = (x8 OR x9)
         + x12*(x13 OR (x10*x11*(x8 OR NOT x9))),
    C(x) = x16,
    E(x) = x25*x26*x27.

Here AND is product of 0/1 values, OR and NOT are Boolean operators (each OR expression is counted as the integer 0 or 1), and the sums of the two clauses in A and B are ordinary integer sums, allowing A and B to equal 2. The four components depend on **disjoint cut clusters**: {2,3,4,5,6}; {8,9,10,11,12,13}; {16}; {25,26,27}. Each of the 13 remaining cuts is globally inert for this D observer.

This provides an exact finite reduction of 268,435,456 original assignments to two 5/6-bit local truth tables and independent 1-bit/3-bit terms; evaluating D from a cut mask requires only constant-size Boolean gates and integer addition once the cut positions are indexed. It neither reconstructs native optimal center configurations nor creates a physical law.

## Proof via complete Möbius certificate

For the 15 active cuts A, enumerate all 2^15=32,768 assignments and directly compute D using the rationally generated frozen event boundaries and the proved optimal radius-2 greedy center-cover algorithm. Define the unique squarefree multilinear expansion

    D(x) = sum_{S subset A} a_S product_{i in S} x_i,
    a_S = sum_{T subset S} (-1)^(|S|-|T|) D(1_T).

Compute the a_S by the subset Möbius transform, subtracting the coefficient of S\{i} from S in increasing bit order. Exactly 19 coefficients are nonzero, including the constant:

| Set S | a_S |
|---|---:|
| empty | 213 |
| {2,3,4} | -1 |
| {5} | -1 |
| {2,3,4,5} | +1 |
| {6} | -1 |
| {5,6} | +1 |
| {2,3,4,5,6} | -1 |
| {8} | -1 |
| {9} | -1 |
| {8,9} | +1 |
| {10,11,12} | -1 |
| {9,10,11,12} | +1 |
| {8,9,10,11,12} | -1 |
| {12,13} | -1 |
| {10,11,12,13} | +1 |
| {9,10,11,12,13} | -1 |
| {8,9,10,11,12,13} | +1 |
| {16} | -1 |
| {25,26,27} | -1 |

All other 2^15-19 coefficients are **exactly zero**. The terms involving each cluster factor algebraically into the four displayed Boolean clauses. The unique multilinear extension agrees with the computed D at all Boolean vertices, which proves the identity for the declared finite domain. The attached independently executable checker verifies both the complete Möbius coefficient list and all 32,768 values of the Boolean expression against the original exact greedy input.

The largest nonzero interaction is the unique six-way monomial {8,9,10,11,12,13} with coefficient +1, so the multilinear degree is **exactly six**. The earlier exact degree-six Bernoulli expectation therefore has a structural, observer-scoped explanation: under i.i.d. Bernoulli-p closure, E[product_{i in S}x_i]=p^|S|, and hence

    F(p) = sum_S a_S p^|S|
         = 213 - 5p + p^2 - 3p^3 + 3p^4 - 3p^5 + p^6.

No cancellation of nonzero interactions above degree six is required: there simply are no such terms. Moreover the sparse support partitions into four disjoint cut-interaction clusters, explaining why higher-order interactions outside them vanish identically.

## Scope and method

This is a complete 15-bit finite exhaustive certificate plus the exact all-background zero-pivotal certificate inherited from PR #2359. The actual research novelty relative to this chain is the explicit four-cluster Boolean formula and Möbius sparsity theorem. It does not assert universal sparsity for different inputs, different radius, future observers, edit distances or optimal-center configurations.

Verification: direct effective-mask enumeration (32,768 cases); complete 15-variable subset Möbius transform; 32,768 Boolean-formula identities; explicit coefficient list and degree-six support. Original native 2,520-byte certificate and 8,192 prefix-query benchmark remain pending. A next direction is to derive these Boolean gates directly from the 29-block interval-cost structure (an independent symbolic proof), and to generalize the transfer to fixed-center-budget total correction costs with provenance-preserving witnesses.
