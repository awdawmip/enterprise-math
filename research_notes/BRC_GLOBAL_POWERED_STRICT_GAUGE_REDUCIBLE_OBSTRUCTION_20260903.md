# BRC Global Powered Strict Gauge and Reducible Critical-Class Obstruction

Status: `RESEARCH / EXACT FINITE POSITIVE-RATIONAL / REDUCIBLE FRONTIER`
Date: `2026-09-03`
Parents: WBRC-T45..T48; PRs #1177–#1180.

## 1. Scope

This note separates two facts that coincide when the critical graph is irreducible but diverge when there are several critical classes:

1. an exact **global rational powered strict gauge** still exists;
2. the resulting individual strict branch ratios are no longer canonical because independent critical-class rescalings remain.

Max-plus subeigenvectors, strict visualization and singular/Puiseux eigenvalue perturbation are classical. Enterprise/BRC content is the exact rational certificate and the typed explanation of which ratio data survive the critical-class gauge quotient.

## 2. Base powered potentials on equality classes

Choose a reference critical cycle `(r0,Q0)` and use WBRC-T45 inside each critical SCC. Normalize one root per critical SCC and obtain rational base potentials `H^0_v` satisfying

\[
a_{uv}^{r_0}H^0_v=Q_0H^0_u
\]

on every critical dominant edge. For states outside the critical graph set `H^0_v=1` initially.

Contract each critical SCC to one equality class; every other state is its own quotient vertex. For an explicit branch `e:u->v`, define its base powered quotient weight

\[
w_e=\frac{q_e^{r_0}H^0_v}{Q_0H^0_u}.
\]

Critical dominant equality edges have `w_e=1` and remain internal to their contracted class. All other branches induce strict quotient edges.

## 3. Every quotient cycle has product < 1

Take any directed quotient cycle and choose the corresponding explicit strict branch on each quotient edge. Inside a contracted critical SCC, join the landing state to the next departure state by a critical path; every such internal path has normalized powered product one.

The quotient-cycle product therefore equals the normalized powered product of a closed walk in the original graph. If the product were `>1`, the walk would contain a simple cycle above the tropical critical mean, impossible. If it were `=1`, every simple-cycle factor in its decomposition would be critical; then every strict quotient edge used would lie on a critical cycle, contradicting that it was outside the critical equality graph.

Hence every quotient directed cycle `C` satisfies

\[
\boxed{w(C)<1.}
\]

This is an exact rational inequality.

## 4. Constructive rational strict potential

Let the finite quotient graph have edge weight

\[
w_{AB}=\max\{w_e:e:A\to B\}
\]

on each supported class edge. Every quotient cycle still has product `<1`.

For each simple quotient cycle `C` of length `r_C`, choose the rational slack

\[
\varepsilon_C=\frac{1-w(C)}{2r_C}>0.
\]

If cycles exist set

\[
\varepsilon=\min_C\varepsilon_C,
\qquad c=1-\varepsilon\in(0,1).
\]

If the quotient is acyclic take `c=1/2`.

By Bernoulli,

\[
c^{r_C}\ge1-r_C\varepsilon>w(C),
\]

so every cycle of the scaled quotient weights `\widetilde w_{AB}=w_{AB}/c` has product `<1`.

For each quotient vertex `A`, define `x_A` to be the maximum product of `\widetilde w` over all simple directed paths starting at `A`, including the empty path of product one. This maximum is finite and rational. Removing any repeated cycle from a walk strictly increases its scaled product, so for every quotient edge

\[
\widetilde w_{AB}x_B\le x_A.
\]

Therefore

\[
\boxed{w_{AB}\frac{x_B}{x_A}\le c<1.}
\]

Define the global powered potential

\[
\boxed{H_v=H^0_v x_{[v]}.}
\]

Then every critical dominant branch still has normalized powered ratio one, while every other explicit branch has strict ratio

