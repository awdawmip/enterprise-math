# R059D Stage AT4-S1 — Proof

Researcher-ID: `EM-R059D-AT4S1-8C4E17`

Task: `RS-R059D-STAGE-AT4-S1-SINGLE-CHAMBER-SECTOR-HIDDEN-CELL-ALGEBRAIC-COLLAPSE`

Taskbook source: `cba1b1bbd5c9e99fa7db0d9fad12e40f90fc5bb5`

AT4 main parent: `44ad1582bd45148b2d3811e4e750efa3771fc197`

## 1. Local chamber and sector

Fix one admissible chamber `Q0` and adjacent native directions `e_x,e_y`. Inside this chamber the frozen algebraic vector law gives

`V = x e_x + y e_y`, `x,y>=0`,

`q(V)=||V||_E^2=x^2+y^2`.

The native triangular incidence carrier is represented by the signed-origin-conjugate auxiliary A2 cell IDs

`U(i,j)=conv((i,j),(i+1,j),(i,j+1))`,

`D(i,j)=conv((i+1,j),(i,j+1),(i+1,j+1))`,

for `i,j>=0`. These are cell/incidence labels. Algebraic zero components on a chamber boundary remain vector-algebra zeros, not native coordinate zero.

Native D6 transports this sector to the other adjacent-direction sectors only after recharting. We never apply one raw `(x,y)` expression across chambers.

## 2. Exact cell q-ranges

### 2.1 U cell

For `U(i,j)`, every point has `x>=i`, `y>=j`; hence the minimum is the lower vertex:

`q_min(U)=i^2+j^2`.

Because `q` is convex, its maximum over the triangle is at a vertex. The two outer vertices have values

`(i+1)^2+j^2`, `i^2+(j+1)^2`,

so

`q_max(U)=i^2+j^2+2 max(i,j)+1`.

### 2.2 D cell

For `D(i,j)`, the maximum is the far vertex `(i+1,j+1)`:

`q_max(D)=(i+1)^2+(j+1)^2`.

The inner edge joins `(i+1,j)` to `(i,j+1)` and has equation

`x+y=s`, `s=i+j+1`.

Minimizing `x^2+y^2` subject to this edge gives the unconstrained minimizer `(s/2,s/2)`. It lies on the edge exactly when `|i-j|<=1`. Therefore

- if `|i-j|<=1`, `q_min(D)=s^2/2`;
- if `j>=i+2`, the closest edge endpoint is `(i+1,j)` and `q_min(D)=(i+1)^2+j^2`;
- if `i>=j+2`, the closest edge endpoint is `(i,j+1)` and `q_min(D)=i^2+(j+1)^2`.

Since each cell is connected and `q` is continuous, `q(C)` is the full interval `[q_min(C),q_max(C)]`.

## 3. Exact algebraic arc-to-cell incidence

At integer radius `r`, the chamber arc is the algebraic level

`ARC_E(r;S0)={q=r^2}`.

Therefore a closed native cell `C` is hit exactly iff

`q_min(C) <= r^2 <= q_max(C)`.

This is not a center-nearest rule. Boundary ties are retained set-valuedly: if the level passes through a native vertex or edge, every sector cell incident to that vertex/edge is a legitimate hit.

The algebraic disk intersects `C` iff `q_min(C)<=r^2`, and fully contains `C` iff `q_max(C)<=r^2`. Full containment follows because the algebraic disk `x^2+y^2<=r^2` is convex and all cell vertices are in it exactly when `q_max(C)<=r^2`.

## 4. First fresh hidden cell

Use the strongest nontrivial interior notion requested by the taskbook: first full containment.

A fully contained cell is lifetime-hidden from integer-radius perimeter history exactly when its interval `[q_min,q_max]` contains no positive integer square.

### 4.1 Radius 1

The only fully contained cell is `U(0,0)`, with q-range `[0,1]`; it is hit by radius 1.

### 4.2 Radius 2

The fully contained cells are

`U(0,0)`, `D(0,0)`, `U(1,0)`, `U(0,1)`.

Their q-ranges contain square 1 or 4, so no hidden cell exists through radius 2.

### 4.3 Radius 3

Consider

`D(1,1)=conv((2,1),(1,2),(2,2))`.

Its inner edge is `x+y=3`; the algebraic minimum occurs at `(3/2,3/2)`:

`q_min=9/2`.

Its maximum is at `(2,2)`:

`q_max=8`.

Hence

