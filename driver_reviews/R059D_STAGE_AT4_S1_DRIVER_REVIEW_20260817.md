# R059D Stage AT4-S1 — Driver Review

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`

Task: `RS-R059D-STAGE-AT4-S1-SINGLE-CHAMBER-SECTOR-HIDDEN-CELL-ALGEBRAIC-COLLAPSE`

Researcher: `EM-R059D-AT4S1-8C4E17`

Taskbook source: `cba1b1bbd5c9e99fa7db0d9fad12e40f90fc5bb5`

Owner branch: `research/r059d-stage-at4-s1-sector-hidden-collapse`

Frozen owner head: `e1768f30f7f844fe8574769f0e6e84928c273908`

AT4 main parent: `44ad1582bd45148b2d3811e4e750efa3771fc197`

## Driver disposition

`DRIVER_ACCEPTED__FIRST_SECTOR_FRESH_HIDDEN_CELL_AT_R3__EXACT_INCIDENCE_DOMINATES__UP_DOWN_ENDPOINT_COLLAPSE_NONCANONICAL`

The result is accepted as an exact theorem for one fixed admissible chamber and one representative fundamental sector only.

Do not promote it yet to a globally glued Enterprise circle theorem.

## 1. Accepted local algebraic sector theorem

Inside the fixed chamber/sector, use the already frozen chamber-local algebraic vector law

`q(x,y)=||V||_E^2=x^2+y^2`, `x,y>=0`.

The signed-origin-conjugate A2 triangular carrier is used strictly as the local native cell-incidence chart:

- `U(i,j)=conv((i,j),(i+1,j),(i,j+1))`;
- `D(i,j)=conv((i+1,j),(i,j+1),(i+1,j+1))`.

Within this local algebraic chart, a radius-r arc is `q=r^2`.

For each closed cell `C`, the exact hit criterion is

`q_min(C) <= r^2 <= q_max(C)`.

Full containment in the algebraic disk is

`q_max(C) <= r^2`.

This is accepted as chamber-local algebraic incidence, not as imported source-circle membership. The proof uses the frozen algebraic norm, exact cell q-ranges, and native triangular incidence; it does not use angles, standard pi, historical AK/AL/N membership, graph distance as radius, or nearest-center projection.

## 2. First fresh hidden cell

The first fully contained sector cell that has never been hit by any historical integer-radius arc is exactly

`D(1,1)`

at

`r_* = 3`.

Its auxiliary local vertices are

`(2,1), (1,2), (2,2)`.

Its native signed-origin vertex encodings are

`(3,2,-4), (2,3,-4), (3,3,-5)`.

Its exact squared-norm interval is

`q(D(1,1))=[9/2,8]`.

Therefore

`4 < 9/2 <= q <= 8 < 9`.

Hence:

- radius 1 and radius 2 do not fully contain the cell;
- radius 3 fully contains it;
- historical integer-radius perimeter levels through 3 have squared radii `1,4,9`, none in `[9/2,8]`;
- no edge/vertex tie can make the cell historically traced.

Minimality is exact: every fully contained sector cell through radius 2 has a q-range containing square 1 or 4; at radius 3, `D(1,1)` is the unique square-gap witness.

Freeze:

`FIRST_SECTOR_FRESH_HIDDEN_CELL = D(1,1)`.

`FIRST_SECTOR_FRESH_HIDDEN_RADIUS = 3`.

`FIRST_HIDDEN_MECHANISM = STRICT_CONSECUTIVE_INTEGER_SQUARE_GAP`.

This is the first exact evidence that the vector-radius formulation permits an interior cell to appear without ever having been a historical integer-radius perimeter cell, unlike the rejected graph-distance-shell model.

## 3. Algebraic overshoot / collapse direction

For a strict overshoot edge `P--Q` with

`q(P) < r^2 < q(Q)`,

the level set `q=r^2` crosses the edge interior at a unique point because q is continuous and strictly monotone on the oriented edge.

That exact shell point belongs to every native triangular cell incident to the crossed edge. In the interior of the sector, this gives a two-cell set-valued hit.

Therefore:

- `PRE/DOWN` is only an endpoint proxy;
- `POST/UP` is only an endpoint proxy;
- `NEAREST_SQUARED_NORM` is only an endpoint proxy;
- the canonical local object is `EXACT_EDGE_INCIDENCE` with all incident cells retained.

Freeze:

`CANONICAL_ALGEBRAIC_COLLAPSE_DIRECTION = NONE_AT_ENDPOINT_LEVEL`.

`CANONICAL_LOCAL_COLLAPSE_OBJECT = EXACT_ALGEBRAIC_CROSSING + INCIDENT_CELL_SET`.

The first strict overshoots already occur at radius 2:

- `(1,1)--(2,1)` with `2<4<5`;
- `(1,1)--(1,2)` with `2<4<5`.

Nearest squared norm chooses POST because the deficits are 2 and 1, but the exact crossings are `(sqrt(3),1)` and `(1,sqrt(3))`. This proves that even an untied nearest choice is not the native incidence law.

## 4. Why UP/DOWN proxies would corrupt the hidden-point theorem

At radius 2, POST/nearest picks proxy vertices `(2,1)` and `(1,2)`. Both are vertices of the later hidden cell `D(1,1)`.

However the exact radius-2 arc does not enter `D(1,1)`, because

`q_min(D(1,1))=9/2>4`.

If proxy endpoint membership were promoted to perimeter cell trace, the model would falsely mark `D(1,1)` as historically traced and erase the genuine radius-3 hidden witness.

Freeze:

`ENDPOINT_PROXY_OVERTRACING_CAN_ERASE_TRUE_HIDDEN_CELLS`.

Thus collapse-direction heuristics are not merely noncanonical; they can change the historical perimeter support incorrectly.

## 5. Reverse shortest paths retain secondary status

For `D(1,1)`, minimum-entry vertices are `(2,1)` and `(1,2)`.

Each has spatial minimum-jump length 3 and exactly three monotone shortest tails, giving six minimum-entry spatial realizations total. With the unique `VOID_E -> O_E` prefix the full minimum jump count is 4.

At the radius-2 overshoot, PRE `(1,1)` has spatial minimum count 2 while POST `(2,1)` or `(1,2)` has 3, despite the same target vector radius 2.

Therefore reverse graph distance cannot select vector radius or algebraic collapse direction.

## 6. Validation and immutability

Deterministic checker:

- `418685 / 418685 PASS`;
- digest `4b2a82f6c768401bc3b7e7810aa511afd80e7a55912f533478dd7a24757de286`;
- exact U/D q-extrema and reflection through local labels 256;
- fresh-hidden generation through radius 256;
- all 5530 strict primitive-edge overshoot events through radius 64;
- all incident-cell hits on every overshoot edge;
- 44 exact nearest-squared-norm ties;
- reverse geodesic cardinality checks;
- external history gate PASS.

Research checkpoint records no prior or AT4-main files modified/deleted.

## 7. Scope boundaries

Not proved here:

- global chamber gluing;
- global Enterprise circle support;
- global perimeter law;
- native area law;
- that `r=3` is already the first hidden level after global chamber gluing;
- any canonical PRE/POST/nearest endpoint collapse policy.

The accepted theorem is local but decisive: the hidden-cell mechanism exists already in one chamber/sector at radius 3, and exact algebraic incidence—not UP/DOWN endpoint collapse—is the correct local shell-to-cell object.

## 8. Routing

AT4-S1 is complete.

Per taskbook stop condition:

`STOP_FOR_DRIVER_REVIEW`.

Do not open a successor automatically and do not consume the AT4 main owner branch.

AT4 main should consume this review as a hard constraint:

1. preserve exact cell incidence under chamber gluing;
2. never replace edge crossings by PRE/POST/nearest endpoint proxies;
3. explicitly test whether the local `r=3`, `D(1,1)` hidden witness survives D6 transport and cross-chamber gluing;
4. distinguish local hidden-cell existence from any later global area theorem.
