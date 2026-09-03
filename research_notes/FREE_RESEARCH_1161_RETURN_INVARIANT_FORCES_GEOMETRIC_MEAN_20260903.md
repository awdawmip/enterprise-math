# Free Research #1161 — the return invariant uniquely forces the geometric-mean channel

Status: `FREE_RESEARCH_RESULT / COARSE-GRAINING CHARACTERIZATION / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependency: exact balanced-return Green/scale invariant.

## 1. Start with only the arithmetic coarse scale

Let

\[
a>b>0,
\qquad
H=a+b,
\qquad
s=\frac{a-b}{a+b}\in(0,1).
\]

The balanced-return Green completion is

\[
G(s)=\sum_{n\ge0}c_ns^{2n},
\qquad
c_n=\frac{\binom{2n}{n}^2}{16^n}>0.
\]

The proved RG invariant is

\[
\mathcal I_{\rm ret}=G(s)/H.
\]

Now choose only the new upper/coarse endpoint by the arithmetic channel

\[
\boxed{A=\frac{a+b}{2}=\frac H2.}
\]

Do **not** assume the geometric mean formula for the new lower endpoint. Let

\[
0<B\le A
\]

be unknown.

Define the new contrast

\[
t=\frac{A-B}{A+B}\in[0,1).
\]

## 2. Invariant preservation becomes one scalar equation

Because

\[
A=\frac{A+B}{2}(1+t),
\]

we have

\[
A+B=\frac{2A}{1+t}=\frac{H}{1+t}.
\]

Require exact preservation of the balanced-return Green/scale invariant:

\[
\frac{G(t)}{A+B}=\frac{G(s)}H.
\]

Substitution gives the scalar equation

\[
\boxed{(1+t)G(t)=G(s).}
\]

Thus, after the arithmetic coarse scale is fixed, the entire second channel is determined by an invariant-preservation equation.

## 3. The invariant equation has a unique admissible solution

Define

\[
K(t)=(1+t)G(t).
\]

Since all coefficients `c_n` are positive,

\[
G(t)>0,
\qquad
G'(t)>0
\]

for `t>0`. Hence

\[
K'(t)=G(t)+(1+t)G'(t)>0.
\]

So `K` is strictly increasing on `[0,1)`.

For `s>0`,

\[
K(0)=1<G(s),
\]

because `G(s)>c_0=1`, while

\[
K(s)=(1+s)G(s)>G(s).
\]

Therefore there exists a unique

\[
\boxed{t\in(0,s)}
\]

satisfying

\[
K(t)=G(s).
\]

## 4. Identify the unique solution from the return-Green quadratic RG

Let

\[
r=\sqrt{1-s^2}.
\]

The independently proved return-Green quadratic renormalization is

\[
G\left(\frac{1-r}{1+r}\right)
=\frac{1+r}{2}G(s).
\]

Set

\[
t_*=\frac{1-r}{1+r}.
\]

Then

\[
1+t_*=\frac{2}{1+r}.
\]

Therefore

\[
(1+t_*)G(t_*)
=\frac{2}{1+r}\cdot\frac{1+r}{2}G(s)
=G(s).
\]

By uniqueness,

\[
\boxed{t=t_*=rac{1-r}{1+r}.}
\]

## 5. The lower channel is forced to be the geometric mean

From the definition of contrast,

\[
\frac BA=\frac{1-t}{1+t}.
\]

For the unique solution above,

\[
\frac{1-t_*}{1+t_*}=r.
\]

Hence

\[
B=Ar.
\]

Now

\[
r=\sqrt{1-s^2}
=\frac{2\sqrt{ab}}{a+b}
=\frac{2\sqrt{ab}}H.
\]

Since `A=H/2`,

\[
\boxed{B=\sqrt{ab}.}
\]

Thus the geometric mean is not required as an independent selector in this characterization.

## 6. Coarse-graining theorem

At derived branch-Green strength:

\[
\boxed{
\begin{array}{c}
\text{fix the arithmetic coarse endpoint }A=(a+b)/2,\\[2mm]
\text{preserve the native-diamond balanced-return Green/scale invariant}
\end{array}
\Longrightarrow
\boxed{B=\sqrt{ab}}
}
\]

and the admissible solution is unique.

This gives a concrete meaning to the phrase that the arithmetic and geometric means are complementary coarse-graining channels:

- the arithmetic channel chooses the new coarse scale;
- the branch-return invariant uniquely forces the compatible lower/geometric channel.

## 7. Relation to the Viète-bisector factorization

The unique solution has

\[
t=s^+=\frac{1-r}{1+r}.
\]

In the #1158 finite bisector coordinates

\[
C^2=(1+r)/2,
\qquad
S^2=(1-r)/2,
\]

this is

\[
t=(S/C)^2.
\]

Therefore the invariant characterization and the earlier bisector-square factorization are the same RG step viewed from two sides:

1. geometric side: `BISECTOR -> COMPONENT SQUARE -> CONE COMPLETION`;
2. branch side: `ARITHMETIC SCALE -> RETURN-INVARIANT PRESERVATION -> UNIQUE GEOMETRIC CHANNEL`.

## 8. Typing and prior-art boundary

The square-lattice Green/AGM relation underlying `G` has classical prior literature; no historical novelty is claimed for the existence of that relation.

The #1161 result is the typed characterization using

- coefficients realized by current-native commuting-diamond provenance masses;
- the exact return-Green/scale RG invariant;
- the arithmetic channel as a declared coarse-scale step;
- uniqueness to derive the geometric channel.

`G` remains a derived completion/readout rather than an N0 Cell primitive. Therefore this theorem is not yet a bare-Cell derivation of square root.

## 9. Strongest conclusion

At free-research-result strength:

`GEOMETRIC_MEAN_CHANNEL_IS_UNIQUELY_FORCED_BY_ARITHMETIC_COARSE_SCALE + RETURN_GREEN_INVARIANT`.

This is stronger than merely checking that the classical AGM update preserves an invariant.
