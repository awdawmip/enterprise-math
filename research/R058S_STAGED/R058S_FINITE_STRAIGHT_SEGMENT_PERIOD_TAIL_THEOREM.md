# R058S Finite Straight-Segment Period/Tail Theorem

Researcher-ID: `EM-R058S-7C91E4`  
Stage: `D`

## Theorem D4.A — exact interval decomposition

Let an infinite edge word `(e_i)` have period `m>=1`. Fix a global period alignment at edge indices congruent to `0 mod m`. Consider a finite interval of `N>=0` consecutive edges beginning at index `a`.

Let `p` be the number of initial edges before the next aligned boundary, truncated by the interval if the interval ends first. Then `0<=p<m`. After removing that prefix, write

`N-p = q m + r`, with `q>=0` and `0<=r<m`.

Therefore the interval is uniquely decomposed, relative to the chosen alignment, as

`prefix_tail(p edges) + q complete m-edge periods + suffix_tail(r edges)`.

The total number of tail edges is

`p+r < 2m`.

The bound is independent of the macroscopic segment length `N`.

## Theorem D4.B — complete-period bulk collapse is exact

Assume the periodic lifted polygonal path satisfies `v_(i+m)=v_i+t`. Every aligned complete period begins at some `j` divisible by `m` and ends at `j+m`, so its endpoint chord is exactly `t` and its chord length is exactly `||t||`.

Consequently, if each of the `q` complete periods is replaced by its endpoint chord, the bulk contribution is exactly

`q ||t||`.

Only the prefix and suffix tails remain unresolved by this period-collapse operation. This is an algebraic consequence of periodicity; no fitted correction is used.

## Frozen-carrier specialization

On each Stage-C straight-boundary class, `||t||=sqrt(Q(t))`. Thus each complete primitive cutting-word period contributes exactly its teacher straight-line translation length in the frozen radical arithmetic.

## Finite square-side localization

A digitized square is the intersection of four frozen exact supporting half-planes. Along a chosen side, the active side half-plane has the same local center/neighbor exposure rule as the corresponding infinite digital half-plane. The other supporting inequalities can alter that exposure only near the two endpoints where adjacent sides become active.

For a fixed frozen orientation/phase and finite carrier neighborhood, translating a local edge orbit by the primitive side translation changes each adjacent-side support slack by a fixed nonzero exact amount per period. Hence only finitely many period translates near each endpoint can fail the single-half-plane local test; the number is bounded independently of the macroscopic side length. Between those two endpoint layers, the square side is exactly a contiguous interval of the frozen primitive cutting word.

Applying Theorem D4.A to that central periodic interval adds fewer than `2m` alignment-tail edges. Therefore an exact primitive-period collapse would eliminate all length error accumulated by complete straight-side periods; any remaining discrepancy is confined to bounded period-alignment tails plus the two finite corner boundary layers.

**Statuses**

- `FINITE_SIDE_TAIL_LOCALIZATION_PROVED`
- `SQUARE_ERROR_REDUCED_TO_FINITE_PERIOD_TAILS_AND_CORNER_LAYERS`
- `CORNER_GENERATOR_STILL_OPEN`

## Proposal boundary

`POST_STAGE_C_PRIMITIVE_PERIOD_COLLAPSE_OPERATOR_PROPOSAL`

The proposed operation is **not deployed in Stage D**. No square prediction is recomputed, no `K>8` empirical packet is generated, and no grammar/predicate/operator is selected from square loss.
