# Cartier unit-root matching and the exact p-torsion BT1 decomposition

Status: `FREE_RESEARCH / DERIVED EXACT INTEGRAL-COMPATIBILITY THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R73-CARTIER-UNIT-ROOT-MATCH / R74-PRYM-BT1-DECOMPOSITION / R75-FULL-JACOBIAN-BT1`.

## 1. Prym Cartier characteristic polynomial

For the Cartier matrix

\[
C_P=
\begin{pmatrix}
0&0&5&4\\
3&0&0&0\\
2&0&0&0\\
5&0&0&0
\end{pmatrix}
\]

over \(\mathbf F_7\), one has

\[
\boxed{\det(TI-C_P)=T^2(T^2-2).}
\]

The stable image is two-dimensional and Cartier acts there with polynomial \(T^2-2=(T-3)(T-4)\).

On the other hand,

\[
f_7(X)=X^8+5X^6+245X^2+2401
\]

reduces modulo seven to

\[
\boxed{f_7(X)\equiv X^6(X^2-2).}
\]

Thus the nonzero Cartier polynomial is exactly the unit-root factor of the Frobenius characteristic polynomial.

## 2. Elliptic invariant block

For

\[
E:y^2=x^3+x^2+1,
\]

the Hasse--Witt scalar is the coefficient of \(x^6\) in \((x^3+x^2+1)^3\), namely

\[
\boxed{4.}
\]

The elliptic Frobenius polynomial is

\[
X^2+3X+7\equiv X(X-4)\pmod7,
\]

so its unit root also matches the Cartier eigenvalue.

Consequently the full genus-five Cartier characteristic polynomial is

\[
\boxed{T^2(T^2-2)(T-4),}
\]

and the unit-root factor of the full Jacobian Frobenius polynomial is

\[
(X^2-2)(X-4).
\]

## 3. Exact BT1 type of the Prym

The specialized Prym polarization has degree four, prime to seven, so it induces a principal quasi-polarization on the 7-divisible group. The final type

\[
(1,2,2,2)
\]

classifies its BT1 over \(\overline{\mathbf F}_7\).

Let

\[
L=\mu_7\oplus\mathbf Z/7\mathbf Z
\]

be the ordinary elliptic BT1 and let \(I_{1,1}\) be the local-local BT1 of a supersingular elliptic curve. The product

\[
L^2\oplus I_{1,1}^2
\]

has dimension four, p-rank two, a-number two and the same final type. By the Ekedahl--Oort classification,

\[
\boxed{P_{46,7}[7]\simeq L^2\oplus I_{1,1}^2}
\]

as principally quasi-polarized BT1 group schemes over the algebraic closure.

This is an integral level-one statement, stronger than the Newton-isocrystal decomposition.

## 4. Full Jacobian

The elliptic quotient contributes one further ordinary elliptic BT1. Since the degree-two Prym/elliptic isogeny is prime to seven, the 7-divisible decomposition is integral. Therefore

\[
\boxed{J(C_{46,7})[7]\simeq L^3\oplus I_{1,1}^2.}
\]

Hence

\[
f(J(C_{46,7}))=3,
\qquad
a(J(C_{46,7}))=2.
\]

## 5. Boundary

The BT1 decomposition does not determine the complete 7-divisible group with all integral extension data, nor the prime-to-seven polarization lattice at the exceptional prime two. It does show that the middle slope-one-half part is already superspecial at level one.

Classification: `DERIVED_CARTIER_UNIT_ROOT_MATCH / EXACT_PRYM_BT1 / EO_TYPE_1222 / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Determine whether the full slope-one-half p-divisible subgroup is the split product of two supersingular elliptic p-divisible groups or a nontrivial integral extension with the same BT1 and isocrystal; then compare its endomorphism order with the completion of \(M_2(F)\) at the degree-two prime above seven.
