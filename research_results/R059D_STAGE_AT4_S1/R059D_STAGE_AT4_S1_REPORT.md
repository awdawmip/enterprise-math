# R059D Stage AT4-S1 — Final Report

Researcher-ID: `EM-R059D-AT4S1-8C4E17`

Task: `RS-R059D-STAGE-AT4-S1-SINGLE-CHAMBER-SECTOR-HIDDEN-CELL-ALGEBRAIC-COLLAPSE`

Taskbook source: `cba1b1bbd5c9e99fa7db0d9fad12e40f90fc5bb5`

Owner: `research/r059d-stage-at4-s1-sector-hidden-collapse`

AT4 main parent: `44ad1582bd45148b2d3811e4e750efa3771fc197`

## Disposition

`FIRST_SECTOR_FRESH_HIDDEN_CELL_AT_R3__EXACT_CELL_INCIDENCE_SET_VALUED__ENDPOINT_COLLAPSE_DIRECTION_NONCANONICAL`

This is a single-chamber / single-sector theorem only. It does not consume or modify AT4 main and does not claim a globally glued circle/perimeter/area law.

## 1. Sector model

A representative chamber `Q0` with adjacent active native directions `e_x,e_y` is recharted to nonnegative local vector components

`V=x e_x+y e_y`, `x,y>=0`, `q=x^2+y^2`.

Native cell incidence is the signed-origin-conjugate A2 triangular carrier:

- `U(i,j)=conv((i,j),(i+1,j),(i,j+1))`;
- `D(i,j)=conv((i+1,j),(i,j+1),(i+1,j+1))`.

The auxiliary labels are cell/vector computation coordinates only. Algebraic component zero does not create native coordinate zero.

All adjacent-direction sectors are equivalent after D6 transport plus mandatory chamber recharting; one raw `(x,y)` expression is never continued across a chamber boundary.

## 2. Exact cell-hit theorem

For each cell `C`, compute its exact continuous q-range `[q_min(C),q_max(C)]`.

For U cells:

`q_min=i^2+j^2`,

`q_max=i^2+j^2+2 max(i,j)+1`.

For D cells:

`q_max=(i+1)^2+(j+1)^2`,

and the minimum lies on the inner diagonal edge. If `|i-j|<=1`,

`q_min=(i+j+1)^2/2`;

otherwise the nearer inner-edge endpoint gives the stated piecewise integer formula.

The exact radius-r algebraic arc hits a closed cell iff

`q_min(C)<=r^2<=q_max(C)`.

The radius-r algebraic disk fully contains a cell iff

`q_max(C)<=r^2`.

All edge/vertex tie cells survive.

## 3. First hidden cell

The first fully contained cell never hit by any historical integer-radius arc is

`D(1,1)`

at radius

`r_*=3`.

Its vertices are `(2,1),(1,2),(2,2)`. The exact q-range is

`[9/2,8]`.

The inner minimum is at `(3/2,3/2)` and the maximum is at `(2,2)`.

Thus

`4 < 9/2 <= q(D(1,1)) <= 8 < 9`.

Radii 1 and 2 cannot fully contain it; radius 3 fully contains it, but historical integer squares `1,4,9` all miss its q-range. No boundary tie can change this.

Minimality is exact: all fully contained cells through radius 2 have q-ranges containing square 1 or 4. At radius 3, `D(1,1)` is the unique new square-gap witness.

The sector census through radius 64 confirms continued lifetime-hidden growth; at r=64 there are 526 fully-contained cells never hit by any integer-radius perimeter, with 20 first admitted at that radius.

## 4. Overshoot and collapse direction

A strict vector-radius overshoot is a primitive edge `P--Q` with

`q(P)<r^2<q(Q)`.

The first two occur at r=2:

- `(1,1)--(2,1)`;
- `(1,1)--(1,2)`.

Both have q bracket `2<4<5`, with deficits

`delta_down=2`, `delta_up=1`.

Nearest squared norm chooses POST.

However the actual algebraic shell crosses the edge interiors at

`(sqrt(3),1)` and `(1,sqrt(3))`.

The horizontal crossing hits `U(1,1)` and `D(1,0)`; the vertical crossing hits `U(1,1)` and `D(0,1)`.

Therefore PRE, POST and nearest are endpoint proxies, not native shell-to-cell laws.

The exact local collapse object is the set of all incident cells of the crossed primitive edge. Away from chamber boundaries that set has two cells.

Through r=64 the checker expands 5,530 strict overshoot events. Nearest has 44 exact ties. H/V edge ties are impossible; diagonal ties satisfy the exact quadratic integer condition frozen in the event artifact.

## 5. Hidden/collapse coupling

The r=3 hidden cell is not caused by choosing DOWN or UP. Its entire q-range lies strictly between historical integer squares 4 and 9.

Endpoint-proxy collapse can falsely erase the witness. At r=2, POST/nearest selects `(2,1)` and `(1,2)`, which are vertices of `D(1,1)`, even though the actual q=4 arc does not enter that cell. Treating proxy-vertex incidence as perimeter trace would therefore over-trace a cell that the algebraic shell never hits.

Hence exact cell incidence dominates endpoint collapse heuristics, and the canonical local r-star is 3.

## 6. Reverse geodesic certificates

Reverse minimum-jump paths are secondary.

The first hidden cell `D(1,1)` has two minimum-entry vertices `(2,1)` and `(1,2)`. Each has spatial tail length 3 and three monotone shortest tails, for six minimum-entry realizations total. Including the unique `VOID_E -> O_E` prefix gives minimum full jump count 4.

At the first r=2 overshoot, PRE `(1,1)` has spatial jump count 2 while POST `(2,1)` or `(1,2)` has 3, even though target vector radius is fixed at 2. This independently confirms that reverse jump count cannot define vector radius or collapse direction.

## 7. Validation

Deterministic checker source:

`research_results/R059D_STAGE_AT4_S1/r059d_stage_at4_s1_deterministic_checker.py`

Independent result before history gate:

- checks: `418685 / 418685 PASS`;
- digest: `4b2a82f6c768401bc3b7e7810aa511afd80e7a55912f533478dd7a24757de286`;
- cell extrema/reflection through local labels 256;
- fresh-hidden generation through r=256;
- every strict overshoot event through r=64;
- exact r=2 edge incidence;
- reverse geodesic cardinalities.

Finite replay supports the implementation. The first-hidden and collapse-direction statements are proved symbolically in `R059D_STAGE_AT4_S1_PROOF.md`.

## 8. Boundaries

Not claimed:

- AT4 global chamber gluing;
- a global Enterprise circle;
- a global perimeter law;
- native area from cell cardinality;
- PRE/DOWN, POST/UP, or nearest as a canonical endpoint-collapse law;
- use of graph distance as radius;
- use of historical AK/AL/N membership as an oracle.

Stop for Driver review after checkpoint freeze.
