# The imaginary unit as the Cell-radius-normalized chiral difference of a native right turn

Status: `FREE_RESEARCH / EXACT CARRIER-OPERATOR THEOREM / NOT NATIVE TYPE IDENTIFICATION`
Date: `2026-09-03`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Main result

Let \(\mathcal R\) denote the nontrivial two-dimensional carrier representation of one positive three-ray right-turn cycle. On this plane,

\[
\mathcal R^3=I,
\qquad
I+\mathcal R+\mathcal R^2=0,
\qquad
\mathcal R^{-1}=\mathcal R^2.
\]

Define the forward-minus-backward chiral difference

\[
D=\mathcal R-\mathcal R^{-1}.
\]

Then

\[
\boxed{D^2=-3I.}
\]

The current Cell radius in nearest-center-spacing-one carrier units is

\[
r_{\mathrm{Cell}}=\frac1{\sqrt3}.
\]

Therefore

\[
\boxed{
\mathcal J
:=
r_{\mathrm{Cell}}
(\mathcal R-\mathcal R^{-1})
}
\]

satisfies

\[
\boxed{\mathcal J^2=-I.}
\]

Thus the imaginary unit has an exact Enterprise carrier/operator correspondence:

\[
\boxed{
i
\longleftrightarrow
\text{Cell-radius-normalized difference between positive and negative right-turn transport}.
}
\]

This result uses no classical \(90^\circ\) primitive axis and no numerical value of \(\pi\).

## 2. Proof

Because \(\mathcal R^{-1}=\mathcal R^2\),

\[
\begin{aligned}
D^2
&=(\mathcal R-\mathcal R^2)^2\\
&=\mathcal R^2-2\mathcal R^3+\mathcal R^4\\
&=\mathcal R^2-2I+\mathcal R\\
&=(\mathcal R+\mathcal R^2)-2I\\
&=-I-2I\\
&=-3I.
\end{aligned}
\]

Multiplying by \(r_{\mathrm{Cell}}^2=1/3\) gives

\[
\mathcal J^2
=
\frac13D^2
=-I.
\]

## 3. Uniqueness of the radius normalization

Let \(a>0\) be any real carrier/readout scalar and set

\[
J_a=aD.
\]

Then

\[
J_a^2=-3a^2I.
\]

Hence

\[
J_a^2=-I
\]

if and only if

\[
3a^2=1.
\]

The unique positive solution is

\[
\boxed{a=1/\sqrt3.}
\]

Therefore the same scalar already selected by the critical gap-free triple-intersection Cell covering is also the unique positive scalar that normalizes the chiral \(C_3\) rotation difference into a complex structure.

This is a genuine independent compatibility, not a numerical fit to \(\pi\).

## 4. Explicit integer certificate

Use the integral companion matrix

\[
\mathcal R=
\begin{pmatrix}
0&-1\\
1&-1
\end{pmatrix}.
\]

Then

\[
\mathcal R^2=
\begin{pmatrix}
-1&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal R^3=I,
\]

and

\[
D=\mathcal R-\mathcal R^2
=
\begin{pmatrix}
1&-2\\
2&-1
\end{pmatrix}.
\]

A direct integer multiplication gives

\[
D^2=
\begin{pmatrix}
-3&0\\
0&-3
\end{pmatrix}
=-3I.
\]

The executable certificate is recorded in

`src/enterprise_math/c3_chiral_complex_structure.py`.

## 5. Even and odd parts of the right turn

The reversal-even part of \(\mathcal R\) is

\[
\frac{\mathcal R+\mathcal R^{-1}}2
=-\frac12I.
\]

The reversal-odd part is

\[
\frac{\mathcal R-\mathcal R^{-1}}2
=\frac{\sqrt3}{2}\mathcal J.
\]

Therefore

\[
\boxed{
\mathcal R
=-\frac12I+\frac{\sqrt3}{2}\mathcal J,
}
\]

and

\[
\boxed{
\mathcal R^{-1}
=-\frac12I-\frac{\sqrt3}{2}\mathcal J.
}
\]

These are the finite carrier/operator forms of the familiar complex conjugate pair

\[
\omega=-\frac12+\frac{\sqrt3}{2}i,
\qquad
\omega^{-1}=-\frac12-\frac{\sqrt3}{2}i,
\]

but the derivation above starts from the order-three rotation relation and the frozen Cell radius, not from classical trigonometry.

## 6. Two distinct meanings of \(i\)

The previous Euler analysis said that the coarse six-state orientation shell contains an exact half-turn \(-1\) but no group element of order four. That remains correct.

The present result reveals a necessary distinction.

### 6.1 Operator \(i\)

Already on the nontrivial real representation of the coarse \(C_3\) right-turn cycle, the normalized chiral difference

\[
\mathcal J
=
\frac{\mathcal R-\mathcal R^{-1}}{\sqrt3}
\]

is an operator with square \(-I\).

Thus a complex-structure coordinate exists at the representation layer.

### 6.2 State \(i\)

