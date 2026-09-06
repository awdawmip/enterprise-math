# X6 all-20 chart V3: unique orientation-preserving lifts and the common A6 skeleton

Status: `FREE_RESEARCH / EXACT GLUING + GROUP UNIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Tasks: `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- 20-chart `J(6,3)` replacement connection and local `S3` holonomy;
- global orientation torsor `Ori_6=S6/A6`;
- triadic positive-axis frame group image `A6`;
- unsigned triadic channel group `A6`.

## 1. Adjacent chart replacement has two natural global involutive extensions

Let adjacent three-axis charts be

`S=K union {a}`

and

`T=K union {b}`,

where `|K|=2` and `a!=b`.

The local chart replacement fixes the two shared axes in `K` and sends the removed axis `a` into the new axis `b`.

Let the two axes outside `S union T` be `{c,d}`.

If the global extension is required to

- fix the two shared axes in `K`;
- exchange the removed/entering pair `a,b` so the transition is reversible;
- preserve the set `{c,d}`;

then exactly two involutive `S6` extensions exist:

`r_odd=(a b)`

and

`r_even=(a b)(c d)`.

Their positive-axis permutation parities are respectively odd and even.

## 2. Unique Ori_6-preserving chart lift

The global orientation charge `Ori_6=S6/A6` is preserved exactly by even axis permutations.

Therefore, among the two natural reversible extensions above, there is exactly one orientation-preserving lift:

`R_ST=(a b)(c d)`.

Call this the **even chart lift**.

Thus, conditional on preserving the triadic orientation sector, every adjacent all-20 chart replacement has a unique full-six-axis frame transport.

No arbitrary complement convention remains: the two completely hidden axes are forced to exchange.

## 3. Relation to current FCC/K4 STAR transitions

A K4 vertex transposition acts on the six K4 edges by exactly two disjoint transpositions. When restricted to the source/target STAR charts, one pair implements the visible removed/entering chart replacement and the other pair acts on the two axes hidden from both charts.

Hence the established FCC/K4 `S4` chart transport is exactly the even-lift rule above on the STAR subatlas.

So the all-20 orientation-preserving lift is a genuine extension of the existing FCC behavior, not a competing convention.

## 4. Global holonomy of the 120 Johnson triangles

Recall the 120 unordered triangular loops of `J(6,3)`.

### Common-pair triangle

Example:

`123 -> 124 -> 125 -> 123`.

The even lifts are

`(34)(56)`, `(45)(36)`, `(35)(46)`

in one-based shorthand.

Their product is identity.

Hence the 60 common-pair triangles remain globally flat under the even lift.

### Four-axis triangle

Example:

`123 -> 124 -> 134 -> 123`.

The product of the three even lifts is

`(23)(56)`

(up to the corresponding relabeling convention):

- one transposition is the previously observed local slot holonomy on the starting chart;
- the second transposition acts on the two axes outside the four-axis union and repairs the full six-axis orientation parity.

Thus every one of the 60 four-axis triangles has a nontrivial **double-transposition** global holonomy in `A6`.

Its restriction to the starting three-slot chart is the old local transposition holonomy.

## 5. All 45 double transpositions occur as chart-edge lifts

An even chart edge lift has cycle type `(2,2)` and fixes exactly two axes.

Conversely, take any double transposition

`(a b)(c d)`

with two remaining fixed axes `K`.

Choose

`S=K union {a}`,

`T=K union {b}`.

Then `{c,d}` is exactly the pair hidden from both adjacent charts, and the unique even chart lift `R_ST` is the given double transposition.

Therefore the set of all even chart-edge lifts is exactly the full conjugacy class of 45 double transpositions in `A6`.

## 6. These chart lifts generate all of A6

The set of all double transpositions is a nontrivial conjugacy class inside `A6`.

Its generated subgroup is normal in `A6`. Since `A6` is simple and the class is nontrivial, the generated subgroup is all of `A6`.

Equivalently, a direct finite closure check gives order 360.

Thus:

`<orientation-preserving all-20 chart edge lifts> = A6`.

This is a carrier/observer-frame transport statement, not yet a claim that each edge lift is one primitive physical rotation event.

## 7. The same A6 already appeared twice independently

Two current upper structures have exactly the same positive-axis/channel group:

### Triadic frame projection

`R_triad=(C2)^6 semidirect A6`

projects to `A6` by forgetting sign flips.

### Minimal unsigned channel dynamics

All oriented triadic `C3` channel circulations generate `A6`, and under the minimal frame-channel coupling their cumulative update is the same projection `pi`.

The present chart theorem adds a third occurrence:

### Orientation-preserving all-20 chart transport

Unique even adjacent chart lifts generate `A6`.

Therefore the common finite skeleton is

`A6 = TRIADIC_POSITIVE_FRAME = MINIMAL_UNSIGNED_CHANNEL_GROUP = ORIENTATION_PRESERVING_CHART_TRANSPORT_GROUP`.

These are distinct semantic actions sharing one group, not one untyped state object.

## 8. Every even chart lift is realizable as a product of triadic positive 3-cycles

A double transposition is a product of two 3-cycles. For example,

`(1 2)(3 4) = (1 4 3)(1 2 3)`

with the usual right-to-left composition convention.

Thus each orientation-preserving chart-edge frame transport lies in the positive-axis group generated by triadic rotations.

At the full signed-frame level one may additionally need sign-kernel corrections to obtain a chosen pure positive-axis lift, but the current `R_triad` already contains the complete `(C2)^6` sign kernel.

Hence no new frame-group generator is needed to realize the even chart transport algebraically.

This does not prove the corresponding physical chart switch occurs as exactly two primitive triadic time events; path/internal/time realization remains a separate law question.

## 9. Observer transport and hidden-axis repair gain a new interpretation

V2 proved that changing one raw three-axis observation requires one new entering-axis coordinate to reconstruct the next chart's raw coordinate values.

The even full-frame lift additionally exchanges the two axes hidden from both charts. This hidden complement action is invisible to both local chart observations but is mandatory if the full frame transport is required to preserve `Ori_6`.

Thus the local chart observer cannot reconstruct the full orientation-preserving frame transport without knowledge of the global six-axis labeling/orientation sector.

This is another exact instance of

`LOCAL OBSERVER TRANSPORT != FULL NATIVE FRAME TRANSPORT`.

## 10. Path dependence is real but globally typed inside A6

The even chart connection is not flat. A four-axis triangle returns to the same chart with a nontrivial double-transposition frame holonomy.

Therefore two chart-transition paths with the same initial/final selected triple can differ by an `A6` frame element.

This route dependence must be retained whenever a future observer uses the full frame or coupled unsigned channel state.

If only local chart slot data is retained, the same route dependence appears as the previously derived local `S3` holonomy.

## 11. Current synthesis

One upper-layer pattern has now converged independently from three directions:

`triadic 120-degree rotation`

`-> A6 positive-axis permutation dynamics`

`-> A6 unsigned channel circulation`

`-> A6 orientation-preserving all-20 chart transport`.

The remaining `S6/A6` bit is exactly the global `Ori_6` sector-changing charge from rotation V6 and is not generated by these orientation-preserving chart/triadic/channel structures.

This makes `A6` the current common **orientation-preserving relational skeleton** of the upper X6 program, conditional on the stated frame/channel/chart couplings.

No claim is made that classical `A6` terminology is itself native ontology, nor that all physical rotations are exhausted by this skeleton without the unresolved `Ori_6` admissibility law.