\[
\boxed{0<\lambda_e=\frac{q_e^{r_0}H_v}{Q_0H_u}<1.}
\]

Thus a global strict rational powered gauge exists without irreducibility.

## 5. Exact full jet still exists — but is gauge-representative dependent

For any chosen global strict powered potential, group equal branch ratios

\[
1=\lambda_0>\lambda_1>\cdots>0
\]

with integer count matrices `M_j`. Then for `m=r0*s`:

\[
\boxed{
Q_0^{-s}D(H^s)^{-1}W^{(m)}D(H^s)
=\sum_j\lambda_j^sM_j,
\qquad M_0=K.
}
\]

This exact finite exponential jet is valid for reducible critical structure as a **chosen gauge representative**.

However, unlike the irreducible T48 case, independent equality-class multipliers remain. Replacing `H_v` by `c_[v] H_v` transforms

\[
\lambda_e\mapsto\lambda_e\frac{c_{[v]}}{c_{[u]}}.
\]

Hence individual inter-class branch ratios and their global ordering are not canonical.

Closed products telescope and remain invariant. Determinant cycle-system normalized bases are precisely such closed products and therefore remain gauge invariant.

## 6. Tied critical classes force Puiseux behavior

Take two unit critical self-loops and two strict cross edges. After one strict gauge representative:

\[
A_s=\begin{pmatrix}1&a^s\\b^s&1\end{pmatrix},
\qquad 0<a,b<1.
\]

Critical-class gauge sends

\[
a\mapsto at,
\qquad b\mapsto b/t,
\]

while `ab` is invariant.

The characteristic equation is

\[
(\lambda-1)^2-(ab)^s=0,
\]

so exactly

\[
\boxed{\rho(A_s)=1+(ab)^{s/2}.}
\]

Thus:

- the determinant coefficient gap is the closed excursion product `ab`;
- the Perron correction exponent is its square root `sqrt(ab)` because the limiting Perron root has multiplicity two;
- no individual cross-edge ratio is canonical.

This is an exact obstruction to extending WBRC-T47/T48 first-response formulas to tied reducible critical classes.

## 7. Unique Perron-winning block behaves differently

For the scalar two-block model

\[
A_s=\begin{pmatrix}\kappa_1&a^s\\b^s&\kappa_2\end{pmatrix},
\qquad \kappa_1>\kappa_2\ge0,
\]

let `x=(ab)^s`. The Perron root is

\[
\rho_s=\frac{\kappa_1+\kappa_2+\sqrt{(\kappa_1-\kappa_2)^2+4x}}2.
\]

The limiting root `kappa_1` is simple, so

\[
\boxed{
\rho_s
=\kappa_1+\frac{(ab)^s}{\kappa_1-\kappa_2}
+O((ab)^{2s}).
}
\]

The first inter-class correction is the **closed excursion product** `ab`, with no square-root exponent. This motivates the next general theorem: a unique Perron-winning critical SCC with all losing states Schur-condensed into exact return excursions.

## 8. Hard boundaries

Freeze:

```text
GLOBAL_STRICT_POWERED_RATIONAL_GAUGE = EXISTS
CRITICAL_DOMINANT_BRANCH <-> LAMBDA_e = 1
ALL_OTHER_BRANCHES -> 0 < LAMBDA_e < 1
REDUCIBLE_FULL_RATIO_JET = GAUGE_REPRESENTATIVE_NOT_CANONICAL
CLOSED_EXCURSION_RATIO_PRODUCTS = CLASS_GAUGE_INVARIANTS
TIED_CRITICAL_PERRON_CLASSES -> POSSIBLE_PUISEUX_FRACTIONAL_EXPONENTS
T48_ETA_EQUALS_MAX_BRANCH_RATIO = IRREDUCIBLE_ONLY
UNIQUE_PERRON_WINNER -> SCHUR_EXCURSION_FRONTIER
```

No generic Puiseux classification is claimed here. Infinite-state, signed/amplitude and complex systems remain outside scope.
