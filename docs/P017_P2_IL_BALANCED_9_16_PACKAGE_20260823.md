# P017 — Balanced `d=9/16` Iwaniec–Laborde Square-P2 Parameter Package

Status: `PROVED PARAMETER SPECIALIZATION + NUMERICAL MAIN-TERM CERTIFICATE / NOT AN EXPLICIT P2 THEOREM / NOT CANONICAL`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

## 1. Motivation

For the square-window specialization `theta=1/2`, two distinct power-level constraints survive after the earlier route simplifications.

### Section 5 bilinear remainder

After Iwaniec–Laborde's circle-method rearrangement, the base exponent pair `(1/2,1/2)` allows

\[
D\le x^{5/8-o(1)}.
\]

Thus a choice `D=x^d` has section-5 power slack

\[
\Delta_5=\frac58-d.
\]

### Section 6 two-dimensional Selberg tail

The legal Selberg level is capped by `D1<=z^2`, with `z=D^(1/6)`.  The leading section-6 remainder term has exponent `d/3+1/4` against the square-window main scale `x^(1/2)`, so its power slack is

\[
\Delta_6=\frac14-\frac d3.
\]

Balancing these two slacks gives

\[
\frac58-d=\frac14-\frac d3,
\]

hence

\[
\boxed{d=\frac9{16}}.
\]

At this choice

\[
\boxed{\Delta_5=\Delta_6=\frac1{16}}.
\]

This is the natural balanced level for an explicit square-window implementation of the 1981 architecture with the base exponent pair.

## 2. Derived exact exponents

Set

\[
\boxed{D=x^{9/16}}.
\]

Then

\[
\alpha=2d-1=\frac18,
\qquad
z=D^{1/6}=x^{3/32},
\qquad
z^2=x^{3/16}.
\]

Taking the long bilinear variable at the square-root scale gives

\[
M\asymp x^{1/2},
\qquad
N\asymp\frac DM=x^{1/16}.
\]

Thus at the modern finite-computation splice point

\[
x_0=10^{31},
\]

one has

\[
\boxed{x_0^{1/16}=10^{31/16}\approx86.5964.}
\]

The same numerical factor is the bare power separation from both section-5 and section-6 ceilings at `x0`:

\[
\boxed{x_0^{\Delta_5}=x_0^{\Delta_6}\approx86.5964.}
\]

This is not by itself an explicit error bound; it is the correct scale against which the hidden constants must be audited.

## 3. Corrected legal main-term function

With `theta=1/2`, `a=6`, and the section-6 cap `D1=z^(2-o(1))`, the corrected square main coefficient is

\[
G_{\rm sq}(b,c;d)=
B_1(c-b)+B_2
-\frac c6\log\frac6{1+\alpha}
-\frac{6-c}{6}\log\frac{6\alpha}{1+\alpha}
-\frac12\left(c-\frac3d\right)^2,
\]

where

\[
b=\frac6d-1-c,
\qquad
\alpha=2d-1.
\]

For fixed `d`, this is a concave quadratic in `c`.  Differentiating gives the exact optimizing coordinate

\[
\boxed{
c_*(d)=\frac3d+2B_1+\frac16\log(2d-1).
}
\]

At `d=9/16`, using the numerical Laborde constants reconstructed from the printed 1981 critical point,

\[
B_1\approx0.24330709,
\qquad
B_2\approx1.33820429,
\]

gives

\[
\boxed{
 c_*\approx5.47337392,
 \qquad
 b_*\approx4.19329274,
 \qquad
 G_{\rm sq}\approx0.14838969.
}
\]

The required order conditions hold with wide room:

\[
3<b_*<\frac3d<c_*<6.
\]

The corresponding prime-weight endpoints have exponents

\[
D^{b/6}=x^{0.393121\ldots},
\qquad
D^{c/6}=x^{0.513129\ldots},
\]

so the special section-6 high-prime tail only extends a shallow distance beyond the square-root line.

## 4. Main-weight scale

The final 1981 normalization is

\[
W(\mathcal A)
\gtrsim
\frac{y}{\log D}
\frac{12}{2c-b-1}
G_{\rm sq},
\]

before explicit remainder deductions.

At the balanced point,

\[
\frac{12}{2c-b-1}\approx2.08570,
\]

so the reproduced positive main coefficient is approximately

\[
0.30950\frac{y}{\log D}
\approx
\boxed{0.55022\frac{y}{\log x}}.
\]

This is a large main-term budget compared with the near-critical `theta=0.45` proof.

## 5. Robustness to printed-value reconstruction

The constants `B1,B2` above are reconstructed from printed decimal data and are therefore not yet certified constants for an explicit theorem.

As a numerical robustness test, allow the 1981 printed critical data to vary over the deliberately broad box

\[
5.182\le c_0\le5.184,
\quad
4.869\le b_0\le4.871,
\quad
0.0017\le G_0\le0.0019.
\]

Using the resulting rectangular envelope for `B1,B2` and fixing the simple square parameter

\[
c=5.4734,
\]

the corrected square coefficient still satisfies

\[
\boxed{G_{\rm sq}>0.1475.}
\]

Thus printed-rounding uncertainty is not the load-bearing issue.

## 6. Why this point is preferable to `d=5/9`

The earlier reference choice `d=5/9` has a larger short variable and asymmetric analytic margins.  The balanced point `9/16` gives simultaneously:

\[
\Delta_5=\Delta_6=1/16,
\]

while also increasing the corrected main coefficient from about `0.1221` to about `0.1484`.

It therefore dominates `5/9` as the default explicit-engineering point unless later constant-level calculations reveal a different optimum.

## 7. P017-specific hybrid implementation

The intended explicit implementation should not copy the 1981 smoothing wholesale.  For the exact square basin

\[
H_d(K)=\frac{2K}{d}+r_K(d),\qquad |r_K(d)|<1,
\]

and

\[
r_K(d)=\psi(K^2/d)-\psi((K^2+2K)/d).
\]

Hence split the sieve remainder at a chosen `D0`:

- `d<=D0`: retain the exact sharp count and use the absolute bound `|r_K(d)|<1`;
- `D0<d<=D`: invoke the Iwaniec bilinear factorization only for the deep tail;
- estimate the deep tail directly from the exact sharp sawtooth difference rather than a `C^infty` smoothing whenever this reduces explicit constants.

At `x=10^31` and `d=9/16`, the global short bilinear variable has scale below `87`, making a blockwise rather than worst-case logarithmic audit especially attractive.

## 8. Remaining load-bearing problem

This package does not prove the desired explicit splice.

The remaining question is finite and quantitative:

> after replacing the 1981 `O`, `<<`, global `x^epsilon`, smoothing and worst-block summations by explicit blockwise constants, is the total section-5 + section-6 + linear-sieve error below the roughly `0.148` normalized Laborde margin for every `x>=10^31`?

The next proof engineering should begin at `d=9/16` and only move `d` if the explicit constant audit demands it.