`4 < 9/2 <= q(D(1,1)) <= 8 < 9`.

The radius-3 disk fully contains the whole cell because `q_max=8<9`, but integer-radius levels 1, 2, 3 have squares 1, 4, 9 and none lies in `[9/2,8]`. Thus no legal tie-realization of any historical integer-radius arc through radius 3 hits this cell.

Enumeration of the ten radius-3 fully contained sector cells shows this is the unique cell with square-free q-range. Therefore

`r_* = 3`,

with unique first hidden sector cell `D(1,1)`.

This is a strict consecutive-square-gap mechanism.

## 5. Overshoot edges and collapse proxies

A primitive sector edge has one of three incidence types:

- `H(i,j): (i,j)--(i+1,j)`;
- `V(i,j): (i,j)--(i,j+1)`;
- `G(i,j): (i+1,j)--(i,j+1)`.

An overshoot at target integer radius `r` is a strict bracket

`q_down < r^2 < q_up`.

For H/V the endpoint q difference is odd, so squared-norm nearest ties are impossible. For G edges a nearest tie is possible and occurs exactly when

`r^2 = i^2+j^2+i+j+1`

on a strict bracket.

But this endpoint comparison is not the native cell-hit law.

On any strict bracket edge, `q` is continuous and strictly monotone from the lower-q endpoint to the higher-q endpoint. Therefore the exact level `q=r^2` crosses the edge interior. The shell point belongs to every triangle incident to that edge, so the canonical local realization is the incident-cell set.

PRE/DOWN, POST/UP and NEAREST replace that shell point by one or two integer endpoints. They are endpoint proxies only.

### 5.1 First overshoot: radius 2

There are exactly two strict events:

`(1,1)--(2,1)`, with `2<4<5`,

`(1,1)--(1,2)`, with `2<4<5`.

Both have

`delta_down=2`, `delta_up=1`,

so nearest chooses POST.

However the exact algebraic crossings are

`(sqrt(3),1)` and `(1,sqrt(3))`.

The horizontal crossing hits `U(1,1)` and `D(1,0)`; the vertical crossing hits `U(1,1)` and `D(0,1)`.

Neither crossing hits `D(1,1)` because that cell has `q_min=9/2>4`.

Thus nearest-to-endpoint is already noncanonical at the first overshoot.

## 6. Coupling to hidden history

The first hidden cell is not produced by choosing DOWN or UP. It is produced because the whole cell q-range lies in the strict square gap `(4,9)`.

If one incorrectly promotes endpoint proxies to cell membership, POST/nearest at radius 2 selects `(2,1)` and `(1,2)`, both vertices of `D(1,1)`, and would falsely mark the hidden cell as historically traced. This is over-tracing: the actual level `q=4` never enters `D(1,1)`.

Therefore exact incidence dominates collapse heuristics, and under the surviving native policy the first hidden radius remains exactly 3.

## 7. Reverse minimum-jump certificates

Reverse shortest paths are computed only after cell/vector selection.

For `D(1,1)`, the minimum-entry vertices are `(2,1)` and `(1,2)`. In the auxiliary A2 spatial-tail graph their distances from the origin are 3. The complete minimum tails are

- to `(2,1)`: `XXY`, `XYX`, `YXX`;
- to `(1,2)`: `XYY`, `YXY`, `YYX`.

Thus the cell has six minimum-entry spatial tails and full VOID-to-cell minimum jump count 4 after the unique `VOID_E -> O_E` prefix.

At the radius-2 horizontal overshoot, PRE `(1,1)` has spatial minimum 2 while POST `(2,1)` has spatial minimum 3, although both are proxies for the same target vector radius 2. Hence reverse jump count cannot select the algebraic collapse direction.

## 8. Theorem package

Freeze within the single representative chamber/sector:

`FIRST_SECTOR_FRESH_HIDDEN_CELL_PROVED__R_STAR_3__STRICT_SQUARE_GAP`.

Freeze:

`EXACT_EDGE_INCIDENCE_DOMINATES__PRE_POST_NEAREST_ENDPOINT_COLLAPSE_NOT_CANONICAL__CELL_HIT_IS_SET_VALUED`.

Combined strongest disposition:

`FIRST_SECTOR_FRESH_HIDDEN_CELL_AT_R3__EXACT_CELL_INCIDENCE_SET_VALUED__ENDPOINT_COLLAPSE_DIRECTION_NONCANONICAL`.

No AT4 main chamber gluing, global circle, global perimeter or native area law is claimed.
