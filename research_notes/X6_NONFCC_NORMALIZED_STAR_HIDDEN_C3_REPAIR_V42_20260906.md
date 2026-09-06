# X6 non-FCC V42: normalized-STAR observer fibers split into common-depth and hidden-C3 repairs

Status: `FREE_RESEARCH / EXACT OBSERVER-FIBER + HOLONOMY DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_NONFCC_STAR_FACE_PATH_CARRIER_NORMALIZATION_V4_20260906.md`;
- `X6_ORIENTATION_PRESERVING_CHART_A6_UNIFICATION_V3_20260906.md`;
- centered signed-X6 slice Foundation and Joint Relation Observer Preservation.
Checker: `experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py`.

## 1. Question

V4 proves that every three-axis chart can be sent to one fixed STAR chart by an orientation-preserving `A6` frame transport, but the normalization lift is not unique.

What exact information does the local normalized STAR carrier erase, and what is the minimum repair when later operations return to native coordinates or to the full six-axis frame?

## 2. Exact stabilizer hierarchy

Fix an ordered visible chart `S={0,1,2}` and hidden complement `H={3,4,5}`. The same calculation applies after relabeling to every chart.

The setwise stabilizer of S in A6 is

`H_set={(sigma,tau) in S3(S) x S3(H) : sgn(sigma)=sgn(tau)}`

and has order 18.

It is isomorphic to

`(C3 x C3) semidirect C2`,

where the simultaneous odd element inverts both C3 factors.

If a cyclic orientation of the visible chart is fixed, the visible restriction must lie in A3 and parity forces the hidden restriction into A3 too. The residual stabilizer has order 9:

`H_cyclic = C3_visible x C3_hidden`.

If the three visible source axes are matched to the three target STAR slots pointwise, the visible restriction is identity and the remaining admissible A6 lift acts only on the hidden complement:

`H_ordered = A3(H) ~= C3`.

Thus V4's numerical fiber hierarchy

`18 -> 9 -> 3`

has the exact group meaning above.

## 3. Local STAR coordinate loss is an independent Z fiber

Let the ordered raw signed selected-axis coordinate be

`n=(n0,n1,n2) in Z^3`.

The established STAR/min-zero carrier observer sees

`r=can3(n)=n-min(n)*(1,1,1)`.

Write

`h=min(n)`.

Then exactly

`n=r+h*(1,1,1)`.

So the local STAR relative-address observer has an integer common-depth fiber Z.

This is native selected-coordinate information erased by the planar carrier kernel. It is unrelated to the hidden complement frame C3.

At the fully ordered visible interface the two losses therefore factor as

`LOCAL NORMALIZED STAR READOUT FIBER = Z_common-depth x C3_hidden-frame`

relative to a chosen reference normalization lift.

Neither factor is a new spatial axis: the Z coordinate reconstructs the three selected raw native coordinates; the C3 factor is frame transport on the omitted three axes.

## 4. Observer hierarchy by future language

Three scoped levels are exact.

### Pure local STAR-carrier future

If all future operations are proved to factor through the planar STAR carrier/min-zero address, retain only

`r`.

### Native selected-coordinate future

If a later operation asks the raw signed selected coordinates or native selected-axis component metric, retain

`(r,h)`.

This is lossless for `n`.

### Full-frame / later-chart future

If future operations may query the orientation-preserving six-axis frame or later expose currently hidden axes, also retain the hidden normalization residue

`kappa in C3_hidden`.

Relative to one fixed reference lift, the exact repair packet is

`(r,h,kappa)`.

This is observer-relative minimality: each coordinate is directly distinguishable by an allowed future at the corresponding level.

## 5. The hidden C3 is written by an actual chart loop

The three-fold residual is not merely a stabilizer count.

Use the all-20 Johnson chart connection with V3's unique even edge lift. Starting at chart

`012`,

traverse the four-edge closed path

`012 -> 013 -> 034 -> 024 -> 012`.

The product of the four even A6 edge lifts is

`(3 4 5)`

in zero-based axis labels:

- axes 0,1,2 are fixed pointwise;
- hidden axes 3,4,5 undergo one 3-cycle.

The reverse loop writes `(3 5 4)`.

Hence the full `C3_hidden` pointwise-visible stabilizer is reachable as genuine chart-path holonomy.

This proves that dropping the ordered-visible three-fold lift fiber can erase relation history that later becomes visible when a hidden axis enters a chart or a full-frame operation is applied.

## 6. Common-depth and hidden-frame losses are independent

The chart loop in section 5 changes no raw visible coordinate at all; it only changes hidden frame transport.

Conversely changing

`n -> n+k*(1,1,1)`

changes common depth while leaving the local STAR carrier readout and the six-axis frame unchanged.

Thus no one-dimensional repair can replace the pair `(h,kappa)` for a future language that queries both native coordinates and full frame.

The two losses have different algebraic types:

`h in Z`,

`kappa in C3`.

## 7. A concrete common-depth witness

Raw selected states

`n=(0,0,0)`

and

`n'=(1,1,1)`

have the same min-zero STAR readout `r=0`.

But under the current signed selected-axis metric their native squared component lengths from the same chosen Cell anchor differ:

`||n||_E^2=0`,

`||n'||_E^2=3`.

So the planar carrier kernel is not a native coordinate equivalence.

## 8. Circle/gate transport status

A chosen A6 normalization lift can pull the established STAR circle/gate/triangular carrier semantics back as a typed observer of the source chart.

The circle/gate object remains a carrier/readout token. It is not the native X6 Cell identity.

For a fully ordered visible normalization, the three hidden C3 lifts produce the same local STAR circle/gate output because they act only on omitted axes.

Therefore the C3 residue may be safely dropped only under a future-operation lease that never exposes the hidden frame.

## 9. Current closure

The normalization ambiguity is now fully typed:

- set-only normalization fiber: order 18;
- cyclic-visible normalization fiber: order 9;
- ordered-visible normalization fiber: hidden C3 of order 3;
- local planar coordinate kernel: independent integer common depth.

The local normalized STAR carrier is therefore a quotient observer, not a full chart state.

V43 compares this curved A6/frame observer with the direct rank-3 FCC basis atlas of the sixteen FACE/PATH charts.
