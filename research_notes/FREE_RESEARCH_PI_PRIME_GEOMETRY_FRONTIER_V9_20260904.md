# Free Research — Pi-to-Prime Geometry Frontier V9

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / ORDERED_CUBIC_VARIANCE_IDENTITY / S3_STANDARD_GAP_ONE / SUPPORT_AVERAGING_NO_GO / WEIGHTED_RELATION_FIELD_SUFFICIENT / NATIVE_ARITHMETIC_DISSIPATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V8_20260904.md`

## 1. Stable completed chain

The current prime extension of the endogenous full-turn geometry remains

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

The PNT closure uses classical real Selberg smoothing after the finite prime-winding/Hamming carrier supplies the positive degree-two energy.  Classical PNT novelty is not claimed.

V8 left open an ordered operator-valued degree-three lift capable of retaining transported quotient fluctuations.  V9 closes that finite carrier problem exactly.

---

## 2. Exact ordered cubic curvature

For quotient actions

\[
q_a(n)=\lfloor n/a\rfloor
\]

and signless defects

\[
\delta_a f(n)=f(n)+f(q_a(n)),
\]

define the common-suffix ordered curvature

\[
\boxed{
\Omega_{a,b\mid c}(f;n)
=\delta_{bc}f(q_a(n))-\delta_{ac}f(q_b(n)).
}
\]

Both closing edges terminate at `q_abc(n)`, so the endpoint cancels:

\[
\boxed{
\Omega_{a,b\mid c}(f;n)
=f(q_a(n))-f(q_b(n)).
}
\]

The curvature is suffix-independent, antisymmetric in `a,b`, and obeys the exact triangular cocycle law.

For a finite action set `S`, positive weights `u_a`, and

\[
U=\sum_a u_a,
\]

define

\[
\mathcal C_{3,S}(f;n)
=\sum_{a,b,c}u_au_bu_c|\Omega_{a,b\mid c}(f;n)|^2.
\]

If `Gamma_S` is the weighted quotient-cloud variance, then

\[
\boxed{
\mathcal C_{3,S}(f;n)=2U^2\Gamma_S(f;n).
}
\]

Thus the requested degree-three comparison is an equality, not merely an upper bound.

---

## 3. Hodge/representation form

The transported cubic closing-edge tensor is

\[
A_f(a,b,c;n)=\delta_{bc}f(q_a(n)).
\]

Under the transposition exchanging the first two labels,

\[
A_f^-:=\frac12(A_f-\tau A_f)
=\frac12\bigl(f(q_a(n))-f(q_b(n))\bigr).
\]

Hence

\[
\boxed{
\Gamma_S(f;n)=\frac{2}{U^2}\|A_f^-\|_u^2.
}
\]

The fluctuation is exactly the antisymmetric ordered-provenance sector.  Product-label pushforward must therefore occur only after this polarization.

For prime-power weights

\[
u_a=\Lambda(a)/a,
\]

the triple coefficient groups as

\[
\sum_{abc=m}u_au_bu_c
=\frac{(\Lambda_Y*\Lambda_Y*\Lambda_Y)(m)}m.
\]

This is the fully split collision sector of

\[
\Lambda_3=D^2\Lambda+3\Lambda*(D\Lambda)+\Lambda^{*3}.
\]

---

## 4. The `3!` provenance fiber now carries a gap-one mixer

For fixed labels `a,b,c`, every ordered history `sigma in S_3` has the same final endpoint.  Its direct closing-edge readout has the form

\[
H(\sigma)=x_{\sigma(1)}+z,
\qquad x_a=f(q_a(n)),
\qquad z=f(q_{abc}(n)).
\]

The sign representation vanishes, the trivial representation is the common mean, and all fluctuation lies in the two-dimensional standard representation.

Let

\[
\mathsf M_3
=\frac13(P_{12}+P_{13}+P_{23})
\]

be uniform averaging over the three position transpositions.  Then

\[
\boxed{
\mathsf M_3H=\Pi_{\rm triv}H,
\qquad
\mathsf M_3|_{\rm std}=0.
}
\]

So the standard-sector gap is exactly `1`.  Globally,

\[
\boxed{
\sum_{a,b,c}u_au_bu_c
\langle H_{a,b,c},(I-\mathsf M_3)H_{a,b,c}\rangle
=4U^2\Gamma_S(f;n).
}
\]

For `r!` histories, the corresponding uniform transposition mixer has standard eigenvalue

\[
\lambda_r=\frac{r-3}{r-1}
\]

and gap

\[
1-\lambda_r=\frac2{r-1}.
\]

Degree three is the unique smallest degree at which this first-history fluctuation sector is annihilated in one step.

---

## 5. Degree elevation alone does not contract

Appending any common suffix word to the two compared ordered histories leaves the curvature unchanged.  At every degree `r>=2`,

\[
\sum u_au_b\prod_j u_{c_j}
|\Omega^{(r)}|^2
=2U^{r-1}\Gamma_S.
\]

Therefore merely increasing provenance degree adds a cylindrical mass factor but no new contraction.  The contraction comes from mixing the ordered first/intermediate label, not from a longer common suffix.

---

## 6. Exact support-only no-go

Current exact BRC recoalescence is Boolean-support union.  Two six-branch configurations can have the same support and the same branch count while carrying different multiplicity-sensitive averages.

The formal witness uses

\[
(0,0,0,1,1,1)
\]

and

\[
(0,0,0,0,0,1).
\]

Both have support `{0,1}` and length `6`, but different true multiplicities.  The existing `NO_RESURRECTION` theorem therefore implies:

\[
\boxed{
\text{support union, even with branch count, cannot recover the history average.}
}
\]

Exact recoalescence literally identifies the two configurations.  Consequently the convex `S_3` mixer is not definable from the current Boolean denotation after recoalescence.

---

## 7. Accepted weighted relation field is the minimal sufficient lift

Reuse the accepted capacity-weighted relation field

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

It is antisymmetric and satisfies

\[
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.
\]

For a finite block family, with

\[
M=\sum_jm_j,
\qquad C=\sum_jc_j,
\qquad R_i=\sum_jZ_{ij},
\]

one has

\[
\boxed{Mc_i=m_iC+R_i.}
\]

Thus masses, grand total, and relation-row sums recover every block total exactly when `M` is nonzero.

For quotient-cloud values `x_a=f(q_a(n))`, set

\[
m_a=u_a,
\qquad c_a=u_ax_a.
\]

Then

\[
Z_{ab}=u_au_b(x_a-x_b)
\]

and

\[
\boxed{
\sum_{a,b}Z_{ab}(x_a-x_b)
=2U\Gamma_S(f;n).
}
\]

Moreover,

\[
\boxed{
\mathcal C_{3,S}=U\mathcal E_Z.
}
\]

The ordered cubic curvature, weighted relation-field energy, and quotient-cloud variance are therefore three exact presentations of one finite object.

A fully averaged state has `c_i=m_i bar x` and hence `Z_ij=0`.  The `S_3` mixer is precisely internal relation-field annihilation.

---

## 8. Tool and formalization status

Reuse classification:

- `T0_BRC`: support/recoalescence and no-resurrection;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: permutation action and standard sector;
- `T8_RELATION_OBSERVABLE_SPECTRUM`: capacity-weighted relation field.

Resolution: `COMPOSE_APPLIED`.  No new general-purpose tool family is claimed.

New Lean files:

- `EnterpriseMath/Relation/OrderedQuotientCurvature.lean`;
- `EnterpriseMath/Relation/BranchAverageNoGo.lean`;
- `EnterpriseMath/Relation/WeightedQuotientRelationField.lean`;
- `EnterpriseMath/Relation/S3ProvenanceMixer.lean`.

New exact checkers:

- `scripts/check_free_research_ordered_cubic_curvature.py`;
- `scripts/check_free_research_s3_provenance_mixer.py`.

The files contain no `sorry`, `admit`, or custom axiom.  Lean-green status is not asserted until the branch workflow succeeds.

---

## 9. Updated boundary

Closed:

1. canonical ordered degree-three operator lift;
2. exact carré-du-champ/variance polarization;
3. cubic collision support;
4. `S_3` standard-sector gap-one mixer;
5. all-degree cylindrical lift and its noncontraction no-go;
6. Boolean support averaging no-go;
7. minimal sufficient weighted relation-field state.

Open:

1. prove that an allowed native branch operation induces `M_3`, or explicitly admit the weighted relation-field mixer as a primitive;
2. derive arithmetic decay of the transported cubic edge norm or internal relation-field energy without importing the completed PNT;
3. convert such decay into a quantitative remainder for `psi(x)-x`;
4. any RH-scale claim.

---

## 10. Next mother question

The geometric carrier and its optimal finite mixer are explicit.  The next discriminating problem is:

> Does the current primitive Enterprise rotation/branch language generate the gap-one transposition projector on every `3!` history fiber while preserving the accepted capacity/total/relation state, or is a weighted mixer a genuinely new primitive?

Conditional on a native realization, the arithmetic target becomes

\[
\boxed{
\frac1{U_Y^2}
\sum_{a,b,c\le Y}
\frac{\Lambda(a)\Lambda(b)\Lambda(c)}{abc}
|\delta_{bc}r(q_a(n))|^2
\longrightarrow0,
}
\]

at `Y=floor(sqrt n)`.  Its antisymmetric part is exactly the quotient-cloud variance.  Proving this decay natively would produce a quantitative prime-remainder mechanism beyond the present real-smoothing closure.
