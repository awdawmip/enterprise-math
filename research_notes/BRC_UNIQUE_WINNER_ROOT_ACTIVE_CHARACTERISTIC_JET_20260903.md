# BRC Unique-Winner Root-Active Characteristic Jet

Status: `RESEARCH / EXACT FINITE POSITIVE-RATIONAL / REDUCIBLE SIMPLE-PERRON FRONTIER`
Date: `2026-09-03`
Parents: PR #1182 global powered strict gauge; WBRC-T39..T48.

## 1. Scope

This note solves the reducible critical case when the limiting critical multiplicity matrix `K` has a **simple Perron root**. For a block-diagonal critical graph this is equivalent to one critical SCC having strictly larger `rho(K_alpha)` than all other critical SCCs.

The tied-winner/multiple-root case is excluded; PR #1182 already gives the exact two-block Puiseux witness `rho=1+(ab)^(s/2)`.

Simple-root perturbation, Schur complements and finite exponential sums are classical. Enterprise/BRC content is the exact gauge-invariant characteristic-ratio jet and the root-active selection rule over the explicit positive-rational branch carrier.

## 2. Chosen global strict gauge and exact matrix jet

PR #1182 gives a positive rational global powered strict gauge `H` with reference critical data `(r0,Q0)` such that, for every explicit branch,

\[
0<\lambda_e\le1,
\qquad
\lambda_e=1\iff e\text{ is critical dominant}.
\]

For `m=r0*s`, after rational similarity/scalar normalization,

\[
A_s
:=Q_0^{-s}D(H^s)^{-1}W^{(r_0s)}D(H^s)
=K+\sum_{j\ge1}\lambda_j^sM_j.
\]

For reducible critical structure this matrix-ratio representation depends on the chosen class gauge.

## 3. Characteristic jet is gauge invariant

Expand

\[
P_s(z)=\det(I-zA_s).
\]

Because the matrix jet is finite, `P_s` is an exact finite exponential sum

\[
\boxed{
P_s(z)=\sum_{\eta\in\mathcal E}\eta^sG_\eta(z),
}
\]

where `E` is a finite set of positive rational bases and each `G_eta(z)` is an integer polynomial. The base `eta=1` term is

\[
\boxed{G_1(z)=p_K(z)=\det(I-zK).}
\]

Each determinant monomial is a disjoint union of directed cycles; after expanding every selected matrix entry down to explicit branches, its exponential base is the product of the selected powered branch ratios around those closed cycles. Therefore all class/vertex gauge factors telescope.

Hence the complete grouped jet

\[
\boxed{\{(\eta,G_\eta)\}}
\]

is independent of the chosen global strict powered gauge, even though the individual inter-class branch ratios are not.

Equivalently, along `m=r0*s`, every `eta` is exactly one of the normalized characteristic bases already implicit in WBRC-T40.

## 4. Simple root / unique Perron winner

Let `z_*` be the smallest positive root of

\[
p_K(z)=\det(I-zK),
\qquad \rho_*=1/z_*.
\]

Assume

