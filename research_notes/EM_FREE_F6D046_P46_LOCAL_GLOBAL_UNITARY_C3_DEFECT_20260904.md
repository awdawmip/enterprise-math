# Local-global unitary C3 defect for the three principalizations

Status: `FREE_RESEARCH / DERIVED EXACT LOCAL-GLOBAL DEFECT THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R98-LOCAL-TEICHMULLER-MU3 / R99-LOCAL-UNITARY-TRANSITIVITY / R100-GLOBAL-NORMONE-UNIT-FAILURE / R101-SCALAR-HERMITIAN-GENUS-C3`.

## 1. The local norm-one cubic units

The unramified quadratic two-adic factor

\[
F_{\mathfrak q_u}=\mathbf Q_2(\sqrt5)
\]

is the unique unramified quadratic extension of \(\mathbf Q_2\). It is therefore also isomorphic to \(\mathbf Q_2(\zeta_3)\). Its maximal order contains the Teichmuller lifts

\[
\mu_3=\{1,\zeta_3,\zeta_3^2\},
\qquad
\zeta_3^2+\zeta_3+1=0.
\]

Complex conjugation sends \(\zeta_3\) to \(\zeta_3^{-1}\), so

\[
N_{F_{\mathfrak q_u}/\mathbf Q_2}(\zeta_3)=1.
\]

Reduction identifies

\[
\mu_3\xrightarrow{\sim}\mathbf F_4^{\times}.
\]

Thus the local norm-one unitary scalar group acts simply transitively on

\[
\mathbf P(K_\lambda)=\mathbf F_4^{\times}.
\]

All three maximal isotropic lines are locally equivalent under polarization-preserving scalar units.

## 2. Global norm-one units

R93 proves

\[
\mathcal O_F^{\times}=\mathcal O_{F^+}^{\times},
\qquad
\mu(F)=\{\pm1\}.
\]

A real unit has CM norm \(u\bar u=u^2\). The global integral norm-one scalar units are therefore

\[
\boxed{
U_F(\mathbf Z)
=
\{u\in\mathcal O_F^{\times}:u\bar u=1\}
=\{\pm1\}.
}
\]

Modulo the prime over two, both reduce to \(1\). Consequently the global norm-one scalar group acts trivially on the three principalization lines.

## 3. Exact local-global defect

The local orbit group is

\[
U_F(\mathbf Z_2)\twoheadrightarrow\mathbf F_4^{\times}\simeq C_3,
\]

while the global image is trivial. Hence the scalar unitary local-global defect is

\[
\boxed{
\frac{\operatorname{im}(U_F(\mathbf Z_2)\to\mathbf F_4^{\times})}
     {\operatorname{im}(U_F(\mathbf Z)\to\mathbf F_4^{\times})}
\simeq C_3.
}
\]

This is the unitary form of the ring-class kernel computed in R95. It proves:

- the three line modifications lie in one local scalar-Hermitian genus;
- they are pairwise distinct under global scalar unitary equivalence;
- their failure to globalize is exactly measured by a cyclic order-three defect.

## 4. Relation to arithmetic Frobenius

The reduction of \(\alpha\) is a primitive element of \(\mathbf F_4^{\times}\). Thus arithmetic Frobenius acts on the local genus through the same generator as a Teichmuller cubic unit. The cubic field of definition of the principalizations is the splitting field of this local-global defect.

This does not yet exclude a global non-scalar isometry in the full rank-two unitary group. It proves the strongest possible scalar statement and identifies the precise group that a matrix isometry would have to collapse.

## 5. Classification

`DERIVED_LOCAL_MU3_UNIT_ACTION / LOCAL_UNITARY_TRANSITIVITY / GLOBAL_NORMONE_UNIT_IMAGE_TRIVIAL / C3_LOCAL_GLOBAL_DEFECT / NONSCALAR_ISOMETRY_OPEN / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Compute the reduction image of the full global unitary automorphism group of the rank-two Hermitian lattice, not just its scalar subgroup. If its image misses the local C3, the three principal quotients are globally pairwise nonisomorphic as polarized varieties; if it contains C3, an explicit non-scalar isometry must be constructed.
