# #1162 — local positive formula and exact range of the persistent roughness memory

Status: RESEARCH_NOTE / FINITE LOCAL ROUGHNESS ENERGY / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-persistent-roughness-local-energy-20260908-b62d
Date: 2026-09-08

## 1. Setting

Continue the exact equal-subdivision roughness law. Let normalized positive cycle gaps satisfy `sum_i g_i=1`. Put

`delta_i=g_i-1/N`,

`e_(i+1)-e_i=delta_i`,

`x_i=e_i-e_bar`.

The exact defect and local variance are

`D=(2/N)sum_i x_i^2`,

`V=(1/N)sum_i(x_(i+1)-x_i)^2`.

The persistent equal-subdivision memory is `H=D-V/3`.

## 2. Local positive formula

Expanding the nearest-neighbor difference gives

`H=(1/N)[2sum x_i^2 -(1/3)sum(x_(i+1)-x_i)^2]`

and therefore

`H=(1/(3N))[4sum x_i^2+2sum x_i x_(i+1)]`.

Equivalently, in manifestly positive local form,

`H=(1/(3N)) sum_i[(x_i+x_(i+1))^2+2x_i^2]`.

Thus H is not a hidden continuum remainder: it is an explicit finite nearest-neighbor quadratic energy of the cumulative gap discrepancy.

The formula immediately proves `H>=0`, with equality only when every x_i=0, hence every normalized gap is `1/N`.

It also gives `H>=D/3`, consistent with the earlier bound `V<=2D`.

## 3. Exact global range on the gap simplex

The map from the normalized gap vector g to the centered cumulative vector x is linear, and the displayed H is a positive quadratic form. Hence H is convex on the closed probability simplex `g_i>=0`, `sum g_i=1`.

Every simplex vertex corresponds to putting all normalized resistance on one edge. By cyclic symmetry all vertices have the same H. Convexity therefore yields

`H(g) <= H(vertex)`.

At a vertex,

`D=(N^2-1)/(6N^2)`,

`V=(N-1)/N^2`,

so

`H_max=(N-1)^2/(6N^2)`.

Therefore

`0 <= H <= (N-1)^2/(6N^2) < 1/6`.

For strictly positive gaps the upper boundary is not attained.

## 4. Range of the rough refinement fixed point

Under repeated equal subdivision the scale-free inverse-trace readout converges along the exact finite refinement orbit to

`C_rough=1/6-H`.

Consequently

`(2N-1)/(6N^2) <= C_rough <= 1/6`

on the closed gap simplex, with strict lower inequality for strictly positive gaps.

Thus the persistent roughness memory can shift the Basel fixed point substantially, but cannot make the scale-free fixed point negative.

## 5. BRC meaning

H is a concrete repair coordinate that is:
- finite;
- positive;
- local in the cumulative-discrepancy state;
- invariant under equal subdivision;
- sufficient to separate the universal uniform coefficient `1/6` from the rough family fixed point `C_rough`.

No microscopic derivative or smooth interpolation is involved.

## 6. Next

1. Compare this local H energy with the project-native permitted roughness/gauge relations.
2. Determine whether analogous finite local quadratic/tensor energies appear in the forest jet for m>=2, noting the exact positive-defect no-go at m=2.
