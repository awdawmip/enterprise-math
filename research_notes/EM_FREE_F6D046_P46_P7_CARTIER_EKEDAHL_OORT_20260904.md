# Explicit Prym Cartier operator and Ekedahl--Oort type at p=7

Status: `FREE_RESEARCH / DERIVED EXACT DIEUDONNE-BT1 CLASSIFICATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R70-P7-PRYM-CARTIER-MATRIX / R71-P7-A-NUMBER / R72-P7-EKEDAHL-OORT-TYPE`.

## 1. Cyclic quartic model and differential basis

Modulo seven,

\[
E:y^2=x^3+x^2+1,
\qquad
n^2=y(x^2+2).
\]

Eliminating \(y\) gives the tame cyclic quartic model

\[
\boxed{n^4=F(x):=(x^3+x^2+1)(x^2+2)^2.}
\]

Put \(D=x^2+2\). From the double-cover line-bundle description, the anti-invariant Prym differentials have basis

\[
\boxed{
u=\frac{dx}{n},
\qquad
v_k=\frac{x^kD\,dx}{n^3},\quad k=0,1,2.
}
\]

The invariant elliptic differential is \(D\,dx/n^2=dx/y\).

## 2. Cartier extraction rule

For a polynomial \(P(x)=\sum a_jx^j\) over \(\mathbf F_7\),

\[
\mathcal C(P(x)dx)=\sum_{m\ge0}a_{7m+6}x^m dx.
\]

Since

\[
n^{-1}=(n^{-3})^7F^5,
\qquad
n^{-3}=(n^{-1})^7F,
\]

Cartier exchanges the order-four character spaces \(j=1\) and \(j=3\), as required by the inert Frobenius action.

Exact coefficient extraction gives

\[
\mathcal C(F^5dx)
=(6+4x+6x^2+2x^3+5x^4)dx
=(3+2x+5x^2)D\,dx,
\]

and the coefficient of \(x^6\) in \(x^kDF\) is respectively

\[
0,5,4\qquad(k=0,1,2).
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal C(u)&=3v_0+2v_1+5v_2,\\
\mathcal C(v_0)&=0,\\
\mathcal C(v_1)&=5u,\\
\mathcal C(v_2)&=4u.
\end{aligned}}
\]

In the ordered basis \((u,v_0,v_1,v_2)\), using images as columns,

\[
\boxed{
C_P=
\begin{pmatrix}
0&0&5&4\\
3&0&0&0\\
2&0&0&0\\
5&0&0&0
\end{pmatrix}.
}
\]

## 3. Rank, stable image, and a-number

Let

\[
L=3v_0+2v_1+5v_2.
\]

Then

\[
\mathcal C(u)=L,
\qquad
\mathcal C(L)=2u.
\]

Thus the stable Cartier image is

\[
\langle u,L\rangle,
\]

and Cartier is invertible on it. Meanwhile

\[
\ker\mathcal C
=\langle v_0,\,2v_1+v_2\rangle.
\]

Consequently

\[
\boxed{\operatorname{rank}C_P=\operatorname{stable\ rank}C_P=2,}
\]

\[
\boxed{f(P_{46,7})=2,\qquad a(P_{46,7})=2.}
\]

The elliptic invariant block is ordinary, so

\[
f(J(C_{46,7}))=3,
\qquad a(J(C_{46,7}))=2.
\]

## 4. Ekedahl--Oort final type

For a dimension-four principally quasi-polarized BT1, let the final sequence be

\[
\nu=(\nu_1,\nu_2,\nu_3,\nu_4).
\]

The identities

\[
f=2,
\qquad
a=4-\nu_4=2
\]

force

\[
\nu_1=1,
\quad\nu_2=2,
\quad\nu_3=\nu_4=2.
\]

Hence

\[
\boxed{\nu(P_{46,7})=(1,2,2,2).}
\]

This refines the Newton statement. The Newton polygon \(0^2,(1/2)^4,1^2\) is an isogeny invariant; the Cartier matrix and final type classify the actual level-one integral p-torsion stratum.

## 5. Structural interpretation

The off-diagonal form of \(C_P\) is the differential counterpart of the inert endomorphism character: Frobenius exchanges the \(i\) and \(-i\) Hodge-character spaces of dimensions one and three. The rank-one maps in each direction compose nontrivially, leaving a two-dimensional ordinary stable image and a two-dimensional Cartier kernel.

Classification: `DERIVED_EXPLICIT_CARTIER_MATRIX / P_RANK_2 / A_NUMBER_2 / EO_TYPE_1222 / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Lift the Cartier calculation to the full covariant Dieudonne module with polarization, identify the slope-one-half rank-four lattice, and compare it with the order-two polarization kernel and the order-three principalization torsor.
