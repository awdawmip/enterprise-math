# p=7 trace transfer, Prym principalization obstruction, and 2-by-3 arithmetic holonomy

Status: `FREE_RESEARCH / DERIVED EXACT CONTINUATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R45-P7-ALL-EXTENSION-TRACE-TRANSFER / R46-WEIL-RESTRICTION-PPAV-NONJACOBIAN-BOUNDARY / R47-PRYM-POLARIZATION-CUBIC-PRINCIPALIZATION-OBSTRUCTION / R48-C2-C3-SIMULTANEOUS-STRICTIFICATION`.

## 1. All-extension trace transfer

Let `C7/F49` be the explicit genus-2 curve whose Jacobian has characteristic polynomial

\[
h(T)=T^4+5T^3+245T+2401.
\]

If `s_m` is the m-th power sum of the roots, then

\[
s_0=4,\quad s_1=-5,\quad s_2=25,\quad s_3=-860,
\]

and for `m>=4`,

\[
\boxed{s_m+5s_{m-1}+245s_{m-3}+2401s_{m-4}=0.}
\]

Since

\[
J(C_{46})_{/\mathbf F_{49}}\sim E_{/\mathbf F_{49}}\times J(C_7)^2,
\]

for every `m>=1`,

\[
\boxed{\#C_{46}(\mathbf F_{49^m})-\#E(\mathbf F_{49^m})=-2s_m.}
\]

Equivalently,

\[
\#C_{46}(\mathbf F_{49^m})=\#E(\mathbf F_{49^m})+2\#C_7(\mathbf F_{49^m})-2(49^m+1).
\]

Over the original field, the outer endomorphism character gives zero odd Prym traces. Thus

\[
\#C_{46}(\mathbf F_{7^n})-\#E(\mathbf F_{7^n})=
\begin{cases}
0,&n\text{ odd},\\
-2s_{n/2},&n\text{ even}.
\end{cases}
\]

The first even differences, for degrees `2,4,6,8`, are

\[
10,-50,1720,8158.
\]

## 2. Canonical Weil-restriction polarization is not a smooth genus-4 Jacobian

Put

\[
A_7=\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}J(C_7)
\]

with the principal polarization obtained by Weil restriction. Over the algebraic closure,

\[
(A_7,\lambda_{\rm Res})\simeq(J(C_7),\lambda_{C_7})\times(J(C_7)^{(7)},\lambda_{C_7}^{(7)}).
\]

The principal polarization is geometrically decomposable. A principally polarized Jacobian of a smooth connected curve has an indecomposable theta divisor. Therefore

\[
\boxed{(A_7,\lambda_{\rm Res})\text{ is not the polarized Jacobian of a smooth genus-4 curve}.}
\]

It is naturally a compact-type stable Jacobian after geometric base change. This does not exclude another principal polarization in the same unpolarized isogeny class from being a smooth Jacobian.

## 3. Kernel and cubic principalization obstruction

For the ramified double cover `pi:C46->E`, the Prym polarization `lambda_P` has type `(1,1,1,2)` and

\[
\boxed{\ker\lambda_P=\pi^*E[2]\simeq E[2].}
\]

A degree-2 isogeny `phi` with principal target and `phi^*lambda'=lambda_P` is equivalent to a Frobenius-stable maximal isotropic line in this two-dimensional symplectic `F2`-space.

The elliptic quotient is

\[
E:y^2=x^3-6x^2+36.
\]

Modulo 7, its nonzero 2-torsion x-coordinates satisfy

\[
x^3+x^2+1=0.
\]

This cubic is irreducible over `F7`. Frobenius therefore cycles the three nonzero points of `E[2]`; on `E[2]` it has characteristic polynomial `T^2+T+1` and order 3. Hence it fixes no isotropic line over `F7` or `F49`. A line is defined over `F_{7^n}` exactly when `3|n`.

Thus

\[
\boxed{\lambda_P\text{ has no compatible degree-2 principal quotient over }\mathbf F_7\text{ or }\mathbf F_{49}.}
\]

The minimal principalization field is

\[
\boxed{\mathbf F_{7^3}.}
\]

Over it all three nonzero lines give degree-2 principal quotients.

## 4. Independent C2 and C3 transports

The endomorphism-field outer character has order 2 and is killed over `F49`, where `P46,7` becomes `B^2`. The Frobenius action on the polarization kernel has order 3 and is killed over `F_{7^3}`. Neither extension kills the other obstruction. Therefore the smallest field on which both the isogeny-square decomposition and all polarization-kernel lines are simultaneously strict is

\[
\boxed{\mathbf F_{7^6}},\qquad \operatorname{lcm}(2,3)=6.
\]

This is a concrete arithmetic holonomy: the `C2` endomorphism character and `C3` 2-torsion permutation are independent typed carriers and may not be collapsed into one Boolean assertion that the reduction splits after extension.

## 5. Boundaries

- The canonical Weil-restriction principal polarization is decomposable; this does not classify all principal polarizations in the isogeny class.
- The cubic statement concerns pullback equality with the Prym polarization, not an arbitrary higher-degree isogeny to a principally polarized variety.
- Degree-six simultaneous strictification does not make the characteristic-zero Prym polarization principal.
- No axiom candidate is reopened and P000 is unchanged.

Classification: `DERIVED_TRACE_TRANSFER / EXACT_POLARIZATION_DESCENT_OBSTRUCTION / ARITHMETIC_HOLONOMY_C2_C3 / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Inside

\[
\operatorname{End}^0_{\overline{\mathbf F}_7}(P_{46,7})\simeq M_2(F),
\]

identify the Rosati-hermitian matrix of the specialized Prym polarization, enumerate the three cubic-field principal quotients, and determine whether any becomes isomorphic to the product/Weil-restriction polarization over `F_{7^6}`. Frobenius polynomials alone cannot decide this integral lattice problem.
