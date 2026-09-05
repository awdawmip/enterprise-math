# X6：V2 common-depth carry 与 full Cell cover fibre 的统一

Status: `DERIVED / EXACT CROSS-BRANCH SYNTHESIS / BRC-FIRST`
Date: `2026-09-05`
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

Thus the **same common-depth carry** discovered and toolized in the derived six-axis BRC/count atlas is exactly the central-extension cocycle of every possible coordinate-faithful connected full Cell cover.

No new hidden-state mechanism is needed.

Associativity of the Cell-cover multiplication is exactly the existing carry 2-cocycle identity.

## 4. Meaning of the three principal cases

### m=1 — coordinate-complete Cell identity

The depth fibre is trivial. `c(a,b)` is pure canonicalization carry and is not Cell identity.

`X6 endpoint = min-zero six-coordinate torsor`.

### finite m>1 — periodic depth memory

Only common depth modulo m belongs to full Cell identity. Coordinate observations see r but forget the residue.

A complete six-axis diagonal cycle advances the fibre by 1; m cycles return.

### m=0 — unbounded depth memory

The entire integer diagonal depth belongs to full Cell identity. No nonzero number of complete diagonal cycles returns the same full Cell.

## 5. BRC observer hierarchy

This synthesis clarifies the correct BRC information rule:

- general six-count / path observer: retain exact depth h and branch provenance;
- coordinate endpoint observer: retain only r=can6(n);
- m-cover Cell endpoint observer: retain `(r,h mod m)`;
- primitive coordinate-complete Cell observer: m=1, so h is not identity but Path/BRC may still retain it as history/count data.

Hence

`DEPTH_NOT_CELL_IDENTITY != DEPTH_INFORMATION_MAY_BE_DELETED_FROM_ALL_OBSERVERS`.

Even at m=1 the general BRC/path layer may need exact h for future concatenation, length/moment or provenance observers.

## 6. Rotation covariance

For any six-axis permutation sigma,

`min(sigma a + sigma b)=min(a+b)`.

So the depth cocycle is S6 invariant.

The existing FCC S4 subgroup inherits this automatically. Therefore no rotation symmetry in the current axis-permutation skeleton distinguishes the possible m-cover choices.

## 7. Research consequence

The X6 native Cell question has now converged to the semantic status of one **already existing, exact, composable** coordinate:

`COMMON_DEPTH`.

No other coordinate/fibre freedom remains in the connected commuting coordinate-faithful model class.

The exact Foundation question is:

`DOES COMMON_DEPTH BELONG TO FULL CELL IDENTITY?`

- no -> m=1;
- periodically mod m -> finite m>1;
- yes as integer -> m=0.

The established three-axis primitive address rule treats its analogous common diagonal offset as outside primitive point/Cell address, which is strong structural evidence for m=1 in the full lift, but the full six-axis choice should be frozen explicitly rather than smuggled in as a theorem.
