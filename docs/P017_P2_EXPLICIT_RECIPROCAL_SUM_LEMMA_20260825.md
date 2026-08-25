# P017 — Explicit Reciprocal-Sum Lemma for the Four-Sevenths P2 Route

Status: `PROVED_WIP EXPLICIT CONSTANT LEMMA + APPLICATION WINDOW / NOT CANONICAL / NOT YET FULL SIEVE ERROR`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- the four-sevenths B-spline package on this owner branch;
- the corrected explicit Kuzmin–Landau and second-derivative bounds in D. Patel (2021), especially the constants `2/pi` and
  \[
  2(L/V+2)(2\sqrt{W/\pi}+1).
  \]

Purpose: replace the hidden implied constant in the terminal reciprocal `m`-sum by one concrete number and verify that its frequency window already overlaps the `X=10^31` scale.

## 1. Standalone reciprocal-sum lemma

Let

\[
\rho=\frac65,
\]

let `M>=2`, and let `t>0`. Define

\[
S(M,t)=\sum_{M<m\le \rho M} e(t/m).
\]

Assume

\[
\boxed{
\rho^{4/3}M^{5/3}\le t\le \frac12M^3.
}
\]

Then

\[
\boxed{
|S(M,t)|\le15\sqrt{\frac tM}.
}
\]

### Low-frequency half

Suppose first that

\[
t\le\frac12M^2.
\]

For

\[
f(x)=t/x
\]

on `[M,rho M]`,

\[
|f'(x)|=\frac{t}{x^2}
\in
\left[\frac{t}{\rho^2M^2},\frac{t}{M^2}\right]
\subset(0,1/2].
\]

Hence the distance of `f'(x)` to the nearest integer is at least

\[
\frac{t}{\rho^2M^2}.
\]

The explicit Kuzmin–Landau bound gives

\[
|S(M,t)|
\le
\frac2\pi\frac{\rho^2M^2}{t}.
\]

The lower hypothesis on `t` is exactly strong enough to imply

\[
\frac{\rho^2M^2}{t}
\le
\sqrt{\frac tM},
\]

because after squaring this is

\[
t^3\ge\rho^4M^5.
\]

Therefore

\[
|S(M,t)|
\le\frac2\pi\sqrt{\frac tM}
<\sqrt{\frac tM}.
\]

### High-frequency half

Now suppose

\[
\frac12M^2<t\le\frac12M^3.
\]

Then

\[
f''(x)=\frac{2t}{x^3}.
\]

On `[M,rho M]`,

\[
\frac{2t}{\rho^3M^3}
\le f''(x)\le
\frac{2t}{M^3}.
\]

Thus Patel's explicit second-derivative lemma applies with

\[
W=\frac{\rho^3M^3}{2t},
\qquad
V=\frac{M^3}{2t}.
\]

The upper assumption `t<=M^3/2` gives `W>=rho^3>1`. Also the interval length is at most

\[
L=(\rho-1)M=\frac M5.
\]

Put

\[
r=\frac{t}{M^2}.
\]

Then `1/2<r<=M/2`, and the explicit lemma yields

\[
|S(M,t)|
\le
2\left(\frac{2r}{5}+2\right)
\left(2\sqrt{\frac{\rho^3M}{2\pi r}}+1\right).
\]

Divide by `sqrt(rM)=sqrt(t/M)`. The Fourier-curvature part is at most

\[
4\left(\frac25+\frac2r\right)
\sqrt{\frac{\rho^3}{2\pi}}.
\]

Since `r>=1/2`, `rho=6/5`, `pi>3`, and `sqrt(5)>11/5`,

\[
\sqrt{\frac{\rho^3}{2\pi}}
<\sqrt{\frac{36}{125}}
=\frac6{5\sqrt5}
<\frac6{11}.
\]

Hence that part is less than

\[
4\left(\frac25+4\right)\frac6{11}
=\frac{528}{55}
=9.6.
\]

The remaining part contributes

\[
\frac{4r/5+4}{\sqrt{rM}}
=\frac45\sqrt{\frac rM}
+\frac4{\sqrt{rM}}.
\]

