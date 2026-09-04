# Free Research — Orthogonal Scattering in the Parity Fold

Status: `FREE_RESEARCH_FRONTIER / EXACT UNITARY TWO-CHANNEL SPLIT / CRUDE CONTRACTION NO-GO / S3-DAMPED BULK PROFILE / CORRELATED BOUNDARY MODE OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLD_ROW_ANOVA_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Exact two-channel coefficient identity

For one first action `a`, put

\[
\alpha_a:=\frac{A_{q_a(N)}}{A_N},
\qquad
\beta_a:=1-\alpha_a,
\qquad
\theta_a:=\beta_a-\alpha_a=1-2\alpha_a.
\]

The exact row ANOVA contains:

1. a transmitted row-mean amplitude with coefficient `theta_a`;
2. a valid/stopped separation amplitude with coefficient `2 sqrt(alpha_a beta_a)`.

These coefficients satisfy

\[
\boxed{
\theta_a^2+4\alpha_a\beta_a=1.
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
\begin{pmatrix}
\theta_a\\
2\sqrt{\alpha_a\beta_a}
\end{pmatrix}
\in S^1.
}
\tag{1.2}
\]

Thus the stopped-history split is an exact orthogonal scattering of one scalar amplitude into a transmitted mean channel and a separation/standard channel.

---

## 2. Structural no-go for crude estimates

Ignore the bounded residual correction for the moment and let `x_a=f(q_a(N))`. If one bounds the row-mean term and the separation potential independently by the same pointwise square `x_a^2`, their coefficient is exactly

\[
\theta_a^2+4\alpha_a\beta_a=1.
\]

Therefore any argument that:

- takes absolute values before the channel split;
- bounds both channels by one undifferentiated energy envelope; and
- does not apply additional damping to the separation channel

can produce at best a critical coefficient `1`.

This is not a failure of constants. It is an exact conservation law.

---

## 3. Effect of the `S_3` standard-sector damping

The separation channel is a standard-history component. The existing weighted `S_3` mixer reduces its amplitude by `1/3` and its energy by `1/9`.

After this damping, the pointwise energy-survival profile becomes

\[
\boxed{
q(\alpha)
:=(1-2\alpha)^2+
\frac19\,4\alpha(1-\alpha)
=1-\frac{32}{9}\alpha(1-\alpha).
}
\tag{3.1}
\]

Hence

\[
q(\alpha)<1
\qquad(0<\alpha<1),
\]

with equality only at the two boundary regimes `alpha=0,1`.

At the balanced point `alpha=1/2`,

\[
q(1/2)=1/9.
\]

Thus the central logarithmic shell is maximally damped, while the only slow modes are forced to the cutoff boundaries.

---

## 4. Logarithmic prime-winding profile

For prime-winding weights,

\[
\alpha_a
=1-\frac{\log a}{\log N}
+O(1/\log N)
\]

away from the finite initial range. In the ideal logarithmic coordinate

\[
s=\frac{\log a}{\log N}\in[0,1],
\]

formula (3.1) becomes

\[
\boxed{
q(s)
=(2s-1)^2+rac49s(1-s)
=1-\frac{32}{9}s(1-s).
}
\tag{4.1}
\]

The unweighted logarithmic average is

\[
\int_0^1q(s)\,ds
=1-\frac{32}{9}\int_0^1s(1-s)\,ds
=\boxed{\frac{11}{27}}.
\tag{4.2}
\]

This number is a useful isotropic benchmark, not yet a uniform contraction theorem.

---

## 5. Why `11/27` cannot be promoted directly

For an arbitrary energy density `|x_a|^2`, the weighted survival is

\[
\frac{\sum_au_aq(\alpha_a)|x_a|^2}
     {\sum_au_a|x_a|^2}.
\]

The energy may correlate with the boundary zones where `q(alpha)` is close to one. Therefore the average coefficient `11/27` cannot replace the pointwise supremum `1` without an additional theorem.

A valid closure must use at least one of:

1. the tail-potential coercivity already present in the V14 adaptive return equation;
2. a bulk/boundary localization proving that near-unit modes lie at strict lower scale or in asymptotically small first-action mass;
3. a profile-state recurrence that retains the factor `alpha(1-alpha)` instead of flattening it;
4. an arithmetic decorrelation estimate between the relation energy and the cutoff boundary.

This is the exact correlated-boundary obstruction.

---

## 6. Bulk quantitative form

For `0<delta<1/2` and

\[
\delta\le\alpha\le1-\delta,
\]

we have

\[
\alpha(1-\alpha)\ge\delta(1-\delta),
\]

hence

\[
\boxed{
q(\alpha)
\le
1-\frac{32}{9}\delta(1-\delta).
}
\tag{6.1}
\]

This is a strict uniform bulk gap.

The two exceptional zones have different semantics:

- `alpha<delta`: the quotient state has small logarithmic capacity and is already a lower-scale state;
- `alpha>1-delta`: the first action lies in the initial logarithmic band of relative mass `delta+O(1/log N)`.

The first is recursive forcing; the second is a small-mass but potentially high-amplitude channel. Their separation is mandatory.

---

## 7. Exact relationship with the V14 potential identity

The separation energy is

\[
\alpha_a\beta_a
\left|-2x_a+\frac{G_f(q_a)}{A_{q_a}}\right|^2.
\]

When the residual is bounded, its leading term is

\[
4\alpha_a\beta_a|x_a|^2.
\]

This is precisely the energy complement of the transmitted coefficient `theta_a^2`. It is also the positive coefficient-potential channel that the rectangular tail-return bridge places on the coercive side of the adaptive relation equation.

Therefore the `S_3` damping and the coefficient-potential absorption are not competing explanations. They act on the same conserved separation channel:

\[
\boxed{
\text{row transmission loss}
=
\text{valid/stopped potential gain}
\xrightarrow{\ S_3\ }
\text{strict standard-sector dissipation}.
}
\tag{7.1}
\]

---

## 8. Updated next theorem

The remaining block theorem should preserve the weighted profile `alpha(1-alpha)` and prove

\[
\boxed{
E_N'
\le
\sum_a p_N(a)q(\alpha_a)E_a
+E_{\rm lower}
+O((\log N)^{-2}),
}
\]

with the near-boundary energy either absorbed by the V14 potential defect or transferred to a strict lower-scale envelope.

A proof that replaces `q(alpha)` by its unweighted average is invalid. A proof that replaces it by its supremum loses all contraction. The correct object is the profile-valued block operator itself.
