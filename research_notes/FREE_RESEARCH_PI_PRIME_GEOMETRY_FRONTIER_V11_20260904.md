# Free Research — Pi-to-Prime Geometry Frontier V11

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / CUBIC_RELATION_RETURN_LIFT_CLOSED / S3_GAP_ONE / BOOLEAN_MIXER_NO_GO / MOVING_CUTOFF_SMALLNESS_NO_GO / HALF_SCALE_TAIL_CASCADE / NATIVE_CASCADE_COERCIVITY_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V10_20260904.md`

## 1. Stable completed geometry

The stable pi-to-prime chain remains:

\[
\tau^2
=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1},
\]

with primes as irreducible Krawtchouk birth directions, prime powers as winding-layer births,

\[
\det\mathcal W_M=\operatorname{lcm}(1,\ldots,M),
\qquad
\psi(M)=\log\det\mathcal W_M,
\]

and the PNT closed by classical real Selberg smoothing after the finite carrier supplies the coefficient-two positive energy.

No classical PNT novelty is claimed.

---

## 2. Ordered cubic fluctuation package

For finite quotient actions and weights `u_a`, total mass `U`,

\[
\Omega_{a,b\mid c}
:=\delta_{bc}f(q_a)-\delta_{ac}f(q_b)
=f(q_a)-f(q_b).
\]

Hence

\[
\sum_{a,b,c}u_au_bu_c|\Omega_{a,b\mid c}|^2
=2U^2\Gamma_S(f;n).
\]

The same fluctuation is the internal capacity-weighted relation field

\[
Z_{ab}=u_au_b(f(q_a)-f(q_b)),
\]

whose energy satisfies

\[
\mathcal E_Z=2U\Gamma_S,
\qquad
\mathcal C_3=U\mathcal E_Z.
\]

Mass, grand total and relation-row sums recover every block total, so this is the minimal sufficient state beyond Boolean support.

---

## 3. Exact operator-valued return lift

For

\[
\rho_S(f;n)=\sum_{c\in S}u_c\delta_cf(n),
\]

every relation coordinate obeys

\[
\boxed{
UZ_{ab}(n)+\sum_cu_cZ_{ab}(q_c(n))
=u_au_b\bigl(\rho_S(q_a(n))-\rho_S(q_b(n))\bigr).
}
\]

In normalized form,

\[
Z+\mathcal P_SZ
=\frac{u_au_b}{U}(\rho_S\circ q_a-\rho_S\circ q_b).
\]

With the natural relation norm,

\[
\boxed{
\|(I+\mathcal P_S)Z\|_{u,*}^2
=\frac2U\operatorname{Var}_{u,n}(\rho_S\circ q).
}
\]

The common-suffix transport is Markov-nonexpansive but not strictly contractive by itself.

---

## 4. Exact `S_3` history gap and semantic boundary

Uniform averaging over the three position transpositions of a six-history fiber has

\[
\mathsf M_3|_{\rm triv}=1,
\qquad
\mathsf M_3|_{\rm std}=0.
\]

Its Dirichlet dissipation is exactly `4U^2 Gamma_S`.  Thus the optimal finite history-label mixer is explicit and has gap `1`.

Current exact BRC recoalescence retains only Boolean union support.  A formal six-branch counterexample proves that support, even together with branch count, cannot recover a multiplicity-sensitive mean.  Therefore the convex mixer cannot be reconstructed after current exact recoalescence.

It must either act before recoalescence on retained ordered histories or be admitted on the weighted capacity/total/relation state.

---

## 5. Moving-cutoff correction

At the natural scale

\[
n=Y^2,
\qquad
m_a=\left\lfloor\frac{Y^2}{a}\right\rfloor,
\]

the local action cloud at `m_a` extends beyond the global cloud `c<=Y`.

Let

\[
A(X)=\sum_{c\le X}\frac{\Lambda(c)}c,
\qquad U_Y=A(Y),
\]

and tail mass

\[
V_Y(a)=A(m_a)-A(Y).
\]

The first-mass law `A(X)=log X+O(1)` implies

\[
\boxed{
\sum_{a\le Y}\frac{\Lambda(a)}aV_Y(a)
=\frac12U_Y^2+O(U_Y).
}
\]

Therefore the moving-cutoff mismatch has limiting normalized mass `1/2`.  It is not a small boundary term.

This rules out every route that attempts to absorb the cutoff change into an undifferentiated `o(U_Y^2)` remainder.

---

## 6. Exact half-scale landing

Although the tail is macroscopic, every omitted suffix is scale-lowering.  If `c>Y`, then

\[
q_c(m_a)=q_{ac}(Y^2)
\le\left\lfloor\frac{Y-1}{a}\right\rfloor.
\]

Every prime-power first action satisfies `a>=2`, hence

\[
\boxed{
q_c(m_a)\le\left\lfloor\frac{Y-1}{2}\right\rfloor.
}
\]

Thus all tail endpoints land in one common half-scale region.

The exact residual decomposition is

\[
\rho_Y(m_a)=\rho_{m_a}(m_a)-T_{a,Y},
\]

where

\[
T_{a,Y}
=V_Y(a)f(m_a)
+\sum_{Y<c\le m_a}\frac{\Lambda(c)}c f(q_c(m_a)).
\]

The second term is entirely supported below `Y/2`.  The first is an explicit label-dependent diagonal term.

---

## 7. Correct renormalization mechanism

The moving-cutoff tail must be split rather than bounded wholesale:

1. its symmetric mass component supplies additional diagonal damping of the relation field;
2. its antisymmetric coefficient component remains in the `S_3` standard sector;
3. every endpoint component descends to the half-scale region;
4. the gap-one history mixer is the natural operator for the remaining standard component.

The required next inequality is therefore a dyadic cascade, not a boundary estimate:

\[
\boxed{
\mathcal E_Z(Y^2)
\le
\theta\,\mathcal E_Z^{\rm same\ scale}(Y^2)
+C\,\mathcal E_Z(\le Y/2)
+\mathcal E_{\rm coefficient\ defect},
}
\]

with `theta<1` after the symmetric tail mass is absorbed.

---

## 8. Formal and exact-computation state

Lean additions:

- `OrderedQuotientCurvature.lean`;
- `BranchAverageNoGo.lean`;
- `WeightedQuotientRelationField.lean`;
- `S3ProvenanceMixer.lean`.

Exact checkers:

- `check_free_research_ordered_cubic_curvature.py`;
- `check_free_research_s3_provenance_mixer.py`;
- `check_free_research_relation_field_return_lift.py`;
- `check_free_research_moving_cutoff_tail.py`.

The structural tail checker verifies quotient composition, sharp lower-scale landing, and exact residual decompositions using integers and `Fraction`.  The `1/2` mass law is derived from the already established analytic first-mass estimate, not inferred from floating-point data.

Workflow status is reported independently; no pending workflow is promoted to a proof claim.

---

## 9. Current boundary

Closed:

1. prime-birth and winding determinant geometry;
2. PNT at real-smoothing strength;
3. exact ordered cubic variance carrier;
4. weighted relation-field realization and recovery;
5. exact operator-valued return lift;
6. `S_3` gap-one mixer;
7. Boolean averaging no-go;
8. moving-cutoff smallness no-go;
9. exact half-scale tail landing.

Open:

1. a coercive dyadic cascade absorbing the symmetric tail mass;
2. control of the antisymmetric tail coefficient field;
3. admission or derivation of weighted `S_3` mixing before recoalescence;
4. native quantitative decay of the centered winding relation energy;
5. any RH-scale consequence.

---

## 10. Next mother question

Can the tail coefficient field

\[
a\longmapsto V_Y(a)
\]

be adjoined to the capacity-weighted relation state so that the `S_3` projector simultaneously annihilates the value fluctuation and its coefficient mismatch, leaving only a uniformly half-scale endpoint forcing?

A positive answer would turn the macroscopic cutoff mismatch into a strict renormalization step and would be the first plausible route from the finite gap-one history geometry to a native quantitative prime remainder.
