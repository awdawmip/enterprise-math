# Free Research — Exact Row ANOVA of the Parity Fold

Status: `FREE_RESEARCH_FRONTIER / EXACT CONDITIONAL MIXTURE / ROW MULTIPLIER EXPOSED / LOWER QUOTIENT VARIANCE AND POSITIVE POTENTIAL SEPARATED / BLOCK RECURRENCE OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLDED_SQUARE_SCALAR_READOUT_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Purpose

The parity-fold scalar theorem reduces the prime error to a folded-square variance. To continue the native proof, that variance must be opened without erasing its stopped-history structure.

The correct decomposition is a rowwise law of total variance. It separates three exact channels:

1. the quotient-cloud variance at the lower state `q_a(N)`;
2. a positive valid/stopped separation potential;
3. a row-mean channel whose multiplier is the signed core/tail mass imbalance at that first action.

No asymptotic input is needed for the identities.

---

## 2. Setup

Let `S_N` be a finite action family with nonnegative weights `u_a`, and put

\[
A=A_N=\sum_{a\in S_N}u_a>0.
\]

For a fixed first action `a`, write

\[
n_a=q_a(N),
\qquad
A_a:=A_{n_a},
\qquad
\alpha_a:=\frac{A_a}{A},
\qquad
\beta_a:=1-\alpha_a.
\]

The oriented folded field is

\[
F_N(a,b)=
\begin{cases}
f(q_b(n_a)),&b\le n_a,\\
f(n_a),&b>n_a.
\end{cases}
\tag{2.1}
\]

Thus, conditioned on `a`, the second action is a mixture of:

- a valid core cloud of mass `alpha_a`;
- a stopped atom of mass `beta_a` at `f(n_a)`.

Assume `A_a>0` and define the core mean and core probability variance

\[
m_a:=\frac1{A_a}
\sum_{b\le n_a}u_bf(q_b(n_a)),
\tag{2.2}
\]

\[
\Gamma_a(f)
:=\frac1{A_a}
\sum_{b\le n_a}u_b
|f(q_b(n_a))-m_a|^2.
\tag{2.3}
\]

The zero-core-mass case is interpreted separately: then the conditional field is constant and all formulas hold after deleting the terms containing `m_a` and `Gamma_a`.

---

## PFR-T01 — Exact residual expression for the core mean

The adaptive residual at `n_a` is

\[
G_f(n_a)
=A_af(n_a)+
\sum_{b\le n_a}u_bf(q_b(n_a)).
\]

Therefore

\[
\boxed{
m_a=-f(n_a)+\frac{G_f(n_a)}{A_a}.}
\tag{3.1}
\]

This is the local sign-reversing mean law.

---

## PFR-T02 — Exact row mean

Let

\[
R_N(a):=\mathbb E_{b\sim p_N}F_N(a,b),
\qquad
p_N(b)=u_b/A.
\]

By the two-component mixture,

\[
R_N(a)=\alpha_am_a+\beta_af(n_a).
\]

Using (3.1),

\[
\boxed{
R_N(a)
=(1-2\alpha_a)f(n_a)
+\frac{G_f(n_a)}A.
}
\tag{4.1}
\]

Thus the exact same-scale multiplier is

\[
\boxed{
\theta_a:=1-rac{2A_{q_a(N)}}{A_N}.}
\tag{4.2}
\]

The multiplier is not inserted by an estimate. It is the signed stopped-tail minus valid-core mass in the second history slot.

---

## PFR-T03 — Exact conditional variance

The variance of a mixture of a probability cloud of mass `alpha`, an atom of mass `beta`, component mean `m`, atom value `x`, and internal variance `Gamma` is

\[
\alpha\Gamma+\alpha\beta|m-x|^2.
\]

Consequently,

\[
\boxed{
\operatorname{Var}_{b\sim p_N}(F_N(a,b))
=
\alpha_a\Gamma_a(f)
+
\alpha_a\beta_a
\left|-2f(n_a)+\frac{G_f(n_a)}{A_a}\right|^2.
}
\tag{5.1}
\]

The first term is a genuine lower-state quotient-cloud variance. The second is the positive valid/stopped separation potential.

For the prime remainder, `G_r=O(1)`. Away from `A_a=0`, the separation potential is therefore asymptotic to

\[
4\alpha_a\beta_a|r(n_a)|^2.
\]

It is strongest in the middle logarithmic bands and vanishes only at the two boundary regimes `alpha_a approximately 0` and `alpha_a approximately 1`.

---

## PFR-T04 — Full folded-square ANOVA

Let

\[
\mathcal F_N(f)
:=\operatorname{Var}_{(a,b)\sim p_N\otimes p_N}(F_N(a,b)).
\]

The law of total variance gives

\[
\boxed{
\begin{aligned}
\mathcal F_N(f)
={}&
\operatorname{Var}_{a\sim p_N}
\left(
\theta_af(n_a)+\frac{G_f(n_a)}A
\right)\\
&+
\mathbb E_{a\sim p_N}
\left[
\alpha_a\Gamma_a(f)
+\alpha_a\beta_a
\left|-2f(n_a)+\frac{G_f(n_a)}{A_a}\right|^2
\right].
\end{aligned}}
\tag{6.1}
\]

Every term is nonnegative. This is the exact block decomposition required after the scalar-readout theorem.

---

## 3. Prime-winding logarithmic geometry

For prime-winding weights,

\[
A_x=\log x+O(1).
\]

Put

\[
s_a:=\frac{\log a}{\log N}.
\]

At macroscopic logarithmic distance from the finite boundary,

\[
\alpha_a
=
\frac{A_{q_a(N)}}{A_N}
=1-s_a+O(1/\log N),
\]

and hence

\[
\boxed{
\theta_a
=2s_a-1+O(1/\log N).
}
\tag{7.1}
\]

The row channel is therefore the first logarithmic Haar mode:

- small actions, `s_a approximately 0`, carry the approximate `-1` return mode;
- middle actions have strict multiplier below one;
- actions near the outer boundary, `s_a approximately 1`, have positive multiplier but send `N` to a small quotient scale.

This identifies the exact location of the remaining slow mode.

---

## PFR-T05 — Bulk/boundary dichotomy

Fix `0<delta<1/2` and define the bulk

\[
B_\delta
:=\{a:\delta\le\alpha_a\le1-\delta\}.
\]

On this set,

\[
\boxed{|	heta_a|\le1-2\delta.}
\tag{8.1}
\]

The complement consists of two typed boundary channels:

1. `alpha_a<delta`: the quotient state `q_a(N)` has very small logarithmic mass and is already at a strict lower scale;
2. `alpha_a>1-delta`: `a` belongs to the first logarithmic action band, whose normalized prime-winding mass is `delta+O(1/log N)`.

For bounded `f`, the second channel has small total `L^2` mass after `delta` is chosen small. The first is recursively lower-scale. Thus the row multiplier supplies a genuine bulk contraction plus two controlled boundary mechanisms.

The positive separation term in (6.1) simultaneously prevents a mode from freely concentrating in the middle band while saturating the row bound.

---

## 4. Relation to the V14 multichannel state

The three terms in (6.1) match existing carriers:

- `Var(theta_a f(n_a)+G/A)` is a coefficient-weighted first-label relation field;
- `alpha_a Gamma_a` is the lower quotient-cloud relation energy transported to `n_a`;
- `alpha_a beta_a |m_a-f(n_a)|^2` is the one-body tail potential already present in the coefficient-lift identity.

Therefore the parity fold introduces no new unidentified forcing. It packages the V14 relation, transport and potential channels into one exact conditional ANOVA.

---

## 5. Updated remaining theorem

A complete native rate now reduces to a coefficient-safe estimate for (6.1):

\[
\boxed{
\mathcal F_N(r)
\le
q\,\sup_{m<N}\mathcal F_m(r)
+O((\log N)^{-1-\epsilon})
}
\]

for some effective cumulative contraction, or to the corresponding two-channel profile recurrence.

The exact decomposition rules out two invalid shortcuts:

1. dropping the positive valid/stopped separation potential;
2. treating the row multiplier as a uniform constant independent of logarithmic action scale.

The next proof must combine the bulk multiplier, small first-band mass, strict lower-scale landing and coefficient-potential coercivity. No scalar-readout ambiguity remains.
