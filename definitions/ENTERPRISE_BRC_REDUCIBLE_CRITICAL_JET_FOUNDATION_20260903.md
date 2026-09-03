# Enterprise Math — Reducible Critical-Jet BRC Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_CRITICAL_RATIO_JET_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_REDUCIBLE_CRITICAL_JET_THEOREM_LEDGER_20260903.json`

## 1. Purpose and prior-art boundary

This addendum freezes the main-backed reducible-critical results of PRs #1182–#1184. Strict max-algebra visualization, Schur complements, simple-root perturbation and Newton/Puiseux polygons are classical/general mathematics. Enterprise Math promotes only their exact specialization to finite explicit positive-rational BRC branch data, rational powered gauges, finite characteristic ratio jets and the existing algebraic root-selector interface.

No floating spectral primitive, complete Puiseux solver, signed/amplitude semantics, infinite-state result or generic novelty claim is made.

## 2. Global strict rational powered gauge — WBRC-T49

Choose reference critical data `(r0,Q0)`. Use WBRC-T45 powered potentials inside every critical SCC, then contract each critical SCC to one equality class; noncritical states remain singleton quotient vertices.

For each strict quotient edge `A->B`, let `w_AB` be the maximum powered normalized rational weight of explicit branches crossing the classes. Every directed quotient cycle has product strictly below one.

Choose an exact rational `c<1` such that every quotient cycle product is `<c^length`; for example

\[
\varepsilon=\min_C\frac{1-w(C)}{2|C|},\qquad c=1-\varepsilon
\]

when quotient cycles exist, and `c=1/2` when the quotient is acyclic. Let `x_A` be the maximum product of the scaled weights `w/c` over simple paths starting at `A`. Then

\[
\boxed{w_{AB}x_B\le c x_A<x_A.}
\]

Multiplying the within-critical powered potential by `x_[v]` gives a global positive rational potential `H_v` for which every explicit branch satisfies

\[
\boxed{\lambda_e=1\iff e\text{ is critical dominant},}
\qquad
\boxed{0<\lambda_e<1\text{ otherwise}.}
\]

For `m=r0*s`, any chosen global strict gauge yields the exact full exponential jet

\[
\boxed{
Q_0^{-s}D(H^s)^{-1}W^{(m)}D(H^s)=\sum_j\lambda_j^sM_j,
\qquad M_0=K.
}
\]

### Reducible gauge boundary

Independent critical-class multipliers remain. Therefore individual inter-class `lambda_e`, and their global ordering, are not canonical. Closed excursion products telescope and are invariant. The gauge-invariant spectral data are the grouped characteristic closed-product layers introduced below.

## 3. Gauge-invariant characteristic ratio jet — WBRC-T50

For any chosen global strict powered gauge, expand

\[
P_s(z)=\det\!\left(I-z\sum_j\lambda_j^sM_j\right).
\]

Because the jet is finite,

\[
\boxed{
P_s(z)=p_K(z)+\sum_{\eta<1}\eta^sG_\eta(z),
}
\]

with a finite set of positive rational bases `eta` and integer polynomials `G_eta`. Every determinant term is a union of closed directed cycles, so every class/vertex gauge factor telescopes. Thus the grouped characteristic jet

\[
\boxed{\{(\eta,G_\eta)\}}
\]

is exactly gauge invariant even when the underlying branch-ratio representative is not.

Let `z_*` be the WBRC-T41 smallest-positive-root selector of `p_K`.

### Simple selected root / unique Perron winner

If