\[
\boxed{p_K'(z_*)\ne0.}
\]

Because every critical SCC block is irreducible, this is equivalent to exactly one critical SCC attaining the largest Perron value among the blocks.

This is an exact algebraic condition. With the WBRC-T41 root selector, simplicity is checked by proving that the selected root is not a root of `gcd(p_K,p_K')`.

## 5. Root-active layers

Sort the strict characteristic bases:

\[
1>\eta_1>\eta_2>\cdots>0.
\]

A layer is **root-active** if

\[
G_{\eta_j}(z_*)\ne0.
\]

This is exactly decidable without numerically evaluating `z_*`:

- if `z_*` is rational, evaluate directly;
- if `z_*` is irrational, compute `gcd(p_K,G_eta)` and use the existing rational Sturm isolating interval to test whether the selected root is shared.

If every strict layer is root-inactive, the selected Perron root remains exactly unchanged for all `s` in the finite jet.

Otherwise let

\[
\boxed{
\eta_*:=\max\{\eta<1:G_\eta(z_*)\ne0\}.
}
\]

Then

\[
P_s(z)
=p_K(z)+\eta_*^sG_{\eta_*}(z)+o(\eta_*^s)
\]

coefficientwise.

## 6. Exact first Perron/log response

Let `z_s` be the smallest positive root of `P_s`. Simple-root perturbation gives

\[
z_s
=z_*
-\frac{G_{\eta_*}(z_*)}{p_K'(z_*)}\eta_*^s
+o(\eta_*^s).
\]

Therefore

\[
\boxed{
\ln\rho(A_s)
=
\ln\rho_*
+\beta_*\eta_*^s
+o(\eta_*^s),
}
\]

with exact algebraic response state

\[
\boxed{
\beta_*
=
\frac{G_{\eta_*}(z_*)}{z_*p_K'(z_*)}>0.
}
\]

The positivity follows from `A_s>=K` entrywise in any strict powered gauge and the unique simple Perron branch: the first nonzero perturbative coefficient of the monotone Perron root cannot be negative.

Combining with the original moment normalization,

\[
\boxed{
\ln\rho(W^{(r_0s)})
=s\ln Q_0
+\ln\rho_*
+\beta_*\eta_*^s
+o(\eta_*^s).
}
\]

## 7. What root activity means geometrically

The characteristic jet automatically filters strict branches that cannot return to the Perron-winning recurrent core.

- A large feed-forward branch with no closed return path contributes no characteristic cycle-system term and is absent from all strict `G_eta`.
- A strict branch inside the winning block can be root-active at first order, reproducing WBRC-T47.
- A route leaving the winning block and returning through losing states contributes a gauge-invariant **closed excursion product**. Its product ratio, not either individual inter-class edge ratio, can become `eta_*`.

Thus `eta_*` is the first spectrally visible closed branch-ratio scale.

## 8. Schur excursion interpretation

Permute states into the unique winning critical block `B` and its complement `L`:

\[
A_s=\begin{pmatrix}A_{BB,s}&X_s\\Y_s&A_{LL,s}\end{pmatrix}.
\]

At `z=z_*`, `I-z_*K_L` is invertible because `rho(K_L)<rho_*`. The exact determinant factorization is

\[
\det(I-zA_s)
=\det(I-zA_{LL,s})
\det\!\left(
I-zA_{BB,s}-z^2X_s(I-zA_{LL,s})^{-1}Y_s
\right).
\]

The second determinant is the winning-block return problem. The term

\[
zX_s(I-zA_{LL,s})^{-1}Y_s
\]

is the closed-excursion correction: leave the winner, traverse the losing subsystem any finite number of times, and return. The root-active characteristic base is exactly the first exponential scale that survives this return condensation.

This is the spectral analogue of the earlier recurrent port/feedback Schur calculus, evaluated at the Perron root rather than at the stable mass point `z=1`.

## 9. Exact two-block regressions

### 9.1 Feed-forward inactive layer

\[
A_s=\begin{pmatrix}2&a^s\\0&1\end{pmatrix}.
\]

The characteristic polynomial is `(1-2z)(1-z)` for every `s`; the strict edge is root-inactive and `rho(A_s)=2` exactly.

### 9.2 Closed excursion active layer

\[
A_s=\begin{pmatrix}2&a^s\\b^s&1\end{pmatrix}.
\]

Then

\[
P_s(z)=(1-2z)(1-z)-z^2(ab)^s.
\]

So

\[
\eta_*=ab,
\qquad
G_{ab}(z)=-z^2,
\qquad
\beta_*=1/2.
\]

Indeed

\[
\rho(A_s)=2+(ab)^s+O((ab)^{2s})
\]

and hence `ln rho=ln2+(1/2)(ab)^s+...`.

### 9.3 Tied winner boundary

\[
A_s=\begin{pmatrix}1&a^s\\b^s&1\end{pmatrix}
\]

has `p_K=(1-z)^2`, so the selected root is not simple. The same determinant strict base `ab` produces root correction `(ab)^(s/2)`, demonstrating exactly why the simple-root hypothesis is necessary.

## 10. Hard boundaries

Freeze:

```text
UNIQUE_PERRON_WINNER <-> SMALLEST_POSITIVE_ROOT_OF_pK_IS_SIMPLE
CHARACTERISTIC_RATIO_JET = CLASS_GAUGE_INVARIANT
ROOT_ACTIVE_BASE = FIRST_SPECTRALLY_VISIBLE_CLOSED_RATIO_SCALE
FEED_FORWARD_STRICT_BRANCH_CAN_BE_ROOT_INACTIVE
UNIQUE_WINNER_CLOSED_EXCURSION -> ORDINARY_EXPONENTIAL_RESPONSE
TIED_WINNER_MULTIPLE_ROOT -> POSSIBLE_PUISEUX_RESPONSE
ROOT_ACTIVE_JET != INDIVIDUAL_REDUCIBLE_BRANCH_RATIO_ORDERING
```

No tied-class Puiseux classification, infinite-state extension, signed/amplitude result or generic novelty claim is made.
