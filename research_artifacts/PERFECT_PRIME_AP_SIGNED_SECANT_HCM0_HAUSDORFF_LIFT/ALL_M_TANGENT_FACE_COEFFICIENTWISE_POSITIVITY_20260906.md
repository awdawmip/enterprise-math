# Perfect Prime AP HCM0 — all-m tangent-face coefficientwise positivity

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260906T2125`  
Date: 2026-09-06  
Status: **ALL-m POSITIVE FACE THEOREM — FULL M6 / HCM0 REMAIN OPEN**

## 1. Setup

Put `n=m-1`. For an actual initial layer `S>=0` and first positive block length `a>0`, let

\[
r_0=mS,\qquad r=m(S+a).
\]

For a second increment `c>=0`, write

\[
s(c)=m(S+a+c).
\]

Let

\[
\mathcal H_b=(mb)^{-2}Q_{mS,m(S+b)}
\]

be the normalized synchronized quotient form. Define

\[
T_m(S,a,c)
:=\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-n.
\]

Then `T_m(S,a,0)=0`.

The finite `m=3,4,5,6` certificates show

\[
T_m(S,a,c)=c\times\frac{\text{positive polynomial}}{\text{positive denominator}}.
\]

This note proves the entire `c^0` numerator face positive for every `m`.

## 2. Tangent trace equals a log-determinant derivative

At `c=0`, the two normalized forms coincide. Therefore

\[
\left.\frac{\partial T_m}{\partial c}\right|_{c=0}
=-\operatorname{tr}\left(
\mathcal H_a^{-1}
\left.\frac{\partial\mathcal H_{a+c}}{\partial c}\right|_{c=0}
\right)
=-\left.\frac{d}{dc}\log|\det\mathcal H_{a+c}|\right|_{c=0}.
\tag{2.1}
\]

The normalized translation matrix has determinant one, so `det Hcal_b` depends on `b` only through the terminal Pascal/Hausdorff metric. The frozen determinant formula is, up to a positive `m`-dependent constant,

\[
|\det H_r|
\propto
\frac{\Delta^nF(r)}{\prod_{j=0}^{n}F(r+j)},
\tag{2.2}
\]

where

\[
F(r)=\mu_r^{-1}
=\frac1{(m-1)!}\prod_{k=1}^{m}(mr+k)
\]

and

\[
\Delta^nF(r)=m^m\left(mr+\frac{m^2+1}{2}\right).
\tag{2.3}
\]

## 3. The contiguous m^2 block

Put

\[
M=m^2,\qquad x=mr=m^2(S+a),\qquad \beta=\frac{M+1}{2}.
\]

Then

\[
\prod_{j=0}^{n}F(r+j)
=\frac1{((m-1)!)^m}
\prod_{k=1}^{M}(x+k).
\]

Define

\[
G_M(x)=\prod_{k=1}^{M}(x+k).
\tag{3.1}
\]

Since `dr/dc=m` at the tangent point, (2.1)-(2.3) give

\[
\boxed{
\left.\frac{\partial T_m}{\partial c}\right|_{c=0}
=m^2\left(
\frac{G_M'(x)}{G_M(x)}-\frac1{x+\beta}
\right).
}
\tag{3.2}
\]

Therefore, after multiplication by the positive denominator `(x+beta)G_M(x)`, the tangent numerator is exactly, up to the positive factor `m^2`,

\[
\boxed{
A_M(x)=(x+\beta)G_M'(x)-G_M(x).
}
\tag{3.3}
\]

## 4. All coefficients of A_M are strictly positive

Write

\[
G_M(x)=\sum_{d=0}^{M}g_d x^d.
\]

Because `G_M` is a product of positive-affine factors `x+k`,

\[
g_d>0\qquad(0\le d\le M).
\]

For `0<=d<M`, the coefficient of `x^d` in (3.3) is

\[
\boxed{
a_d=(d-1)g_d+\beta(d+1)g_{d+1}.}
\tag{4.1}
\]

The leading coefficient is

\[
a_M=(M-1)g_M>0.
\]

For `d>=1`, (4.1) is immediately positive: at `d=1` the first term vanishes and the second is positive; for `d>=2` both are nonnegative and the second is strict.

For `d=0`,

\[
a_0=-g_0+\beta g_1.
\]

But

\[
\frac{g_1}{g_0}=\sum_{k=1}^{M}\frac1k=H_M,
\]

so

\[
\boxed{
a_0=g_0(\beta H_M-1)>0.}
\tag{4.2}
\]

Indeed `m>=2` gives `M=m^2>=4`, hence `beta>1` and `H_M>1`.

Thus:

### Theorem 4.1 — all-m positive tangent face

For every `m>=2`, all coefficients of

\[
A_{m^2}(x)
=\left(x+\frac{m^2+1}{2}\right)
\frac{d}{dx}\prod_{k=1}^{m^2}(x+k)
-\prod_{k=1}^{m^2}(x+k)
\]

are strictly positive.

Since

\[
x=m^2(S+a),
\]

expanding `x^d=m^{2d}(S+a)^d` shows that every monomial coefficient in the two variables `(S,a)` is also strictly positive.

## 5. Meaning for the finite P_m certificates

Let `P_m(a,c,S)` denote the oriented polynomial numerator appearing after the common positive factors are removed from `T_m/c`, as in the exact `m=3,4,5,6` certificates.

Theorem 4.1 proves, for every `m`, that the entire face

\[
P_m(a,0,S)
\]

is coefficientwise strictly positive. In particular it has every possible monomial

\[
S^u a^v,\qquad u,v\ge0,\quad u+v\le m^2,
\]

with positive coefficient. Hence this face contains exactly

\[
\boxed{\binom{m^2+2}{2}}
\]

nonzero monomials.

At `m=6`, this gives `binom(38,2)=703`, exactly the observed full `c=0` slice of the 6214-term certificate.

## 6. BRC interpretation

This theorem uses the BRC observer discipline without violating the signed boundary.

The contiguous `m^2` factors

\[
\{x+1,\ldots,x+m^2\}
\]

are retained as labeled denominator-block provenance. The signed determinant cancellation is first resolved through the exact log-determinant identity. Only then is the resulting polynomial expanded into positive affine-factor branches. No positive-weight BRC total is substituted for a signed determinant.

## 7. Boundary and next target

Proved all `m` here:

- exact tangent identity (3.2);
- coefficientwise positivity of the full `c=0` numerator face;
- full monomial support of that face.

Still open:

- coefficientwise positivity of the `c^j` faces for `j>=1`;
- the full all-m M6 trace inequality;
- other three-support mixed coefficients;
- HCM0 and parent determinant nonvanishing.

The next deterministic step is to differentiate the inverse/trace identity one further order and determine whether the `c^1` numerator face also admits a dimension-free positive contiguous-block formula. If successful, this starts an induction over the observed finite range `0<=deg_c<=2m-1`.