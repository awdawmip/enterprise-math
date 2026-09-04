# Internal phase quantization and a log-free Euler-product route for #1159

Status: `FREE_RESEARCH / NEW INTERNAL ANALYTIC STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 0. Why this note exists

The original #1159 theorem packet proves the Euler sine product by combining finite Dirichlet determinants, fixed-mode convergence, and a logarithmic tail estimate. A fresh audit finds two improvements:

1. the finite mode quantization can be derived directly from the project-internal power-series rotation law `(S,C,tau)`, with no Chebyshev polynomial and no classical `pi` in the proof;
2. the logarithmic tail estimate is unnecessary. A direct product-defect estimate is simpler, stronger, and exposes a missing domain condition in the old tail-log statement.

The classical Chebyshev/cosine formulas remain valid as a downstream finite compatibility readout, but they are no longer needed for the internal Euler-product proof.

## 1. Internal rotation law

Let

\[
S(x)=\sum_{j\ge0}\frac{(-1)^j x^{2j+1}}{(2j+1)!},
\qquad
C(x)=\sum_{j\ge0}\frac{(-1)^j x^{2j}}{(2j)!}.
\]

Use only the internally proved power-series laws

\[
S'=C,\qquad C'=-S,
\]

\[
S(x+y)=S(x)C(y)+C(x)S(y),
\]

\[
C(x+y)=C(x)C(y)-S(x)S(y),
\]

\[
S(x)^2+C(x)^2=1.
\]

Let `tau` be the first positive zero of `S`.

From first-zero minimality and `S'(0)=1`,

\[
S(x)>0\qquad(0<x<\tau).
\]

Since

\[
0=S(\tau)=2S(\tau/2)C(\tau/2)
\]

and `S(tau/2)>0`,

\[
C(\tau/2)=0,
\qquad
S(\tau/2)=1.
\]

Hence

\[
C(\tau)=C(\tau/2)^2-S(\tau/2)^2=-1.
\]

The addition laws then give for every integer `m>=0`

\[
\boxed{
S(m\tau)=0,
\qquad
C(m\tau)=(-1)^m.
}
\]

## 2. A recurrence identity that quantizes the finite spectrum internally

Let the recurrence-level Dirichlet continuant be

\[
D_0(u)=1,
\qquad
D_1(u)=2-u,
\]

\[
D_{n+2}(u)=(2-u)D_{n+1}(u)-D_n(u).
\]

For every real `theta` and integer `n>=0`, define

\[
u(\theta)=2-2C(\theta).
\]

Then

\[
2-u(\theta)=2C(\theta).
\]

The sine addition law implies the same second-order recurrence

\[
S((n+2)\theta)
=2C(\theta)S((n+1)\theta)-S(n\theta).
\]

Matching the two initial values gives the exact identity

\[
\boxed{
D_n(2-2C(\theta))\,S(\theta)
=S((n+1)\theta).
}
\tag{IPQ-1}
\]

No trigonometric naming, circle spectrum, Chebyshev polynomial, or classical `pi` is used.

## 3. Internal phase quantization theorem

For `M>=2` and `1<=k<M`, set

\[
\theta_{k,M}=\frac{k\tau}{M},
\]

\[
\boxed{
u_{k,M}=2-2C(\theta_{k,M}).}
\]

Because

\[
0<\theta_{k,M}<\tau,
\]

we have `S(theta_(k,M))>0`. Applying (IPQ-1) with `n=M-1` gives

\[
D_{M-1}(u_{k,M})S(\theta_{k,M})
=S(k\tau)=0,
\]

hence

\[
\boxed{D_{M-1}(u_{k,M})=0.}
\tag{IPQ-2}
\]

Moreover, `C'=-S<0` on `(0,tau)`, so `C` is strictly decreasing there. Therefore

\[
\boxed{
0<u_{1,M}<u_{2,M}<\cdots<u_{M-1,M}<4.
}
\tag{IPQ-3}
\]

Since `D_(M-1)` has degree `M-1`, these are all finite Dirichlet roots.

This yields an internal phase quantization of the finite spectrum before classical `pi` is named.

Classification: `INTERNAL_ANALYTIC_READOUT_FROM_NATIVE_FINITE_RECURRENCE`.

## 4. Exact internal mode-radius formula

The double-angle law gives

