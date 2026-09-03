# Free Research #1161 — explicit precision-doubling bound from chord/shape renormalization

Status: `FREE_RESEARCH_RESULT / EXPLICIT ERROR THEOREM / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`

## 1. Setup

Use the already-derived Gauss–Legendre cone variables

\[
H_n=a_n+b_n,\quad U_n=a_n-b_n,\quad V_n=2\sqrt{a_nb_n},
\]

\[
A_n=4t_n,\quad P_n=2^n,
\]

and normalized shape coordinates

\[
s_n=U_n/H_n,\qquad r_n=V_n/H_n,\qquad r_n^2+s_n^2=1.
\]

The exact shape recursion is

\[
s_{n+1}=\frac{s_n^2}{(1+r_n)^2}.
\]

For the standard seed,

\[
q:=s_0=3-2\sqrt2.
\]

The endogenous target is

\[
\Pi_*:=H_\infty^2/A_\infty,
\]

and the monotone lower readout is

\[
R_n=H_n^2/A_n.
\]

Define defect mass

\[
\delta_n=P_nU_n^2=P_nH_n^2s_n^2.
\]

## 2. Rational bounds on the seed shape

One has

\[
\boxed{\frac16<q<\frac14}.
\]

For the lower inequality,

\[
3-2\sqrt2>1/6
\iff
17/6>2\sqrt2,
\]

and both sides are positive while

\[
(17/6)^2=289/36>288/36=8.
\]

For the upper inequality,

\[
3-2\sqrt2<1/4
\iff
11/4<2\sqrt2,
\]

and

\[
(11/4)^2=121/16<128/16=8.
\]

Thus these bounds use only exact rational square comparisons.

## 3. Uniform strengthening of the quadratic shape contraction

The shape sequence decreases, so `s_n<=q<1/4`. Hence

\[
r_n^2=1-s_n^2>1-1/16=15/16.
\]

Since `r_n>0`, this implies in particular

\[
r_n>15/16,
\]

because `(15/16)^2<15/16`.

Therefore

\[
(1+r_n)^2>(31/16)^2=961/256>15/4.
\]

Substitution into the exact shape recursion gives

\[
\boxed{
s_{n+1}<\frac4{15}s_n^2.
}
\]

Induction yields the closed double-exponential bound

\[
\boxed{
s_n<\frac{15}{4}\left(\frac{4q}{15}\right)^{2^n}.
}
\]

Since `q<1/4`,

\[
\boxed{
s_n<\frac{15}{4}\,15^{-2^n}.}
\]

This is a direct quantitative expression of the chord/shape squaring mechanism.

## 4. A uniform positive denominator certificate

Let

\[
B_n:=A_n-2\delta_n.
\]

The exact defect scaling law is

\[
2\delta_{n+1}=s_{n+1}\delta_n.
\]

Hence

\[
B_{n+1}
=A_n-\delta_n-2\delta_{n+1}
=B_n+\delta_n(1-s_{n+1})
>B_n.
\]

So

\[
B_n\ge B_0.
\]

Now

\[
B_0=1-2(1-2^{-1/2})^2=2\sqrt2-2,
\]

and

\[
B_0^2=4(3-2\sqrt2)=4q>2/3.
\]

Thus

\[
\boxed{A_nB_n>B_0^2>2/3.}
\]

Also

\[
H_n\le H_0=1+1/\sqrt2,
\]

and using `q=(sqrt2-1)^2`,

\[
H_0^2=\frac1{2q}<3
\]

because `q>1/6`.

## 5. Explicit error theorem

The finite certificate gives

\[
\Pi_*\le\frac{H_n^2}{A_n-2\delta_n}=\frac{H_n^2}{B_n},
\]

while monotonicity gives

\[
R_n=\frac{H_n^2}{A_n}<\Pi_*.
\]

Therefore

\[
0<\Pi_*-R_n
<
\frac{H_n^2}{B_n}-\frac{H_n^2}{A_n}
=
\frac{2H_n^2\delta_n}{A_nB_n}.
\]

Using

\[
H_n^2<3,
\qquad
\delta_n=P_nH_n^2s_n^2<3P_ns_n^2,
\qquad
A_nB_n>2/3,
\]

one obtains

\[
\boxed{
0<\Pi_*-R_n<27P_ns_n^2.
}
\]

Since `P_n=2^n` and

\[
s_n^2<\frac{225}{16}\,15^{-2^{n+1}},
\]

we get the explicit no-pi bound

\[
\boxed{
0<\Pi_*-R_n
<\frac{6075}{16}\,2^n\,15^{-2^{n+1}}.
}
\]

Finally,

\[
\frac{6075}{16}<512=2^9,
\]

and

\[
15^{2^{n+1}}=(15^2)^{2^n}>128^{2^n}=2^{7\cdot2^n},
\]

because `15^2=225>128`.

Therefore the completely binary form is

\[
\boxed{
0<\Pi_*-R_n
<2^{-\left(7\cdot2^n-n-9\right)}.
}
\]

For small `n` the exponent may be weak, but asymptotically it makes the precision doubling explicit.

## 6. Precision consequence

Define absolute binary precision of a certified lower readout by

\[
\operatorname{AbsPrec}_2(R_n;\Pi_*)
=
\max\{m\in\mathbb N_0:\Pi_*-R_n<2^{-m}\}.
\]

Whenever `7*2^n-n-9>=0`, the theorem gives

\[
\boxed{
\operatorname{AbsPrec}_2(R_n;\Pi_*)
\ge 7\cdot2^n-n-9.
}
\]

Thus the Enterprise #1161 mechanism does not merely inherit the phrase `quadratic convergence`: its normalized rotation/chord defect squaring produces a concrete endogenous lower bound on certified precision growth.

The stronger task-local interval checker empirically/certifiably gives substantially more digits at the first few steps (2, 7, 18, 39 decimal places for steps 1..4), but those values are not used to prove this theorem.

## 7. Typing

This theorem is entirely internal to the exact derived cone/defect recursion and its integer precision readout. It does not identify `Pi_*` with classical pi.

Freeze only at free-research-result strength:

`CHORD_SHAPE_SQUARING -> EXPLICIT_DOUBLE_EXPONENTIAL_ERROR_BOUND`.

`ABS_BINARY_PRECISION_LOWER_BOUND = 7*2^n-n-9` when nonnegative.

`PI_STAR_EQUALS_CLASSICAL_PI = ANALYTIC_COMPLETION`.
