# R284AU-PACK — Finite scalar Port identifiability by bounded-height coefficient packing

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AT (all-dimensional directed spanning-tree identifiability from *formal multivariate polynomial* readings); R284AS; R284AR.
Scientific baseline: R284AT's frozen source, `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This note changes the observation *resolution/height* contract, not P000 or frozen inputs.
Object type: auxiliary named Port-channel integer matrices, **not** native X6 spatial dynamics. Signed determinant coefficients and all named channel indices are retained.

## AU1. Exact theorem: n scalar determinant readings suffice with bounded integer height

Let `n>=2`, `H>=1` be known integers, and let `C=(c_ij)` range over all matrices in `{1,...,H}^{n x n}`. The observer may select nonnegative integer diagonal settings `D` and apply one integer single-entry intervention `E_0v` per read. All readouts are **exact integers** (their binary lengths are counted).

There is a deterministic, explicitly computable common diagonal `D=D(n,H)` such that the following **n scalar readings** uniquely determine *every* entry of `C`:

- `y_0 = det(D-C)`;
- `y_v = det(D-C-E_{0v})`, `v=1,...,n-1`.

Each selected diagonal entry and each output has polynomial bit length in `n` and `log(H+1)`; reconstruction uses polynomial-time exact integer arithmetic. This is a constructive *sufficiency* bound for scalar queries under the declared unbounded-range exact-integer instrument; no claim of minimal scalar-query count is made.

## AU2. A polynomial-height 3-separating weight family

Choose positive increasing integers `w_0,...,w_{n-1}` such that for every `k=1,2,3`, distinct `k`-element subsets have distinct sums of their weights. The following deterministic greedy construction suffices.

Starting from the empty list, after `t` weights have been chosen, forbid the finitely many integers
`sum_{b in B} w_b - sum_{a in A} w_a`, for all `k=1,2,3`, `A subset [t]` with `|A|=k-1` and `B subset [t]` with `|B|=k`. Choose the least integer larger than the last weight and outside that forbidden set.

Induction: two equal `k`-subset sums involving the new index on both sides reduce to an old collision; if the index occurs on exactly one side, the new weight was forbidden. The number of newly forbidden integers is at most
`sum_{k=1}^3 binom(t,k-1)binom(t,k)=O(t^5)`.
Therefore `w_{n-1}=O(n^6)` and `sum_i w_i=O(n^7)`. (For a direct closed formula, `w_i=(i+1)+M(i+1)^2+M^2(i+1)^3`, `M>3n^3`, also works, with a larger polynomial bound.)

Let `W=1+sum_i w_i`, and define for each named subset `S subset [n]`:
`e(S)=|S|W+sum_{i in S}w_i`.
The `|S|W` bands are disjoint. Within each fixed cardinality `n-1`, `n-2` or `n-3`, the complement has size 1,2 or 3, so `S -> e(S)` is injective. The maximal exponent obeys `e([n])=O(n^8)`.

## AU3. One exact integer packs all required polynomial coefficients

Let `A=2^n n! H^n` and choose an even power-of-two radix `B>2A`.
Set `D_i=B^{W+w_i}`.

Both `F(d)=det(diag(d)-C)` and each difference
`G_v(d)=det(diag(d)-C-E_{0v})-F(d)`
are multiaffine integer polynomials. A coefficient of `F` is a signed determinant of a principal submatrix of `C`, of absolute value at most `n!H^n`. A coefficient of `G_v` is a signed cofactor determinant (or zero), with the same conservative bound. There are at most `2^n` terms in either polynomial. Hence the aggregate coefficient at **every** exponent after substitution `d_i=B^{W+w_i}` has absolute value at most `A<B/2`, including when several monomials share an exponent.

The integer `F(D)=sum_S f_S B^{e(S)}` therefore has a unique balanced-base-`B` signed-digit expansion. Its digit at `e([n]\\T)`, for `|T|<=3`, equals the **single** coefficient `[prod_{i notin T}d_i]F`. The same holds for `G_v(D)=y_v-y_0`. Balanced digits can be extracted exactly by repeated Euclidean remainder followed by centering into `(-B/2,B/2)` and exact division by `B`. No coefficient sign is discarded.

