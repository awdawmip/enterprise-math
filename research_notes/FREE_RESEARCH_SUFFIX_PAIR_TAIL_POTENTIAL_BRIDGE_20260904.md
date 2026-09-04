# Free Research — Suffix-Pair Density to Tail-Potential Bridge

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_SUFFIX_PAIR_DOMINATION / POSITIVE_TAIL_POTENTIAL_ABSORPTION / HIGH_AND_LOW_BRANCHES_CLOSED_ALGEBRAICALLY / RETURN_EQUATION_COMPOSITION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_V14_NORMALIZATION_AUDIT_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the existing tail-augmented relation state and weighted coefficient-coercivity identity.

## 1. Executive advance

The clipped-Beta analysis identifies the correct asymptotic shape of the deepest high/low marginals, but the normalization audit proves that converting that profile back to the canonical shell norm at every level has unavoidable coefficient `3/2`.

There is a stronger finite route.  The induced quadratic suffix density is bounded by the square of a one-body tail mass.  That one-body tail mass is exactly the coefficient potential already present in the tail-augmented relation state.

For a centered value channel `x`, the existing coefficient-lift identity is

\[
\boxed{
\mathcal E_u((U+V)x)
=U^2\mathcal E_u(x)
+4U^2\sum_a u_aV_ax_a^2
+\mathcal E_u(Vx).
}
\tag{1.1}
\]

The middle term is a positive potential defect.  This checkpoint proves that every deepest suffix-pair marginal variance is bounded by such a defect.  Therefore the density bridge can be absorbed into the existing coercive side of the relation equation instead of being transported as an external profile norm.

---

## 2. Finite variance and potential notation

Let `S` be finite, let `u_a>=0`, and put

\[
U=\sum_{a\in S}u_a>0.
\]

For a value channel `x`, write

\[
\bar x_u=U^{-1}\sum_a u_ax_a,
\qquad
x_a^\circ=x_a-\bar x_u.
\]

For any nonnegative coefficient field `V_a`, define the exact potential defect

\[
\begin{aligned}
\mathfrak D_V(x)
:=&\;\mathcal E_u((U+V)x^\circ)
-U^2\mathcal E_u(x^\circ)
-\mathcal E_u(Vx^\circ).
\end{aligned}
\tag{2.1}
\]

By (1.1),

\[
\boxed{
\mathfrak D_V(x)
=4U^2\sum_a u_aV_a(x_a^\circ)^2
\ge0.
}
\tag{2.2}
\]

This is finite and exact for arbitrary positive weights.

---

## SPT-T01 — Abstract suffix-pair domination

For every `a`, let `T_a` be a finite suffix set with nonnegative weights `v_b`, and define its one-body mass

\[
V_a:=\sum_{b\in T_a}v_b.
\]

Let `D_a` be any admissible subset of `T_a x T_a`, and define the two-body mass

\[
Q_a:=\sum_{(b,c)\in D_a}v_bv_c.
\]

Positivity and set inclusion give

\[
\boxed{Q_a\le V_a^2.}
\tag{3.1}
\]

If

\[
V_a\le V_{\max}
\]

for every `a`, then

\[
\boxed{Q_a\le V_{\max}V_a.}
\tag{3.2}
\]

Give the first labels the induced measure

\[
\mu_Q(a):=u_aQ_a.
\]

Since variance is translation invariant, use the canonical centered channel `x^circ`.  Then

\[
\begin{aligned}
\mathscr V_{\mu_Q}(x)
&=\mathscr V_{\mu_Q}(x^\circ)\\
&\le\sum_a u_aQ_a(x_a^\circ)^2\\
&\le V_{\max}\sum_a u_aV_a(x_a^\circ)^2.
\end{aligned}
\]

Combining with (2.2) gives the exact bridge

\[
\boxed{
\mathscr V_{\mu_Q}(x)
\le
\frac{V_{\max}}{4U^2}
\mathfrak D_V(x).
}
\tag{3.3}
\]

No logarithmic asymptotic, total-variation estimate, bounded-readout assumption, or profile conversion is used.

---

## 4. High-branch specialization

At scale `n=Y^3`, fix the color in which `a<=Y` is the unique uncut action.  Put

\[
h_a=\left\lfloor\frac{Y^3}{a}\right\rfloor.
\]

Any two overcut suffixes `b,c>Y` satisfying

\[
abc\le Y^3
\]

must individually satisfy

\[
b,c\le\frac{Y^2}{a}.
\]

Define the one-body high tail mass

\[
\boxed{
V_H(a)
:=A(Y^2/a)-A(Y).
}
\tag{4.1}
\]

The exact deepest pair mass is

\[
Q_H(a)
:=\sum_{\substack{b,c>Y\\bc\le Y^3/a}}u_bu_c.
\]

Its admissible pair set is contained in the square of the tail interval `(Y,Y^2/a]`, hence

\[
\boxed{Q_H(a)\le V_H(a)^2.}
\tag{4.2}
\]

Let

\[
U_0:=A(Y),
\qquad
U_1:=A(Y^2)-A(Y).
\]

Then `V_H(a)<=U_1`, so for the high readout

\[
x_a=f(h_a)
\]

SPT-T01 gives

\[
\boxed{
\mathscr V_{\mu_H}(x)
\le
\frac{U_1}{4U_0^2}
\mathfrak D_{V_H}(x).
}
\tag{4.3}
\]

The right side is exactly the positive excess in the coefficient-lift relation energy on the uncut action cloud.

---

## SPT-T02 — Abstract cross-pair domination

Let an outer label `b` carry two nonnegative one-body coefficient fields

\[
R_b,
\qquad S_b,
\]

and suppose its induced cross-pair mass satisfies

