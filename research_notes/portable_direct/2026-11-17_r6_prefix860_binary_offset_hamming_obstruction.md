# PREFIX-860 — Exact binary-popcount obstruction for two-read near-full moduli

Date: 2026-11-17. Scientific status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Predecessor: PREFIX-859 arbitrary odd two-reading collision-distance theorem.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (preserved).
Scope: auxiliary provenance-retaining named positive BRC scalar observer, not a native X6 Cell/Link/Port event-law assertion.

## Setup

For `p` named binary sources, let `N=2^p`, `U(x)=sum_{i=0}^{p-1} 2^i x_i` and allow a no-op or one named source-bit flip at a heartbeat. The initial state is unknown and only the complete terminal state needs recovery. Two consecutive observations use odd moduli `q1,q2`, with any known baseline and invertible odd-modulus heartbeat multipliers removed by modular inversion. The legal predecessor set of terminal value `v` is `P(v)={v} union {v XOR 2^i: 0<=i<p}`.

This theorem focuses on **both individual observers being noninjective**: `q1=N-1`, `q2=N-c`. Here `c` is an odd integer `>=3`, `L=ceil(log2(c))=(c-1).bit_length()`, and `p>=L+3`. Thus `3<=c<N/2` and both q are odd positive integers less than N.

## Theorem 860-A (binary popcount iff)

Under the stated conditions, the ordered two-heartbeat observer

```text
(q1,q2)=(2^p-1, 2^p-c)
```

recovers every terminal complete named-source state, for every legal initial state and single-step update, **if and only if**

```text
popcount(c-1) >= 3.
```

Equivalently, it fails exactly when `c-1` is expressible as the sum of at most two nonnegative powers of two (with the empty/zero summand allowed).

**Proof.** Since `q2=N-c>N/2`, every collision between two different terminal integers modulo `q2` is exactly the pair `u` and `w=N-c+u`, with `0<=u<c`. All high `p-L` bits of `u` are zero. All corresponding high bits of `w=N-(c-u)` are one because `1<=c-u<=c<2^L`. Their Hamming distance is thus at least `p-L>=3`. Their predecessor Hamming balls of radius one `P(u)` and `P(w)` are therefore disjoint as sets of **integers**.

Modulo `q1=N-1`, two distinct integers in `[0,N-1]` have the same residue only if they are `0` and `N-1`. Since the predecessor sets are already disjoint, a first-read collision is possible precisely when one predecessor set contains 0 and the other contains `N-1`. A predecessor of `u<c` can be zero exactly when `u` is zero or a power of two. A predecessor of `w=N-c+u` can equal `N-1` exactly when `c-1-u` is zero or a power of two (flipping a zero bit in `w` to one).

Consequently, both observations collide for some distinct terminal states iff
`c-1=u+(c-1-u)`, with both summands in `{0,1,2,4,8,...}`. Such a decomposition exists iff `popcount(c-1)<=2`: two powers at distinct positions, one power, or two equal powers; these cover precisely the positive even integers of binary popcount at most two. Conversely, if the popcount is at least three, no such decomposition is possible and all terminal ambiguities disappear. The legal bit flips are precisely the predecessor choices just enumerated. QED.

## Corollary 860-B (least eligible fixed offset)

The least odd `c>=3` with `popcount(c-1)>=3` is `c=15`, since `14=1110_2` has three set bits. Thus for every `p>=7` the ordered observer `(2^p-1,2^p-15)` succeeds. Direct exhaustive checking also establishes the isolated extension `p=6,c=15`. This is a minimum **offset within this one-parameter near-full-modulus family**, not the minimum total bits or peak width among arbitrary pairs.

If `popcount(c-1)<=2`, the constructive proof itself identifies indistinguishable histories: choose `u` as one nonnegative power-of-two summand, let `w=N-c+u`; select first predecessors `0` and `N-1` and let each perform the permitted flip to its respective terminal state. Both first observations vanish modulo `N-1`; the second observations match modulo `N-c`. This gives a verifiable collision witness.

## Exact computations

The standard-library Python checker `PREFIX860_R6_OFFSET_HAMMING_CHECK.py` independently builds each precursor-residue pair and tests their intersections for every pair of `q2`-colliding terminals. It checks all eligible odd `3<=c<128` for `6<=p<=16`, within the theorem's `p>=L+3` range. The results file `PREFIX860_R6_OFFSET_HAMMING_RESULTS.json` records counts [3,7,15,31,63,63,63,63,63,63,63] by p and `ALL_EXACT_ASSERTIONS_PASSED`, plus the separately checked p=6,c=15 boundary extension.

Run: `python3 research_notes/portable_direct/PREFIX860_R6_OFFSET_HAMMING_CHECK.py > reproduced.json`; compare decoded JSON with committed results. These finite checks test implementation and boundaries; the unbounded theorem is proved symbolically.

## Resource implications and next question

Both q1 and q2 in this family generally require p raw bits, so it identifies an exact **arithmetic obstruction**, not an improvement over the minimum Pareto widths of PREFIX-859. The useful new distinction is that source-residual collisions in this near-full family depend on the binary support of c-1, with three occupied bit positions as the sharp threshold.

Next: seek general closed-form classifications of the undominated two-read width classes (PREFIX-859), and determine when a short first port separates a q2 residue collision graph by a bounded Hamming-support condition. Do not infer native X6 event authorization from this auxiliary bit-source model.
