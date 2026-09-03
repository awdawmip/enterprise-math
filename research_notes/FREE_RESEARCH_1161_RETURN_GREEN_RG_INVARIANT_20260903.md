# Free Research #1161 — balanced-return Green invariant of the AGM chord RG

Status: `FREE_RESEARCH_RESULT / EXACT RG COCYCLE INVARIANT / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependencies:
- finite Weighted-BRC return masses `c_n`;
- power-series quadratic transformation;
- Viète-bisector square factorization.

## 1. Finite branch return coefficients

For each `n`, the explicit paired-binary balanced-return system has total return mass

\[
c_n=\frac{\binom{2n}{n}^2}{16^n}.
\]

Define the positive return Green readout

\[
\boxed{
G(s)=\sum_{n=0}^\infty c_ns^{2n},
\qquad 0\le s<1.
}
\]

Thus `G(s)=F(s^2)` for the pi-free power series used in the internal normalization proof.

Each coefficient is finite positive-rational branch mass; the infinite sum is a derived completion/readout.

## 2. AGM shape/scale state

For an AGM pair `a>b>0`, put

\[
H=a+b,
\qquad
U=a-b,
\qquad
V=2\sqrt{ab},
\]

and normalize

\[
s=U/H,
\qquad
r=V/H=\sqrt{1-s^2}.
\]

The exact #1161 update is

\[
\boxed{
H^+=\frac{1+r}{2}H,
}
\]

and

\[
\boxed{
s^+=\frac{1-r}{1+r}.
}
\]

## 3. Return Green renormalizes by exactly the same scale factor

The power-series quadratic transformation proved independently is

\[
F(1-x^2)
=
\frac{2}{1+x}
F\left(\left(\frac{1-x}{1+x}\right)^2\right).
\]

Set

\[
x=r=\sqrt{1-s^2}.
\]

Then `1-x^2=s^2` and

\[
\frac{1-x}{1+x}=s^+.
\]

Therefore

\[
G(s)
=
\frac{2}{1+r}G(s^+),
\]

or equivalently

\[
\boxed{
G(s^+)=\frac{1+r}{2}G(s).
}
\]

But the AGM hypotenuse/scale update is exactly

\[
H^+=\frac{1+r}{2}H.
\]

Hence

\[
\boxed{
\frac{G(s^+)}{H^+}
=
\frac{G(s)}H.
}
\]

The quantity

\[
\boxed{
\mathcal I_{\rm ret}(H,s):=\frac{G(s)}H
}
\]

is therefore an exact invariant of the AGM chord/shape renormalization.

## 4. Viète-bisector form

The #1158/#1161 exact cross-family factorization introduces the finite bisector coordinates `(C,S)` with

\[
C^2=\frac{1+r}{2},
\qquad
S^2=\frac{1-r}{2},
\qquad
C^2+S^2=1.
\]

Then

\[
H^+=C^2H,
\qquad
s^+=\left(\frac SC\right)^2.
\]

The return Green cocycle becomes

\[
\boxed{
G\left(\left(\frac SC\right)^2\right)
=C^2G(s).
}
\]

Thus the same squared longitudinal bisector coordinate `C^2` simultaneously rescales

1. the AGM geometric scale `H`;
2. the balanced-return Green completion `G`.

Their ratio is preserved.

This is a direct answer to the #1161 question of what is preserved by the arithmetic/geometric dual coarse-graining: beyond the cone equation, the dual update preserves a branch-return Green/scale ratio.

## 5. Limit value of the invariant

As the AGM converges,

\[
s_n\to0,
\qquad
G(s_n)\to G(0)=1,
\qquad
H_n\to H_\infty=2M.
\]

Therefore

\[
\boxed{
\mathcal I_{\rm ret}
=\frac1{H_\infty}
=\frac1{2M}.
}
\]

Equivalently, at every finite step,

\[
\boxed{
H_\infty=\frac{H_n}{G(s_n)}.
}
\]

For a general initial pair `(a,b)`, this supplies the common AGM scale from the finite branch-return Green readout of its normalized contrast.

In symmetric pair variables

\[
h=\frac{a+b}{2},
\qquad
s=\frac{a-b}{a+b},
\]

one has

\[
\boxed{
\frac1{M(a,b)}
=\frac1hG(s)
=\frac{2}{a+b}
G\left(\frac{a-b}{a+b}\right).
}
\]

This is the reciprocal-AGM relation expressed entirely through the balanced-return completion.

## 6. Finite truncation certificate

Define the finite return polynomial

\[
G_N(s)=\sum_{n=0}^N c_ns^{2n}.
\]

Since `0<c_n<=1`,

\[
0<G(s)-G_N(s)
\le
\sum_{n=N+1}^\infty s^{2n}
=
\boxed{
\frac{s^{2N+2}}{1-s^2}.
}
\]

Thus the RG invariant has a finite branch certificate at every finite truncation depth.

For the standard Gauss–Legendre seed,

\[
s_0=3-2\sqrt2<1/4,
\]

so already at the initial state

\[
0<G(s_0)-G_N(s_0)
<
\frac{16}{15}\,4^{-2N-2}.
\]

After each AGM step, `s_n` contracts quadratically, making the same finite return polynomial rapidly more accurate.

## 7. Relation to a square-lattice return Green function

The coefficients `c_n` are also the standard return probabilities at time `2n` for a two-dimensional simple symmetric square-lattice walk (equivalently, for two coupled binary balance coordinates after an elementary linear relabeling). Hence `G` is a square-lattice return Green generating readout after the even-time variable is used.

This lattice-Green/AGM relation has classical prior literature; no historical novelty is claimed for that association. The #1161 contribution is the typed integration with the existing finite Weighted-BRC return carrier, the Viète-bisector square factorization, the chord-loss state, and the independent #1159 rotation-completion normalization.

## 8. Scope

Freeze at free-research-result strength:

`BALANCED_RETURN_GREEN G(s) = DERIVED COMPLETION OF FINITE POSITIVE-RATIONAL BRANCH MASSES`.

`G(s+)/G(s) = H+/H = C^2 = EXACT`.

`G(s)/H = EXACT AGM RG INVARIANT`.

`FINITE G_N TAIL CERTIFICATE = PROVED`.

`RETURN_GREEN_INVARIANT != N0_CELL_PRIMITIVE`.

`FULL CELL-LEVEL COARSE-GRAINING REALIZATION = STILL OPEN`.