The coarse orientation group \(C_6\) itself has no element \(q\) satisfying

\[
q^2=-1.
\]

After the first canonical phase subdivision,

\[
C_6\hookrightarrow C_{12},
\]

the positive midpoint state \(q_1=3\in C_{12}\) has order four and satisfies

\[
q_1^2=-1.
\]

Under the compatible fundamental character,

\[
\chi(q_1)=i.
\]

Therefore:

\[
\boxed{
\text{coarse level: }i\text{ exists as a derived chiral operator but not a phase state};
}
\]

\[
\boxed{
\text{first dyadic refinement: the operator is realized by an actual quarter-turn state}.
}
\]

## 7. Exact compatibility with the refined quarter-turn

In the standard finite character realization inside the twelve-state phase shell, let

\[
\omega=\chi(4),
\]

so \(\omega\) represents the embedded positive \(C_3\) right turn, and let

\[
q=\chi(3)
\]

be the positive quarter-turn state.

Then

\[
\omega^3=1,
\qquad
q^2=-1,
\]

and

\[
\boxed{
q
=
\frac1{\sqrt3}
(\omega-\omega^{-1}).
}
\]

Thus the quarter-turn state appearing after refinement is exactly the Cell-radius-normalized chiral operator already latent in the coarse right-turn representation.

This is the finite operator-to-state realization bridge.

## 8. Geometric meaning for Euler's formula

Let \(\mathcal J\) be the normalized chiral operator above. The real operator algebra

\[
\{aI+b\mathcal J:a,b\in\mathbf R\}
\]

is isomorphic to \(\mathbf C\) because \(\mathcal J^2=-I\).

The continuous rotation character is then written

\[
\exp(\theta\mathcal J)
=
\cos\theta\,I+\sin\theta\,\mathcal J.
\]

Under the scalar identification \(\mathcal J\leftrightarrow i\), this is

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

The new geometric typing is:

- \(\mathcal R\): finite positive native-right-turn carrier action;
- \(\mathcal R^{-1}\): the reversed carrier action;
- \(\mathcal J\): normalized chirality operator;
- \(i\): scalar coordinate of \(\mathcal J\);
- \(e^{i\theta}\): analytic character generated by continuous transport along \(\mathcal J\);
- \(\pi\): the archimedean phase assigned to the half-turn where the character equals \(-1\).

So Euler's formula is not evidence that a primitive imaginary spatial axis must be inserted into the Enterprise plane. It is the continuous character calculus of the chiral transport operator extracted from finite right-turn/reversal data.

## 9. Why the sign of \(i\) is chiral

Reversing the cyclic order exchanges

\[
\mathcal R\longleftrightarrow\mathcal R^{-1}.
\]

Therefore

\[
\mathcal J
\longmapsto
-\mathcal J.
\]

At the scalar level,

\[
i\longmapsto-i.
\]

Thus the sign of the imaginary unit records the orientation convention of the rotation carrier. It is not an arbitrary decoration once a chirality has been fixed, but it is not selected by the unoriented carrier alone.

Freeze:

`UNORIENTED_C3_CARRIER DOES_NOT_SELECT SIGN_OF_I`.

## 10. Relation to Cell radius

The equality

\[
r_{\mathrm{Cell}}=1/\sqrt3
\]

already has a carrier-covering role: it is the critical radius for the declared nearest-center-spacing-one triangular cover with triple intersections.

The present theorem gives the same scalar a second independent role:

\[
\boxed{
R_{\mathrm{Cell}}^2=1/3
\iff
[R_{\mathrm{Cell}}(\mathcal R-\mathcal R^{-1})]^2=-I.
}
\]

This is a high-value cross-constraint between:

1. local Cell overlap geometry; and
2. the normalized algebra of right-turn chirality.

It does not yet prove that the carrier radius is a native operator scalar. That type bridge remains to be supplied.

Freeze:

`CELL_LENGTH_SCALAR × ROTATION_OPERATOR = CARRIER/READOUT CONSTRUCTION`,

not a promoted native multiplication law.

## 11. Revised Euler candidate

`AC-EM-FREE-F6D046-EULER-CHIRAL-RIGHT-TURN-V3`:

> On the nontrivial two-dimensional representation of the Enterprise three-positive-ray right-turn cycle, the forward-minus-backward turn operator squares to \(-3I\). The frozen Cell radius \(1/\sqrt3\) is the unique positive normalization that converts this chiral difference into a complex structure \(\mathcal J^2=-I\). At coarse resolution \(\mathcal J\) is a derived operator rather than a phase state; after the first non-split dyadic refinement \(C_6\hookrightarrow C_{12}\), the positive quarter-turn state realizes the same operator character. Euler's formula is the continuous character decomposition generated by this normalized chiral transport.

Status:

`EXACT C3 OPERATOR ALGEBRA + EXACT RADIUS COMPATIBILITY + EFFECTIVE CHARACTER REALIZATION / NATIVE TYPE BRIDGE OPEN`.
