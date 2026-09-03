# Euler's formula from Cell rotation: finite geometry, segment spinors, and unit-speed completion

Status: `FREE_RESEARCH / SYNTHESIS / FINITE CORE CLOSED / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

This note supersedes the provisional architecture in
`EULER_FORMULA_ROTATION_CHARACTER_GEOMETRY_20260903.md` wherever the two differ.
The earlier note treated endpoint reversal as an explicit external `C2`
augmentation and left the dyadic square-root rule underived. The present theorem
package derives the six-state rotor, the first gate refinement, the chiral
complex structure, and the normalized root rule inside one typed character
construction.

## 1. Final theorem diagram

The completed result is

```text
ordered primitive Cell pair modulo common translation
    -> six oriented neighbor directions C6
    -> quotient by endpoint reversal: three positive-ray classes C3
    -> C3 right-turn representation R
    -> G = I + R, with G^2 = R and G^3 = -I
    -> actual Cell-gate refinement H = (I + G)/sqrt(3)
    -> J = H^3 = (R - R^-1)/sqrt(3), with J^2 = -I
    -> native Pythagorean component segment is a spinor of its character
    -> normalized adjacency bisector beta(U) gives the unique forward root
    -> dyadic root states U_n and exact finite Cayley half-turn certificates
    -> monotone target-free squeeze P_n < L < Q_n
    -> unit-speed continuous completion exp(tJ)
    -> L = classical pi and exp(pi J) = -I.
