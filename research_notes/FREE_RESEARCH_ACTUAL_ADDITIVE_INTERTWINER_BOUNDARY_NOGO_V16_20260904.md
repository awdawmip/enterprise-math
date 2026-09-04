# Free Research — Actual Additive Intertwiner and the Small-Action Boundary No-Go

Status: `FREE_RESEARCH_CORRECTION / EXACT SYMMETRIC-ROW INTERTWINER / ESSENTIAL SPECTRUM TOUCHES MINUS ONE / PURE THRESHOLD GAP RETAINED / FIXED-DEPTH UNIFORM CONTRACTION RULED OUT / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Corrects the overstrong phrase `ADDITIVE SECTOR CLOSED` in `FREE_RESEARCH_LOG_THRESHOLD_HANKEL_GAP_V16_20260904.md`.
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Correction in one line

The pure threshold operator

\[
\mathsf S_Nx(a)
=\sum_bp_N(b)\operatorname{sgn}(ab-N)x(b)
\]

has the genuine limiting norm `2/pi`. However, the actual additive component of the symmetric parity fold is not `S_N` alone. It also contains a multiplication operator whose logarithmic boundary value is `-1`.

Consequently:

\[
\boxed{
\text{pure threshold overlap has a strict gap, but the full fixed-depth additive block does not.}
}
\]

---

## 2. Exact symmetric-fold row mean

Let

\[
x_a=f(q_a(N)),
\qquad
\bar x=\sum_ap_N(a)x_a,
\]

and let

\[
G_a:=G_f(q_a(N)),
\qquad
\alpha_a:=\frac{A(q_a(N))}{A(N)},
\qquad
\theta_a:=1-2\alpha_a.
\]

For the symmetric folded pair field

\[
\widetilde F_N(a,b)=
\begin{cases}
f(q_{ab}(N)),&ab\le N,\\
\dfrac{x_a+x_b}{2},&ab>N,
\end{cases}
\]

define its row mean

\[
R_N(a):=\sum_bp_N(b)\widetilde F_N(a,b).
\]

The valid part is determined by the adaptive residual:

\[
\sum_{ab\le N}p_N(b)f(q_{ab}(N))
=\frac{G_a}{A(N)}-\alpha_ax_a.
\tag{2.1}
\]

Let

\[
T_x(a):=\sum_{ab>N}p_N(b)x_b.
\]

The stopped part is

\[
\frac12(1-\alpha_a)x_a+rac12T_x(a).
\]

Since

\[
T_x(a)=\frac{\bar x+(\mathsf S_Nx)(a)}2,
\]

we obtain the exact formula

\[
\boxed{
R_N(a)
=\frac{G_a}{A(N)}
+\frac14\left[
(3\theta_a-1)x_a
+(\mathsf S_Nx)(a)
+\bar x
\right].}
\tag{2.2}
\]

This is the missing arithmetic additive intertwiner.

---

## 3. Centered finite operator

Let `P_N` denote orthogonal projection onto the mean-zero subspace of `L^2(p_N)`. Since `P_N` kills the constant term `bar x`, the centered additive component is

\[
\boxed{
P_NR_N
=P_N\left[
\frac{3M_{\theta_N}-I+\mathsf S_N}{4}
\right]x
+P_N\left(\frac{G_\bullet}{A(N)}\right),}
\tag{3.1}
\]

where `M_theta` is multiplication by the row degree `theta_N(a)`.

Thus the homogeneous additive block is

\[
\boxed{
\mathsf B_N
:=P_N\frac{3M_{\theta_N}-I+\mathsf S_N}{4}P_N.}
\tag{3.2}
\]

The two previously separate mechanisms now appear in one exact operator:

- `S_N`: global valid/stopped overlap, norm tending to `2/pi`;
- `M_theta`: local row transmission, touching `-1` at the small-action boundary.

---

## 4. Continuum limit

In logarithmic action coordinate

\[
s=\frac{\log a}{\log N},
\]

we have

\[
\theta_N(a)=2s-1+o(1).
\]

Hence the limiting centered block is

\[
\boxed{
\mathsf B
=P\left[
M_{m}+\frac14\mathsf S
\right]P,}
\tag{4.1}
\]

where

\[
\boxed{m(s)=\frac32s-1}
\tag{4.2}
\]

and `S` is the log-threshold Hankel operator.

The operator `S/4` is compact and `P-I` is finite rank. Therefore `B` has the same essential spectrum as multiplication by `m`:

\[
\boxed{
\operatorname{Spec}_{\rm ess}(\mathsf B)
=[-1,1/2].}
\tag{4.3}
\]

In particular,

\[
\boxed{-1\in\operatorname{Spec}_{\rm ess}(\mathsf B),
\qquad
\|\mathsf B\|_{\rm ess}=1.}
\tag{4.4}
\]

There is no uniform `L^2` contraction constant below one for the full additive block.

---

## 5. Explicit Weyl sequence

Choose mean-zero unit vectors `x_epsilon` supported in the interval

\[
0\le s\le\epsilon
\]

and oscillating once inside that interval. As `epsilon` tends to zero,

\[
M_mx_\epsilon+x_\epsilon\to0
\]

because `m(s)->-1` uniformly on the support.

The sequence converges weakly to zero, so compactness gives

\[
\mathsf Sx_\epsilon\to0.
\]

Since the vectors are already centered,

\[
\boxed{
\|(\mathsf B+I)x_\epsilon\|_2\to0.}
\tag{5.1}
\]

This is an explicit approximate `-1` boundary mode.

It corresponds arithmetically to energy concentrated on prime-power actions

\[
a\le N^\epsilon,
\]

for which the first quotient remains near the parent scale and almost every second action is still valid.

---

## 6. What remains true from the threshold-Hankel theorem

The following results remain valid and useful:

\[
\operatorname{Spec}(\mathsf S)
=\left\{\pm\frac2{(2k+1)\pi}:k\ge0\right\},
\]

\[
\|\mathsf S\|=2/\pi,
\]

and

\[
\|\mathsf S_N\|
=2/\pi+O((\log N)^{-1/2}).
\]

They rule out a unit-modulus mode created by the **global threshold overlap term itself**. They do not rule out the boundary multiplication mode in (3.2).

Accordingly, the status `ADDITIVE SECTOR CLOSED` must be replaced by

\[
\boxed{
\text{PURE THRESHOLD SUBBLOCK CLOSED / FULL ADDITIVE BOUNDARY MODE OPEN}.}
\]

---

## 7. Fixed-depth no-go

The same mechanism persists at every fixed provenance depth.

Any finite-depth return/mixer block assembled from:

- finitely many action slots;
- multiplication coefficients continuous at the all-small-action corner;
- compact integral overlap operators;
- finite-rank centering projections

has an approximate parity mode supported where all logarithmic action coordinates are at most `epsilon`. On that corner every action remains valid for the fixed number of steps, so the signed history contributes the deterministic factor `(-1)^r` at depth `r`.

Therefore no fixed history depth can furnish a uniform contraction on arbitrary `L^2` energy densities without an additional input.

The additional input must be at least one of:

1. increasing history depth as the scale grows;
2. a coercive weight that penalizes concentration on the all-small-action corner;
3. a quantitative regularity/slow-oscillation theorem for the actual prime-error field;
4. a separate arithmetic decorrelation statement.

This explains structurally why the fixed three-history `S_3` gap, though exact, could not by itself close a quantitative PNT remainder.

---

## 8. Updated next route

The most native continuation is an increasing-depth provenance block. If the active action logarithms are concentrated below `epsilon`, a depth of order `1/epsilon` is needed before their cumulative logarithmic displacement reaches a fixed fraction of the parent scale.

Thus the next operator should be a variable-depth stopped-history transform rather than another fixed-degree mixer. Its acceptance target is a scale-dependent gap whose cumulative loss diverges, not a one-step constant gap.

The alternative is to import a slow-oscillation modulus. Classical elementary remainder proofs follow precisely this second pattern through iterated smoothing.

---

## 9. Boundary

Closed:

1. exact symmetric-fold additive intertwiner;
2. exact decomposition into multiplication, threshold and residual blocks;
3. continuum essential spectrum;
4. explicit small-action Weyl sequence;
5. correction of the overstrong additive-sector claim;
6. fixed-depth uniform-contraction no-go.

Open:

1. variable-depth provenance mixing;
2. a weighted boundary-coercive norm;
3. a native modulus of slow oscillation strong enough to suppress the Weyl sequence;
4. unconditional native quantitative decay.
