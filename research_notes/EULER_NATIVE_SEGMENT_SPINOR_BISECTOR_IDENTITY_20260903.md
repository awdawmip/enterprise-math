# Native Pythagorean segment as the spinor square root of its Euler rotation character

Status: `FREE_RESEARCH / EXACT ALGEBRAIC BRIDGE / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Exact bridge

Work in the derived two-component algebra

\[
A_J=\mathbf R[J]/(J^2+1).
\]

This algebra is already used as a sector-local component marker for the native Pythagorean law. It is not identified with the classical carrier plane.

For a nonzero native component pair `(a,b)`, let

\[
n=a^2+b^2,
\qquad
v=a+bJ.
\]

Define its normalized spinor

\[
S[a:b]=\frac{a+bJ}{\sqrt{a^2+b^2}}
\]

and its projective rotation character

\[
\mathcal C[a:b]
=
\frac{(a^2-b^2)+2abJ}{a^2+b^2}.
\]

Then exactly

\[
\boxed{\mathcal C[a:b]=S[a:b]^2}.
\]

The rotation phase is therefore the square of the normalized line-segment component state. The segment direction is a spinor coordinate: it carries half the character phase.

## 2. The normalized adjacency bisector recovers the segment

Assume `a>0`. Then

\[
1+\mathcal C[a:b]
=
\frac{2a(a+bJ)}{a^2+b^2},
\]

and

\[
2+\mathcal C[a:b]+\mathcal C[a:b]^{-1}
=
\frac{4a^2}{a^2+b^2}.
\]

Hence the forward normalized-bisector map

\[
\beta(U)=
\frac{1+U}{\sqrt{2+U+U^{-1}}}
\]

satisfies

\[
\boxed{
\beta(\mathcal C[a:b])
=
S[a:b].
}
\]

Thus the same operation that generates the dyadic Euler/Viète root tower is not an imported angle-halving instruction. On a Pythagorean segment character, it literally recovers the normalized underlying segment.

## 3. The singular endpoint and chirality

At `[a:b]=[0:1]`,

\[
\mathcal C[0:1]=-1.
\]

The formula for `beta` is singular because `1+(-1)=0`. Nevertheless its two square roots are

\[
\pm J.
\]

Choosing the orientation of the native sector or of the directed gate cycle selects one of them. After that first chirality choice, all later forward roots have positive scalar coordinate and are uniquely selected by `beta`.

Therefore:

\[
\boxed{
\text{the only irreducible branch choice in the Euler root tower is the sign of the first square root of reversal}.
}
\]

## 4. Three distinguished projective segment states

The exact character values are

\[
\mathcal C[1:0]=1,
\qquad
\mathcal C[1:1]=J,
\qquad
\mathcal C[0:1]=-1.
\]

So within one native Pythagorean sector:

- the first boundary axis reads as the identity character;
- the balanced component line reads as the quarter-turn character `J`;
- the second boundary axis reads as the half-turn character `-1`.

This does **not** say that the 120-degree carrier opening is a classical 180-degree physical angle. It says that the projective spinor character doubles the native component-direction parameter. The character phase and the carrier drawing are different typed objects.

Consequently the balanced trace `[1:1]`, whose native length is `sqrt(2)` and whose path fiber has two representatives, has a distinguished Euler role:

\[
\boxed{
\text{balanced native segment}
\longmapsto
\text{quarter-turn character }i.
}
\]

## 5. Rational Cayley coordinate

For `a != 0`, put

\[
t=\frac ba.
\]

Then

\[
\mathcal C(t)
=
\frac{1-t^2+2tJ}{1+t^2}.
\]

Composition is rational:

\[
\mathcal C(t)\mathcal C(u)
=
\mathcal C\!\left(\frac{t+u}{1-tu}\right)
\]

when `tu != 1`, with the projective point at infinity handling the remaining case.

The continuous exponential is therefore downstream of an exact projective composition calculus. Under the standard analytic decoder,

\[
t=\tan(\theta/2),
\qquad
\mathcal C(t)=e^{J\theta},
\]

but inverse trigonometry is not needed to define the finite algebra.

## 6. Pell residuals become segment half-phase defects

If

\[
P^2-DQ^2=-1,
\]

then the normalized near-axis segment `(P,1)` has length `Q sqrt(D)` and Cayley/half-phase coordinate

\[
\frac1{P+Q\sqrt D}
=Q\sqrt D-P.
\]

Thus the familiar Ramanujan factors

\[
\sqrt2-1,
\qquad
13\sqrt{29}-70,
\qquad
13\sqrt{58}-99
\]

are all the same typed object: positive segment half-phase defects in different quadratic shells.

## 7. Consequence for Euler's formula

The finite causal chain is now

```text
native component segment (a,b)
    -> normalized spinor S[a:b]
    -> projective rotation character C[a:b] = S[a:b]^2
    -> exact Cayley composition
    -> normalized adjacency bisectors / compatible root tower
    -> unit-speed continuous completion
    -> exp(theta J) = cos(theta) + J sin(theta).
```

The complex exponential does not create line-segment rotation. It is the continuous multiplicative decoder of a projective segment-spinor calculus already present in the finite Pythagorean component algebra.

Freeze candidate:

`AC-EM-FREE-F6D046-NATIVE-SEGMENT-SPINOR-EULER-BRIDGE-V1`:

> A nonzero native Pythagorean component pair is naturally a spinor for its derived rotation character: the normalized segment squares to the character, and the normalized adjacency-bisector operation recovers that segment from the character. The balanced component line maps to the quarter-turn character, while the two sector boundaries map to identity and reversal.

Boundary:

`SPINOR_CHARACTER_DOUBLE_COVER != CARRIER_ANGLE_IDENTITY`.

`J_COMPONENT_MARKER != PRIMITIVE_NATIVE_SPATIAL_AXIS`.