```

Every arrow up to the target-free squeeze is finite algebra, finite incidence,
or a declared carrier readout. The final extension to a real one-parameter
subgroup uses standard analysis.

## 2. Minimal native source object

A single homogeneous Cell cannot possess a nonconstant translation-invariant
direction label. Direction is relational.

For ordered neighboring Cell centers `(x,y)`, common translation preserves the
relative direction. The orbit set is exactly the six oriented nearest-neighbor
direction classes:

\[
\{(x,y):x\sim y\}/\text{common translation}\cong C_6.
\]

Endpoint exchange is the half-turn. Forgetting endpoint order gives the three
unoriented positive-ray classes. A chosen cyclic order supplies chirality.

This is the operation-safe local source required for Euler rotation. A theorem
covering every possible long native Cell trajectory is a separate globalization
problem, not a missing premise of the pivoted segment theorem.

## 3. Three-ray transport already contains the six-state shell

On the nontrivial two-dimensional representation of the three ray labels, take

\[
R=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}.
\]

Then

\[
R^3=I,
\qquad
I+R+R^2=0.
\]

Set

\[
G=I+R.
\]

Direct algebra gives

\[
\boxed{G^2=R},
\qquad
\boxed{G^3=-I},
\qquad
\boxed{G^6=I}.
\]

Hence the six-state direction rotor and endpoint reversal are not unrelated
extra data. They are generated inside the linear character algebra of the
three-ray right turn.

The sign of the square root remains chiral: `G` is the forward normalized
adjacency root, while `-G` is the opposite branch.

## 4. The current Cell radius is exactly the gate normalizer

Let

\[
Q=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

Both `R` and `G` preserve `Q`. The adjacent direction sum has dilation

\[
(I+G)^TQ(I+G)=3Q.
\]

Therefore the unique positive scalar normalizing that sum to a unit character
is

\[
\boxed{r=\frac1{\sqrt3}}.
\]

This is numerically the current Cell radius at unit center spacing.

Define the unit gate-ray character

\[
H=r(I+G).
\]

Then

\[
\boxed{H^2=G},
\qquad
\boxed{H^6=-I},
\qquad
\boxed{H^{12}=I}.
\]

Its even powers are the six oriented center directions and its odd powers are
the six intervening gate directions.

The unit phase and physical displacement must not be confused. In the chosen
carrier-character realization, the triple-intersection gate displacement is

\[
\boxed{rH=\frac{I+G}{3}}.
\]

This is the centroid/circumcenter vector of the elementary unit center triangle.
Thus the first dyadic refinement is not an abstract postulate: it is the actual
alternating Cell-direction/gate incidence cycle.

## 5. The geometric meaning of `i`

Set

\[
J=H^3.
\]

Then

\[
\boxed{
J=\frac1{\sqrt3}(R-R^{-1})
}
\]

and

\[
\boxed{J^2=-I}.
\]

Therefore `i` has the following typed meaning:

\[
\boxed{
 i=\text{Cell-radius-normalized forward-minus-backward right-turn operator}.
}
\]

It is not a primitive negative axis, not a seventh spatial direction, and not
the native metric plane itself.

There are two related but different facts.

- The operator `J` is already latent in the two-dimensional representation of
  the coarse `C3` right turn.
- A quarter-turn *state* first occurs at the actual `C12` Cell-gate layer, where
  it is `H^3`.

Reflection sends `R` to `R^-1`, hence `J` to `-J`, while leaving `-I` fixed.
So Euler's endpoint is chirality-independent, but the sign of `i` is not.

## 6. The native segment is a spinor

In the sector-local component algebra with `J^2=-1`, let

\[
v=a+bJ,
\qquad
n=a^2+b^2.
\]

The normalized segment is

\[
S[a:b]=\frac{a+bJ}{\sqrt n}.
\]

Its projective rotation character is

\[
\mathcal C[a:b]
=\frac{(a^2-b^2)+2abJ}{n}.
\]

Exactly,

\[
\boxed{\mathcal C[a:b]=S[a:b]^2}.
\]

Thus the segment carries half the phase of its rotation character: it is a
spinor coordinate.

For `a>0`, define

\[
\beta(U)=\frac{1+U}{\sqrt{2+U+U^{-1}}}.
\]

Then

\[
\boxed{\beta(\mathcal C[a:b])=S[a:b]}.
\]

The normalized adjacency-bisector operation literally recovers the underlying
normalized segment from its doubled character.

The distinguished projective states are

\[
\mathcal C[1:0]=1,
\qquad
\mathcal C[1:1]=J,
\qquad
\mathcal C[0:1]=-1.
\]

So the balanced two-component segment maps to the quarter-turn character.
This is a spinor/character statement, not an identification of the native
120-degree carrier opening with a classical 180-degree angle.

## 7. Why the root tower is canonical

The combinatorial refinement is the directed barycentric subdivision of a
cycle. Old states occupy even positions; each new odd state is the midpoint of
one directed adjacent pair.

In the linear character plane, the unnormalized midpoint direction of `1` and
`U` is `1+U`. The unique `J`-invariant positive quadratic norm, calibrated by
`q(I)=1`, is

\[
q(aI+bJ)=a^2+b^2.
\]

Normalizing the midpoint therefore gives exactly `beta(U)`.

For every unit `U != -1`,

\[
\beta(U)^2=U,
\]

and the root with positive scalar component is unique. At the antipodal input
`U=-1`, the chord midpoint is zero and the two roots are `+J` and `-J`. A
chirality choice selects the first branch. Thereafter the forward roots are
forced.

Hence

\[
\boxed{
\text{the only irreducible branch choice is the initial chirality; the remaining dyadic tower is canonical.}
}
\]

## 8. Viète factors without an imported angle

Choose `U_1=J` and recursively set

\[
U_{n+1}=\beta(U_n).
\]

Write

\[
U_n=c_n+s_nJ.
\]

Then

\[
c_n^2+s_n^2=1,
\]

\[
\boxed{c_{n+1}=\sqrt{\frac{1+c_n}{2}}},
\]

and

\[
\boxed{s_n=2c_{n+1}s_{n+1}}.
\]

Starting from `c_1=0`, the scalar traces are

\[
\frac{\sqrt2}{2},
\quad
\frac{\sqrt{2+\sqrt2}}2,
\quad
\frac{\sqrt{2+\sqrt{2+\sqrt2}}}{2},
\ldots
\]

Thus Viète's nested radicals are the scalar traces of repeated normalized
adjacency bisectors.

## 9. Finite Euler identities before the exponential

Define the Cayley half-phase coordinate

\[
\tau_n=\frac{s_n}{1+c_n}.
\]

Then

\[
\boxed{
U_n=\frac{1+J\tau_n}{1-J\tau_n}
}
\]

and, at every finite depth,

\[
\boxed{
\left(\frac{1+J\tau_n}{1-J\tau_n}\right)^{2^n}=-1.
}
\]

The half-step law is exact:

\[
\tau_n=\frac{2\tau_{n+1}}{1-\tau_{n+1}^2}.
\]

So `e^(J pi)=-1` is preceded by an infinite compatible family of exact finite
Cayley half-turn certificates; it is not introduced only after a limiting
approximation has lost the discrete structure.

## 10. The internal half-period constant

Define

\[
P_n=2^n s_n,
\qquad
Q_n=2^{n+1}\tau_n.
\]

Then

\[
P_n<P_{n+1},
\]

\[
Q_{n+1}<Q_n,
\]

\[
P_n<Q_n,
\]

and

\[
\boxed{Q_n-P_n=P_n\tau_n^2}.
\]

Since `tau_(n+1)<tau_n/2`, the interval width tends to zero. Hence

\[
\boxed{
L=\lim P_n=\lim Q_n
}
\]

exists without using classical `pi` as input, with

\[
2<L<4.
\]

The same constant is the unique scale for which the dyadic character has unit
infinitesimal generator:

\[
\lim_{n\to\infty}
\frac{U_n-I}{L/2^n}=J.
\]

## 11. Why `e` appears

Let

\[
L_n=Q_n=2^{n+1}\tau_n.
\]

The finite endpoint identity is

\[
\left(
\frac{1+J L_n/2^{n+1}}
     {1-J L_n/2^{n+1}}
\right)^{2^n}
=-1.
\]

The standard Cayley-composition limit is

\[
\lim_{N\to\infty}
\left(
\frac{1+Jx/(2N)}{1-Jx/(2N)}
\right)^N
=e^{Jx}.
\]

Because `L_n -> L`, the exact finite half-turn certificates complete to

\[
\boxed{e^{JL}=-1}.
\]

Thus

\[
\boxed{
 e=\text{the analytic notation for continuous multiplicative composition of infinitesimal finite rotations}.
}
\]

It is not a geometric axis or an additional state.

## 12. Why the completion constant is classical pi

The compatible dyadic character

\[
E_0(kL/2^n)=U_n^k
\]

extends uniquely to a continuous one-parameter subgroup. Its unit-speed
generator is `J`, so

\[
E(t)=\exp(tJ).
\]

The entire forward short-root tower selects the first positive winding; the
finite squeeze gives `0<L<4`. Under the standard complex identification
`J=i`, the first positive half-period of the unit-speed exponential is
classical `pi`. Therefore

\[
\boxed{L=\pi}
\]

and

\[
\boxed{e^{i\pi}+1=0}.
\]

The equality with classical `pi` is an analytic identification of the internal
finite completion constant, not an input to the finite recursion.

## 13. Final typed meaning of the five symbols

\[
\boxed{
\begin{aligned}
1&=\text{identity orientation},\\
-1&=\text{endpoint reversal / half-turn state},\\
i&=\text{normalized chiral right-turn operator and first gate-level quarter state},\\
e&=\text{continuous multiplicative-composition completion},\\
\pi&=\text{first positive half-period in the unit-speed completion}.
\end{aligned}
}
\]

Euler's identity therefore says:

\[
\boxed{
\text{unit-speed completion of Cell-normalized chiral segment rotation through one half-period equals endpoint reversal}.
}
\]

## 14. What is solved and what remains open

### Closed in this package

1. A relational, operation-safe local source of six oriented directions.
2. Internal generation `C3 -> C6` in the character algebra.
3. Exact physical first refinement by the six Cell gates.
4. Cell-radius normalization of that first gate bisector.
5. Exact construction `J^2=-I` and the chirality no-go.
6. Segment-spinor/rotation-character identity.
7. Canonical normalized root rule after the first chirality choice.
8. Viète nested-radical recursion from the root rule.
9. Exact finite Cayley half-turn identities.
10. Target-free lower/upper period squeeze.
11. Standard unit-speed completion to Euler's exponential and classical `pi`.

### Still open but no longer blocking the local Euler theorem

1. A global factorization of every arbitrary native Cell trajectory through one
   phase tower.
2. A one-step physical Cell realization of roots beyond the actual `C12`
   Cell/gate layer; current deeper roots are typed transition-history states.
3. An intertwiner identifying the spinor `C2`, tetrahedral residual `C2`, and
   paired-Pell conjugacy `C2`.
4. A theorem deriving the ordinary scalar exponent six in the `N=58` defect
   product from the six Cell gates.

These are extension questions, not missing algebraic steps in the present
Euler/Viète completion theorem.

## 15. Formal and executable surfaces

Exact finite checkers:

- `src/enterprise_math/euler_rotation_refinement.py`;
- `src/enterprise_math/euler_native_bisector.py`;
- `src/enterprise_math/euler_dyadic_cayley_bridge.py`;
- merged companion `src/enterprise_math/euler_cayley_spinor.py`.

Lean proof modules:

- `EnterpriseMath/Precision/EulerCellRadiusBisector.lean`;
- `EnterpriseMath/Precision/EulerPhysicalGate.lean`;
- `EnterpriseMath/Precision/EulerCayleyBridge.lean`.

Theorem ledger:

- `research_notes/EULER_CELL_RADIUS_BISECTOR_THEOREM_LEDGER_20260903.json`.

Candidate freeze:

`AC-EM-FREE-F6D046-EULER-GEOMETRIC-COMPLETION-SYNTHESIS-V1`.
