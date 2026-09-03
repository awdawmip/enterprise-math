# Euler formula through Pythagorean spinors and the Cayley segment map

Status: `FREE_RESEARCH / FINITE_ALGEBRAIC_THEOREM_PACKAGE / NOT_FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 0. Main result

The current three-positive-axis foundation gives a sector-local Pythagorean law

\[
L_E(a,b,0)^2=a^2+b^2.
\]

From the same two active integer coordinates, introduce a *derived rotation-character algebra* with an orientation operator \(J\) satisfying \(J^2=-1\), and define

\[
\mathcal C[a:b]
=
\frac{(a+Jb)^2}{a^2+b^2}
=
\frac{a^2-b^2}{a^2+b^2}
+J\frac{2ab}{a^2+b^2}.
\]

This map:

1. uses only the Pythagorean norm, integer multiplication, and rational normalization;
2. sends every nonzero rational projective pair to an exact rational unit rotation;
3. is multiplicative under Gaussian pair composition;
4. parametrizes every rational point of the unit-character conic;
5. sends \([1:0]\), \([1:1]\), and \([0:1]\) to \(1\), \(J\), and \(-1\), respectively;
6. turns negative-Pell near-axis line segments into exact Cayley half-angle defects;
7. completes through finite exact Cayley products to \(e^{J\theta}\).

Thus the line-segment coordinates are most naturally interpreted as a projective *half-angle/spinor state*, while Euler's complex value is the normalized square/character readout of that state.

Freeze:

`PYTHAGOREAN_SEGMENT_SPINOR != PRIMITIVE_COMPLEX_NUMBER`.

`J_IS_DERIVED_ORIENTATION_OPERATOR_NOT_NATIVE_SPATIAL_AXIS`.

`CHARACTER_UNIT_CONIC != NATIVE_ENTERPRISE_METRIC_SPACE`.

## 1. Typed source and target

The source is a nonzero two-coordinate sector/displacement state

\[
(a,b)\in K^2\setminus\{0\},
\]

where \(K\) may first be \(\mathbf Z\) or \(\mathbf Q\). The source norm-square is

\[
N(a,b)=a^2+b^2.
\]

The target is the two-dimensional rotation-character algebra

\[
K[J]/(J^2+1).
\]

The target is a representation/readout layer. This note does not identify its classical planar angle or Euclidean metric with the native Enterprise \(120^\circ\) right-sector geometry.

Scaling the source pair does not change the character:

\[
\mathcal C[\lambda a:\lambda b]=\mathcal C[a:b],
\qquad \lambda\ne0.
\]

Therefore the natural source type is the rational projective line \(\mathbf P^1(K)\), not a magnitude-bearing segment.

## 2. Exact Pythagorean character theorem

Write

\[
X=a^2-b^2,
\qquad
Y=2ab,
\qquad
R=a^2+b^2.
\]

Then

\[
X^2+Y^2
=(a^2-b^2)^2+4a^2b^2
=(a^2+b^2)^2
=R^2.
\]

Hence

\[
\mathcal C[a:b]\overline{\mathcal C[a:b]}=1.
\]

So every integer pair produces an exact rational point on the unit-character conic. The familiar Pythagorean-triple map is therefore simultaneously a rotation-character map:

\[
(a,b)
\longmapsto
(a^2-b^2,2ab,a^2+b^2).
\]

No trigonometric function and no value of \(\pi\) is used.

## 3. Exact composition law

Define projective pair multiplication by

\[
[a:b]\star[c:d]
=
[ac-bd:ad+bc].
\]

This is simply multiplication in the formal algebra \(K[J]/(J^2+1)\):

\[
(a+Jb)(c+Jd)
=(ac-bd)+J(ad+bc).
\]

Norms multiply:

\[
N(ac-bd,ad+bc)=N(a,b)N(c,d).
\]

Consequently,

\[
\boxed{
\mathcal C(u\star v)=\mathcal C(u)\mathcal C(v).
}
\]

Thus exact rotation composition exists already on integer/projective segment coordinates. Classical angle addition is a decoder of this algebraic law, not its prerequisite.

The inverse is

\[
[a:b]^{-1}=[a:-b].
\]

## 4. Rational completeness

Every rational unit-character point

\[
(x,y)\in\mathbf Q^2,
\qquad
x^2+y^2=1,
\]

comes from a rational projective spinor.

If \(x\ne-1\), choose

\[
[a:b]=[1+x:y].
\]

A direct substitution gives

\[
\mathcal C[1+x:y]=x+Jy.
\]

The missing point \((-1,0)\) is

\[
\mathcal C[0:1]=-1.
\]

Therefore

\[
\boxed{
\mathbf P^1(\mathbf Q)
\simeq
\{x+Jy:x,y\in\mathbf Q,\ x^2+y^2=1\}.
}
\]

The rational source states form a dense classical character family after the standard topological completion. Density is a standard external topological fact; the exact rational parametrization above is finite algebra.

## 5. The Euler constants as the three simplest projective segment states

The character map gives

\[
\mathcal C[1:0]=1,
\]

\[
\mathcal C[1:1]=J,
\]

\[
\mathcal C[0:1]=-1.
\]

Moreover,

\[
[1:1]\star[1:1]=[0:1],
\]

so

\[
J^2=-1.
\]

This gives a line-segment meaning to the finite endpoint data in Euler's identity:

- \(1\): the zero-turn projective segment state;
- \(J\): a chirality-selected square root of endpoint reversal;
- \(-1\): the half-turn/reversal state.

The sign choice is not canonical under reflection:

\[
[1:1]\longleftrightarrow[1:-1]
\]

under orientation reversal, corresponding to \(J\leftrightarrow-J\).

## 6. Cayley parameter without an angle

For finite parameter \(t=b/a\),

\[
\mathcal C(t)
=
\frac{1-t^2}{1+t^2}
+J\frac{2t}{1+t^2}.
\]

Equivalently,

\[
\boxed{
\mathcal C(t)=\frac{1+Jt}{1-Jt}.
}
\]

The projective point \(t=\infty\) maps to \(-1\).

The exact composition law is

\[
\mathcal C(s)\mathcal C(t)
=
\mathcal C\!\left(\frac{s+t}{1-st}\right),
\]

with the zero denominator interpreted projectively as \(\infty\). This Möbius law follows from pair multiplication and does not require \(\arctan\).

The states

\[
t=0,\qquad t=1,\qquad t=\infty
\]

map to

\[
1,\qquad J,\qquad-1.
\]

Thus the projective parameter orders the zero-turn, quarter-turn, and half-turn endpoints without using radians.

## 7. Square roots and the spin double cover

To solve

\[
\mathcal C(u)^2=\mathcal C(t),
\]

one must solve the purely algebraic half-step equation

\[
t=\frac{2u}{1-u^2}.
\]

Each regular target has two roots related by the sign character of the rotation cover. For the half-turn \(t=\infty\), the two solutions are

\[
u=1,\qquad u=-1,
\]

which give \(J\) and \(-J\).

This is the projective/spinor form of the non-split \(C_2\) root fiber proved in the finite cyclic tower. A directed rotation path or chirality frame selects one branch; a static unoriented carrier does not.

Starting with the forward root \(u_1=1\), the next forward root solves

\[
1=\frac{2u_2}{1-u_2^2},
\]

hence

\[
\boxed{u_2=\sqrt2-1.}
\]

The classical half-angle defect has therefore been recovered as the next projective line-segment root coordinate, not inserted as a trigonometric value.

## 8. Negative-Pell segment theorem

Let integers \(P,Q,D>0\) satisfy

\[
P^2-DQ^2=-1,
\]

or equivalently

\[
P^2+1=DQ^2.
\]

Set

\[
R=Q\sqrt D,
\qquad
\tau=R-P.
\]

Then

\[
(R-P)(R+P)=R^2-P^2=1,
\]

so

\[
\tau=\frac1{R+P}.
\]

Furthermore,

\[
1+\tau^2=2R\tau,
\qquad
1-\tau^2=2P\tau.
\]

Substitution into the Cayley map gives the exact identity

\[
\boxed{
\mathcal C(\tau)
=
\frac{P}{Q\sqrt D}
+J\frac1{Q\sqrt D}.
}
\]

Thus \(Q\sqrt D-P\) is precisely the projective half-angle coordinate of the normalized near-axis segment \((P,1)\), whose Pythagorean length is \(Q\sqrt D\).

This supplies a direct segment-rotation interpretation of a negative-Pell residual: it is not merely a small algebraic error; it is the exact Cayley coordinate needed to rotate the reference direction onto the normalized segment.

## 9. The three defects occurring in the N=58 line

Three negative-Pell segment identities are

\[
1^2+1=2\cdot1^2,
\]

\[
70^2+1=29\cdot13^2,
\]

\[
99^2+1=58\cdot13^2.
\]

Their forward Cayley defects are

\[
\tau_2=\sqrt2-1,
\]

\[
\tau_{29}=13\sqrt{29}-70,
\]

\[
\tau_{58}=13\sqrt{58}-99.
\]

Each is the exact half-angle coordinate of a one-unit-transverse line segment:

\[
(1,1),\qquad(70,1),\qquad(99,1).
\]

The previously observed Ramanujan/Borwein factorization becomes

\[
\boxed{
99\sqrt2-70-13\sqrt{29}
=
\tau_2^6\tau_{29}\tau_{58}.
}
\]

The equality is algebraic. The new geometric reading is that every factor is a Cayley half-angle defect of a Pythagorean/Pell segment. The exponent \(6\) is suggestive of the six-state orientation shell, but no theorem currently derives that multiplicity from the Cell gates; that possible identification remains open.

## 10. Machin composition as an exact integer certificate

The same pair law gives a useful cross-check. Without evaluating any inverse tangent,

\[
[5:1]^{\star4}\star[239:-1]
=[1:1].
\]

Before projective reduction, both coordinates are \(114244\):

\[
(5+J)^4(239-J)=114244(1+J).
\]

Applying \(\mathcal C\) gives

\[
\mathcal C(1/5)^4\mathcal C(-1/239)=J.
\]

Classical angle decoding turns this into Machin's identity. The integer composition certificate is prior to and independent of that decoder.

This result is supplied to the independent Machin free-research branch as a reusable interface; it is not claimed as historical novelty.

## 11. Why the base e appears

The finite character law needs no real exponential. To pass from finite/rational rotations to a continuous one-parameter rotation group, define the exact norm-one Cayley step

\[
Q_n(\theta)
=
\frac{1+J\theta/(2n)}{1-J\theta/(2n)}
\]

and compose it \(n\) times:

\[
E_n(\theta)=Q_n(\theta)^n.
\]

Every finite \(E_n(\theta)\) lies exactly on the unit-character conic. There is no radial drift. Standard analysis gives

\[
\boxed{
\lim_{n\to\infty}E_n(\theta)=e^{J\theta}.
}
\]

Therefore \(e\) is not a fourth spatial ingredient added to \(1,J,-1\). It is the notation selected by the continuous completion of repeated multiplicative forward composition. The role of \(J\) is to make that generator rotational rather than exponentially growing.

Freeze:

`E_IS_COMPOSITION_COMPLETION_NOT_SPATIAL_DIRECTION`.

## 12. Euler formula and the winding quotient

The dyadic Cell–gate tower independently defines a target-free half-period constant \(\pi_{\mathrm{rot}}\). In normalized turn coordinates, the finite and completed character laws require only

\[
E(0)=1,
\qquad
E(1/2)=-1,
\qquad
E(t+u)=E(t)E(u).
\]

Assigning continuous generator length \(2\pi_{\mathrm{rot}}\) to one full turn gives

\[
\theta=2\pi_{\mathrm{rot}}t.
\]

After the standard analytic identifications \(J=i\) and \(\pi_{\mathrm{rot}}=\pi\),

\[
e^{i\theta}=\cos\theta+i\sin\theta,
\]

and the half-turn endpoint is

\[
e^{i\pi}+1=0.
\]

The strongest current geometric reading is therefore:

\[
\boxed{
\text{projective Pythagorean segment spinor}
\xrightarrow{\text{normalized square}}
\text{exact rotation character}
\xrightarrow{\text{composition/topological completion}}
e^{i\theta}.
}
\]

Here:

- \(1\) is the zero-turn character;
- \(i\) is the chirality-selected character of the first root of reversal;
- \(-1\) is endpoint reversal;
- \(e\) records continuous composition;
- \(\pi\) calibrates half a winding period.

## 13. Restricted operation-safe orientation quotient

There is also a sharp typing theorem behind the source state.

Let a translation group act transitively on Cell centers. Any translation-invariant map from a *single* Cell center to a nontrivial direction set must be constant. Therefore orientation cannot be a unary attribute of one homogeneous Cell state.

By contrast, for ordered neighboring endpoint states \((x,y)\), the relative direction/displacement is translation-invariant. Two ordered primitive segments have the same direction iff a common translation carries one to the other. Hence

\[
\boxed{
\{\text{ordered primitive Cell pairs}\}/\{\text{common translations}\}
\simeq
\{\text{six oriented neighbor directions}\}.
}
\]

Endpoint exchange induces the half-turn; a chosen cyclic neighbor order induces the successor rotation. The quotient respects translation, endpoint exchange, and this restricted pivot-preserving rotation operation.

Thus a two-endpoint relation is sufficient, and a single instantaneous Cell is insufficient. This closes the operation-safe quotient only for the declared primitive ordered-segment subsystem. It does not prove that every admissible native rotating-Cell trajectory carries such a globally coherent endpoint pair.

## 14. Current theorem boundary

`PYTHAGOREAN_CHARACTER_AND_COMPOSITION_PROVED_FINITE_ALGEBRAIC`.

`RATIONAL_UNIT_CONIC_PARAMETRIZATION_PROVED`.

`NEGATIVE_PELL_CAYLEY_SEGMENT_IDENTITY_PROVED`.

`RESTRICTED_ORDERED_SEGMENT_QUOTIENT_PROVED_AT_CARRIER_RELATION_LEVEL`.

`CAYLEY_PRODUCT_TO_EXPONENTIAL_IS_STANDARD_ANALYTIC_COMPLETION`.

`N58_FACTOR_MULTIPLICITY_SIX_NOT_DERIVED_FROM_CELL_GATES`.

`NO_GLOBAL_NATIVE_CELL_TRAJECTORY_ORIENTATION_THEOREM`.

`NO_IDENTIFICATION_OF_CHARACTER_J_WITH_A_NATIVE_AXIS`.

## 15. Next attacks

1. Formalize the projective pair group law and character homomorphism in Lean.
2. Formalize the transitive-action unary no-go and directed-edge orbit quotient.
3. Determine whether the Cell trajectory semantics naturally carry ordered endpoints or require a history augmentation.
4. Test whether the exponent \(6\) in \(\tau_2^6\tau_{29}\tau_{58}\) is generated by the six Cell gates or by independent modular data.
5. Connect the Cayley finite product \(E_n(\theta)\) to the dyadic root tower by an explicit commuting approximation diagram.
6. Preserve the distinction between the projective spinor sign fiber, the tetrahedral residual \(C_2\), and the paired-Pell conjugacy until an intertwiner is proved.

Executable exact checker:

`src/enterprise_math/euler_cayley_spinor.py`

Regression:

`tests/test_euler_cayley_spinor.py`
