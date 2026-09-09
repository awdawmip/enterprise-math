# Full mu-ordinary p-divisible group and local endomorphism matching at seven

Status: `FREE_RESEARCH / DERIVED PEL-DIEUDONNE CLASSIFICATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R76-FULL-MU-ORDINARY-PDIVISIBLE / R77-SUPERSPECIAL-MIDDLE-BLOCK / R78-LOCAL-ENDOMORPHISM-MATCH / R79-COMPLETELY-SLOPE-DIVISIBLE`.

## 1. Unique mu-ordinary object with unitary structure

At \(p=7\),

\[
K_7=\mathbf Q_7(i)
\]

is the unramified quadratic extension of \(\mathbf Q_7\). The specialized \(\mathbf Z[i]\)-action is prime-to-the-discriminant integral, and R67--R72 identify the reduction as the mu-ordinary point of unitary signature \((3,1)\), with final type \((1,2,2,2)\).

The general uniqueness theorem for the mu-ordinary p-divisible group with unramified PEL structure therefore applies: the actual p-divisible group is completely slope divisible and isomorphic, not merely isogenous, to its standard three-block model.

Thus

\[
\boxed{
P_{46,7}[7^\infty]
\simeq X_0\oplus X_{1/2}\oplus X_1,
}
\]

where the heights are \(2,4,2\), the dimensions are \(0,2,2\), and polarization exchanges \(X_0\) with \(X_1\) while making \(X_{1/2}\) self-dual.

## 2. Underlying p-divisible group

Let \(G_{1/2}\) denote the unique supersingular elliptic p-divisible group over \(\overline{\mathbf F}_7\), of height two and dimension one. Forgetting the unitary labels,

\[
\boxed{
P_{46,7}[7^\infty]
\simeq
(\mathbf Q_7/\mathbf Z_7)^2
\oplus G_{1/2}^{\oplus2}
\oplus\mu_{7^\infty}^{\oplus2}.
}
\]

In particular the slope-one-half block is the split superspecial product

\[
\boxed{X_{1/2}\simeq G_{1/2}^{\oplus2},}
\]

not a nontrivial integral extension with the same isocrystal. Truncating to level one recovers

\[
L^2\oplus I_{1,1}^2.
\]

## 3. Completion of the quartic CM field

The exact prime decomposition in the quartic CM field is

\[
7\mathcal O_F=\mathfrak p_0\mathfrak p_{1/2}\mathfrak p_1,
\]

with ramification indices all one and residue degrees \(1,2,1\). Hence

\[
\boxed{F\otimes\mathbf Q_7\simeq\mathbf Q_7\times K_7\times\mathbf Q_7.}
\]

Therefore

\[
M_2(F)\otimes\mathbf Q_7
\simeq
M_2(\mathbf Q_7)\times M_2(K_7)\times M_2(\mathbf Q_7).
\]

The three factors act on the slope-zero, slope-one-half and slope-one blocks respectively.

## 4. Middle-block endomorphism algebra

The rational endomorphism algebra of \(G_{1/2}\) is the quaternion division algebra

\[
D_{1/2}/\mathbf Q_7,
\qquad\operatorname{inv}_7(D_{1/2})=\tfrac12.
\]

Consequently

\[
\operatorname{End}^0(G_{1/2}^{\oplus2})=M_2(D_{1/2}).
\]

The unramified quadratic field \(K_7\) embeds as a maximal subfield of \(D_{1/2}\), whose centralizer is itself. Therefore

\[
\boxed{
\operatorname{Cent}_{M_2(D_{1/2})}(K_7)=M_2(K_7).
}
\]

This is exactly the \(\mathfrak p_{1/2}\)-factor of

\[
\operatorname{End}^0_{\overline{\mathbf F}_7}(P_{46,7})\otimes\mathbf Q_7
=M_2(F)\otimes\mathbf Q_7.
\]

Hence the global Honda--Tate endomorphism algebra, the unitary PEL action, the Newton decomposition and the integral mu-ordinary p-divisible group agree block by block.

## 5. Consequences and boundary

The p-primary integral structure at seven is now fixed up to unique unitary PEL isomorphism. The still-open polarization problem is located at primes over two, because the Prym polarization kernel has order four and the p=7 p-divisible polarization is principal.

Thus the missing Hermitian lattice datum from R65 cannot be recovered by further refinement at seven: its only nontrivial elementary divisors are two-primary.

Classification: `DERIVED_FULL_MU_ORDINARY_PDIVISIBLE / SUPERSPECIAL_MIDDLE_BLOCK / LOCAL_ENDOMORPHISM_MATCH / TWO_PRIMARY_POLARIZATION_FRONTIER / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Compute \(\mathcal O_F\otimes\mathbf Z_2\), the two-primary Hermitian lattice and the Rosati-stable kernel \(E[2]\). This is now the unique local place where the Prym polarization differs from a principal one.