\[
C(\theta)=1-2S(\theta/2)^2.
\]

Therefore

\[
\boxed{
u_{k,M}=4S\!\left(\frac{k\tau}{2M}\right)^2.}
\tag{IPQ-4}
\]

Because the half-phase lies in `(0,tau/2)`, `S` is positive there, hence the normalized mode radius

\[
\rho_{k,M}:=M\sqrt{u_{k,M}}
\]

satisfies exactly

\[
\boxed{
\rho_{k,M}
=2M\,S\!\left(\frac{k\tau}{2M}\right).
}
\tag{IPQ-5}
\]

Thus for every fixed `k`,

\[
\rho_{k,M}
=k\tau\,\frac{S(k\tau/(2M))}{k\tau/(2M)}
\longrightarrow k\tau.
\]

This proves fixed-mode convergence internally, without the classical cosine spectrum.

## 5. Intrinsic linear radius bounds

On `[0,tau]`, `S>=0`, so

\[
S''=-S\le0.
\]

Hence `S` is concave. Since

\[
S(0)=0,
\qquad
S(\tau/2)=1,
\]

the chord bound on `[0,tau/2]` is

\[
\boxed{
S(y)\ge \frac{2y}{\tau}
\qquad(0\le y\le\tau/2).
}
\tag{IPQ-6}
\]

Substituting `y=k tau/(2M)` into (IPQ-5) yields

\[
\boxed{\rho_{k,M}\ge2k.}
\tag{IPQ-7}
\]

There is also a useful opposite inequality. From `S^2+C^2=1`,

\[
C\le1,
\]

so `S'=C<=1` and `S(0)=0` give

\[
S(y)\le y\qquad(y\ge0\text{ in the first phase}).
\]

Thus

\[
\boxed{2k\le\rho_{k,M}\le k\tau.}
\tag{IPQ-8}
\]

In particular, evaluating `S(tau/2)=1<=tau/2` gives the target-free lower bound

\[
\boxed{\tau\ge2.}
\]

Together with the already verified rational sign certificate `tau<4`,

\[
\boxed{2\le\tau<4.}
\]

## 6. Exact finite spectral product

Because the `M-1` roots in (IPQ-2) are all roots and

\[
D_{M-1}(0)=M,
\]

the normalized continuant factorization is

\[
\boxed{
\frac{D_{M-1}(z)}{M}
=\prod_{k=1}^{M-1}
\left(1-\frac{z}{u_{k,M}}\right).
}
\tag{IPQ-9}
\]

For `z=x^2/M^2`, this is exactly

\[
\boxed{
F_M(x)
=\prod_{k=1}^{M-1}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right).
}
\tag{IPQ-10}
\]

So the finite determinant is already a true product over internally quantized rotation modes.

## 7. Correction to the old tail-log statement

The old theorem packet stated, for real `|x|<=R` and `K>=R`,

\[
\left|
\log\prod_{k=K+1}^{M-1}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right)
\right|
\le\frac{R^2}{3K}.
\]

As written, this is missing a positivity condition on `K`. For example, if

\[
0<R<1,\qquad K=0,
\]

then `K>=R` is false if `R>0`; more generally the intended natural-number statement must explicitly prevent the zero denominator in `1/K`. The safe statement requires at least

\[
K\ge1.
\]

The log estimate is not needed anyway; the next section gives a stronger direct bound.

## 8. Stronger log-free tail-product certificate

Let

\[
T_{M,K}(x)
:=\prod_{k=K+1}^{M-1}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right).
\]

Assume

\[
R\ge0,
\qquad
K\ge1,
\qquad
2K\ge R,
\qquad
|x|\le R.
\]

For `k>K`, (IPQ-7) gives

\[
0\le
\frac{x^2}{\rho_{k,M}^2}
\le
\frac{R^2}{4k^2}
<1.
\]

Therefore every tail factor lies in `[0,1]`. The elementary finite-product defect inequality gives

\[
0\le1-T_{M,K}(x)
\le
\sum_{k=K+1}^{M-1}
\frac{x^2}{\rho_{k,M}^2}.
\]

Using `rho_(k,M)>=2k`,

\[
1-T_{M,K}(x)
\le
\frac{R^2}{4}
\sum_{k=K+1}^{M-1}\frac1{k^2}.
\]

For `k>=2`,