\[
P_b\le R_bS_b.
\tag{5.1}
\]

Let the outer base weights be `w_b` with total mass

\[
W=\sum_bw_b>0.
\]

Assume

\[
R_b\le R_{\max},
\qquad
S_b\le S_{\max}.
\]

Since both

\[
P_b\le S_{\max}R_b
\]

and

\[
P_b\le R_{\max}S_b,
\]

we have

\[
\boxed{
P_b
\le\frac12\left(S_{\max}R_b+R_{\max}S_b\right).
}
\tag{5.2}
\]

For the induced measure

\[
\mu_P(b)=w_bP_b,
\]

centering `x` with respect to `w` and applying (2.2) separately to `R` and `S` gives

\[
\boxed{
\mathscr V_{\mu_P}(x)
\le
\frac{
S_{\max}\mathfrak D_R(x)
+R_{\max}\mathfrak D_S(x)}{8W^2}.
}
\tag{5.3}
\]

Thus a cross suffix density is absorbed by two ordinary coefficient potentials.

---

## 6. Low-branch specialization

For a low action

\[
Y<b\le Y^2,
\]

put

\[
\ell_b=\left\lfloor\frac{Y^3}{b}\right\rfloor,
\qquad
Z_b=Y^2/b.
\]

The low marginal sums pairs

\[
a\le Z_b,
\qquad
c>Y,
\qquad
ac\le YZ_b.
\]

Define

\[
\boxed{
R_L(b):=A(Z_b),
}
\tag{6.1}
\]

and

\[
\boxed{
S_L(b):=A(YZ_b)-A(Y)
=A(Y^3/b)-A(Y).
}
\tag{6.2}
\]

The admissible `(a,c)` set is contained in the Cartesian product of these two one-body ranges.  Therefore its exact mass `P_L(b)` satisfies

\[
\boxed{P_L(b)\le R_L(b)S_L(b).}
\tag{6.3}
\]

Moreover,

\[
R_L(b)\le U_0,
\qquad
S_L(b)\le U_1.
\]

The outer low shell has base mass `U_1`.  Applying SPT-T02 to

\[
x_b=f(\ell_b)
\]

gives

\[
\boxed{
\mathscr V_{\mu_L}(x)
\le
\frac{
U_1\mathfrak D_{R_L}(x)
+U_0\mathfrak D_{S_L}(x)}{8U_1^2}.
}
\tag{6.4}
\]

Both coefficient fields are scale-local and finite:

- `R_L` is the small-action capacity below the relative quotient `Y^2/b`;
- `S_L` is the moving-cutoff tail mass at the low intermediate vertex.

They can be carried by the same product-channel relation architecture as the existing tail coefficient `Vx`.

---

## SPT-T03 — Full deepest history-mean bridge

Let `T_Y` be the full ordered degree-three packet mass.  After endpoint disintegration, the exact high/low inequality for one color is

\[
\mathcal M_j
\le\frac12\mathscr V_{\mu_H}
+2\left(
\mathscr V_{\mu_{L_1}}
+\mathscr V_{\mu_{L_2}}
\right).
\tag{7.1}
\]

The two low marginals have the same upper bound.  Insert (4.3) and (6.4), sum the three colors, and divide by `T_Y`.  The result is

\[
\boxed{
\begin{aligned}
\mathcal E_{\rm mean}^{\rm deep}
\le\frac3{T_Y}
\Bigg[
&\frac{U_1}{8U_0^2}
\mathfrak D_{V_H}\\
&+\frac{
U_1\mathfrak D_{R_L}
+U_0\mathfrak D_{S_L}}{2U_1^2}
\Bigg].
\end{aligned}
}
\tag{7.2}
\]

Every term on the right is a positive coefficient-lift defect already representable by an ordinary weighted relation field.

Equation (7.2) is the finite energy form of the remaining density bridge.  The Beta profile is the asymptotic shadow of these nested one-body tail capacities.

---

## 8. Relation to the V14 `3/2` no-go

The clipped-Beta route enlarged the induced measure and then compared the resulting profile to the canonical shell measure.  Paying that comparison at every level gives the universal noncontractive coefficient `3/2`.

SPT-T03 does something different:

\[
\boxed{
\text{two-body suffix density}
\longrightarrow
\text{one-body positive potential defect}.
}
\]

The potential defect sits on the coercive side of the coefficient-lift identity.  It is not a new norm that must be converted back at every recursive level.

Thus SPT-T03 bypasses the normalization no-go rather than trying to optimize around it.

---

## 9. Exact checker

The script

- `scripts/check_free_research_suffix_pair_potential_bridge.py`

uses `Fraction` only and verifies:

1. the exact coefficient-lift potential identity;
2. high suffix-pair domination `Q<=V^2<=Vmax*V`;
3. the induced-variance bound by the high potential defect;
4. cross-pair domination `P<=RS`;
5. the two-potential low-branch bound;
6. the full three-color normalized algebra of (7.2).

---

## 10. Updated boundary

Closed algebraically and without asymptotics:

1. high two-suffix density to one tail potential;
2. low cross-suffix density to two tail potentials;
3. arbitrary-readout variance control;
4. exact composition with the existing weighted coefficient-coercivity identity;
5. full deepest mean contribution as a positive sum of coefficient-lift defects.

Still open:

1. insert the three specific coefficient lifts `V_H`, `R_L`, and `S_L` into the exact arithmetic relation-return equation;
2. show which defects are absorbed on the left and which product channels descend to lower scale;
3. close the resulting finite block singular-value/coercivity estimate;
4. integrate with the standard `1/9` channel and the complete odd-simplex energy.

The remaining bridge has now moved from measure comparison to a finite multichannel return-law calculation.
