# Oriented rational BRC rotation chart and its spectral projective quotient

Status: `FREE_RESEARCH / CROSS-LINE ALGEBRAIC CHART THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Primary issue: `#1159`
Cross-line target: BRC coordinate-to-algebra interface.

## 1. A two-dimensional rotation algebra

Let `K` be a characteristic-zero field and introduce a symbol `J` with

\[
J^2=-1.
\]

The commutative quadratic algebra

\[
\mathcal A=K[J]/(J^2+1)
\]

has the faithful `2x2` representation

\[
\boxed{
A(a,b)=
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix}.
}
\tag{RC-1}
\]

Matrix multiplication is exactly

\[
\boxed{
A(a,b)A(c,d)
=A(ac-bd,ad+bc).
}
\tag{RC-2}
\]

This is ordinary commutative algebra.  No angle, sine, cosine, or Euclidean metric is required.

---

## 2. Projective affine chart and rational composition

Work projectively, so a common nonzero scalar multiple of `(a,b)` represents the same projective transfer direction.

On the chart `a != 0`, define

\[
\boxed{z=b/a.}
\tag{RC-3}
\]

For two chart values `z,w`, (RC-2) gives

\[
\boxed{
z\oplus w
=\frac{z+w}{1-zw},
}
\tag{RC-4}
\]

whenever `1-zw != 0` in this affine chart.

The apparent pole is a chart boundary, not a failure of the homogeneous pair `(a,b)`.  When `a=0` one uses the reciprocal projective chart instead of deleting the state.

Thus the homogeneous pair is globally algebraic, while `z` is one rational atlas coordinate.

---

## 3. BRC transfer interpretation

The current BRC finite-state lift turns declared path/frame systems into ordinary commutative transfer matrices over rational-function coefficient fields.  If a Schur-reduced boundary module lands in the subalgebra (RC-1), then its serial composition is represented exactly by (RC-2), and its affine coordinate composes by (RC-4).

This gives a concrete coordinate-to-algebra bridge:

`serial module composition -> rational coordinate law`.

Hard boundary: no claim is made that every BRC module or every P000 rotation lies in this one-dimensional quadratic subalgebra.  It is a declared rotation-sector chart.

---

## 4. The projective spectral trace defect is the unoriented quotient

For `A(a,b)`,

\[
\operatorname{tr}A=2a,
\qquad
\det A=a^2+b^2.
\]

The projective trace-defect observable from the #1159/BRC bridge is

\[
u_{\rm pr}(A)
=4-\frac{(\operatorname{tr}A)^2}{\det A}.
\]

Therefore

\[
\boxed{
u_{\rm pr}(A)=\frac{4b^2}{a^2+b^2}.}
\tag{RC-5}
\]

In the affine coordinate `z=b/a`,

\[
\boxed{
u=\frac{4z^2}{1+z^2}.}
\tag{RC-6}
\]

Thus the projective spectral coordinate forgets precisely the sign sheet

\[
z\leftrightarrow -z.
\]

It is an unoriented quadratic quotient of the rational rotation chart.

---

## 5. Integer repetition descends to spectral decimation

Let

\[
z^{\oplus n}
\]

denote the `n`-fold rational composition (RC-4), equivalently the projective coordinate of `A(a,b)^n`.

The general projective-trace theorem gives

\[
\boxed{
\frac{4(z^{\oplus n})^2}{1+(z^{\oplus n})^2}
=R_n\!\left(\frac{4z^2}{1+z^2}\right).
}
\tag{RC-7}
\]

So the integer spectral decimation polynomial is exactly the quotient of the rational oriented repetition law by the sign-sheet involution.

This is a finite algebraic identity, not a trigonometric multiple-angle input.

---

## 6. Formal group logarithm of the oriented chart

The rational law

\[
z\oplus w=(z+w)/(1-zw)
\]

has invariant differential

\[
\boxed{
\omega=\frac{dz}{1+z^2}.
}
\tag{RC-8}
\]

Indeed direct differentiation of left/right translation preserves `omega`.

Define the unique normalized formal group logarithm

