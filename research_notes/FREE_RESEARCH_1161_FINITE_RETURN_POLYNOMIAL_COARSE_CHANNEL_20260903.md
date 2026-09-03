# Free Research #1161 — finite return-polynomial coarse channel converging to the geometric mean

Status: `FREE_RESEARCH_RESULT / FINITE BRANCH COARSE-GRAINING SCHEME / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependency: return-invariant characterization of the geometric mean.

## 1. Finite return polynomial

The exact balanced-return Green completion is

\[
G(t)=\sum_{k\ge0}c_kt^{2k},
\qquad
c_k=\frac{\binom{2k}{k}^2}{16^k}.
\]

For finite branch depth `N`, define

\[
\boxed{
G_N(t)=\sum_{k=0}^N c_kt^{2k}.
}
\]

Every coefficient is a finite native-diamond provenance-balance mass. Thus `G_N` requires only finitely many explicit branch-count statistics.

## 2. Finite invariant-preserving shape equation

Let the current AGM pair have

\[
H=a+b,
\qquad
s=\frac{a-b}{a+b}.
\]

Fix the arithmetic coarse endpoint

\[
A=H/2.
\]

For each `N>=0`, define the finite coarse contrast `t_N` as the unique solution in `[0,s)` of

\[
\boxed{
(1+t_N)G_N(t_N)=G_N(s).
}
\]

Existence and uniqueness are immediate because

\[
K_N(t):=(1+t)G_N(t)
\]

is strictly increasing,

\[
K_N(0)=1\le G_N(s),
\]

and

\[
K_N(s)=(1+s)G_N(s)>G_N(s).
\]

For `N=0`, `G_0=1` and `t_0=0`.

For `N>=1` and `s>0`, `t_N>0`.

## 3. Exact target

The full return invariant uniquely forces

\[
\boxed{
t_*=\frac{1-r}{1+r}},
\qquad
r=\sqrt{1-s^2},
\]

because

\[
(1+t_*)G(t_*)=G(s).
\]

For the standard Gauss–Legendre orbit,

\[
s\le s_0=3-2\sqrt2<1/4.
\]

The remainder of the theorem is stated on the simple uniform domain

\[
0<s\le1/4.
\]

## 4. Every finite coarse contrast lies below the exact target

Let

\[
R_N(u)=G(u)-G_N(u)
=\sum_{k>N}c_ku^{2k}.
\]

At the exact target,

\[
\begin{aligned}
K_N(t_*)-G_N(s)
&=R_N(s)-(1+t_*)R_N(t_*).
\end{aligned}
\]

For `s<=1/4`, one has

\[
t_*\le s^2\le1/16.
\]

Hence for every `k>=1`,

\[
(1+t_*)\left(\frac{t_*}{s}\right)^{2k}
\le
\frac{17}{16}\left(\frac14\right)^2
<1.
\]

Thus each term in `R_N(s)` strictly dominates the corresponding term in `(1+t_*)R_N(t_*)`, so

\[
K_N(t_*)>G_N(s).
\]

Since `K_N` is strictly increasing and `K_N(t_N)=G_N(s)`,

\[
\boxed{t_N<t_*}.
\]

## 5. The finite contrasts increase with branch depth

At the previous root `t_N`,

\[
\begin{aligned}
&[(1+t_N)G_{N+1}(t_N)-G_{N+1}(s)]\\
&=c_{N+1}\left[(1+t_N)t_N^{2N+2}-s^{2N+2}\right].
\end{aligned}
\]

Because

\[
t_N<t_*\le s^2
\]

and `s<=1/4`,

\[
(1+t_N)(t_N/s)^{2N+2}<1.
\]

Therefore the displayed quantity is negative. The next strictly increasing function `K_{N+1}` crosses its target to the right of `t_N`:

\[
\boxed{t_{N+1}>t_N.}
\]

Hence

\[
\boxed{
0=t_0<t_1<t_2<\cdots<t_*.
}
\]

## 6. Explicit finite error certificate

At the exact target,

\[
0<K_N(t_*)-G_N(s)
\le R_N(s).
\]

Since `c_k<=1`,

\[
R_N(s)
\le
\frac{s^{2N+2}}{1-s^2}.
\]

Also

\[
K_N'(t)
=G_N(t)+(1+t)G_N'(t)
\ge1.
\]

By the mean value theorem between `t_N` and `t_*`,

\[
\boxed{
0<t_*-t_N
\le
\frac{s^{2N+2}}{1-s^2}.
}
\]

Thus a finite set of branch return coefficients produces a rigorous monotone lower approximation to the exact next shape.

## 7. Finite lower-endpoint channel

Define

\[
\boxed{
B_N
=A\frac{1-t_N}{1+t_N}.
}
\]

The map `(1-t)/(1+t)` is strictly decreasing. Since `t_N` increases to `t_*`,

\[
B_N\downarrow
A\frac{1-t_*}{1+t_*}.
\]

The exact target ratio is

\[
\frac{1-t_*}{1+t_*}=r,
\]

so

\[
\boxed{B_N\downarrow Ar=\sqrt{ab}.}
\]

Moreover the derivative magnitude of `(1-t)/(1+t)` is at most `2`, hence

\[
0<B_N-\sqrt{ab}
\le2A(t_*-t_N).
\]

Since `2A=H`,

\[
\boxed{
0<B_N-\sqrt{ab}
\le
H\frac{s^{2N+2}}{1-s^2}.
}
\]

## 8. Meaning for the native-root boundary

The exact current scalar language still does not contain an N0 operation taking an arbitrary already-irrational native length to its positive square root.

This finite return-polynomial construction gives a different route:

1. fix the arithmetic coarse endpoint;
2. compute finitely many native-diamond provenance balance counts;
3. form the rational-coefficient polynomial `G_N`;
4. choose the unique invariant-preserving finite contrast `t_N`;
5. obtain `B_N` with a rigorous monotone error certificate.

The square root `sqrt(ab)` appears only when identifying the limit `N->infinity`, not as the finite selector rule.

At finite precision, `t_N` can be isolated by ordinary integer/rational polynomial sign tests and bisection, so the construction is compatible with the existing finite-precision philosophy.

## 9. Scope

Freeze at free-research-result strength:

`FINITE_RETURN_POLYNOMIAL_COARSE_CHANNEL = DEFINED`.

`T_N INCREASES TO EXACT AGM NEXT SHAPE = PROVED on s<=1/4`.

`B_N DECREASES TO GEOMETRIC_MEAN = PROVED`.

`EXPLICIT ERROR <= H s^(2N+2)/(1-s^2) = PROVED`.

`FINITE RULE DOES NOT USE SQRT(ab) AS SELECTOR`.

`EXACT N0 GEOMETRIC-MEAN OPERATION = STILL NOT PROMOTED`.
