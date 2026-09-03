# BRC Multiple-Root First Newton Edge

Status: `RESEARCH / EXACT FINITE CHARACTERISTIC JET / MULTIPLE-PERRON FRONTIER`
Date: `2026-09-03`
Parents: PR #1182 reducible obstruction; PR #1183 root-active simple-root characteristic jet; WBRC-T39..T48.

## 1. Scope

This note addresses the first asymptotic scale when the smallest positive root `z_*` of

\[
p_0(z)=p_K(z)=\det(I-zK)
\]

has multiplicity `r>=2`.

It does **not** claim a complete Newton-Puiseux expansion.  It extracts only the first Newton edge from the already finite, exact, gauge-invariant characteristic jet

\[
P_s(z)=p_0(z)+\sum_{\eta<1}\eta^sG_\eta(z).
\]

Newton polygons/Puiseux theory are classical.  Enterprise/BRC content is the exact finite rational-base carrier, root-selector contact orders, root-free candidate-scale comparison, and its interpretation for tied critical multiplicity classes.

## 2. Contact order at the selected critical root

Let `z_*` be the WBRC-T41 exact smallest-positive-root state and let

\[
r=\operatorname{ord}_{z_*}p_0\ge2.
\]

For each strict characteristic layer `eta`, define

\[
q_\eta=\operatorname{ord}_{z_*}G_\eta.
\]

If `q_eta>=r`, that layer does not compete with the leading `r`-fold root at the first Newton edge and is ignored at this stage.

For `q_eta<r`, define the candidate root scale

\[
\boxed{
\theta_\eta=\eta^{1/(r-q_\eta)}.
}
\]

No radical needs to be numerically materialized.  Candidate scales compare exactly:

\[
\eta_1^{1/d_1}>\eta_2^{1/d_2}
\iff
\eta_1^{d_2}>\eta_2^{d_1},
\]

where `d_i=r-q_i`.  Equality is likewise an exact rational power equality.

## 3. First Newton scale

If there exists at least one strict layer with `q_eta<r`, define

\[
\boxed{
\theta_*=\max_\eta\theta_\eta.
}
\]

Let `E_*` be the finite set of layers attaining this same scale.  Choose any representative `(eta_0,d_0)` so that formally

\[
\theta_*^{d_0}=\eta_0.
\]

Set

\[
z=z_*+\theta_*^s y.
\]

Write the first nonzero local coefficients

\[
p_0(z_*+x)=a_r x^r+O(x^{r+1}),
\]

\[
G_\eta(z_*+x)=b_\eta x^{q_\eta}+O(x^{q_\eta+1}).
\]

For every layer on the first edge,

\[
\eta\,\theta_*^{q_\eta}=\theta_*^r.
\]

Every other local characteristic term has a strictly smaller exponential base.  Therefore

\[
\boxed{
\theta_*^{-rs}P_s(z_*+\theta_*^s y)
\longrightarrow
E(y),
}
\]

coefficientwise on bounded `y`, where the **first edge polynomial** is

\[
\boxed{
E(y)=a_ry^r+\sum_{\eta\in\mathcal E_*}b_\eta y^{q_\eta}.
}
\]

The edge polynomial coefficients are exact algebraic evaluations at the already-certified root selector.  When `z_*` is rational they are rational.

## 4. First Puiseux response

Suppose `E(y)` has a simple negative real root `y_*<0` corresponding to the Perron/smallest-positive-root branch.  Ordinary simple-root continuity applied to the scaled equation gives

\[
\boxed{
z_s=z_*+y_*\theta_*^s+o(\theta_*^s).}
\]

Hence

\[
\boxed{
\ln\rho(A_s)
=
\ln\rho(K)
-\frac{y_*}{z_*}\theta_*^s
+o(\theta_*^s),
}
\]

with positive coefficient `-y_*/z_*>0`.

The exact response state is therefore

```text
p_0(z)
selected multiple root z_*
root multiplicity r
finite strict jet {(eta,G_eta)}
contact orders q_eta
first-edge scale state theta_*^d=eta
edge polynomial E(y)
selected simple negative edge root y_*
```