Because `r<=M/2`, `r>=1/2`, and `M>=2`, this is less than `4.8`.

Therefore the total normalized constant is less than `14.4`, and the clean integer bound

\[
\boxed{|S(M,t)|\le15\sqrt{t/M}}
\]

follows.

## 2. Application to the balanced P017 block

Use the frozen B-spline parameters

\[
\theta=\frac{4999}{10000},
\qquad
D=X^{4/7},
\qquad
\eta=\frac1{70},
\]

and

\[
M=X^{16/35},
\qquad
N=X^{4/35}.
\]

Replace broad dyadic blocks by geometric blocks of ratio

\[
\boxed{\rho=6/5}.
\]

Thus

\[
M<m\le\rho M,
\qquad
N<n_i\le\rho N.
\]

Take the Fourier cutoff

\[
H=\frac{4D}{y}X^\eta.
\]

For an off-diagonal tuple define

\[
k=h_1n_2-h_2n_1\ne0,
\qquad
 t=\frac{|k|X}{n_1n_2}.
\]

### Lower edge

Since `|k|>=1` and `n_i<=rho N`,

\[
t\ge\frac{X}{\rho^2N^2}.
\]

The desired lower condition

\[
t\ge\rho^{4/3}M^{5/3}
\]

is therefore implied by

\[
X^{1-2(4/35)-(5/3)(16/35)}
\ge\rho^{10/3}.
\]

The exponent simplifies exactly to

\[
1-\frac8{35}-\frac{16}{21}
=\boxed{\frac1{105}}.
\]

Hence it suffices that

\[
\boxed{
X\ge\rho^{350}=\left(\frac65\right)^{350}.
}
\]

Numerically,

\[
\left(\frac65\right)^{350}
\approx5.17\times10^{27}
<10^{31}.
\]

### Upper edge

Because `|h_i|<H` and `n_i<=rho N`,

\[
|k|<2\rho HN.
\]

Therefore

\[
t<2\rho H\frac XN
=8\rho X^{d+1+\eta-\theta-\nu}.
\]

Here

\[
3\mu-(d+1+\eta-\theta-\nu)
=\boxed{\frac{3999}{10000}}.
\]

Thus `t<=M^3/2` follows once

\[
X^{3999/10000}\ge16\rho=\frac{96}{5},
\]

which requires only `X` of order `10^3` and is overwhelmingly dominated by the lower-edge condition.

Consequently, throughout every geometric off-diagonal block, for

\[
\boxed{X\ge(6/5)^{350}},
\]

the explicit reciprocal-sum estimate

\[
\boxed{
\left|
\sum_{M<m\le(6/5)M}
 e\!\left(
 \frac{kX}{mn_1n_2}
 \right)
\right|
\le
15
\sqrt{
\frac{|k|X}{Mn_1n_2}
}
}
\]

is valid.

## 3. Significance

A previous crude effectivity pressure test suggested that the generic reciprocal exponential-sum constants might themselves force an astronomical threshold. This lemma shows that conclusion was an artifact of leaving the terminal B-process constant hidden and of using coarse blocks.

The reciprocal-sum **local analytic window** is already fully effective below `10^31`.

This does not yet prove overlap of the entire P2 sieve with Campbell's finite range. The remaining constants come from:

1. counting / grouping `(n_1,n_2,h_1,h_2)` after Cauchy;
2. the number of geometric sieve blocks;
3. Rosser–Iwaniec factorization coefficients;
4. the explicit B-spline Fourier tail;
5. comparison with the certified positive main reserve `>0.145713553`.

Those are now finite bookkeeping tasks rather than a missing exponential-sum theorem at the terminal `m`-sum.

## 4. Prior-art boundary

Kuzmin–Landau, second-derivative estimates and reciprocal exponential sums are classical. The constant `15` here is only an explicit specialization/packaging for the current P017 effectivity route. No historical novelty claim is made.

## 5. Next

Propagate the constant `15` through the expanded Cauchy sum, using the arithmetic multiplicity of

\[
k=h_1n_2-h_2n_1
\]

rather than bounding all quadruples independently. The next target is an explicit block-level estimate with a concrete constant multiplying the already known power saving.