\[
\boxed{
\lambda(z)
=\int_0^z\frac{ds}{1+s^2}
=z-\frac{z^3}{3}+\frac{z^5}{5}-\cdots.
}
\tag{RC-9}
\]

This is a formal power series definition; the later classical name `arctan` is not required.

Then

\[
\boxed{
\lambda(z\oplus w)
=\lambda(z)+\lambda(w),
}
\tag{RC-10}
\]

and in particular

\[
\lambda(z^{\oplus n})=n\lambda(z).
\]

So the oriented coordinate has an additive formal phase.

---

## 7. Recovering the #1159 formal phase

From (RC-6),

\[
u=\frac{4z^2}{1+z^2}.
\]

A direct differential calculation gives

\[
\boxed{
\frac{du^2}{u(4-u)}
=4\frac{dz^2}{(1+z^2)^2}
=4d\lambda(z)^2.
}
\tag{RC-11}
\]

Therefore the unoriented #1159 formal phase is

\[
\boxed{
\ell(u)=4\lambda(z)^2,
\qquad
u=\frac{4z^2}{1+z^2}.
}
\tag{RC-12}
\]

Because `lambda(z^{oplus n})=n lambda(z)`, equation (RC-12) immediately gives

\[
\ell(R_n(u))=n^2\ell(u).
\]

Thus the common spectral formal phase is the square of the oriented BRC formal-group logarithm.

---

## 8. Why the frame/sheet is material

The scalar `u` cannot distinguish `z` from `-z`.  Yet under arbitrary composition,

\[
(z\oplus w)
\neq
((-z)\oplus w)
\]

in general.

Therefore forgetting the sign sheet before arbitrary serial composition is not operation safe.

Concrete matrix counterexample to a more general scalar-only quotient:

- `A=I` and `A'=[[1,1],[0,1]]` both have projective trace defect zero;
- `B=[[1,0],[1,1]]` also has projective defect zero;
- but `AB=B` still has defect zero, while
  `A'B=[[2,1],[1,1]]` has projective defect `4-9=-5`.

So projective trace defect alone is **not** a congruence for arbitrary multiplication of general `2x2` transfers.

Inside the declared rotation subalgebra (RC-1), retaining the oriented chart/homogeneous pair restores exact rational composition.

This is precisely consistent with the current BRC requirement to retain frame/orientation data rather than infer it back from a scalar summary.

---

## 9. Algebraic atlas interpretation

The rotation-sector coordinate atlas is now entirely algebraic:

```text
homogeneous state [a:b]
  -> global projective chart, no affine pole loss

local affine chart z=b/a
  -> z⊕w=(z+w)/(1-zw)

formal oriented phase lambda(z)
  -> additive under composition

unoriented quotient u=4z^2/(1+z^2)
  -> polynomial decimation R_n under repetition

formal spectral phase ell(u)=4 lambda(z)^2
  -> ell(R_n)=n^2 ell
```

This realizes, in one exact transfer sector, the user-requested principle that the algebra itself should display coordinate composition.

---

## 10. Relation to current BRC work

For the current Schur-module elimination task, a useful exact contract is:

1. retain boundary frame/port variables through elimination;
2. test whether the reduced `2x2` transfer lies in or is conjugate to the declared quadratic rotation subalgebra;
3. if yes, extract homogeneous `(a,b)` or affine `z` without numerical roots;
4. verify direct graph composition and port-composed transfer agree under the rational law (RC-2)/(RC-4);
5. only then apply the projective quotient `u` when the requested observation is orientation-insensitive;
6. compile root blocks in `z` or `u` according to the observation contract, not by silently collapsing the sheet.

Freeze at free-research strength:

`ORIENTED_BRC_ROTATION_CHART = RATIONAL_FORMAL_GROUP`.

`SPECTRAL_DECIMATION = UNORIENTED_PROJECTIVE_QUOTIENT_OF_RATIONAL_ROTATION_COMPOSITION`.

`FORMAL_SPECTRAL_PHASE = SQUARE_OF_ORIENTED_FORMAL_GROUP_LOGARITHM`.
