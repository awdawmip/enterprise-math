# Free Research — Exact Return Lift for the Prime-Winding Relation Field

Status: `FREE_RESEARCH_FRONTIER / OPERATOR_VALUED_RETURN_LAW_CLOSED / MARKOV_NONEXPANSION / STRICT_ARITHMETIC_CONTRACTION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_WEIGHTED_RELATION_FIELD_LIFT_20260904.md`

## 1. Executive advance

The weighted relation field does not merely encode the quotient-cloud variance statically.  The scalar signless return equation lifts exactly to every internal relation coordinate.

This supplies the missing dynamic bridge:

\[
\boxed{
\text{scalar return residual differences}
\longleftrightarrow
\text{signless transport residual of the ordered relation field}.
}
\]

The lift is finite, cutoff-generic, and independent of prime asymptotics.

---

## 2. Finite return residual

For a finite action family `S`, weights `u_c`, and

\[
U=\sum_{c\in S}u_c,
\]

define

\[
\boxed{
\rho_S(f;n)
:=\sum_{c\in S}u_c\delta_cf(n)
=Uf(n)+\sum_{c\in S}u_cf(q_c(n)).
}
\tag{2.1}
\]

For quotient-cloud values

\[
x_a(n)=f(q_a(n)),
\]

define the weighted internal relation coordinate

\[
\boxed{
Z_{ab}(f;n)
:=u_au_b\bigl(x_a(n)-x_b(n)\bigr).
}
\tag{2.2}
\]

This is the capacity-weighted relation field of the block totals `c_a=u_ax_a`.

---

## RFR-T01 — Pointwise common-suffix transport

For every suffix action `c`, quotient composition gives

\[
q_a(q_c(n))=q_c(q_a(n)).
\]

Hence

\[
\boxed{
Z_{ab}(f;n)+Z_{ab}(f;q_c(n))
=u_au_b\left(
\delta_cf(q_a(n))-\delta_cf(q_b(n))
\right).
}
\tag{3.1}
\]

This is the relation-field version of a signless edge equation.  The left side is a present relation coordinate plus its transported copy; the right side is the difference of scalar signless defects at the two ordered intermediate vertices.

---

## RFR-T02 — Exact operator-valued return lift

Multiply (3.1) by `u_c` and sum over `c`.  The result is

\[
\boxed{
UZ_{ab}(f;n)
+\sum_{c\in S}u_cZ_{ab}(f;q_c(n))
=u_au_b\left(
\rho_S(f;q_a(n))-\rho_S(f;q_b(n))
\right).
}
\tag{4.1}
\]

Define the normalized relation transport

\[
(\mathcal P_SZ)_{ab}(n)
:=\frac1U\sum_{c\in S}u_cZ_{ab}(q_c(n)).
\]

For `U != 0`, (4.1) becomes

\[
\boxed{
Z_{ab}(n)+(\mathcal P_SZ)_{ab}(n)
=\frac{u_au_b}{U}
\left(
\rho_S(q_a(n))-\rho_S(q_b(n))
\right).
}
\tag{4.2}
\]

Thus the scalar return law has a canonical ordered operator-valued lift.  No product-label collapse occurs.

---

## RFR-T03 — Exact residual norm identity

Assume all action weights are positive and define the natural relation norm

\[
\|Z\|_{u,*}^2
:=\sum_{a,b\in S}\frac{|Z_{ab}|^2}{u_au_b}.
\tag{5.1}
\]

For the quotient relation field,

\[
\boxed{
\|Z(f;n)\|_{u,*}^2
=\sum_{a,b}u_au_b|f(q_a(n))-f(q_b(n))|^2
=2U\Gamma_S(f;n).
}
\tag{5.2}
\]

Applying (4.2) coordinatewise yields

\[
\boxed{
\|(I+\mathcal P_S)Z(f;n)\|_{u,*}^2
=\frac1{U^2}
\sum_{a,b}u_au_b
|\rho_S(q_a(n))-\rho_S(q_b(n))|^2.
}
\tag{5.3}
\]

Equivalently,

\[
\boxed{
\|(I+\mathcal P_S)Z(f;n)\|_{u,*}^2
=\frac{2}{U}
\operatorname{Var}_{u,n}(\rho_S\circ q).
}
\tag{5.4}
\]

This is the exact dynamic carré-du-champ identity.  The signless failure of the internal relation field is measured by the quotient-cloud variance of the scalar residual itself.

---

## RFR-T04 — Markov nonexpansion

Because `P_S` is a convex average over common suffix transports, Jensen's inequality gives

\[
\boxed{
\|\mathcal P_SZ(n)\|_{u,*}^2
\le\frac1U\sum_{c\in S}u_c
\|Z(q_c(n))\|_{u,*}^2.
}
\tag{6.1}
\]

The relation transport is therefore nonexpansive in its natural weighted norm.

This is not yet a strict contraction.  A common-suffix lift leaves the ordered curvature invariant, and quotient chains may retain approximate sign alternation.  This agrees with the earlier cylindrical-lift and nilpotent-pseudospectral no-go results.

---

## 7. Prime-winding specialization

For

\[
u_a=\Lambda(a)/a
\]

on prime powers up to a finite cutoff, `rho_S` is the truncated prime-winding signless return residual.  Equation (4.2) says that every internal prime-direction relation coordinate obeys the same signless return law, forced only by residual differences across its two intermediate quotient vertices.

For the centered field

\[
r(n)=\psi(n)/n-1,
\]

a quantitative native remainder theorem can now be sought in the form

\[
\operatorname{Var}_{u,n}(\rho_S\circ q)
\quad\text{small}
\quad\Longrightarrow\quad
\Gamma_S(r;n)\quad\text{small},
\]

provided the approximate `-1` relation mode is removed.

The gap-one `S_3` provenance mixer is exactly the finite operator that removes that mode on the ordered first-history sector.  Current Boolean support semantics cannot realize its convex averaging, while the weighted relation-field state can represent it exactly.

---

## 8. Formal and computational status

Lean file:

- `EnterpriseMath/Relation/WeightedQuotientRelationField.lean`.

New formal theorems include:

1. `relationField_signless_transport`;
2. `relationField_return_lift`;
3. `relationField_normalized_return_lift`.

Exact checker:

- `scripts/check_free_research_relation_field_return_lift.py`.

It verifies with rational arithmetic:

1. the coordinatewise return lift;
2. its normalized form;
3. the natural relation norm identity;
4. the residual-variance identity;
5. Markov nonexpansion.

Lean-green status is not claimed until the branch workflow succeeds.

---

## 9. Updated boundary

Closed:

- static ordered cubic curvature;
- exact relation-field representation of quotient variance;
- exact operator-valued signless return lift;
- exact residual-variance forcing identity;
- nonexpansion of common-suffix transport;
- explicit gap-one `S_3` standard-sector mixer.

Open:

- realization of the convex mixer as an allowed weighted branch primitive;
- arithmetic control of the truncated residual variance at compatible moving cutoffs;
- strict contraction after combining quotient transport with provenance mixing;
- a quantitative decay rate for `psi(x)-x`.

---

## 10. Next discriminating theorem

The next target is a two-operator coercivity estimate for

\[
\mathcal K_S:=\mathsf M_3\mathcal P_S
\]

on the ordered weighted relation state.

At the purely history-label level, `M_3` kills the standard sector exactly.  The unresolved issue is to place `M_3` inside the allowed weighted branch dynamics and control boundary/cutoff mismatch when `S=S_{\sqrt n}` varies with `n`.

A successful finite estimate would convert the scalar residual bound into direct decay of the internal relation field and hence of the prime-winding quotient variance.
