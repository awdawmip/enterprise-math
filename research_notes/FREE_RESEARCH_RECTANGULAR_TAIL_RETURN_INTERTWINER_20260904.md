# Free Research — Rectangular Tail Return Intertwiner

Status: `FREE_RESEARCH_FRONTIER / RECTANGULAR_RETURN_LIFT_CLOSED / HIGH_LOW_DENSITY_ABSORPTION_CLOSED / ADAPTIVE_RESIDUAL_GATE_ISOLATED / NATIVE_QUANTITATIVE_PRIME_REMAINDER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_SUFFIX_PAIR_TAIL_POTENTIAL_BRIDGE_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the existing relation-field return lift, tail-augmented relation state, and weighted coefficient-coercivity identity. No new general-purpose tool family is claimed.

## 1. Executive result

The V13 pushforward-density bridge is now reduced to an exact finite return-law calculation.

The deepest high marginal contains two overcut suffix labels. Its two-body mass is bounded by the square of one moving tail capacity. The deepest low marginal contains one uncut and one overcut suffix label. Its cross mass is bounded by the ordinary cutoff mass times one moving tail capacity. These capacities are exactly the coefficients appearing when a fixed-cutoff return residual is embedded into an adaptive complete residual.

The coefficient lift therefore has two simultaneous meanings:

\[
\boxed{
\text{positive potential absorbing induced history density}
=
\text{diagonal part of an exact adaptive return equation}.
}
\]

After this substitution, no same-scale Beta or canonical density norm remains. The deepest history-mean energy is forced only by:

1. adaptive complete scalar residual relation fields;
2. moving-cutoff tail endpoint channels;
3. the already known common-suffix relation transport.

The remaining native arithmetic gate is consequently precise: control the relation energy of the adaptive complete residual

\[
\rho_X(r;n),
\qquad r(n)=\psi(n)/n-1,
\]

without importing the PNT backward. This is the local coefficient-two Selberg residual gate.

---

## 2. Rectangular relation-field setup

Let `I` be a finite first-label family with nonnegative weights `w_i` and mass

\[
W:=\sum_{i\in I}w_i.
\]

Let `C` be an independent finite suffix family with nonnegative weights `v_c` and mass

\[
A:=\sum_{c\in C}v_c.
\]

For a scalar field `f`, a state `n`, and first-label quotients

\[
x_i:=f(q_i(n)),
\]

define the suffix-transported values

\[
x_i^{(c)}:=f(q_c(q_i(n))).
\]

Quotient commutation gives

\[
q_c(q_i(n))=q_i(q_c(n)).
\]

For any value vector `z=(z_i)`, define the weighted first-label relation coordinate

\[
Z_{ij}^{z}:=w_iw_j(z_i-z_j).
\tag{2.1}
\]

Define

\[
T_i:=\sum_{c\in C}v_cx_i^{(c)}
\tag{2.2}
\]

and the suffix-family residual evaluated at the first quotient vertex

\[
R_i^{C}:=\rho_C(f;q_i(n))=Ax_i+T_i.
\tag{2.3}
\]

---

## RTR-T01 — Exact rectangular return lift

For every pair `i,j`,

\[
\boxed{
A Z_{ij}^{x}
+
\sum_{c\in C}v_c Z_{ij}^{x^{(c)}}
=
Z_{ij}^{R^C}.
}
\tag{3.1}
\]

Equivalently, at the value-vector level modulo constants,

\[
\boxed{Ax+T=R^C.}
\tag{3.2}
\]

The original return lift used the same action family for first labels and suffixes. Equation (3.1) shows that this equality of families is unnecessary. The first cloud and suffix cloud may have different supports and different total masses.

This rectangular form is exactly what the deepest high/low split requires.

---

## RTR-T02 — General centered coefficient-lift identity

Let `V_i>=0` be any coefficient field on `I`. Assume the standard gauge

\[
\sum_iw_ix_i=0.
\tag{4.1}
\]

Define

\[
y_i:=(A+V_i)x_i,
\qquad
z_i:=V_ix_i.
\]

For the complete first-label pair energy

\[
\mathcal E_w(x)
:=\sum_{i,j}w_iw_j(x_i-x_j)^2,
\]

a moment expansion gives

\[
\boxed{
\mathcal E_w((A+V)x)
=
A^2\mathcal E_w(x)
+4AW\sum_iw_iV_ix_i^2
+\mathcal E_w(Vx).
}
\tag{4.2}
\]

Define the positive coefficient defect

\[
\boxed{
\mathfrak D_{A,V}(x)
:=
\mathcal E_w((A+V)x)
-A^2\mathcal E_w(x)
-\mathcal E_w(Vx).
}
\tag{4.3}
\]

Then

\[
\boxed{
\mathfrak D_{A,V}(x)
=4AW\sum_iw_iV_ix_i^2
\ge0.
}
\tag{4.4}
\]

The earlier weighted coefficient theorem is the special case `A=W`. The rectangular low branch needs the genuinely more general case `A!=W`.

For an arbitrary value channel, replace `x` by its `w`-centered representative. Relation energy is translation invariant. The resulting mean-times-coefficient relation channel is part of the already retained tail-augmented state; it is not discarded.

---

## 5. Adaptive completion identity

Suppose each first label `i` has an adaptive larger suffix family obtained by adjoining a tail of mass `V_i`. Let

\[
E_i:=\sum_{c\in C_i^{\rm tail}}v_cf(q_c(q_i(n)))
\tag{5.1}
\]

be its tail endpoint channel, and let

\[
R_i:=\rho_{C\cup C_i^{\rm tail}}(f;q_i(n))
\tag{5.2}
\]

be the adaptive complete residual. By definition,

\[
R_i=(A+V_i)x_i+T_i+E_i.
\]

Hence

\[
\boxed{
(A+V)x+T=R-E.
}
\tag{5.3}
\]

Taking first-label relation fields gives the exact adaptive return equation

\[
\boxed{
Z^{(A+V)x}+Z^T=Z^R-Z^E.
}
\tag{5.4}
\]

No asymptotic approximation occurs in (5.3)--(5.4).

---

## RTR-T03 — High-branch adaptive return

Put

\[
u_q:=\Lambda(q)/q,
\qquad
A(X):=\sum_{q\le X}u_q,
\]

and define

\[
U_0:=A(Y),
\qquad
U_1:=A(Y^2)-A(Y).
\]

For the unique high first label `a<=Y`, let

\[
h_a:=q_a(Y^3)=\left\lfloor\frac{Y^3}{a}\right\rfloor
\]

and

\[
X_a:=\left\lfloor\frac{h_a}{Y}\right\rfloor
=\left\lfloor\frac{Y^2}{a}\right\rfloor.
\tag{6.1}
\]

Use first labels `a<=Y` and fixed suffixes `c<=Y`. Both have total mass `U_0`. Define

\[
V_H(a):=A(X_a)-A(Y),
\tag{6.2}
\]

\[
T_H(a):=\sum_{c\le Y}u_cf(q_c(h_a)),
\tag{6.3}
\]

\[
E_H(a):=\sum_{Y<c\le X_a}u_cf(q_c(h_a)),
\tag{6.4}
\]

and

\[
R_H(a):=\rho_{X_a}(f;h_a).
\tag{6.5}
\]

Then

\[
\boxed{
(U_0+V_H(a))f(h_a)+T_H(a)
=R_H(a)-E_H(a).
}
\tag{6.6}
\]

Therefore

\[
\boxed{
Z^{(U_0+V_H)x_H}+Z^{T_H}
=Z^{R_H}-Z^{E_H}.
}
\tag{6.7}
\]

The exact high suffix-pair mass

\[
Q_H(a)
:=\sum_{\substack{b,c>Y\\bc\le Y^3/a}}u_bu_c
\]

satisfies

\[
Q_H(a)\le V_H(a)^2\le U_1V_H(a).
\tag{6.8}
\]

For the induced high measure

\[
\mu_H(a)=u_aQ_H(a),
\]

RTR-T02 gives

\[
\boxed{
\mathscr V_{\mu_H}(x_H)
\le
\frac{U_1}{4U_0^2}
\mathfrak D_{U_0,V_H}(x_H^\circ).
}
\tag{6.9}
\]

Thus the exact coefficient in the high adaptive return equation absorbs the complete two-suffix high density.

---

## RTR-T04 — Low-branch adaptive return

Use low first labels

\[
Y<b\le Y^2
\]

with total first-label mass `U_1`, but keep the fixed suffix family `c<=Y` with suffix mass `U_0`. Let

\[
\ell_b:=q_b(Y^3)=\left\lfloor\frac{Y^3}{b}\right\rfloor.
\]

Define

\[
S_L(b):=A(\ell_b)-A(Y),
\tag{7.1}
\]

\[
T_L(b):=\sum_{c\le Y}u_cf(q_c(\ell_b)),
\tag{7.2}
\]

\[
E_L(b):=\sum_{Y<c\le\ell_b}u_cf(q_c(\ell_b)),
\tag{7.3}
\]

and

\[
R_L(b):=\rho_{\ell_b}(f;\ell_b).
\tag{7.4}
\]

Then

\[
\boxed{
(U_0+S_L(b))f(\ell_b)+T_L(b)
=R_L(b)-E_L(b),
}
\tag{7.5}
\]

so

\[
\boxed{
Z^{(U_0+S_L)x_L}+Z^{T_L}
=Z^{R_L}-Z^{E_L}.
}
\tag{7.6}
\]

The exact low cross-pair mass is

\[
P_L(b)
:=\sum_{\substack{a\le Y,\ c>Y\\ac\le Y^3/b}}u_au_c.
\]

The admissible set is contained in

\[
\{a\le Y\}\times\{Y<c\le\ell_b\},
\]

hence

\[
\boxed{P_L(b)\le U_0S_L(b).}
\tag{7.7}
\]

For the induced low measure

\[
\mu_L(b)=u_bP_L(b),
\]

RTR-T02 now uses external baseline `A=U_0` and first-label mass `W=U_1`. It yields the sharper one-potential estimate

\[
\boxed{
\mathscr V_{\mu_L}(x_L)
\le
\frac1{4U_1}
\mathfrak D_{U_0,S_L}(x_L^\circ).
}
\tag{7.8}
\]

The auxiliary small-action potential introduced in the first V14 draft is therefore unnecessary for the low density bound.

---

## RTR-T05 — Return forcing bound

For any first-label value channels satisfying

\[
D+T=R-E,
\]

the elementary edgewise inequality

\[
(r-e-t)^2\le4r^2+4e^2+2t^2
\]

gives

\[
\boxed{
\mathcal E_w(D)
\le
4\mathcal E_w(R)
+4\mathcal E_w(E)
+2\mathcal E_w(T).
}
\tag{8.1}
\]

Since every coefficient defect is a positive subterm of `E_w(D)`, (6.9), (7.8), and the adaptive return equations imply

\[
\boxed{
\mathscr V_{\mu_H}(x_H)
\le
\frac{U_1}{U_0^2}
\left[
\mathcal E(R_H)
+\mathcal E(E_H)
+\frac12\mathcal E(T_H)
\right],
}
\tag{8.2}
\]

and

\[
\boxed{
\mathscr V_{\mu_L}(x_L)
\le
\frac1{U_1}
\left[
\mathcal E(R_L)
+\mathcal E(E_L)
+\frac12\mathcal E(T_L)
\right].
}
\tag{8.3}
\]

All relation energies in (8.2)--(8.3) use the relevant first-label base weights.

These estimates contain no induced marginal density on the right.

---

## RTR-T06 — Rectangular Markov nonexpansion

For

\[
T_i=\sum_{c\in C}v_cx_i^{(c)},
\]
weighted Cauchy--Schwarz gives, edgewise,

\[
\left(\sum_cv_c d_c\right)^2
\le
A\sum_cv_cd_c^2.
\]

Therefore

\[
\boxed{
\mathcal E_w(T)
\le
A\sum_{c\in C}v_c
\mathcal E_w(x^{(c)}).
}
\tag{9.1}
\]

Thus `T_H` and `T_L` are exactly the already known common-suffix nonexpansive relation transport. They do not create a new density mismatch.

The tail channels `E_H,E_L` use suffixes larger than `Y`; every such suffix lowers the corresponding intermediate vertex by a factor strictly larger than `Y`. They are the existing moving-cutoff boundary channels.

---

## RTR-T07 — Full deepest mean bridge

For one color, the V13 high/low square certificate gives

\[
\mathcal M_j
\le
\frac12\mathscr V_{\mu_H}(x_H)
+2\left(
\mathscr V_{\mu_{L_1}}(x_{L_1})
+
\mathscr V_{\mu_{L_2}}(x_{L_2})
\right).
\tag{10.1}
\]

Using (8.2)--(8.3), and symmetry of the two low positions,

\[
\boxed{
\begin{aligned}
\mathcal M_j\le{}&
\frac{U_1}{2U_0^2}
\left[
\mathcal E(R_H)+\mathcal E(E_H)
+\frac12\mathcal E(T_H)
\right]\\
&+\frac4{U_1}
\left[
\mathcal E(R_L)+\mathcal E(E_L)
+\frac12\mathcal E(T_L)
\right].
\end{aligned}
}
\tag{10.2}
\]

Summing the three colors and dividing by the full ordered degree-three packet mass gives the complete normalized deepest history-mean estimate.

Equation (10.2) is the sought mathematical bridge:

\[
\boxed{
\text{deep induced high/low conditional variance}
\longrightarrow
\text{adaptive complete residual}
+
\text{tail boundary}
+
\text{common-suffix transport}.
}
\]

The Beta law remains useful as the asymptotic shadow of the exact capacities, but it is no longer required as an external recursive norm.

---

## 11. The isolated native arithmetic gate

The only genuinely new same-scale forcing in (10.2) is

\[
\mathcal E(R_H)
\quad\text{and}\quad
\mathcal E(R_L),
\]

where

\[
R_H(a)=\rho_{X_a}(f;h_a),
\qquad
R_L(b)=\rho_{\ell_b}(f;\ell_b).
\]

For the actual centered prime remainder

\[
r(n)=\psi(n)/n-1,
\]
these are adaptive truncated prime-winding signless residuals. Their relation energy is precisely the operator-valued version of the scalar Selberg return defect.

The remaining target is therefore not another density theorem. It is the following local coefficient-two statement.

### Native residual target

Find a positive full-energy envelope `E_full` and a summable/lower-scale forcing `F_low` such that uniformly over the adaptive quotient vertices,

\[
\boxed{
\mathcal E_w(\rho_X(r;\cdot))
\le
\theta\,E_{\rm full}
+F_{\rm low},
\qquad
\theta<1,
}
\tag{11.1}
\]

without using `psi(x)~x` as an input.

At the scalar level this is the same arithmetic information carried by the exact Selberg coefficient-two identity. At the relation level it must be combined with the `S_3` provenance mixer to remove the approximate signless `-1` mode.

---

## 12. Exact checker

The script

- `scripts/check_free_research_rectangular_tail_return_intertwiner.py`

uses `Fraction` only and verifies:

1. the rectangular relation-field return identity;
2. the generalized centered coefficient-lift identity with `A!=W`;
3. exact high suffix-square absorption;
4. exact low cross-suffix absorption by one tail potential;
5. the adaptive return decomposition;
6. the return forcing inequality;
7. rectangular Markov nonexpansion;
8. the full high/low coefficient bookkeeping.

---

## 13. Updated boundary

Closed at finite algebraic/research-note theorem strength:

1. endpoint disintegration;
2. the false canonical-TV target and the correct Beta profile;
3. high and low two-body density absorption into one-body tail potentials;
4. the rectangular relation-field return lift;
5. exact adaptive completion for both high and low branches;
6. elimination of the induced density from the right side of the mean estimate;
7. isolation of the adaptive scalar residual relation energy as the unique same-scale arithmetic forcing.

Still open:

1. native control of the adaptive complete residual relation energy in (11.1);
2. a finite two-operator coercivity theorem for common-suffix transport followed by the `S_3` provenance mixer;
3. incorporation of every tail boundary channel into one summable lower-scale envelope;
4. end-to-end normalization against the complete odd-simplex energy;
5. any promoted quantitative prime remainder, Working Truth, Foundation, or RH-scale statement.

The remaining mathematical bridge is now one sharply typed Selberg-residual coercivity problem rather than a vague pushforward-density comparison.
