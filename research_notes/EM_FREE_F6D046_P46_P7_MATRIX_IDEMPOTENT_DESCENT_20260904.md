# Matrix idempotents, Frobenius descent, and a non-automorphic Tate correspondence

Status: `FREE_RESEARCH / DERIVED EXACT ENDOMORPHISM-DESCENT THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R61-MATRIX-IDEMPOTENT-SPLITTING / R62-FROBENIUS-SWAP-DESCENT / R63-HERMITIAN-SIMILITUDE-MODEL / R64-NONAUTOMORPHIC-TATE-CORRESPONDENCE`.

## 1. Endomorphism-algebra jump

Let

\[
h(T)=T^4+5T^3+245T+2401
\]

and let \(F=\mathbf Q(\alpha)\), \(h(\alpha)=0\). The irreducibility of

\[
f_7(X)=h(X^2)
\]

shows that \(\alpha\) is not a square in \(F\). Put

\[
L=F(u),\qquad u^2=\alpha.
\]

Then \([L:F]=2\), \([L:\mathbf Q]=8\), and the finite-field endomorphism algebras are

\[
\boxed{\operatorname{End}^0_{\mathbf F_7}(P_{46,7})=L=\mathbf Q(\pi_7),}
\]

\[
\boxed{\operatorname{End}^0_{\mathbf F_{49}}(P_{46,7})=M_2(F).}
\]

The first is a field, so the reduction is simple over \(\mathbf F_7\); the second contains rank-one idempotents, giving the square decomposition over \(\mathbf F_{49}\).

## 2. Explicit companion embedding

Embed \(L\) in \(M_2(F)\) by

\[
u\longmapsto
J=\begin{pmatrix}0&\alpha\\1&0\end{pmatrix},
\qquad J^2=\alpha I.
\]

The centralizer is

\[
\boxed{
\operatorname{Cent}_{M_2(F)}(J)
=
\left\{
\begin{pmatrix}a&\alpha b\\b&a\end{pmatrix}:a,b\in F
\right\}
=F[J]\simeq L.
}
\]

Take the orthogonal coordinate idempotents

\[
e_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
e_1=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]

They satisfy

\[
e_i^2=e_i,\qquad e_0e_1=0,\qquad e_0+e_1=I,
\]

and

\[
\boxed{Je_0J^{-1}=e_1,\qquad Je_1J^{-1}=e_0.}
\]

Thus the two \(B\)-factors are exchanged by the quadratic descent action. A descent-invariant idempotent would commute with \(J\), but the fixed algebra \(F[J]\) is a field and hence has only the idempotents \(0,1\). This gives a direct matrix proof of

\[
\boxed{\text{the }B^2\text{ splitting exists over }\mathbf F_{49}\text{ and does not descend to }\mathbf F_7.}
\]

## 3. Hermitian similitude model

Let the CM involution on \(F\) be complex conjugation, so \(\bar\alpha=49/\alpha\). With

\[
H_0=\begin{pmatrix}1&0\\0&7\end{pmatrix},
\]

one has the exact Frobenius-similitude identity

\[
\boxed{\bar J^{\mathsf t}H_0J=7H_0.}
\]

Both \(e_0,e_1\) are self-adjoint for the corresponding rational Rosati involution. Thus the decomposition is orthogonal after the quadratic base change in this rational isogeny frame.

More generally, every Hermitian matrix in this frame satisfying the same descent equation has the form

\[
H=\begin{pmatrix}a&b\\\bar b&7a\end{pmatrix},
\qquad a\in F^+,
\qquad \alpha\bar b=7b.
\]

Since \(b_0=\alpha+7\) is a nonzero solution, the off-diagonal solutions are

\[
b=c(\alpha+7),\qquad c\in F^+.
\]

Hence the rational polarization problem is a one-parameter Hermitian family over \(F^+=\mathbf Q(\sqrt{417})\). The integral Prym lattice and its type \((1,1,1,2)\) select a discrete point inside this family; Frobenius polynomials do not determine that integral selection.

## 4. Non-automorphic algebraic correspondence

Tate's theorem identifies rational homomorphisms of finite-field abelian varieties with the Frobenius-equivariant Tate-module homomorphisms. Consequently the rank-one matrix idempotents \(e_0,e_1\) are represented by algebraic endomorphism correspondences after base change to \(\mathbf F_{49}\).

Composing a projector with the Prym inclusion into \(J(C_{46})\) and an isogeny from its image to \(J(C_7)\) gives a rational algebraic correspondence between \(C_{46,\mathbf F_{49}}\) and the explicit genus-two curve \(C_7\). R60 proves that this correspondence does not arise from any curve automorphism.

The matrix formula is explicit at the semisimple isogeny-category level. It does not yet give a low-bidegree equation for a divisor in \(C_{46}\times C_7\), and it is noncanonical up to conjugation by \(\operatorname{GL}_2(F)\).

## 5. Classification

`DERIVED_ENDOMORPHISM_DESCENT / EXPLICIT_EXCHANGED_IDEMPOTENTS / NONAUTOMORPHIC_TATE_CORRESPONDENCE / INTEGRAL_POLARIZATION_OPEN / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Determine the integral Hermitian lattice representing the specialized Prym polarization inside this companion frame. Its off-diagonal parameter and local elementary divisors at \(2\) will decide how the three cubic-field principal quotients sit relative to the two Frobenius-exchanged factors.
