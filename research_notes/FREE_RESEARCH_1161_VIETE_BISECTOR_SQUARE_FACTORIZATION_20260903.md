# Free Research #1161 — Viète-bisector square factorization of the AGM update

Status: `FREE_RESEARCH_RESULT / CROSS-FAMILY EXACT FACTORIZATION / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Cross-family source: `#1158`, finite normalized equal-endpoint bisector theorem

## 1. Input cone state

Use the exact #1161 cone variables

\[
H=a+b,\qquad U=a-b,\qquad V=2\sqrt{ab},
\]

with positive AGM state `a>b>0`, so

\[
H^2=U^2+V^2.
\]

Normalize the cone direction by

\[
v=(r,s):=(V/H,U/H).
\]

Then

\[
r^2+s^2=1,
\qquad r>0,
\qquad s>0.
\]

## 2. Apply the finite Viète bisector

The #1158 finite orientation theorem defines, for `r>-1`,

\[
B(v)=(C,S)
:=
\frac{(1+r,s)}{\sqrt{2(1+r)}}.
\]

It satisfies

\[
C^2+S^2=1,
\]

and explicitly

\[
\boxed{C^2=\frac{1+r}{2}},
\qquad
\boxed{S^2=\frac{1-r}{2}}.
\]

No target pi value or classical circle circumference is used in this construction.

## 3. AGM pair update as complementary quadratic channels

The Gauss–Legendre pair update is

\[
a^+=\frac{a+b}{2}=\frac H2,
\qquad
b^+=\sqrt{ab}=\frac V2=\frac{Hr}{2}.
\]

Because

\[
C^2+S^2=1,
\qquad
C^2-S^2=r,
\]

one obtains the exact factorization

\[
\boxed{
a^+=\frac H2(C^2+S^2),
\qquad
b^+=\frac H2(C^2-S^2).
}
\]

Thus the arithmetic and geometric means are not two unrelated operations after the normalized bisector state is formed. They are the two complementary even quadratic readouts

\[
Q_+(C,S)=C^2+S^2,
\qquad
Q_-(C,S)=C^2-S^2
\]

of one finite bisector state.

This directly answers the #1161 mother question at derived finite-algebraic strength:

`ARITHMETIC_CHANNEL = BISector quadratic sum`,

`GEOMETRIC_CHANNEL = BISector quadratic difference`.

The word `bisector` here refers to the #1158 finite normalized equal-endpoint resultant theorem, not an imported classical half-angle formula.

## 4. Componentwise square gives the next hypotenuse/gap coordinates

For the next AGM pair, define

\[
H^+=a^++b^+,
\qquad
U^+=a^+-b^+.
\]

Using the quadratic-channel formulas,

\[
\boxed{
H^+=HC^2,
\qquad
U^+=HS^2.
}
\]

Therefore the normalized next shape defect is

\[
\boxed{
s^+:=\frac{U^+}{H^+}
=\left(\frac SC\right)^2.
}
\]

The full update factors as

\[
\boxed{
\text{finite bisector}
\to
(C,S)
\to
(C^2,S^2)
\to
\text{next cone state}.
}
\]

This is the exact source of the superattracting quadratic shape contraction.

## 5. Chord-loss coordinate is the squared transverse bisector coordinate

The #1161 chord-loss coordinate was defined by

\[
\ell=\frac{1-r}{2}.
\]

The bisector identity gives immediately

\[
\boxed{\ell=S^2}.
\]

Hence

\[
\boxed{
\frac{H^+}{H}=C^2=1-\ell,
\qquad
s^+=\frac{S^2}{C^2}=\frac{\ell}{1-\ell}.
}
\]

So `chord loss` is not an independently invented scalar: after the cross-family comparison it is exactly the transverse energy/square of the finite Viète bisector state.

## 6. Pythagorean cone completion

The remaining next cone leg is

\[
V^+=2\sqrt{a^+b^+}=\sqrt{HV}.
\]

Since

\[
C^4-S^4=(C^2-S^2)(C^2+S^2)=r,
\]

we have

\[
\boxed{
V^+=H\sqrt{C^4-S^4}.
}
\]

Therefore the entire cone update can be written

\[
\boxed{
(H^+,U^+,V^+)
=H\left(C^2,S^2,\sqrt{C^4-S^4}\right).
}
\]

The cone invariant follows immediately:

\[
(H^+)^2-(U^+)^2
=H^2(C^4-S^4)
=H^2r
=HV
=(V^+)^2.
\]

Thus the update is precisely

`VIETE_BISECTOR -> COMPONENTWISE_SQUARE -> PYTHAGOREAN_CONE_COMPLETION`.

## 7. Why AGM accelerates more strongly than Viète

In the #1158 Viète family, one finite bisector step halves the orientation phase; the scalar chord-versus-arc precision error is second order in that shrinking phase, giving asymptotic quartering of scalar error.

In #1161, the same bisector is followed by **componentwise squaring** before the next shape is read out:

\[
s^+=(S/C)^2.
\]

Near the fixed direction, `S/C` is already first-order small. Squaring it makes the shape map superattracting of order two:

\[
s^+\sim s^2/4.
\]

This cross-family factorization explains structurally why the Gauss–Legendre precision roughly doubles its digit count per iteration while a plain Viète chord refinement has only geometric error contraction.

## 8. Native/derived boundary

This factorization is exact at the finite orientation/cone readout layer, but it does not by itself promote either family to G0/N0 Cell strength.

The #1158 result already records that a canonical Cell-to-orientation quotient is not supplied by current P000/Cell foundations. #1161 additionally requires iterated positive-root/cone completion for an exact scalar state, though finite precision root cells compile to the existing integer-root/precision calculus.

Therefore the current bridge is classified as

`EXACT_G1/G2_CROSS_FAMILY_FACTORIZATION`,

not `N0_NATIVE_ROTATION_DERIVATION`.

## 9. Strongest frozen statement at free-research strength

\[
\boxed{
\text{Gauss--Legendre AGM step}
=
\text{Viète finite bisector}
+
\text{quadratic sum/difference channels}
+
\text{coordinate squaring}
+
\text{Pythagorean cone completion}.
}
\]

In particular:

`ARITHMETIC_MEAN = H/2 * (C^2+S^2)`.

`GEOMETRIC_MEAN = H/2 * (C^2-S^2)`.

`CHORD_LOSS = S^2`.

`NEXT_SCALE_RATIO = C^2`.

`NEXT_SHAPE_DEFECT = (S/C)^2`.

`PI_STAR_EQUALS_CLASSICAL_PI = still analytic completion`.
