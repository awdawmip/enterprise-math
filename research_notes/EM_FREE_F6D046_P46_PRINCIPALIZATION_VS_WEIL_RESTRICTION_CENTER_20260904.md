# Principalized Pryms are not the canonical Weil-restriction ppav

Status: `FREE_RESEARCH / DERIVED EXACT INTEGRAL-CENTER SEPARATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R102-WEIL-RESTRICTION-MAXIMAL-CENTER / R103-PRINCIPALIZATION-CENTER-DROP / R104-INTEGRAL-CENTER-SEPARATION / R105-SMOOTH-JACOBIAN-ROUTE-SEPARATION`.

## 1. Two principally polarized objects in one rational isogeny class

Let

\[
A_{\rm Res}=\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}J(C_7)
\]

with its canonical principal polarization, and let

\[
A_\ell=P_{46,7}/\ell
\]

be any of the three degree-two principal quotients attached to a maximal isotropic line

\[
\ell\subset\ker\lambda_P\simeq\mathbf F_4.
\]

They have the same rational Frobenius polynomial and therefore lie in the same unpolarized \(\mathbf F_7\)-isogeny class. The question is whether they can be isomorphic as abelian varieties or as ppav.

## 2. The canonical Weil restriction has maximal unramified two-adic center

Let \(\mathfrak q_u\) be the unramified prime of the quartic CM field \(F\) over two, so

\[
F_{\mathfrak q_u}=\mathbf Q_2(\sqrt5),
\qquad
\mathcal O_u/2\mathcal O_u\simeq\mathbf F_4.
\]

For the absolutely simple surface \(B/\mathbf F_{49}\), the Frobenius--Verschiebung order \(R=\mathbf Z[\alpha,49/\alpha]\) is already maximal at \(\mathfrak q_u\):

\[
R_{\mathfrak q_u}=\mathcal O_u.
\]

Hence \(T_2(B)_{\mathfrak q_u}\) is a torsion-free rank-one module over the discrete valuation ring \(\mathcal O_u\), and is therefore free. After geometric base change,

\[
A_{\rm Res}\sim B\times B^{(7)},
\]

so the scalar center of its geometric integral endomorphism ring has local component

\[
\boxed{Z(\operatorname{End}_{\overline{\mathbf F}_7}A_{\rm Res})_{\mathfrak q_u}=\mathcal O_u.}
\]

No larger local scalar order exists because \(\mathcal O_u\) is the maximal order of the field.

## 3. Every Prym principalization drops the center by index two

Let \(\Lambda=T_2(P_{46,7})_{\mathfrak q_u}\). The polarization dual lattice satisfies

\[
\Lambda^\#/\Lambda\simeq\ker\lambda_P\simeq\mathcal O_u/2\mathcal O_u.
\]

The quotient by \(\ell\) corresponds to the intermediate self-dual lattice \(M_\ell\) whose image in \(\Lambda^\#/\Lambda\) is \(\ell\). A scalar \(a\in F_{\mathfrak q_u}\) is integral on \(M_\ell\) only if it is integral over \(\mathbf Z_2\), hence \(a\in\mathcal O_u\). Within \(\mathcal O_u\), it preserves \(M_\ell\) exactly when its residue preserves the line \(\ell\).

The scalar stabilizer of any \(\mathbf F_2\)-line in the one-dimensional \(\mathbf F_4\)-space is \(\mathbf F_2\). Therefore

\[
\boxed{
Z(\operatorname{End}_{\overline{\mathbf F}_7}A_\ell)_{\mathfrak q_u}
=
\mathcal O(\ell)
=\mathbf Z_2+2\mathcal O_u,
}
\]

and

\[
\boxed{[\mathcal O_u:\mathcal O(\ell)]=2.}
\]

This is an equality, not merely a guaranteed suborder: the local center of the multiplier ring is precisely the scalar multiplier ring of \(M_\ell\).

## 4. Integral-center separation

An isomorphism of abelian varieties over the algebraic closure conjugates their integral endomorphism rings and hence identifies their centers. But the local center orders above two are different:

\[
\mathcal O_u
\ne
\mathbf Z_2+2\mathcal O_u.
\]

Consequently, for every principalization line \(\ell\),

\[
\boxed{A_\ell\not\simeq A_{\rm Res}}
\]

already as unpolarized abelian varieties over \(\overline{\mathbf F}_7\), and a fortiori not as principally polarized varieties.

Thus the explicit compact-type stable Jacobian on the boundary \(\Delta_2\) supplied by the canonical Weil-restriction polarization is not one of the three Prym principalizations.

## 5. Consequence for the smooth genus-four Jacobian question

If one of the three \(A_\ell\) is a smooth genus-four Jacobian, it must represent a genuinely different principally polarized object in the same rational isogeny class. It cannot be obtained merely by relabeling the canonical product/Weil-restriction polarization.

The present theorem does not decide whether an \(A_\ell\) lies in the smooth Jacobian locus. It separates that question from the already known \(\Delta_2\) boundary point and proves that the two routes have distinct integral centers.

Classification: `DERIVED_INTEGRAL_CENTER_SEPARATION / PRINCIPALIZATION_NOT_CANONICAL_WEIL_RESTRICTION / JACOBIAN_ROUTE_SEPARATED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Distinguish the three \(A_\ell\) from one another under the full non-scalar polarized automorphism group of the rank-two Hermitian lattice, and then test their theta divisors for geometric indecomposability.
