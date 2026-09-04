# Half-integer telescoping sharpened tail for the #1159 Euler product

Status: `FREE_RESEARCH / STRENGTHENING OF IPQ-11 / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Parent: `WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md`

Let

\[
T_{M,K}(x)
=\prod_{k=K+1}^{M-1}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right),
\]

with the internally proved mode-radius bound

\[
\rho_{k,M}\ge2k.
\]

Assume `R>=0`, `|x|<=R`, and `2K>=R`.  Then every tail factor is in `[0,1]`, and

\[
0\le1-T_{M,K}(x)
\le
\frac{R^2}{4}
\sum_{k=K+1}^{M-1}\frac1{k^2}.
\]

For every integer `k>=1`,

\[
\frac1{k-1/2}-\frac1{k+1/2}
=\frac1{k^2-1/4}
>\frac1{k^2}.
\]

Therefore the finite sum telescopes:

\[
\sum_{k=K+1}^{M-1}\frac1{k^2}
<
\frac1{K+1/2}-\frac1{M-1/2}
=
\frac{2}{2K+1}-\frac{2}{2M-1}.
\]

Hence

\[
\boxed{
0\le1-T_{M,K}(x)
<
\frac{R^2}{2}
\left(
\frac1{2K+1}-\frac1{2M-1}
\right).
}
\tag{HIT-1}
\]

In particular,

\[
\boxed{
|1-T_{M,K}(x)|
<\frac{R^2}{2(2K+1)}.
}
\tag{HIT-2}
\]

This strictly sharpens the earlier direct bound `R^2/(4K)` for `K>=1` and naturally includes the degenerate `K=R=0` case.

Combining with the uniform head estimate

\[
\prod_{k=1}^{K}
\left|1-\frac{x^2}{\rho_{k,M}^2}\right|
\le e^{R^2/2},
\]

gives

\[
\boxed{
\left|
F_M(x)-
\prod_{k=1}^{K}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right)
\right|
<
 e^{R^2/2}\frac{R^2}{2(2K+1)}.
}
\tag{HIT-3}
\]

Passing first `M->infinity` and then `K->infinity` as in the internal phase-quantization route yields the strengthened compact Euler-product rate

\[
\boxed{
\sup_{|x|\le R}
\left|
\frac{S(x)}x-
\prod_{k=1}^{K}
\left(1-\frac{x^2}{k^2\tau^2}\right)
\right|
\le
 e^{R^2/2}\frac{R^2}{2(2K+1)}
}
\]

for `2K>=R`, with the normalized value at `x=0` understood as `1`.

Freeze:

`HALF_INTEGER_TELESCOPE -> STRONGER_LOG_FREE_TAIL`.
