# Native Enterprise filament codes: primorial nearest-neighbor error graph

Status: `FREE_RESEARCH_EXACT_ERROR_GRAPH_TOPOLOGY / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_DISTANCE_ERROR_CORRECTION_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_MULTIPROBE_GCD_ACCESS_20260824.md`.

## 1. Nearest-neighbor graph

Let

`M=P_d`, `d>=2`,

be a primorial modulus, so

`M=6U`

with U odd and coprime to6.

For a fixed length `k>=3`, form the graph

`E_k(M)`

whose vertices are the codewords of `C_k(M)` and whose edges join pairs at the minimum Hamming distance

`floor(k/2)`.

Since

`|C_k(M)|=M^2/3`,

we classify this graph exactly.

## 2. Two parity-layer partner maps

Represent a codeword by effective parameters

`(R mod 2U,c mod M)`.

Let

`chi=(-1)^R`.

### Even-layer partner

The unique other word agreeing on every even coordinate is

`T_E(R,c)=(R+U,c)`.

Because U is odd, this flips chirality.  On even positions the chirality offset vanishes and

`3U*(even index)`

is a multiple of M.

Thus `T_E` is a fixed-point-free involution.

### Odd-layer partner

The unique other word agreeing on every odd coordinate is

`T_O(R,c)=(R+U,c+chi-3U)`.

On every odd position, the slope shift contributes `3U` modulo M and the chirality flip contributes `-chi`; the intercept adjustment cancels both.

`T_O` is also a fixed-point-free involution.

## 3. Odd code length: perfect matching

Let k be odd.

There are

`E=(k+1)/2`

even positions and

`O=(k-1)/2`

odd positions.

Minimum distance is O, so a nearest pair must agree on E positions.

The only agreement set of that maximal size is the full even layer; any mixed q-periodic set for `q>=5` is smaller.

Therefore every vertex has exactly one nearest neighbor, namely `T_E`.

Hence

`E_k(M)`

is a perfect matching with

`|C_k(M)|/2=M^2/6`

edges.

This applies to `k=3,5,7,9`.

## 4. Even code length: degree-two cycle graph

Let k be even.

Both parity layers have size `k/2`, equal to the maximum agreement size.

Thus every vertex has exactly two nearest neighbors:

- `T_E`, agreeing on all even positions;
- `T_O`, agreeing on all odd positions.

No mixed-period agreement set is large enough to create another minimum-distance neighbor.

Therefore the nearest-neighbor graph is 2-regular and is a disjoint union of cycles.

## 5. Exact cycle length

Apply the two involutions successively.

Starting from `(R,c)`:

`T_O(T_E(R,c))`

returns the shell class R and translates c by

`-(3U+chi)`.

Because

`gcd(3U+chi,6U)=2`,

this translation has exact order

`6U/2=3U`.

Each translation step corresponds to two graph edges, so every nearest-neighbor cycle has length

`2*(3U)=6U=M`.

Since the whole graph has `M^2/3` vertices, the number of cycles is

`(M^2/3)/M=M/3=2U`.

Freeze:

`EVEN-k NEAREST GRAPH = DISJOINT UNION OF M/3 CYCLES OF LENGTH M`.

This applies to `k=4,6,8`.

## 6. Initial examples

### M=6

- odd k: 6 matching edges on12 codewords;
- even k: 2 cycles of length6.

### M=30

- odd k: 150 matching edges on300 codewords;
- even k: 10 cycles of length30.

### M=210

- odd k: 7350 matching edges on14700 codewords;
- even k: 70 cycles of length210.

## 7. High-dimensional interpretation

Every generic prime channel q>3 replaces

`M -> Mq`.

For even k, this simultaneously

- multiplies each nearest-neighbor cycle length by q;
- multiplies the number of cycles by q.

The total vertex count therefore grows by q^2, matching the finite-quotient collapse-fiber theorem.

For odd k the matching-edge count also grows by q^2.

Thus the same q^2 lift splits symmetrically into a longitudinal and transverse factor in the even-length error geometry.

## 8. Prime-valued boundary

Actual prime islands select a sparse subset of code vertices.  The matching/cycle theorem concerns the native finite quotient carrier and does not assert that prime realizations are uniformly distributed on those cycles.

Its role is to identify the exact error geometry in which prime packets live after collapse.

## 9. Boundary

Regular error graphs and involution products are classical.  The research-specific result is the reappearance of the primorial modulus as the exact nearest-neighbor cycle length of the native alternating-curvature code.