\[
\frac1{k^2}
\le
\frac1{k(k-1)}
=
\frac1{k-1}-\frac1k.
\]

Hence the finite sum telescopes and

\[
\sum_{k=K+1}^{M-1}\frac1{k^2}
\le\frac1K.
\]

Thus

\[
\boxed{
|1-T_{M,K}(x)|
\le\frac{R^2}{4K}.
}
\tag{IPQ-11}
\]

This is stronger and simpler than the old logarithmic `R^2/(3K)` certificate.

Classification: `EXACT_FINITE_PRODUCT_CERTIFICATE`.

## 9. Uniform head bound

For every mode,

\[
\left|1-\frac{x^2}{\rho_{k,M}^2}\right|
\le
1+\frac{R^2}{4k^2}
\le
\exp\left(\frac{R^2}{4k^2}\right).
\]

The elementary telescope

\[
\sum_{k=1}^{\infty}\frac1{k^2}\le2
\]

gives the uniform finite-head estimate

\[
\boxed{
\prod_{k=1}^{K}
\left|1-\frac{x^2}{\rho_{k,M}^2}\right|
\le e^{R^2/2}.
}
\tag{IPQ-12}
\]

Combining with (IPQ-11),

\[
\boxed{
\left|
F_M(x)-
\prod_{k=1}^{K}
\left(1-\frac{x^2}{\rho_{k,M}^2}\right)
\right|
\le
 e^{R^2/2}\frac{R^2}{4K}.
}
\tag{IPQ-13}
\]

uniformly for `|x|<=R`, `K>=1`, `2K>=R`, and `M>K+1`.

## 10. Euler product with an explicit compact tail rate

WSR-T02 already gives compact convergence

\[
F_M\to F,
\qquad
F(x)=\frac{S(x)}x
\]

with the normalized value `F(0)=1`.

For every fixed `K`, (IPQ-5) gives

\[
\rho_{k,M}\to k\tau
\qquad(k=1,\dots,K),
\]

so the finite head in (IPQ-13) converges uniformly on `|x|<=R` to

\[
P_K(x)
:=
\prod_{k=1}^{K}
\left(1-\frac{x^2}{k^2\tau^2}\right).
\]

Taking `M->infinity` in (IPQ-13) yields

\[
\boxed{
\sup_{|x|\le R}
|F(x)-P_K(x)|
\le
 e^{R^2/2}\frac{R^2}{4K},
}
\tag{IPQ-14}
\]

for `K>=1` and `2K>=R`.

Therefore

\[
\boxed{
\frac{S(x)}x
=
\prod_{k=1}^{\infty}
\left(1-\frac{x^2}{k^2\tau^2}\right)
}
\]

locally uniformly in `x`.

This proves WSR-T04 internally without classical `pi` and without logarithmic tail estimates.

## 11. Wallis readout remains internal

At `x=tau/2`,

\[
S(\tau/2)=1,
\]

so

\[
\frac{2}{\tau}
=
\prod_{k=1}^{\infty}
\left(1-\frac1{4k^2}\right).
\]

The right-hand side is the inverse Wallis product. Thus

\[
\boxed{
\tau=2W_\infty.
}
\]

Again, the equality is obtained before naming `tau` as classical `pi`.

## 12. Research consequence

The stronger structural route is now

```text
finite integer/rational Dirichlet recurrence
    -> compact coefficient completion S,C
    -> first positive phase tau
    -> internal phase quantization u_(k,M)=2-2C(k tau/M)
    -> exact mode radii rho_(k,M)=2M S(k tau/(2M))
    -> intrinsic linear bound rho_(k,M)>=2k
    -> exact finite spectral product
    -> log-free finite tail defect
    -> locally uniform Euler product
    -> Wallis readout at tau/2
```

The classical Chebyshev/cosine spectrum is demoted to a compatibility theorem:

`CLASSICAL_CHEBYSHEV_READOUT != NATIVE_EULER_PRODUCT_INPUT`.

Freeze at free-research strength:

`INTERNAL_PHASE_QUANTIZATION -> EXACT_FINITE_SPECTRUM`.

`FINITE_PRODUCT_DEFECT -> LOG_FREE_EULER_COMPLETION`.

`TAU = 2 W_INFINITY BEFORE CLASSICAL_PI_NAMING`.
