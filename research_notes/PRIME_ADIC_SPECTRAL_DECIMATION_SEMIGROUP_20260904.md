# Prime-adic spectral decimation semigroup for finite Dirichlet chains

Status: `FREE_RESEARCH / EXACT FINITE ALGEBRAIC GENERALIZATION / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 1. Rescaled trace polynomials

Define the integer polynomials

\[
C_0(x)=2,
\qquad C_1(x)=x,
\qquad C_{n+1}(x)=xC_n(x)-C_{n-1}(x).
\]

These are the rescaled Chebyshev/Dickson trace polynomials; the recurrence definition is sufficient for the finite algebra below.

Define the `n`-fold spectral decimation polynomial

\[
\boxed{
R_n(u):=2-C_n(2-u).
}
\tag{PAS-1}
\]

The first cases are

\[
R_1(u)=u,
\]

\[
R_2(u)=u(4-u),
\]

\[
R_3(u)=u(3-u)^2,
\]

\[
R_4(u)=u(4-u)(u-2)^2,
\]

\[
R_5(u)=u(u^2-5u+5)^2.
\]

All coefficients are integers.

## 2. Multiplicative composition semigroup

The trace-polynomial composition identity gives

\[
C_{mn}(x)=C_m(C_n(x))=C_n(C_m(x)).
\]

Therefore

\[
\boxed{
R_{mn}
=R_m\circ R_n
=R_n\circ R_m.
}
\tag{PAS-2}
\]

Thus positive integers under multiplication act by a commuting semigroup of finite spectral-decimation polynomials.

For `n=2`, (PAS-2) reduces to the dyadic logistic decimation already used in WSR-T09.

## 3. General finite continuant decimation

Let

\[
H_M(u):=\frac{D_{M-1}(u)}M,
\]

with the Dirichlet continuant recurrence

\[
D_0=1,
\quad D_1=2-u,
\quad D_{r+2}=(2-u)D_{r+1}-D_r.
\]

The general multiplication identity is

\[
\boxed{
D_{mn-1}(u)
=
D_{m-1}(u)\,
D_{n-1}(R_m(u)).
}
\tag{PAS-3}
\]

Equivalently, after normalization,

\[
\boxed{
H_{mn}(u)
=
H_m(u)\,
H_n(R_m(u)).
}
\tag{PAS-4}
\]

This is the exact `m`-fold site-decimation law.

A recurrence/transfer-matrix proof is available entirely at finite algebraic level.  The phase/Chebyshev identity is only a convenient compatibility readout, not required as a primitive spectral assumption.

## 4. Cocycle commutation identity

Because `mn=nm` and the maps commute,

\[
\boxed{
H_m(u)H_n(R_m(u))
=
H_n(u)H_m(R_n(u)).
}
\tag{PAS-5}
\]

Thus `H` is a multiplicative cocycle over the commuting spectral-decimation semigroup.

This identity gives two different exact factorizations of the same finite characteristic determinant according to the order in which scale factors are removed.

## 5. Prime-power generation factorization

For a prime `p`, iterating (PAS-4) gives

\[
\boxed{
H_{p^m}(u)
=
\prod_{j=0}^{m-1}
H_p(R_p^{\circ j}(u)).
}
\tag{PAS-6}
\]

The `j`-th factor has degree

\[
(p-1)p^j.
\]

Since

\[
\sum_{j=0}^{m-1}(p-1)p^j=p^m-1,
\]

the factors account for the complete finite spectrum.

Define the `p`-adic generation

\[
Z_{p,j}:=
\{u:H_p(R_p^{\circ j}(u))=0\}.
\]

Then

\[
\boxed{|Z_{p,j}|=(p-1)p^j.}
\tag{PAS-7}
\]

## 6. Every prime-adic generation has spectral root product exactly p

The base factor `H_p` has constant coefficient one and its complete root product is `p` because

\[
D_{p-1}(0)=p.
\]

For every `j`, the composition factor

\[
H_p(R_p^{\circ j}(u))
\]

also has constant coefficient one because `R_p(0)=0`.

Its degree is `(p-1)p^j`. Tracking the unit leading coefficient of `R_p` and the leading coefficient of `H_p` shows that the signed product-of-roots formula again yields exactly `p`.

Hence

\[
\boxed{
\prod_{u\in Z_{p,j}}u=p
\qquad(j=0,\ldots,m-1).
}
\tag{PAS-8}
\]

The total root product is therefore

\[
\prod_{j=0}^{m-1}p=p^m,
\]

recovering `D_(p^m-1)(0)=p^m` generation by generation.

## 7. p-adic valuation of mode indices

Under the internal phase quantization

\[
u_{k,p^m}=2-2C(k\tau/p^m),
\]

`R_p` multiplies phase by `p`:

\[
R_p(u_{k,p^m})
=
2-2C(pk\tau/p^m).
\]

The factor `H_p` vanishes at the `p-1` nonzero phase classes

\[
\frac{r\tau}{p},
\qquad r=1,\ldots,p-1.
\]

Therefore

\[
\boxed{
u_{k,p^m}\in Z_{p,j}
\iff
v_p(k)=m-1-j.}
\tag{PAS-9}
\]

The cardinality matches:

\[
\#\{1\le k<p^m:v_p(k)=m-1-j\}
=(p-1)p^j.
\]

Thus the spectral-generation filtration is exactly the arithmetic `p`-adic valuation filtration of the mode labels.

## 8. Equal spectral mass law on valuation strata

Combining (PAS-8) and (PAS-9), for every prime `p`, every `m>=1`, and every `r=0,...,m-1`,

\[
\boxed{
\prod_{\substack{1\le k<p^m\\v_p(k)=r}}
 u_{k,p^m}
=p.
}
\tag{PAS-10}
\]

This is a prime-adic equal spectral mass law.

The original dyadic parity products are the `p=2` specialization:

- odd modes: `v_2(k)=0`, one deepest generation, product `2`;
- even modes: union of `m-1` ancestral generations, aggregate product `2^(m-1)=q`.

Hence the constants `2` and `q` in WSR-T08 are the first visible instance of (PAS-10).

## 9. General length and odd/core factorization

Let

\[
M=p^m s,
\qquad p\nmid s.
\]

Iterating (PAS-4) gives

\[
\boxed{
H_M(u)
=
\left[
\prod_{j=0}^{m-1}H_p(R_p^{\circ j}(u))
\right]
H_s(R_p^{\circ m}(u)).
}
\tag{PAS-11}
\]

Thus the spectrum consists of:

1. `m` universal `p`-adic generations, each with multiplicative root mass `p`;
2. an `m`-fold inverse image of the `p`-free core spectrum of length `s`, carrying the remaining root mass `s`.

The degree identity is

\[
(p^m-1)+p^m(s-1)=M-1,
\]

and the root-product identity is

\[
p^m\cdot s=M.
\]

## 10. Prime-factor order independence

For

\[
M=\prod_i p_i^{e_i},
\]

one may factor the spectrum by removing prime powers in any order. Equation (PAS-5) guarantees that different prime-decimation orders produce the same normalized determinant.

This gives a finite spectral analogue of arithmetic factor-order independence:

```text
integer scale factorization
    -> commuting prime decimation maps R_p
    -> cocycle factors H_p
    -> p-adic spectral generations
    -> prime-order-independent full determinant
```

No claim is made that this is a Chinese remainder theorem on carriers; it is a commuting finite renormalization/cocycle structure indexed by integer multiplication.

## 11. Research consequence

The dyadic Wallis/rotation structure is the `p=2` face of a broader prime-adic finite spectrum:

\[
\boxed{
\text{INTEGER MULTIPLICATION}
\to
\text{COMMUTING SPECTRAL DECIMATION SEMIGROUP}
\to
\text{PRIME-ADIC GENERATIONS}.
}
\]

Freeze:

`R_(mn)=R_m∘R_n`.

`H_(mn)=H_m*(H_n∘R_m)`.

`v_p(MODE_INDEX)=PRIME_DECIMATION_GENERATION`.

`EACH_p_ADIC_GENERATION_ROOT_PRODUCT = p`.
