# R022 Ninth-Pass Deepening — Future Precision Debt and Replay Information Lower Bounds

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `NINTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

Pass 8 identified the monotone refinement of required precision when the future language strengthens. Pass 9 quantifies the information that must be retained if a runtime wants to upgrade from an old quotient to a stronger quotient **without replaying the original fine source**.

Let `E` be the old equivalence/precision partition and `F` a finer partition. For each old class `C`, let

`r_F(C) = number of F-classes contained in C`.

Define

`M(E -> F) = max_C r_F(C)`.

### Refinement-Debt Alphabet Theorem

The minimum cardinality of an arbitrary side-metadata alphabet `M` such that

`(old_E_token(x), side_metadata(x))`

can determine the new `F`-token for every fine state is exactly

`M(E -> F)`.

Hence the minimum fixed-width side information is

`B(E -> F) = ceil(log2 M(E -> F))` bits.

This is a clean NO_RESURRECTION lower bound. If the runtime stored fewer distinguishable side states and has no replay/checkpoint source, some newly required distinction is unrecoverable.

For future languages `U subseteq V`, define the **future precision debt** by applying this to

`E=K(U)`, `F=K(V)`.

Pass 6's bounded deletion model becomes a concrete instance: extending horizon `h -> H` splits only the old saturated class into `H-h+1` new classes, so the minimum abstract side alphabet is `H-h+1` and fixed-width debt is `ceil(log2(H-h+1))` bits.

Recommended classification:

`BRC_FUTURE_PRECISION_DEBT_FOUND / REFINEMENT_SIDE_INFORMATION_LOWER_BOUND_EXACT / DEBT_COMPOSITION_LAW_FOUND / REPLAY_EXACT_INFORMATION_REQUIREMENT_QUANTIFIED / NOT_CANONICAL`.

---

## 1. Partition refinement setup

Let `E` and `F` be equivalence relations on finite `X`, with `F subseteq E`, so `F` is finer.

For each `E`-class `C`, define

`r_{E->F}(C) = |{D in X/F : D subseteq C}|`.

This is the number of stronger semantic cases that were previously merged inside old token `C`.

The **debt vector** is

`R(E->F) = (r(C))_{C in X/E}`.

The worst local split count is

`M(E->F) = max_C r(C)`.

If `E=F`, every entry is 1 and `M=1`.

## 2. Refinement-Debt Alphabet Theorem

Suppose the old runtime retains only:

1. the old class identifier `[x]_E`;
2. one side label `m(x)` from a shared finite alphabet `A`.

We ask for a decoder

`decode([x]_E,m(x)) = [x]_F`.

### Lower bound

Choose an old class `C` realizing `M(E->F)`. It contains `M` distinct new `F`-classes.

Inside the same old token `C`, those new classes must receive different side labels, or the decoder would map one identical `(old token,side label)` pair to two different new classes.

Therefore

`|A| >= M(E->F)`.

This is just the pigeonhole principle, but it is exactly the missing information lower bound required by BRC replay semantics.

### Upper bound

For each old class independently, enumerate its contained `F`-classes by local indices `0,...,r(C)-1`. Reuse the same side alphabet across different old classes.

Then

`|A| = max_C r(C) = M(E->F)`

suffices.

Thus the lower bound is exact.

## 3. Fixed-width bit debt

If side labels use a fixed-width binary code, the minimum number of additional bits is

`B(E->F)=ceil(log2 M(E->F))`.

This is an **abstract information minimum**. A real executable carrier may require more because:

- side labels themselves must be computable/realizable;
- context/provenance may be observed;
- carrier grammar may forbid arbitrary local numbering;
- persistence/checkpoint headers cost storage;
- variable-length or compressed coding follows a different objective.

So `B` is a lower bound / idealized exact optimum, not a promise that every system achieves it.

## 4. Zero-debt boundary

`B(E->F)=0`

iff

`M(E->F)=1`

iff

no old class splits

iff

`E=F`.

For language extension `U subseteq V`, this means zero precision debt exactly when

`K(U)=K(V)`.

By pass 8, this occurs exactly when every future added by `V` is already observationally safe on `K(U)`, i.e. adds no new future distinction.

Thus the closure test is also a **zero-replay-debt test**.

## 5. Bounded deletion instance

Pass 6:

`tau_h(n)=min(n,h+1)`.

Extend `h -> H>h`.

Old nonsaturated classes remain unchanged. The old saturated class

`n>=h+1`

splits into

`h+1, h+2, ..., H, >=H+1`.

Number of new subclasses:

`H-h+1`.

Therefore

`M = H-h+1`,

`B = ceil(log2(H-h+1))`.

For `h=2`, `H=5`:

- old saturated class is `n>=3`;
- new classes are `3,4,5,>=6`;
- `M=4`;
- minimum fixed-width static side debt is **2 bits**.

If those 2 bits (or equivalent stronger information) were not retained, exact strengthening requires replay from a source that still contains the distinction.

## 6. Debt composition law

Consider successive refinements

`E >= F >= G`.

For an old `E`-class `C`, the number of final `G`-classes inside it is exactly

`r_{E->G}(C)
 = sum_{D in X/F, D subseteq C} r_{F->G}(D)`.

So refinement debt composes by summing child split counts through the refinement tree.

Consequently:

`M(E->G) <= M(E->F) * M(F->G)`.

For fixed-width bit debt:

`B(E->G) <= B(E->F) + B(F->G)`.

This gives an exact staged-accounting law for future-language strengthening.

It also explains why retaining incremental side metadata at multiple semantic checkpoints can upper-bound the information needed for a later stronger query.

## 7. Exhaustive finite verification

Artifact:

`experiments/r022_future_precision_debt.py`.

On five labeled states:

- all **52** equivalence partitions;
- all **358** refinement pairs;
- all **1,304** refinement triples;
- constructive local side-label scheme verified for every refinement pair;
- split-count composition verified for every refinement triple;
- `M` submultiplicativity and fixed-width bit subadditivity verified throughout;
- counterexamples: **0**.

Distribution of `M` over the 358 refinement pairs:

- `M=1`: 52 pairs;
- `M=2`: 205;
- `M=3`: 85;
- `M=4`: 15;
- `M=5`: 1.

Focused pass-9 tests: **4/4 PASS** in the research execution environment.

## 8. Replay lower bound

A `REPLAY_EXACT` implementation can avoid storing all debt bits live only by retaining access to some stronger source/checkpoint from which the missing subclass can later be recomputed.

Formally, if the retained state `R(x)` is supposed to reconstruct `[x]_F`, then the complete retained/replay-accessible encoding must refine `F`:

`R(x)=R(y) => x F y`.

Otherwise NO_RESURRECTION applies.

So there are two ways to pay future precision debt:

### Store now

Retain enough static side metadata to distinguish the future refined subclasses.

### Recompute later

Retain a checkpoint/source whose reconstruction process still has access to those distinctions, and charge replay storage/work/depth.

There is no third exact route in which the distinction is physically destroyed and later recovered from the old coarse token alone.

## 9. Relation to causal rewind

Causal rewind now has an information target.

When a stronger future fails on the current carrier, do not merely ask “how many stages should we go back?” Ask:

> what is the latest checkpoint whose retained encoding still contains enough information to pay the required refinement debt?

A checkpoint that predates the semantic loss but itself stores an encoding coarser than the new `F` is still insufficient.

Thus rewind depth and information debt are distinct resource coordinates:

- **where** must execution rewind?;
- **how much missing distinction** must be reconstructed there?

## 10. Relation to branch tokens and certificate caches

The debt theorem concerns deterministic semantic refinement classes, but it informs BRC runtime design directly.

- an RCC may merge histories under old future language `U`;
- language extension to `V` induces finer `K(V)`;
- the debt vector identifies which old merged classes need how many new semantic alternatives;
- CS-NCC/context certificate caches may remain reusable on unaffected context/language regions;
- only classes with `r(C)>1` need semantic re-refinement.

This makes “on-demand re-refinement” quantitatively local.

## 11. Resource-accounting delta

R021/R014 should add:

- `future_precision_debt_vector`;
- `max_refinement_split = M`;
- `minimum_static_side_alphabet = M`;
- `minimum_fixed_side_bits = ceil(log2 M)`;
- `classes_with_nonzero_debt` (those with split count >1);
- `checkpoint_information_level`;
- `replay_source_available`;
- `replay_work/depth to discharge debt`;
- language-version pair `(U,V)` / kernel pair `(K(U),K(V))`.

Do not compare replay against stored metadata without charging both sides.

## 12. Prior-art/rooting boundary

Partition refinement, quotient indices, information lower bounds, and pigeonhole arguments are standard. R022 claims no generic novelty for those facts.

The Enterprise Math residue is defining them as an explicit **future precision debt** for BRC and connecting the exact lower bound to:

- future-language Galois refinement;
- NO_RESURRECTION;
- replay-exact execution;
- causal rewind;
- branch-token metadata accounting.

## 13. R021 feedback

Recommended additions:

1. For every future-language extension `U -> V`, compute/estimate the refinement debt vector from `K(U)` to `K(V)`.
2. Record the exact lower bound `M=max split count` for side-label cardinality.
3. Record fixed-width lower bound `ceil(log2 M)` bits.
4. Zero debt iff the stronger language lies inside the old language closure / does not refine the kernel.
5. Make replay checkpoints prove they retain enough information to reconstruct the target refined kernel; stage position alone is insufficient.
6. Track rewind depth and information debt separately.
7. Use debt only as a semantic lower bound; executable carrier grammar/provenance/context can increase actual cost.
8. For successive language extensions, use the split-count composition law and bit-debt subadditivity for staged accounting.

No correction is requested to R023. The result is a quantitative corollary of its no-resurrection/future-signature discipline.

## 14. Ninth-pass classification

`BRC_FUTURE_PRECISION_DEBT_FOUND / REFINEMENT_SIDE_INFORMATION_LOWER_BOUND_EXACT / ZERO_DEBT_CLOSURE_TEST / DEBT_COMPOSITION_LAW_FOUND / REPLAY_EXACT_INFORMATION_REQUIREMENT_QUANTIFIED / CAUSAL_REWIND_INFORMATION_TARGET_ADDED / R021_FEEDBACK_READY / NOT_CANONICAL`.

Cumulative compiler picture after nine passes:

`future language -> required kernel -> semantic frontier -> executable macro basis -> exact proof-carrying rewrite -> compositional descent operations -> future extension -> local refinement debt -> store metadata or replay from a sufficiently informative checkpoint`.
