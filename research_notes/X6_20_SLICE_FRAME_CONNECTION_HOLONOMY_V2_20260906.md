# X6 20-slice frame connection: Johnson-graph transport and exact S3 holonomy

Status: `FREE_RESEARCH / EXACT COMBINATORIAL GLUING / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NONFCC-SLICE-REALIZATION`
Depends on: `X6_NONFCC_THREE_AXIS_CARRIER_CLASSIFICATION_V1_20260906.md`

## 1. Why the residue is a gluing problem

V1 closes the three realization strengths:

- every one of the 20 three-axis selections exists natively as a signed X6 `Z^3` subtorsor and has intrinsic C6/C12 path dynamics;
- only the four STAR selections are 120-degree charts inside the one fixed FCC six-line carrier;
- no single ordinary real-inner-product carrier with six fixed line identities can realize all 20 as equal-unit 120-degree triples.

Thus any all-20 carrier atlas must allow chart-dependent frames and nontrivial transition data.

This note constructs the smallest axis-label/frame connection forced by the 20 selections themselves. It is a combinatorial observer atlas; it does not yet identify carrier points across charts.

## 2. Johnson graph of three-axis selections

Let

`B = { S subset {1,...,6} : |S|=3 }`.

There are 20 charts. Join `S` and `T` by an edge when

`|S intersect T|=2`.

This is the Johnson graph `J(6,3)`.

An edge changes exactly one visible axis:

`S = K union {a}`,

`T = K union {b}`,

with `|K|=2`.

## 3. Canonical replacement transport

For an oriented adjacent edge `S -> T`, define the canonical axis-bijection

`r_ST:S -> T`

by

- fixing each axis in `K=S intersect T`;
- sending the unique removed axis `a` to the unique entering axis `b`.

This is the unique bijection that preserves the two shared axis identities.

A local triangular **frame** on chart `S` is a bijection

`f_S:S -> {0,1,2}`

to the three slots of one abstract 120-degree triangular template.

Transport the frame along `S->T` by

`f_T = f_S o r_ST^{-1}`.

Equivalently, the two shared axes keep their slot labels and the entering axis inherits the slot vacated by the removed axis.

No geometry beyond axis identity is used.

## 4. Loop holonomy

For a chart loop

`S_0 -> S_1 -> ... -> S_m=S_0`,

compose the replacement maps:

`h = r_{S_{m-1}S_m} ... r_{S_0S_1}: S_0 -> S_0`.

This is a permutation in `Sym(S_0) ~= S3`.

Changing the initial slot frame only conjugates its `S3` matrix representation, so the cycle type of `h` is gauge invariant.

Thus the atlas has a well-defined combinatorial frame holonomy.

## 5. The 120 triangular loops split into two exact types

The Johnson graph has 120 unordered 3-cycles. They split evenly.

### Type F: common-pair triangles

Example:

`{1,2,3} -> {1,2,4} -> {1,2,5} -> {1,2,3}`.

All three charts share the same two-axis core. Their union has size 5 and triple intersection has size 2.

The replacement transport cycles only the temporary third-axis occupant while returning the original third axis to its original slot. The loop holonomy is identity.

There are exactly 60 such flat triangles.

### Type C: four-axis triangles

Example:

`{1,2,3} -> {1,2,4} -> {1,3,4} -> {1,2,3}`.

The three charts lie inside one four-axis set; their union has size 4 and triple intersection has size 1.

The replacement transport returns to the starting chart with the two non-common starting axes exchanged. Hence the holonomy is a transposition.

There are exactly 60 such curved triangles.

Therefore the simplest all-20 triangular-frame atlas is not flat.

## 6. Holonomy group is the full S3

Fix one base chart `S={i,j,k}`.

For each fourth axis `l` outside `S`, suitable four-axis triangular loops based at `S` realize the three transpositions

`(ij)`, `(ik)`, `(jk)`

on the base chart.

These transpositions generate `S3`.

Hence the connection holonomy group at every chart is

`Hol(J(6,3)) = S3`.

This proves that no choice of local slot frames can make all canonical replacement transports path-independent.

The obstruction is not a failure of native X6 consistency. It is exactly the transition data required when one insists on presenting all native three-axis selections through one three-slot triangular carrier template.

## 7. Relation to the global Euclidean no-go

V1 showed that a single fixed six-line Euclidean Gram representation cannot realize all 20 local 120-degree triads.

V2 shows what survives instead:

- each chart may carry its own triangular template;
- overlapping charts admit a canonical shared-axis frame transition;
- the transition connection has nontrivial `S3` holonomy.

Thus the appropriate all-20 carrier object is an **atlas/bundle with transition data**, not one globally fixed six-vector picture.

The present holonomy is combinatorial chart-frame holonomy. It must not be renamed physical curvature/spin without an additional bridge theorem.

## 8. Full-state transport requires a repair coordinate

Frame transport is not enough to transport arbitrary full X6 state observations.

Let adjacent charts be

`S=K union {a}` and `T=K union {b}`.

For a full signed X6 coordinate state `z in Z^6`, the raw selected-coordinate observation on `S` gives

`(z_k : k in K, z_a)`.

The raw observation on `T` requires

`(z_k : k in K, z_b)`.

The new coordinate `z_b` is not determined by the old chart observation. Exactly one additional signed integer coordinate is sufficient for this one chart switch.

Therefore:

`FRAME_TRANSITION != FULL_STATE_OBSERVER_TRANSITION`.

An adjacent all-state chart switch needs the entering-axis coordinate as an explicit repair datum, or must retain the full X6 state upstream.

For min-zero/relative carrier observers, the appropriate common-depth repair is additionally required whenever native signed coordinates are needed.

## 9. Canonical transport versus physical rotation

The replacement map `r_ST` is an observer/chart transport between two selected coordinate frames. It is not automatically a physical native rotation event and carries no Cell-path duration by itself.

Physical rotation remains governed by `Q_S`, `ROT_PATH_X6`, triadic/internal state and native time.

The chart connection is instead the correct bookkeeping layer for comparing local carrier descriptions without collapsing axis identity.

## 10. Current carrier frontier

At this point the original non-FCC task is reduced to a sharply typed residue:

1. native realization for all 20: closed;
2. current fixed FCC realization: exactly four STAR, closed;
3. one global fixed real-inner-product six-line realization: impossible, closed;
4. abstract all-20 triangular-frame atlas with canonical overlap transport: constructed;
5. exact frame holonomy group: `S3`, closed;
6. physical/engineering meaning of chart holonomy and choice of useful non-Euclidean/richer carrier readout: open.

No P000/Foundation mutation is made.
