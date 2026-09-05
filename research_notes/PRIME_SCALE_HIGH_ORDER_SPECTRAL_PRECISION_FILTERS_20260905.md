# Prime-scale high-order spectral precision filters

Status: `FREE_RESEARCH / EXACT ANALYTIC-CERTIFICATE THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Extends the dyadic fourth-order certificate and arbitrary-order dyadic annihilation hierarchy.
Depends on:
- internal completion series `S` and `tau<4`;
- first-mode radius `T_q=rho_(1,q)=2q S(tau/(2q))`.

## 1. Prime-scale refinement operator

Fix an integer scale `p>=2`; prime `p` is the main spectral-generation case, but the analytic filter itself only needs integer `p>=2`.

Define

\[
T_q:=2qS\left(\frac{\tau}{2q}\right).
\]

Let

\[
(E_pf)(q):=f(pq).
\]

For level `m>=1`, define

\[
\boxed{
\mathcal A_{m,p}
:=\prod_{r=1}^{m}
\frac{p^{2r}E_p-I}{p^{2r}-1}.
}
\tag{PSF-1}

Write

\[
A_{m,p}(q):=(\mathcal A_{m,p}T)(q).
\]

## 2. Exact annihilation of the first m even error modes

Set

\[
y=\frac{\tau}{2q},
\qquad
F(y)=\frac{S(y)}y
=\sum_{s\ge0}\frac{(-1)^s y^{2s}}{(2s+1)!}.
\]

Then

\[
T_q=\tau F(y),
\]

and `E_p` acts on `y^(2s)` by eigenvalue `p^(-2s)`.

Hence the level-`m` filter multiplier on the `s`-th correction mode is

\[
\lambda_{m,p}(s)
:=\prod_{r=1}^{m}
\frac{p^{2(r-s)}-1}{p^{2r}-1}.
\]

Therefore

\[
\boxed{
\lambda_{m,p}(0)=1,
\qquad
\lambda_{m,p}(s)=0\quad(1\le s\le m).
}
\tag{PSF-2}

So `A_(m,p)` kills exactly the first `m` finite-resolution modes

\[
q^{-2},q^{-4},\ldots,q^{-2m}.
\]

## 3. Residual series and sign

For `s>m`, define the positive number

\[
b_s
:=(-1)^m\lambda_{m,p}(s)
=\prod_{r=1}^{m}
\frac{1-p^{-2(s-r)}}{p^{2r}-1}>0.
\]

Then

\[
\boxed{
\frac{A_{m,p}(q)}\tau
=
1+\sum_{s=m+1}^{\infty}
(-1)^{s+m}
 b_s\frac{y^{2s}}{(2s+1)!}.
}
\tag{PSF-3}

The first residual coefficient simplifies completely:

\[
\boxed{
b_{m+1}=p^{-m(m+1)}.}
\tag{PSF-4}

Indeed the numerator product is `prod_(j=1)^m(1-p^(-2j))`, which cancels the denominator product after extracting `p^(-2 sum j)`.

The coefficient ratio telescopes:

\[
\boxed{
\frac{b_{s+1}}{b_s}
=
\frac{1-p^{-2s}}
{1-p^{-2(s-m)}}
<\frac1{1-p^{-2}}
\le\frac43.
}
\tag{PSF-5}

Since `tau<4` and `q>=1`, `0<y<2`.  Therefore consecutive absolute residual terms satisfy

\[
\frac{\text{term}_{s+1}}{\text{term}_s}
<
\frac43\frac{4}{(2s+2)(2s+3)}<1
\]

for `s>=m+1>=2`.

Thus (PSF-3) is a strictly alternating decreasing tail beginning with a negative term.

## 4. Arbitrary-order one-sided lower certificate

The alternating remainder theorem gives

\[
\boxed{
A_{m,p}(q)<\tau
}
\tag{PSF-6}

and

\[
0<\tau-A_{m,p}(q)
<\tau\,b_{m+1}
\frac{y^{2m+2}}{(2m+3)!}.
\]

Using (PSF-4) and `y=tau/(2q)`:

\[
\boxed{
0<\tau-A_{m,p}(q)
<
\frac{
\tau^{2m+3}
}{
2^{2m+2}(2m+3)!\,
p^{m(m+1)}q^{2m+2}
}.
}
\tag{PSF-7}

Finally `tau<4` removes the unknown target from the right side:

\[
\boxed{
0<\tau-A_{m,p}(q)
<
\frac{
2^{2m+4}
}{
p^{m(m+1)}(2m+3)!\,q^{2m+2}
}.
}
\tag{PSF-8}

This is an arbitrary-order target-free finite completion certificate.

### recovery of WSR-T12

For `p=2,m=1`,

\[
A_{1,2}(q)=\frac{4T_{2q}-T_q}{3},
\]

and (PSF-8) becomes

\[
0<\tau-A_{1,2}(q)<\frac{2}{15q^4},
\]

exactly the previous quartic certificate.

## 5. Closed linear-combination weights

Expanding (PSF-1),

\[
\boxed{
A_{m,p}(q)
=\sum_{j=0}^{m}w_{m,j}^{(p)}T_{p^jq},
}
\tag{PSF-9}

where

\[
\boxed{
w_{m,j}^{(p)}
=(-1)^{m-j}
\frac{
p^{j(j+1)}
}{
\displaystyle
\prod_{r=1}^{j}(p^{2r}-1)
\prod_{r=1}^{m-j}(p^{2r}-1)
}.
}
\tag{PSF-10}

This follows from the q-binomial identity for elementary symmetric polynomials of

\[
p^2,p^4,\ldots,p^{2m}.
\]

The weights sum to one, as required by exact preservation of the constant mode.

## 6. Exact condition number

The worst-case linear input-noise amplification is

\[
\kappa_{m,p}:=\sum_{j=0}^{m}|w_{m,j}^{(p)}|.
\]

Replacing all minus signs by plus signs in the factorized operator polynomial gives

\[
\boxed{
\kappa_{m,p}
=
\prod_{r=1}^{m}
\frac{p^{2r}+1}{p^{2r}-1}.
}
\tag{PSF-11}

For fixed `m`, every factor decreases with `p`.  Hence the worst integer scale is `p=2`.  The already proved dyadic bound gives

\[
\boxed{
\kappa_{m,p}\le\kappa_{m,2}<2
\qquad(p\ge2).
}
\tag{PSF-12}

Thus arbitrary-order extrapolation remains uniformly well conditioned at the level of coefficient l1 norm.

## 7. Monotonicity in resolution

Let

\[
e_{m,p}(y):=1-A_{m,p}(q)/\tau,
\qquad y=\tau/(2q).
\]

Differentiate the alternating residual series.  The ratio of consecutive absolute derivative terms is

\[
\frac{b_{s+1}}{b_s}
\frac{y^2}{2s(2s+3)}
<1
\]

for `0<y<2` and `s>=m+1>=2`.

The derivative tail begins positive, hence

\[
\boxed{e_{m,p}'(y)>0.}
\tag{PSF-13}

Since increasing `q` decreases `y`,

\[
\boxed{
A_{m,p}(q)<A_{m,p}(pq)<\tau.
}
\tag{PSF-14}

## 8. Monotonicity in annihilation order

The filters obey

\[
A_{m+1,p}(q)
=
\frac{
p^{2m+2}A_{m,p}(pq)-A_{m,p}(q)
}{p^{2m+2}-1}.
\]

Therefore

\[
A_{m+1,p}(q)-A_{m,p}(q)
=
\frac{p^{2m+2}}{p^{2m+2}-1}
\bigl(A_{m,p}(pq)-A_{m,p}(q)\bigr)>0.
\]

So

\[
\boxed{
A_{m,p}(q)<A_{m+1,p}(q)<\tau.
}
\tag{PSF-15}

The two coordinates `(resolution q, annihilation order m)` form a monotone lower-approximation lattice.

## 9. Scale-step tradeoff and why p=2 remains special

At fixed base `q` and filter order `m`, larger `p` improves both the explicit error factor `p^(-m(m+1))` and the condition number.

But the finest evaluated scale is

\[
Q=p^m q.
\]

Express (PSF-7) in terms of fixed `Q`:

\[
q=Q/p^m,
\]

so the p-dependent factor becomes

\[
p^{-m(m+1)}q^{-2m-2}
=
\frac{p^{m(m+1)}}{Q^{2m+2}}.
\]

Hence at fixed finest physical resolution `Q`, the smallest admissible integer scale `p=2` minimizes the error bound.

Thus:

\[
\boxed{
\text{fixed number of steps: larger p is more accurate and better conditioned},
}
\]

but

\[
\boxed{
\text{fixed finest resolution: p=2 is resolution-efficient optimal}.
}
\tag{PSF-16}

Dyadic refinement is additionally special because its inverse phase step is quadratic and produces nested square roots, whereas odd-prime inverse steps have algebraic degree `p`.

## 10. Interpretation

The earlier fourth-order Richardson formula is now the first point of a three-parameter hierarchy:

```text
prime/scale p
x annihilation order m
x base finite resolution q
```

All members preserve the same internal completion target and have an explicit target-free one-sided certificate.

Freeze:

`DYADIC_QUARTIC_CERTIFICATE = (p=2,m=1) OF PRIME_SCALE_HIERARCHY`.

`PRIME_SCALE_FILTER KILLS FIRST m EVEN RESOLUTION MODES`.

`PRIME_SCALE_FILTER IS UNIFORMLY WELL CONDITIONED`.

`p=2 = RESOLUTION-EFFICIENT + QUADRATIC-INVERSE SPECIAL CASE`.