## AU4. Exact reconstruction from the packed digits

Write `a_i=c_{ii}`, `p_{ij}=c_{ij}c_{ji}>0`.
From `F`, take complement-one and complement-two digits:
`a_i=-[d_{[n]\\{i}}]F`,
`p_{ij}=a_i a_j-[d_{[n]\\{i,j}}]F`.

For each directed star edit `E_{0v}`, the complemented-pair digit of `G_v` is `-c_{v0}`. Thus
`c_{v0}=-[d_{[n]\\{0,v}}]G_v`,
`c_{0v}=p_{0v}/c_{v0}`.

For any `1<=i<j<n`, the complement-three digit of `G_i` is
`a_j c_{i0}-c_{ij}c_{j0}`.
Consequently
`c_{ij}=(a_j c_{i0}-[d_{[n]\\{0,i,j}}]G_i)/c_{j0}`,
and `c_{ji}=p_{ij}/c_{ij}`.

Every denominator is strictly positive. All reconstructed values equal the original entries by R284AT's directly verifiable cofactor identities. Thus one baseline and `n-1` perturbed scalar measurements suffice.

## AU5. Full cost and finite-precision boundary

The construction is exact but deliberately high-range. Greedy weights give `W=O(n^7)`, `e_max=O(n^8)`, and
`log_2 B=O(n(log n+log(H+1)))`. Each diagonal setting has `O(n^8(log n+log(H+1)))` bits (a conservative bound); the n-by-n integer determinant and its output have polynomial bit length. Exact determinant computation (e.g. fraction-free elimination), balanced-digit extraction, and rational divisions are polynomial-bit-complexity operations. These are *upper bounds*, not a practical runtime advantage over polynomial interpolation or cofactor readouts.

Instruments restricted to a fixed numeric range, finite absolute resolution, noisy readouts or unknown height `H` **do not satisfy** this theorem's input contract. The compression buys a low *number* of readings by spending large numeric range and exact output precision. An information-theoretic lower bound for an injective encoding of `H^{n^2}` possible inputs is `n^2 log_2 H` total binary output bits; the displayed construction is far above that lower bound.

Known-common-denominator rational corollary: if `C=A_0/L` for an **a priori known** positive integer `L` and unknown `A_0 in {1,...,H}^{n x n}`, query the n rational determinants at `D/L` with interventions `E_{0v}/L`, multiply each readout by `L^n`, and apply the integer algorithm. The scaling and known-denominator restriction are essential to this exact reduction.

## AU6. Verification, provenance and continuation

Companions: `R284AU_scalar_packing_checker.py` and `R284AU_scalar_packing_exact_verification.json` (separate from an existing, differently scoped `R284AU_exact_verification.json` file). Exact Python standard-library checker uses Bareiss integer determinants and balanced radix digits, then reconstructs full matrices and checks entry-by-entry. It passed 47 deterministic random positive-integer matrices (n=2:12; 3:16; 4:12; 5:7), an exhaustive 512-matrix test of all 3x3 positive matrices with entries in {1,2}, plus one fixed n=3 example; the largest observed determinant bit length among these tests was 2856. These finite tests confirm the implementation on the declared sample, while AU2–AU4 prove the all-n theorem. Independent review remains NOT_REVIEWED.

The previous R284AT uses formal coefficient access; R284AU is a new exact *finite scalar measurement realization* with explicit precision accounting. BRC/observer relevance: the signed joint/cofactor and named directed paths are preserved in balanced digits; these exact digits are a declared sufficient observer for the specific star-edit family. No transfer to unrestricted future Port operations or P000/X6 dynamics is asserted.

Remaining scientific question: reduce the output/diagonal bit length for n scalar readings, or obtain useful scalar-vs-precision Pareto bounds and robust bounded-noise reconstruction under a specified instrument.
