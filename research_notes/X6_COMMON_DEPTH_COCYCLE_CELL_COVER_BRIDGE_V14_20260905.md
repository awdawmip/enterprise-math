# X6：V2 common-depth carry 与 full Cell cover fibre 的统一

Status: `DERIVED_EXACT_COVER_CLASSIFICATION / HISTORICAL_NATIVE_SELECTION_SUPERSEDED_BY_P000_V5`
Date: `2026-09-05`
Current type reconciliation: `2026-11-13` (P000 V5 signed native X6 pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`).

**Current selection within this exact cover family:** the native Cell torsor is `Z^6` and retains integer common depth `h` (`m=0` below). The `m=1` quotient `Z^6/Z1` remains a valid **relative observer**, not current native Cell identity. Every finite `m>1` is a mathematical quotient/cover alternative, not an additional currently admitted native spatial type. This retyping preserves the normal form, the carry cocycle and BRC pushforward calculations for all `m`.

Depends on:
- six-axis derived foundation V2 `normalize_counts`, `CountAtlas`, `depth_carry`;
- X6 coordinate completion V7;
- connected Cell cover classification V13.

## 1. Existing exact V2 state split

The already-main-backed V2 tool takes any nonnegative six-count tuple n and writes uniquely

`n = r + h*1`,

where

`r=can6(n)`, `min(r)=0`, `h=min(n)>=0`.

It explicitly retains r and h separately rather than setting the common depth to zero inside the general count observer.

For two min-zero residuals a,b (possibly after an atlas frame permutation), the existing exact carry is

`c(a,b)=min_i(a_i+b_i)>=0`.

The normalized residual product is

`a star b = can6(a+b)`

and the depth updates by

`h_new = h_a+h_b+c(a,b)`.

V2 already proved/checked the associativity 2-cocycle law for c.

## 2. Cover normal form

For finite `m>=1`, every class in

`G6^(m)=Z^6/mZ*1`

has a unique normal form

`(r, s)`

with

- `r in A6_D` min-zero;
- `s in Z/mZ` the diagonal/common-depth residue.

For `m=0`, use

`(r,s) with s in Z`.

Indeed for an arbitrary integer lift z,

`r=can6(z)`, `s=min(z)` modulo m (or as an integer for m=0).

## 3. Exact multiplication law

In these normal coordinates,

`(a,rho) * (b,sigma)`

`= ( can6(a+b), rho+sigma+c(a,b) )`,

where the second component is interpreted in `Z/mZ` for finite m and in Z for m=0.

Thus the **same common-depth carry** discovered and toolized in the derived six-axis BRC/count atlas supplies the exact algebraic composition cocycle for this `m`-indexed cover family (as native only at the currently selected `m=0`, otherwise as a hypothetical or observer construction).

No new hidden-state mechanism is needed.

Associativity of the Cell-cover multiplication is exactly the existing carry 2-cocycle identity.

## 4. Meaning of the three principal cases

### m=1 — historical relative-quotient Cell candidate; current observer

The depth fibre is trivial *in this quotient*. The historical proposal identified Cell endpoints with the min-zero six-coordinate torsor; **current P000 V5 instead treats this as the lower-information relative-coordinate observer**. `c(a,b)` remains exact section carry; the raw common depth is still part of current native Cell displacement.

### finite m>1 — mathematical periodic-depth quotient models

Only common depth modulo `m` belongs to **these hypothetical quotient model endpoints**. Their coordinate observations see `r` but forget the residue.

A complete six-axis diagonal cycle advances the fibre by 1; m cycles return.

### m=0 — current P000 V5 native signed-X6 depth

The entire integer diagonal depth belongs to actual signed native Cell identity. No nonzero number of complete diagonal cycles returns the same full Cell. `z=r+h*1` is a lossless chart of `Z^6`; `G(z)=sum_i z_i^2` must be evaluated on the restored full signed vector.

## 5. BRC observer hierarchy

This synthesis clarifies the correct BRC information rule:

- general six-count / path observer: retain exact depth h and branch provenance;
- relative coordinate endpoint observer: retain only `r=can6(n)`;
- finite-m quotient endpoint observer: retain `(r,h mod m)`;
- current native signed-X6 Cell endpoint (`m=0`): retain exact `(r,h)`, equivalently the raw full displacement `z`;
- historical m=1 Cell candidate: depth was not endpoint identity *within that hypothetical quotient*, although Path/BRC could still retain it as history/count data.

Hence

`DEPTH_NOT_QUOTIENT_ENDPOINT_IDENTITY != DEPTH_INFORMATION_MAY_BE_DELETED_FROM_ALL_OBSERVERS`.

In the **current native Cell model**, depth *is* part of spatial endpoint identity.

Even at m=1 the general BRC/path layer may need exact h for future concatenation, length/moment or provenance observers.

## 6. Rotation covariance

For any six-axis permutation sigma,

`min(sigma a + sigma b)=min(a+b)`.

So the depth cocycle is S6 invariant.

The existing FCC S4 subgroup inherits this automatically. Therefore no rotation symmetry in the current axis-permutation skeleton distinguishes the possible m-cover choices.

## 7. Research consequence

At the historical 2026-09-05 research frontier, the native Cell model selection within this cover family was reduced to one **already existing, exact, composable** coordinate:

`COMMON_DEPTH`.

No other coordinate/fibre freedom remains in the connected commuting coordinate-faithful model class.

The historical Foundation selection question was:

`DOES COMMON_DEPTH BELONG TO FULL CELL IDENTITY?`

- no -> m=1;
- periodically mod m -> finite m>1;
- yes as integer -> m=0.

This was an open selection criterion at the time, not an unresolved choice after P000 V5. The current frozen signed-X6 Foundation selects `m=0`, preserving the integer depth in native identity, while the old min-zero addresses remain valid observer objects.
