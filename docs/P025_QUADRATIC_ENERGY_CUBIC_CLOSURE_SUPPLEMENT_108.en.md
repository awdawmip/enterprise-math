# P025 Supplement 108 — Cubic History Closure for Quadratic Rank Energy

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonlinear-observable-stage107`  
Depends on: P025 Supplements 102, 107  
Hard block: `NONE`

## 1. The Stage102 closure order is not universal

Stage102 proves that the **linear activation-area observable** closes at second action-interaction order.

Stage108 keeps the same threshold/node operation algebra and the same incidence geometry, but replaces area by

\[
E=\sum_j r_j^2.
\]

The response order increases.

## 2. Finite extension envelope

Let current thresholds be `T_k`, current node values be `rho_c`, candidate thresholds be `U_i`, and prospective future nodes be `v_j`.

Write current column ranks

\[
r_c:=\#\{k:\rho_c\ge T_k\}.
\]

For candidate threshold `U_i`, define old-column incidence

\[
a_{ic}:=\mathbf1_{\{\rho_c\ge U_i\}}.
\]

For future node `v_j`, define

\[
R_j:=\#\{k:v_j\ge T_k\},
\qquad
C_{ij}:=\mathbf1_{\{v_j\ge U_i\}}.
\]

Let `x_i,y_j` be independent Boolean selection variables for candidate rows and future columns.

## 3. P025-T246 — exact degree-three response polynomial

The exact quadratic-energy response is

\[
E(x,y)
=
\sum_c\left(r_c+\sum_i x_i a_{ic}\right)^2
+
\sum_j y_j\left(R_j+\sum_i x_iC_{ij}\right)^2.
\]

Using `x_i^2=x_i`, this expands to

\[
\boxed{
\begin{aligned}
E(x,y)=E_0
&+\sum_i D_i x_i
+\sum_{i<k}P_{ik}x_ix_k\\
&+\sum_j N_jy_j
+\sum_{i,j}M_{ij}x_iy_j\\
&+\sum_{i<k,j}K_{ikj}x_ix_ky_j,
\end{aligned}}
\]

with

\[
D_i=2\sum_c r_ca_{ic}+\sum_ca_{ic},
\]

\[
P_{ik}=2\sum_c a_{ic}a_{kc},
\]

\[
N_j=R_j^2,
\]

\[
M_{ij}=C_{ij}(2R_j+1),
\]

and

\[
\boxed{K_{ikj}=2C_{ij}C_{kj}.}
\]

Therefore the response polynomial has degree at most three.

## 4. P025-CE43 — exact arithmetic nonzero cubic interaction

Use the exact dyadic pressure orbit `(q,p,m)=(3,41,2)` through one doubling:

\[
\rho_0=\frac1{22},
\qquad
\rho_1=\frac{13}{22}.
\]

Take no old thresholds and two candidate thresholds

\[
U_1=\frac1{10},
\qquad
U_2=\frac12.
\]

The old node lies below both candidates, while the future node lies above both.

Hence

\[
R_1=0,
\qquad
C_{11}=C_{21}=1.
\]

The energy response on the three action variables is exactly

\[
\boxed{
E(x_1,x_2,y)
=y(x_1+x_2)^2
=x_1y+x_2y+2x_1x_2y.
}
\]

Therefore the irreducible third Boolean difference is

\[
\boxed{
\Delta_{x_1}\Delta_{x_2}\Delta_yE=2\ne0.
}
\]

A genuine third-order action interaction is present.

## 5. P025-T247 — exact closure order is three

P025-CE43 proves that second order is insufficient in general for this observable.

P025-T246 proves that degree never exceeds three.

Therefore

\[
\boxed{
\text{quadratic rank energy has exact worst-case history interaction order }3.
}
\]

All irreducible Boolean finite differences of order four or higher vanish identically.

## 6. Why the cubic term appears

A future node contributes the square of its **final** threshold rank.

If two candidate thresholds are both selected and both crossed by that future node, their contributions multiply inside

\[
(R_j+x_i+x_k)^2.
\]

The pairwise threshold interaction is therefore gated by the future-column selection variable `y_j`, producing a cubic `x_ix_ky_j` term.

This mechanism is absent for linear area because each active cell contributes independently.

## 7. Observable degree controls response order here

For this incidence model:

- linear rank observable `r` gives at most second-order row/column interaction after future-column gating;
- quadratic rank observable `r^2` gives at most third-order interaction.

Stage108 does not yet claim a theorem for arbitrary polynomial degree, but it identifies a concrete pattern worth testing:

\[
\boxed{
\text{rank polynomial degree }d
\quad\leadsto\quad
\text{history interaction order at most }d+1.
}
\]

## 8. Architectural consequence

The required response-jet order is not determined by the operation family alone.

The same operations `{threshold insertion, node append}` yield:

- order `2` for activation area;
- order `3` for quadratic rank energy.

Thus an architecture should treat

\[
\boxed{
\text{observable algebra}
}
\]

as an independent determinant of minimum future precision.

## 9. Prior-art / novelty boundary

Boolean polynomial expansion, finite differences and quadratic cross terms are classical mathematics. P025 claims none individually.

The project-side result is the exact arithmetic pressure-test demonstration that changing only the observable changes the required history-closure order while leaving the operation algebra fixed. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_quadratic_history_closure.py`;
- `tests/test_abc_quadratic_history_closure.py`.

## 11. Next frontier

Stage109 should distinguish response order from generator-state complexity again: although the energy response is cubic, the threshold incidences remain nested on one total order. The question is whether a compact generator can produce the full cubic jet without storing all cubic coefficients explicitly.