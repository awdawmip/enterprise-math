# X6 rotation V12: complete signed-cycle phase atlas for all 46080 integral frame isometries

Status: `FREE_RESEARCH / COMPLETE STATIC CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FULL_INTEGRAL_ISOMETRY_AND_ORI6_GATE_V7_20260906.md`;
- `X6_ORI6_EVENT_CHARGE_AND_OBSERVER_BOUND_V8_20260906.md`;
- V10 global C12 and V11 double-triad C6+C6 classes.
Checker: `experiments/x6_signed_cycle_atlas_v12_20260906/check_signed_cycle_atlas.py`.

## 1. Signed cycle type

Every integral X6 frame isometry is a signed permutation

`g(E_i)=epsilon_i E_{p(i)}`.

Decompose the positive-axis permutation `p` into disjoint cycles. For each positive-axis cycle `C`, record:

- its length `ell(C)`;
- its sign holonomy `h(C)=product_{i in C}epsilon_i in {+1,-1}`.

Define two integer partitions:

`lambda_+(g)=sorted lengths of cycles with h=+1`,

`lambda_-(g)=sorted lengths of cycles with h=-1`.

The pair

`Sigma(g)=(lambda_+,lambda_-)`

is the **signed cycle type**.

The total of all parts is six.

## 2. Signed cycle type is the complete B6 conjugacy invariant

Conjugating by a signed permutation relabels the positive-axis cycles and changes local sign gauges, but preserves cycle lengths and the product of signs around each cycle. Hence `Sigma` is conjugacy invariant under the full integral frame group

`B6=(C2)^6 semidirect S6`.

Conversely, if two signed frames have the same signed cycle type, first relabel positive axes so cycles of equal length/holonomy align. On each aligned cycle, diagonal sign conjugation can move all local sign choices while preserving the cycle product. Therefore the two frames are B6-conjugate.

Thus:

`B6 CONJUGACY CLASSES <-> SIGNED CYCLE TYPES`.

For total rank six there are exactly **65** such types.

## 3. Exact class-size formula

For every length `ell`, let

`a_ell=# positive-holonomy cycles of length ell`,

`b_ell=# negative-holonomy cycles of length ell`.

The centralizer order in `B6` is

`z(Sigma)=product_ell (2ell)^(a_ell) a_ell! (2ell)^(b_ell) b_ell!`.

Hence the B6 conjugacy-class size is

`|Class(Sigma)| = 2^6 6! / z(Sigma)`.

The checker verifies this formula against all 46080 signed frames.

Examples:

- one negative 6-cycle: centralizer 12, class size 3840 — exactly V10 global C12;
- two negative 3-cycles: centralizer 72, class size 640 — exactly V11 double-C6.

## 4. Primitive signed-direction phase partition

For a positive-axis cycle of length `ell`:

- holonomy `+1` produces **two** signed-direction cycles of length `ell`;
- holonomy `-1` produces **one** signed-direction cycle of length `2ell`.

Therefore `Sigma` maps to a coarser phase partition of 12:

`Phi(Sigma)=`

- two parts `ell,ell` for every part `ell` of `lambda_+`;
- one part `2ell` for every part `ell` of `lambda_-`.

Across all 65 signed cycle types, only **40 distinct primitive-direction orbit-length partitions** occur.

So phase orbit lengths alone are not a complete static frame invariant.

## 5. Ori6 from signed cycle type

The positive-axis permutation parity depends only on its number of cycles `c`:

`Ori_6(g) = (6-c) mod 2`,

where

`c=len(lambda_+)+len(lambda_-)`.

The sign holonomies do not change `Ori_6`.

Thus signed cycle type always determines the current orientation charge.

But its coarser phase partition `Phi` need not.

Exact atlas counts:

- 31 phase partitions occur in `Ori_6=0`;
- 27 occur in `Ori_6=1`;
- **18 occur in both sectors**;
- their union contains 40 partitions.

This gives a sharp observer warning:

`PRIMITIVE_DIRECTION_ORBIT_LENGTHS != ORI6_COMPLETE_OBSERVER`.

## 6. Key examples and correction to overgeneralization

### One C12

Phase partition

`(12)`

occurs only in the odd sector, with exactly 3840 frames. This is V10's global signed-direction-transitive class.

So one global primitive-direction C12 does imply `Ori_6=1`.

### C6+C6

Phase partition

`(6,6)`

occurs in both sectors:

- 640 even frames from the two-negative-3-cycle class — V11's double-triad family;
- 3840 odd frames from a **positive-holonomy 6-cycle**, which splits into two C6 signed-direction orbits.

Therefore:

`C6+C6 PHASE TOPOLOGY ALONE != ORI6=0`.

V11 remains exactly correct for the explicitly typed complementary-triad class, but its topology must not be generalized into a global orientation classifier.

This is a self-correction/strength guard supplied by the complete atlas.

## 7. R_triad conjugacy can refine a B6 class

Current orientation-preserving frame changes use

`R_triad=(C2)^6 semidirect A6`,

an index-two normal subgroup of `B6`.

A B6 conjugacy class either remains one `R_triad` conjugacy orbit or splits into exactly two equal `R_triad` orbits.

