# Frozen R5: sharp global transition for pairwise optimal-center nestedness

**Date:** 2026-11-14. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.  
**Status:** author-side finite mathematical theorem with exact computations; independent review `NOT_REVIEWED`.  
**Domain:** precisely the 954-event integer-coordinate, radius-2, indexed-center **derived one-dimensional observer**; original event identities are retained. No native X6/BRC-state quotient, full path-provenance compression, or physical performance claim.

## Theorem: exact threshold 292 for all 268,435,456 closure backgrounds

Let `B` be an arbitrary subset of the 28 originally length-three inter-block gaps. Shorten each chosen gap to two, keep the 954 original event labels, and let `D_B` be the minimum number of indexed centers required to cover every event within radius two. Define the optimal indexed-center family at budget `K` as `Opt_B(K)`, with total cost equal to the sum of distances to the nearest center. For a *jointly feasible adjacent pair* `D_B≤K<954`, let

```
rho_B(K) = min{|S \ U| : S in Opt_B(K), U in Opt_B(K+1)}.
```

Then, **for every B**, the following dichotomy holds:

```
D_B ≤ K ≤ 291     => rho_B(K) >= 1  (no nested optimal pair);
292 ≤ K ≤ 953     => rho_B(K) = 0   (a nested optimal pair exists).
```

There are no feasible budgets below `D_B`, and no `K+1` budget above 954. The global minimal feasible center count over all backgrounds is 207, and `D_B` lies in `207..213`. This theorem classifies the **existence** of an optimal nested pair, not its exact positive low-budget deletion distance, nor the existence of one globally coherent optimal chain across many budgets. It strengthens the separate high-budget theorem: **all closure patterns have the same sharp transition at K=292 despite different low-budget optimum costs and optimizer-family sizes.**

## Lemma 1: one feasible center insertion can reduce total cost by at most 3

Let `x_0<...<x_(n-1)` be *distinct integers*, let `S` be any nonempty center-index set with covering radius at most two, and let `h` be an event not already selected. Write `c=x_h`. Before insertion every event has a nearest-center integer distance `d(t)≤2`. After inserting the center at `c`, only events at integer coordinates `c-1,c,c+1` can get a *strictly smaller* distance: an event at distance at least two from c has new distance at least two, and old distance at most two.

For the event at c itself, the saving is `d(c)∈{1,2}`. Each of the two possible events at c±1 can save at most one. However **both** adjacent events cannot simultaneously save one. If `d(c)=2`, an existing center is at `c-2` or `c+2`, which already gives the corresponding adjacent event (if present) distance at most one. If `d(c)=1`, an existing center is at `c-1` or `c+1`, so that adjacent event (if present) is already distance zero. Therefore at most **one** adjacent event has a strict improvement. In either case the total decrease is at most `2+1=3`. Missing adjacent events only decrease this bound.

Consequently, for any nested feasible pair `S⊂U=S∪{h}`, its cost drop obeys

```
C_B(S)-C_B(U) ≤ 3.
```

The bound is independent of the 954-event seed, original gaps and closure mask, relying only on distinct integer event positions, radius two and center-at-event semantics.

## Lemma 2: every low-budget optimum cost drop strictly exceeds 3

The prior exact 32-class all-closure cost-spectrum theorem in Draft PR #2379, with data `research_notes/brc_r5_exact_cost_spectrum_20261114/EXACT_OUTPUT.json`, exhaustively classifies all `2^28` masks into 32 exact cost spectra. For all feasible adjacent budgets `207≤K≤213`, comparing successive class entries (and using the uniform `J_B(214)=1064` when `K=213`) gives:

| K | Exact minimum of `J_B(K)-J_B(K+1)` across all feasible B | Exact maximum |
|---:|---:|---:|
|207|14|14|
|208|7|14|
|209|7|14|
|210|7|14|
|211|6|14|
|212|6|14|
|213|5|6|

All 32 classes were checked at every applicable K, 128 exact class-transition comparisons (a class covers a known number of closure masks); the overall minimum low-budget drop is 5.

For the remaining low-budget range `214≤K≤291`, the preceding universal cost-invariance theorem gives `J_B(K)=J_empty(K)`; independent exact indexed-center path DP on the frozen no-closure 954-event seed gives

```
J_B(K)-J_B(K+1) = 5  for K=214..221  (8 transitions)
                         4  for K=222..291  (70 transitions).
```

Thus every feasible adjacent optimal-cost drop throughout `D_B≤K≤291` is at least four.

## Proof of the global dichotomy

Suppose a low-budget nested optimal pair existed: `S∈Opt_B(K)`, `U=S∪{h}∈Opt_B(K+1)`. By definition, `C_B(S)-C_B(U)=J_B(K)-J_B(K+1)≥4` (Lemma 2). But every insertion into a feasible radius-two indexed-center set decreases cost by at most 3 (Lemma 1). Contradiction. Therefore `rho_B(K)≥1` for all feasible `K≤291`, every B.

The immediately preceding `UNIVERSAL_PAIRWISE_NESTEDNESS_THEOREM.md` proves by an exact, 662-transition optimal-insertion-gain DP on the no-closure frozen R5 input and by monotone objective/family transfer that `rho_B(K)=0` for every B and `K=292..953`. Combining the two proves the stated **sharp universal phase transition**.

The 292 threshold concerns the pairwise observer and does not automatically imply a single nested chain of optimal sets, nor the exact positive reconfiguration distance in the earlier range.

## Reproduction and verification

The companion `VERIFY_R5_SHARP_NESTEDNESS_TRANSITION.py` crosschecks (1) the already-published 32-class exact cost table for all low-budget K207..213 and `J_B(214)=1064`; (2) no-closure path-DP J(K) and its drops for K214..291; and (3) the full optimal-insertion-gain recurrence against J(K)-J(K+1) for K292..953. The latter is also independently checked on 240 small exact-input brute-force instances in its separate verifier, and with three additional two-bit masks. Published `EXACT_NESTEDNESS_TRANSITION_CERTIFICATE.json` contains the exact bounded comparison counts and drop bands.

Local calculations checked all 32 predecessor cost classes and recomputed the no-closure 954-event path DP. The transition verifier as published is reproducible in the PR checkout. Original upstream imported GitHub bytes were not independently re-executed in the present local reconstruction. All mathematically load-bearing predecessor results retain their own author-side/NOT_REVIEWED evidence status; this theorem is not a formal accepted Result and does not assert live Task CLAIM or reviewer independence.

**Next:** in `K=207..291`, compute exact minimal positive deletion distances and optimizer-provenance witnesses across effective closure patterns. Keep the separate native R5 performance benchmark (2,520-byte seed; 28 coordinates; 8,192 prefix queries) unfinished.
