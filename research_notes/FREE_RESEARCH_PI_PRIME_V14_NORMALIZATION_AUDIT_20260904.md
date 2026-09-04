# Free Research — V14 Mass/Variance Normalization Audit

Status: `FREE_RESEARCH_FRONTIER / MASS_FACTOR_AUDIT_CLOSED / ENDPOINT_VARIANCE_NORMALIZATION_CLOSED / NAIVE_PROFILE_TO_CANONICAL_ITERATION_NO_GO / PROFILE_STATE_INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_CLIPPED_BETA_DENSITY_BRIDGE_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Purpose

The V13/V14 chain uses three related quadratic quantities:

1. raw weighted pair energy;
2. mass-weighted variance;
3. probability-normalized variance.

Because the deepest chamber already has relative mass `1/9`, an incorrect conversion between these quantities could count the chamber mass twice.  This note fixes the convention and audits every factor.

---

## 2. The three normalizations

Let `mu` be a finite positive measure with mass

\[
M_\mu:=\sum_x\mu(x)>0.
\]

Define the raw pair energy

\[
P_\mu(f)
:=\sum_{x,y}\mu(x)\mu(y)|f(x)-f(y)|^2.
\tag{2.1}
\]

Define the mass-weighted variance

\[
\mathscr V_\mu(f)
:=\inf_c\sum_x\mu(x)|f(x)-c|^2.
\tag{2.2}
\]

Define the probability variance

\[
\operatorname{Var}_{\widehat\mu}(f)
:=\frac1{M_\mu}\mathscr V_\mu(f),
\qquad
\widehat\mu:=\mu/M_\mu.
\tag{2.3}
\]

The exact relations are

\[
\boxed{
P_\mu(f)=2M_\mu\mathscr V_\mu(f)
=2M_\mu^2\operatorname{Var}_{\widehat\mu}(f).
}
\tag{2.4}
\]

Thus the Lean quantity

\[
\frac{P_\mu}{2M_\mu}
\]

is the mass-weighted variance, not the probability variance.

---

## 3. Full-packet contribution

Let `T_Y` be the full ordered degree-three packet mass.  For one color/endpoint fiber `F_(j,m)` with mass `W_(j,m)`, let `P_(j,m)` be its raw history-mean pair energy, including the factor `3` from the trivial `S_3` line.

The correct normalized contribution of this fiber to the full packet is

\[
\boxed{
\frac1{T_Y}\frac{P_{j,m}}{2W_{j,m}}
=
\frac{W_{j,m}}{T_Y}
\operatorname{Var}_{\widehat\mu_{j,m}}(\text{history mean}).
}
\tag{3.1}
\]

Summing fibers gives

\[
\boxed{
\mathcal E_{\rm mean}^{\rm deep}
=
\frac1{T_Y}
\sum_{j,m}\mathscr V_{\mu_{j,m}}(\text{history mean}).
}
\tag{3.2}
\]

The chamber mass is present exactly once, through `W_(j,m)/T_Y`.  Multiplying (3.2) by an additional deepest mass ratio would be double-counting.

---

## 4. Endpoint disintegration at the audited normalization

For one fixed color and one branch coordinate, let `mu_m` be its endpoint-fiber pushforward and let

\[
\mu=\sum_m\mu_m.
\]

The exact law of total variance is

\[
\boxed{
\mathscr V_\mu(f)
=
\sum_m\mathscr V_{\mu_m}(f)
+
\sum_mM_m|\bar f_m-\bar f|^2.
}
\tag{4.1}
\]

Therefore

\[
\boxed{
\frac1{T_Y}\sum_m\mathscr V_{\mu_m}(f)
\le
\frac1{T_Y}\mathscr V_\mu(f).
}
\tag{4.2}
\]

No endpoint mass factor is lost or added in this aggregation.

---

## 5. Exact V14 profile formula

Let the aggregate actual high and low branch measures be `mu_H`, `mu_L1`, `mu_L2`.  Let `nu_H`, `nu_L` be any positive profile envelopes with masses `B_H`, `B_L`, and suppose

\[
\mu_i\le\lambda_Y\nu_i.
\]

Positive measure monotonicity and homogeneity give

\[
\mathscr V_{\mu_i}(f)
\le\lambda_Y\mathscr V_{\nu_i}(f)
=\lambda_YB_i
\operatorname{Var}_{\widehat\nu_i}(f).
\tag{5.1}
\]

The exact V13 high/low inequality, after endpoint aggregation, therefore gives

\[
\boxed{
\mathcal E_{\rm mean}^{\rm deep}
\le
\frac{\lambda_Y}{T_Y}
\sum_{j=1}^{3}
\left[
\frac12B_H E_{H,j}
+2B_L(E_{L_1,j}+E_{L_2,j})
\right],
}
\tag{5.2}
\]

where each `E` is a probability-normalized profile variance.

If all six profile variances lie below one envelope `E_prof`, then

\[
\boxed{
\mathcal E_{\rm mean}^{\rm deep}
\le
\frac{3\lambda_Y}{T_Y}
\left(\frac12B_H+4B_L\right)E_{\rm prof}.
}
\tag{5.3}
\]

For the V14 clipped profile,

\[
B_H,B_L
=\left(\frac16+\frac1{3K^{3/2}}\right)L^3+O(CL^2),
\]

\[
T_Y=\frac92L^3+O(CL^2),
\]

and `lambda_Y=1+O_K(C/L)`.  Hence (5.3) has limiting coefficient

\[
\boxed{
q_K
=3\left(\frac16+\frac1{3K^{3/2}}\right)
=\frac12+K^{-3/2}.
}
\tag{5.4}
\]

This calculation uses the chamber mass exactly once.

---

## 6. Naive per-level conversion back to the canonical measure fails

Let the limiting clipped profile on normalized logarithmic coordinate `s` be

\[
\phi_K(s)
:=\max\left\{\frac{(1-s)^2}{2},\frac1{2K}\right\}.
\]

Its total mass is

\[
I_K=\frac16+\frac1{3K^{3/2}}.
\]

The normalized profile density relative to the uniform canonical logarithmic probability has maximum

\[
\boxed{
C_K^{\uparrow}
=\frac{1/2}{I_K}.
}
\tag{6.1}
\]

If one closes the V14 step by immediately applying the worst-case comparison

\[
\operatorname{Var}_{\widehat\nu_K}(f)
\le C_K^{\uparrow}
\operatorname{Var}_{\rm canonical}(f)
\]

at every scale, the limiting coefficient becomes

\[
\boxed{
q_KC_K^{\uparrow}
=(3I_K)\frac{1/2}{I_K}
=\frac32.
}
\tag{6.2}
\]

This is independent of `K` and is strictly larger than one.

The cruder two-sided condition-number estimate gives the same obstruction in weaker form:

\[
Kq_K
=\frac K2+K^{-1/2}
\ge\frac32.
\tag{6.3}
\]

Therefore:

\[
\boxed{
\text{PROFILE DOMINATION}
+\text{PER-LEVEL WORST-CASE CANONICAL CONVERSION}
\quad\text{IS NOT A CONTRACTIVE PROOF.}
}
\]

This is a structural normalization no-go, not a bad choice of clipping parameter.

---

## 7. Correct remaining intertwiner problem

The V14 marginal-density estimate is closed, but a complete native cascade must avoid paying (6.1) at every level.  There are two valid routes.

### Route A — Propagate the profile state

Construct a shell-resolved return/intertwining law in which the same Beta or clipped-Beta profile is the recursive energy state.  The high and low branches already have the same profile after multiplicative shell translation, so only the arithmetic value transport remains to be proved.

### Route B — Route the profile boundary to lower scale

Use the fact that the profile is small only near the action-shell boundary.  Those labels send the intermediate quotient vertex into a strict lower logarithmic band.  A bulk/boundary decomposition can therefore replace the failed canonical comparison by:

\[
\text{bulk profile energy}
+\text{strictly lower-scale boundary forcing}.
\]

Either route preserves the strict `1/2` mean mass budget.  Direct per-level norm equivalence does not.

---

## 8. Scale-resolved coefficient split

Before any clipping or discrepancy error, the pure Beta mass `L^3/6` splits the full history-mean coefficient into:

\[
\boxed{
q_H
=
\frac{3(1/2)(1/6)}{9/2}
=rac1{18},
}
\tag{8.1}
\]

for the unique high branch, and

\[
\boxed{
q_L
=
\frac{3(2+2)(1/6)}{9/2}
=rac49,
}
\tag{8.2}
\]

for the two low branches.  Thus

\[
q_H+q_L=\frac12.
\]

The high values lie in the top logarithmic third `[2L,3L]`; the low values lie in the middle third `[L,2L]`; the final endpoint lies in the bottom third `[0,L]`.

This exact three-band geometry is the preferred state space for the next intertwiner.  It retains the strict total coefficient `1/2` without converting the Beta profile to uniform at the same scale.

---

## 9. Updated boundary

Closed:

1. all pair/mass/probability variance conversion factors;
2. proof that deepest mass is counted exactly once;
3. endpoint aggregation at the correct normalization;
4. exact profile-envelope coefficient formula;
5. the universal `3/2` no-go for naive per-level canonical conversion;
6. the scale-resolved coefficient split `(1/18,4/9)`.

Open:

1. a profile-state arithmetic value intertwiner; or
2. a bulk/boundary theorem routing the vanishing-profile boundary into a strict lower scale;
3. composition with the exact relation-return residual identity;
4. final identification with the complete odd-simplex energy.

The remaining obstruction is no longer density estimation or normalization.  It is a precisely typed state-propagation problem.