\[
\boxed{p_K'(z_*)\ne0,}
\]

the selected root is simple; equivalently exactly one critical SCC attains the maximal Perron value among the critical blocks.

A strict characteristic layer is **root-active** if

\[
G_\eta(z_*)\ne0.
\]

Root activity is exact: evaluate directly for rational `z_*`; for irrational `z_*`, polynomial gcd together with the existing Sturm isolating interval decides whether the selected root is shared.

If all strict layers are root-inactive, the Perron root is exactly unchanged. Otherwise define

\[
\boxed{
\eta_*:=\max\{\eta<1:G_\eta(z_*)\ne0\}.
}
\]

Then

\[
z_s=z_*-\frac{G_{\eta_*}(z_*)}{p_K'(z_*)}\eta_*^s+o(\eta_*^s),
\]

and

\[
\boxed{
\ln\rho_s
=\ln\rho_*+
\frac{G_{\eta_*}(z_*)}{z_*p_K'(z_*)}\eta_*^s
+o(\eta_*^s).
}
\]

The coefficient is positive for the Perron branch. Large feed-forward ratios can be root-inactive; closed excursions through losing blocks can be root-active. This is the correct reducible simple-root replacement for the irreducible `eta_T40=lambda_1` rule.

## 4. Multiple selected root and first Newton edge — WBRC-T51

Assume now that `z_*` has multiplicity

\[
\boxed{r=\operatorname{ord}_{z_*}p_K\ge2.}
\]

For each strict characteristic layer define its contact order

\[
q_\eta=\operatorname{ord}_{z_*}G_\eta.
\]

Layers with `q_eta>=r` do not enter the first Newton edge. For `q_eta<r`, define the exact candidate scale state

\[
\boxed{
\theta_\eta^{\,r-q_\eta}=\eta.
}
\]

Candidate scales compare without radical evaluation:

\[
\boxed{
\eta_1^{1/d_1}\lesseqgtr\eta_2^{1/d_2}
\iff
\eta_1^{d_2}\lesseqgtr\eta_2^{d_1}.
}
\]

Let `theta_*` be the maximum candidate scale and collect every layer attaining it. With

\[
z=z_*+\theta_*^s y,
\]

write

\[
p_K(z_*+x)=a_r x^r+O(x^{r+1}),
\]

\[
G_\eta(z_*+x)=b_\eta x^{q_\eta}+O(x^{q_\eta+1}).
\]

Then the first scaled limit is the exact **first-edge polynomial**

\[
\boxed{
E(y)=a_r y^r+\sum_{\theta_\eta=\theta_*}b_\eta y^{q_\eta}.
}
\]

All other local characteristic terms are strictly lower scale. If `E` has a simple negative real root `y_*` on the Perron branch,

\[
\boxed{
z_s=z_*+y_*\theta_*^s+o(\theta_*^s),}
\]

\[
\boxed{
\ln\rho_s
=\ln\rho(K)-\frac{y_*}{z_*}\theta_*^s+o(\theta_*^s).
}
\]

If the selected edge root is itself multiple, a later Newton edge is required and is not promoted here.

### Important consequences

- two tied unit classes with closed ratio product `ab`: `r=2,q=0`, first scale `(ab)^(1/2)`;
- three tied classes on one directed cycle: `r=3`, first scale equals the one-edge ratio;
- contact order `q=1` with `r=2` gives ordinary `eta`, not `sqrt(eta)`;
- determinant-base ordering need not equal root-scale ordering: `(eta,q)=(1/3,0)` can dominate `(1/2,1)` because `1/sqrt(3)>1/2`.

## 5. Exact semantic split

Freeze the reducible decision tree:

```text
GLOBAL_STRICT_RATIONAL_POWERED_GAUGE = EXISTS
REDUCIBLE_BRANCH_RATIO_REPRESENTATIVE = NOT_CANONICAL
CLOSED_CHARACTERISTIC_RATIO_JET = CANONICAL_GAUGE_INVARIANT
SIMPLE_SMALLEST_ROOT -> ROOT_ACTIVE_ORDINARY_EXPONENTIAL_RESPONSE
MULTIPLE_SMALLEST_ROOT -> FIRST_NEWTON_EDGE
MULTIPLE_EDGE_ROOT -> LATER_NEWTON_EDGE_REQUIRED
FEED_FORWARD_STRICT_LAYER_CAN_BE_ROOT_INACTIVE
DETERMINANT_BASE_ORDER != ROOT_SCALE_ORDER_IN_GENERAL
```

## 6. Hard boundaries

Canonical negative IDs: `WBRC-N31..N35`.

- individual reducible inter-class branch ratios are not canonical observables;
- the largest strict branch ratio/determinant base need not be the first spectral correction scale;
- ordinary simple-root derivative formulas are invalid at a multiple selected root;
- the first Newton edge is not a complete Newton-Puiseux expansion;
- all statements remain finite-state, positive-rational and unsigned.

## 7. Tool routing

Reusable companion T0 subtool:

`t0.weighted_brc_reducible_critical_jet` -> `src/enterprise_math/brc_reducible_critical_jet.py`.

It is an exact reference implementation for one global strict rational gauge, gauge-invariant characteristic layers, simple-root root activity, multiple-root contact orders and first Newton-scale states. It does not implement a floating eigensolver or a general Puiseux-series engine.
