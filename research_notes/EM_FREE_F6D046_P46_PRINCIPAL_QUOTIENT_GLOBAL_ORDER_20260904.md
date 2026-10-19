# The global scalar order shared by the three principal quotients

Status: `FREE_RESEARCH / DERIVED EXACT ORDER-AND-DISCRIMINANT THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R89-EXPLICIT-LINE-STABILIZER-ORDER / R90-INDEX-28 / R91-ORDER-DISCRIMINANT / R92-THREE-QUOTIENT-ORDER-BLINDNESS`.

## 1. Frobenius order basis

Let

\[
R=\mathbf Z[\alpha,\bar\alpha]
=\mathbf Z[x,\alpha],
\qquad x=\alpha+\bar\alpha,
\]

with

\[
x^2+5x-98=0,
\qquad
\alpha^2-x\alpha+49=0.
\]

Then

\[
\boxed{R=\mathbf Z\langle1,x,\alpha,x\alpha\rangle.}
\]

At the unramified prime above two, \(x\equiv1\) and \(\alpha\) generates \(\mathbf F_4/\mathbf F_2\). For

\[
r=a+bx+c\alpha+dx\alpha,
\]

the residue is

\[
(a+b)+(c+d)\alpha\in\mathbf F_4.
\]

It preserves any chosen \(\mathbf F_2\)-line in the one-dimensional \(\mathbf F_4\)-kernel exactly when its residue lies in \(\mathbf F_2\), equivalently

\[
c+d\equiv0\pmod2.
\]

## 2. Explicit global suborder

The line-stabilizer order is therefore

\[
\boxed{
R_{\mathrm{pr}}
=
\mathbf Z\langle
1,
 x,
 \alpha(1+x),
 2x\alpha
\rangle.
}
\]

Indeed, an integral combination of the last two generators has \(\alpha,x\alpha\)-coefficients \((m,m+2n)\), whose sum is even; conversely every pair \((c,d)\) of equal parity is of this form.

Hence

\[
\boxed{[R:R_{\mathrm{pr}}]=2.}
\]

Since \([\mathcal O_F:R]=14\),

\[
\boxed{[\mathcal O_F:R_{\mathrm{pr}}]=28.}
\]

## 3. Discriminant

The maximal order has

\[
\operatorname{disc}(\mathcal O_F)=2^3 3^3 139^2.
\]

Therefore

\[
\operatorname{disc}(R)
=14^2\operatorname{disc}(\mathcal O_F)
=2^5 3^3 7^2 139^2,
\]

and

\[
\boxed{
\operatorname{disc}(R_{\mathrm{pr}})
=28^2\operatorname{disc}(\mathcal O_F)
=2^7 3^3 7^2 139^2.
}
\]

The order is stable under CM conjugation. Explicitly,

\[
\overline{\alpha(1+x)}=98-4x-\alpha(1+x),
\]

\[
\overline{2x\alpha}=196-10x-2x\alpha.
\]

## 4. Why all three lines give the same order

For any nonzero \(v\in\mathbf F_4\), the scalar stabilizer of the \(\mathbf F_2\)-line \(\mathbf F_2v\) is \(\mathbf F_2\). Thus the preimage stabilizer ring is independent of which of the three lines is chosen.

Consequently all three degree-two principal quotients inherit the same scalar order \(R_{\mathrm{pr}}\). Their cubic torsor distinction survives only in the integral module/isogeny data, not in this commutative order:

\[
\boxed{
\text{same scalar endomorphism order}
\ne
\text{same principal quotient or polarization class}.
}
\]

The full geometric rational endomorphism algebra remains \(M_2(F)\); \(R_{\mathrm{pr}}\) records only the guaranteed scalar integral endomorphisms descending through the chosen kernel line.

## 5. Classification

`DERIVED_GLOBAL_PRINCIPALIZATION_ORDER / INDEX_28 / DISCRIMINANT_CERTIFICATE / ORDER_BLIND_TO_C3_TORSOR / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Classify rank-two projective modules over \(R_{\mathrm{pr}}\) carrying unimodular positive Hermitian forms. The three Frobenius-cyclic quotients must occur as distinct module/polarization classes inside that common order.