The class stays one orbit iff the B6 centralizer of one representative contains at least one `Ori_6=1` element. Such an odd centralizer element relates the two possible even-frame coordinate orientations.

It splits iff its entire centralizer lies in `R_triad`.

## 8. Exact splitting criterion

The centralizer has an odd positive-axis permutation in either of two situations.

### Even-length cycle

Rotating one positive-axis cycle of even length by one step is an odd permutation and centralizes the frame cycle.

Therefore any signed cycle type containing an even-length positive-axis cycle does **not** split.

### Repeated equal odd signed-cycle type

If two cycles have the same odd length and the same sign holonomy, exchanging those two cycles is a product of an odd number of transpositions, hence an odd centralizer element.

Therefore such a type also does not split.

Conversely, if all cycle lengths are odd and no pair `(length,holonomy)` is repeated, every centralizer permutation is even. Hence the B6 class splits into two `R_triad` orbits.

So:

`SPLIT_UNDER_R_TRIAD`

iff

`ALL CYCLE LENGTHS ODD`

and

`EACH (LENGTH,HOLONOMY) TYPE OCCURS AT MOST ONCE`.

## 9. Exactly five split types in X6

At total positive-axis size six, the criterion leaves exactly five signed cycle types:

1. `lambda_+=(5,1)`, `lambda_-=()`;
2. `lambda_+=(5)`, `lambda_-=(1)`;
3. `lambda_+=(1)`, `lambda_-=(5)`;
4. `lambda_+=()`, `lambda_-=(5,1)`;
5. `lambda_+=(3)`, `lambda_-=(3)`.

The first four are the four holonomy choices on a `5+1` positive-axis cycle structure. The fifth has two length-three cycles with **opposite** holonomy signs, so the cycles cannot be exchanged by a centralizer element without changing signed type.

Hence:

- B6 has 65 signed-cycle conjugacy classes;
- current `R_triad` has **70** conjugacy orbits on the same 46080 frame elements.

The extra five are exact even-frame chirality splittings.

## 10. Why V10 and V11 are unsplit

V10 global C12 has one **negative length-6** cycle. Length six is even, so its centralizer contains an odd cycle rotation. Its 3840 frames stay one `R_triad` orbit, as already proved.

V11 double-triad class has two **negative length-3** cycles of the same signed type. Swapping the two odd cycles is an odd centralizer element. Its 640 frames also stay one `R_triad` orbit.

Thus the V10/V11 conjugacy results become instances of the general V12 criterion rather than isolated enumerations.

## 11. Interpretation of the split bit

For one of the five split B6 types, full signed-frame relabeling regards all elements as one static type, but current `Ori_6=0` frame changes cannot conjugate between the two halves.

Therefore a task that works only with current triadic/even coordinate changes may need one extra **conjugacy-chirality bit** to distinguish the two halves.

This bit is not the global `Ori_6` event charge: both split halves belong to the same B6 signed-cycle type and have the same positive permutation parity.

An admitted odd frame relabeling would exchange the two split halves and erase this distinction at the full-B6 conjugacy level.

No physical observable meaning is assigned without a future-operation bridge.

## 12. Complete static phase-observer hierarchy

For one integral frame isometry, increasingly coarse readouts are now:

1. exact signed permutation frame `g`;
2. `R_triad` conjugacy orbit — 70 possible static orbit types;
3. full-B6 signed cycle type `Sigma` — 65 types;
4. primitive signed-direction orbit-length partition `Phi(Sigma)` — 40 types;
5. coarse period/order or a single phase token — still less information.

`Ori_6` is recoverable from level 2 or 3, but not always from level 4.

As usual, no downward projection is globally safe merely because it is easy to compute. The future operation/observer language decides which distinctions may be discarded.

## 13. Reusable classifier interface

The static frame classifier needed by later tasks is finite and exact:

Input:

`signed permutation frame g`.

Return:

- positive-axis cycle decomposition;
- sign holonomy of every cycle;
- signed cycle type `Sigma=(lambda_+,lambda_-)`;
- primitive-direction phase partition `Phi`;
- frame order;
- `Ori_6` charge;
- B6 class size;
- whether the B6 class splits under `R_triad`;
- special predicates such as `GLOBAL_C12` or `DOUBLE_TRIAD_C6_C6`.

The checker implements the core of this interface. If multiple downstream programs reuse it, it can be promoted later through the normal toolbox admission route.

## 14. Verification

The exact checker scans all 46080 signed frame isometries and verifies:

- exactly 65 signed cycle types;
- the class-size formula for all 65;
- exactly 40 primitive-direction orbit partitions;
- exact `Ori_6=(6-cycle_count) mod2` rule;
- 31 even-sector and 27 odd-sector phase partitions, with 18 shared;
- `(12)` occurs `0/3840` in even/odd sectors;
- `(6,6)` occurs `640/3840` in even/odd sectors;
- exactly five signed cycle types satisfy the splitting criterion;
- direct enumeration of **70** `R_triad` conjugacy orbits;
- every split B6 class divides into two equal current-frame conjugacy orbits.

No Foundation promotion, physical law or external novelty claim is made.
