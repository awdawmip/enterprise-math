# Free Research — Pi-to-Prime Geometry Frontier V10

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / CUBIC_VARIANCE_AND_RETURN_LIFT_CLOSED / S3_GAP_ONE / BOOLEAN_NATIVE_MIXER_NO_GO / WEIGHTED_RELATION_MIXER_CANDIDATE / MOVING_CUTOFF_DECAY_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V9_20260904.md`

## 1. Stable prime geometry

The stable chain remains

\[
\boxed{
\begin{aligned}
\tau^2
&=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1},\\
\text{prime }p
&=\text{irreducible Krawtchouk birth direction},\\
p^a
&=\text{winding-layer birth},\\
\det\mathcal W_M
&=\operatorname{lcm}(1,\ldots,M),\\
\psi(M)&=\log\det\mathcal W_M,\\
\Psi_2(M)&=2M\log M+O(M),\\
\psi(M)&\sim M,\\
\pi(M)&\sim M/\log M.
\end{aligned}}
\]

The PNT conclusion is closed by classical real Selberg smoothing fed by the finite prime-winding/Hamming energy.  No external novelty claim is made for the PNT.

---

## 2. Static fluctuation carrier is exact

For

\[
q_a(n)=\lfloor n/a\rfloor,
\qquad
\delta_a f(n)=f(n)+f(q_a(n)),
\]

the ordered common-suffix curvature is

\[
\Omega_{a,b\mid c}(f;n)
=\delta_{bc}f(q_a(n))-\delta_{ac}f(q_b(n)).
\]

Commuting quotient composition cancels the common endpoint and gives

\[
\boxed{
\Omega_{a,b\mid c}(f;n)=f(q_a(n))-f(q_b(n)).
}
\]

For finite action weights `u_a` with total mass `U`,

\[
\boxed{
\sum_{a,b,c}u_au_bu_c|\Omega_{a,b\mid c}|^2
=2U^2\Gamma_S(f;n),
}
\]

where `Gamma_S` is the weighted quotient-cloud variance.

Thus the degree-three carré du champ is no longer an inequality target; it is an exact finite identity.

---

## 3. Capacity-weighted relation-field form

Set

\[
x_a=f(q_a(n)),
\qquad m_a=u_a,
\qquad c_a=u_ax_a.
\]

The accepted relation field

\[
Z_{ab}=m_bc_a-m_ac_b
\]

becomes

\[
\boxed{Z_{ab}=u_au_b(x_a-x_b).}
\]

It satisfies antisymmetry and the weighted triangular closure law.  Its positive pairing is

\[
\boxed{
\mathcal E_Z
:=\sum_{a,b}Z_{ab}(x_a-x_b)
=2U\Gamma_S(f;n).
}
\]

The cubic curvature energy is exactly

\[
\boxed{
\mathcal C_{3,S}=U\mathcal E_Z.
}
\]

Masses, the grand total, and the relation-row sums recover every block total:

\[
Mc_i=m_iC+R_i.
\]

Therefore the relation field is a sufficient minimal state for the fluctuation lost under support-only recoalescence.

---

## 4. Exact dynamic return lift

Define the finite scalar signless residual

\[
\rho_S(f;n)
:=\sum_{c\in S}u_c\delta_cf(n).
\]

Every relation coordinate obeys the exact pointwise transport identity

\[
Z_{ab}(n)+Z_{ab}(q_c(n))
=u_au_b\left(
\delta_cf(q_a(n))-\delta_cf(q_b(n))
\right).
\]

After weighted summation over the common suffix:

\[
\boxed{
UZ_{ab}(n)+\sum_cu_cZ_{ab}(q_c(n))
=u_au_b\left(
\rho_S(q_a(n))-\rho_S(q_b(n))
\right).
}
\]

With

\[
(\mathcal P_SZ)_{ab}(n)
=U^{-1}\sum_cu_cZ_{ab}(q_c(n)),
\]

this becomes

\[
\boxed{
Z_{ab}+\mathcal P_SZ_{ab}
=\frac{u_au_b}{U}
\left(
\rho_S\circ q_a-ho_S\circ q_b
\right).
}
\]

This is the canonical ordered operator-valued lift that V8 required.

---

## 5. Dynamic carré-du-champ identity

Use the natural relation norm

\[
\|Z\|_{u,*}^2
=\sum_{a,b}\frac{|Z_{ab}|^2}{u_au_b}.
\]

Then

\[
\|Z(f;n)\|_{u,*}^2=2U\Gamma_S(f;n)
\]

and the lifted return law gives

\[
\boxed{
\|(I+\mathcal P_S)Z(f;n)\|_{u,*}^2
=\frac{2}{U}
\operatorname{Var}_{u,n}(\rho_S\circ q).
}
\]

Moreover `P_S` is a Markov nonexpansion:

\[
\boxed{
\|\mathcal P_SZ(n)\|_{u,*}^2
\le U^{-1}\sum_cu_c\|Z(q_c(n))\|_{u,*}^2.
}
\]

The remaining obstruction is therefore exact: nonexpansion does not exclude an approximate sign-reversing relation mode.

---

## 6. `3!` history mixer removes the remaining mode

For one six-history fiber, define

\[
H(\sigma)=x_{\sigma(1)}+z,
\qquad \sigma\in S_3.
\]

Uniform averaging over the three position transpositions

\[
\mathsf M_3=\frac13(P_{12}+P_{13}+P_{23})
\]

preserves the trivial mean and annihilates the standard representation:

\[
\boxed{
\mathsf M_3|_{\rm triv}=1,
\qquad
\mathsf M_3|_{\rm std}=0.
}
\]

The sign component is absent for closing-edge readouts.  Thus `M_3` has gap `1` on all nontrivial information actually present.

Its weighted Dirichlet dissipation is exactly

\[
\boxed{
4U^2\Gamma_S(f;n).
}
\]

For general `r!` fibers, the standard eigenvalue is `(r-3)/(r-1)`; degree three is the unique smallest exact one-step projector.

---

## 7. Current Boolean language cannot realize the convex mixer

Current exact BRC denotation remembers only union support.  Exact recoalescence identifies six-branch configurations with equal support even when their multiplicities and uniform means differ.

A formal six-branch witness proves that no decoder from

\[
(\text{support union},\text{branch count})
\]

can recover the history-average numerator.  Exact union recoalescence is still less informative.

Therefore, within the current support-extensional semantics,

\[
\boxed{
\mathsf M_3\text{ cannot be realized as a numerical convex average after recoalescence.}
}
\]

This closes the V9 native-realization dichotomy negatively for the present Boolean language.

A realization requires either:

1. retaining the ordered live history list and applying the readout before recoalescence; or
2. admitting the accepted capacity/total/relation field as an explicit weighted branch state and letting `M_3` annihilate its internal field.

The second option is the minimal sufficient extension.

---

## 8. Formal and exact-computation state

New Lean files on the active branch:

- `EnterpriseMath/Relation/OrderedQuotientCurvature.lean`;
- `EnterpriseMath/Relation/BranchAverageNoGo.lean`;
- `EnterpriseMath/Relation/WeightedQuotientRelationField.lean`;
- `EnterpriseMath/Relation/S3ProvenanceMixer.lean`.

New exact checkers:

- `check_free_research_ordered_cubic_curvature.py`;
- `check_free_research_s3_provenance_mixer.py`;
- `check_free_research_relation_field_return_lift.py`.

The formal files contain no `sorry`, `admit`, or custom axioms.  Workflow status is reported separately; pending execution is not treated as a mathematical blocker.

---

## 9. Current boundary

Closed:

1. ordered cubic curvature and exact variance identity;
2. Hodge/standard-sector interpretation;
3. capacity-weighted relation-field realization and recovery;
4. exact operator-valued return lift;
5. residual-variance forcing identity;
6. `S_3` gap-one mixer;
7. current Boolean BRC averaging no-go.

Open:

1. explicit adoption or derivation of a weighted relation-field mixer in the primitive state language;
2. moving-cutoff compatibility for `S_{sqrt n}` under quotient transport;
3. an arithmetic estimate forcing normalized residual-cloud variance to decay independently of the completed PNT;
4. a quantitative remainder for `psi(x)-x`;
5. any RH-scale statement.

---

## 10. Next mother question

The finite geometry and operator algebra are now closed.  The next problem is purely arithmetic/dynamical:

> At the natural moving cutoff `Y=floor(sqrt n)`, can the exact relation-field return lift and the gap-one `S_3` projection be combined with cutoff-comparison bounds to prove
> \[
> \mathcal E_Z(r;n)=o(U_Y)
> \]
> directly from finite prime-winding energy identities?

Equivalently, control the mismatch between the action clouds attached to `n`, `q_a(n)`, and `q_{ab}(n)` strongly enough that the local gap-one history mixer survives the changing arithmetic cutoff.

This is the first unresolved step that is neither a carrier-identification problem nor a generic spectral-gap search.