No floating Puiseux solver is required as a proof primitive.

If the selected negative edge root is multiple, or if the edge polynomial itself has unresolved root collision, a later Newton edge is required.  That case is not promoted here.

## 5. Exact special cases

### 5.1 Two tied critical classes

\[
A_s=\begin{pmatrix}1&a^s\\b^s&1\end{pmatrix}.
\]

Here

\[
p_0(z)=(1-z)^2,
\qquad
G_{ab}(z)=-z^2,
\]

so `r=2`, `q=0` and

\[
\theta_*=(ab)^{1/2}.
\]

At `z_*=1`,

\[
E(y)=y^2-1.
\]

The Perron branch selects `y_*=-1`, giving

\[
\rho(A_s)=1+(ab)^{s/2}
\]

exactly.

### 5.2 Three tied classes on one directed cycle

For

\[
A_s=I_3+a^sC_3
\]

with `C_3` the directed three-cycle,

\[
P_s(z)=(1-z)^3-z^3a^{3s}.
\]

Thus `r=3`, `eta=a^3`, `q=0`, `theta_*=a`, and

\[
E(y)=-y^3-1.
\]

The selected negative root is `-1`, hence `rho=1+a^s`.

### 5.3 Contact-order one

\[
A_s=\operatorname{diag}(1+a^s,1).
\]

Then

\[
P_s(z)=(1-z)^2-a^sz(1-z).
\]

The strict polynomial vanishes once at `z_*=1`: `q=1`. Hence

\[
\theta_*=a^{1/(2-1)}=a.
\]

The edge polynomial is `y^2+y`, whose Perron branch root is `-1`; again `rho=1+a^s` exactly.

### 5.4 A smaller determinant base can dominate the root scale

Take

\[
A_s=\begin{pmatrix}
1+(1/2)^s&(1/2)^s\\
(2/3)^s&1
\end{pmatrix}.
\]

The diagonal strict layer has

\[
\eta_1=1/2,
\quad q_1=1,
\quad \theta_1=1/2.
\]

The closed cross excursion has

\[
\eta_2=1/3,
\quad q_2=0,
\quad \theta_2=(1/3)^{1/2}>1/2.
\]

So the **smaller determinant base** `1/3` gives the larger Perron root scale `1/sqrt(3)`.  This proves that sorting strict characteristic bases alone is insufficient when the limiting root is multiple.

## 6. Root-free exact comparison of first scales

A scale state is stored as the pair

\[
(\eta,d),\qquad \theta^d=\eta,
\]

with positive rational `eta` and positive integer `d`.

For `(eta_1,d_1)` and `(eta_2,d_2)`:

\[
\boxed{
\theta_1\lesseqgtr\theta_2
\iff
\eta_1^{d_2}\lesseqgtr\eta_2^{d_1}.
}
\]

Thus the first Newton edge can be selected using only integer powers and exact rational comparisons.  `ROOT`/algebraic materialization is optional readout.

## 7. Boundaries

Freeze:

```text
MULTIPLE_CRITICAL_ROOT -> NEWTON_EDGE_REQUIRED
CONTACT_ORDER_q_eta = ORD_{z_*}(G_eta)
CANDIDATE_ROOT_SCALE^_(r-q_eta) = eta
FIRST_ROOT_SCALE = MAX_CANDIDATE_SCALE
DETERMINANT_BASE_ORDER != ROOT_SCALE_ORDER_IN_GENERAL
FIRST_EDGE_POLYNOMIAL = SURVIVING_LOCAL_TERMS_AT_MAX_SCALE
SIMPLE_NEGATIVE_EDGE_ROOT -> FIRST_PUISEUX_RESPONSE
MULTIPLE_EDGE_ROOT -> LATER_NEWTON_EDGE_REQUIRED
```

No complete Newton-Puiseux series, tied-class all-orders classification, signed/amplitude or infinite-state result is claimed.
