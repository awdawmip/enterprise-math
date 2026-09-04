# Spectral Möbius inversion and primitive Dirichlet mode mass

Status: `FREE_RESEARCH / EXACT DIVISOR-ARITHMETIC SPECTRAL LAW / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on the general scale-decimation cocycle `H_(mn)=H_m*(H_n∘R_m)`.

## 1. Divisor-selected sub-spectrum product

Let

\[
M=dn.
\]

Consider the length-`M` mode indices divisible by `n`:

\[
k=nr,
\qquad r=1,\ldots,d-1.
\]

Under the internal phase quantization,

\[
u_{nr,M}
=2-2C\left(\frac{nr\tau}{dn}\right)
=2-2C\left(\frac{r\tau}{d}\right)
=u_{r,d}.
\]

Thus this divisor-selected sub-spectrum is exactly the complete interior spectrum of the shorter length `d`.

Since the total root product at length `d` is `d`,

\[
\boxed{
\prod_{r=1}^{d-1}u_{nr,M}=d.
}
\tag{SMP-1}
\]

Equivalently, for every divisor `n|M`,

\[
\boxed{
\prod_{\substack{1\le k<M\\ n\mid k}}
u_{k,M}
=\frac{M}{n}.
}
\tag{SMP-2}
\]

The case `n=M` is the empty product `1=M/M`.

This is an exact finite divisor-product law.

## 2. Primitive denominator classes

For `d>1`, define the primitive denominator-`d` spectral mass

\[
\boxed{
P_d
:=
\prod_{\substack{1\le r<d\\\gcd(r,d)=1}}
u_{r,d}.
}
\tag{SMP-3}
\]

Every nonzero fraction `k/M` reduces uniquely to

\[
\frac{a}{d},
\qquad d\mid M,
\quad d>1,
\quad \gcd(a,d)=1.
\]

Since the mode value depends only on the reduced phase fraction, the complete length-`M` spectrum is the disjoint union of primitive denominator classes indexed by divisors `d|M`, `d>1`.

Therefore

\[
\boxed{
M
=
\prod_{\substack{d\mid M\\d>1}}P_d.
}
\tag{SMP-4}
\]

This is the multiplicative divisor-zeta relation for primitive spectral mass.

## 3. Multiplicative Möbius inversion

Take logarithms formally, or apply multiplicative Möbius inversion directly. From (SMP-4),

\[
\boxed{
P_d
=
\prod_{e\mid d}
e^{\mu(d/e)}.
}
\tag{SMP-5}
\]

Here the `e=1` factor is harmless.

This formula is entirely arithmetic once the divisor decomposition has been established.

## 4. Prime-power dichotomy

### Prime-power case

Let

\[
d=p^a.
\]

Only `d/e=1` and `d/e=p` contribute nonzero Möbius values, so

\[
P_{p^a}
=
(p^a)^1(p^{a-1})^{-1}
=p.
\]

Thus

\[
\boxed{P_{p^a}=p.}
\tag{SMP-6}
\]

### At least two distinct prime factors

Let `d` have at least two distinct prime divisors. For a fixed prime `p|d`, the exponent of `p` in (SMP-5) is

\[
\sum_{e\mid d}
\mu(d/e)\,v_p(e).
\]

Writing `f=d/e`, this becomes

\[
\sum_{f\mid d}
\mu(f)\,(v_p(d)-v_p(f)).
\]

The constant part vanishes because

\[
\sum_{f\mid d}\mu(f)=0.
\]

The remaining squarefree-subset sum also vanishes when there is at least one prime divisor of `d` other than `p`: subsets containing `p` pair by toggling one of the other primes.

Hence every prime exponent is zero and

\[
\boxed{P_d=1}
\tag{SMP-7}
\]

whenever `d` has at least two distinct prime factors.

Combining:

\[
\boxed{
P_d
=
\begin{cases}
p,&d=p^a,\\[2mm]
1,&d\text{ has at least two distinct prime factors}.
\end{cases}
}
\tag{SMP-8}
\]

for every `d>1`.

## 5. Equal prime-adic mass is the prime-power specialization

At length `p^m`, the primitive denominator classes are `p,p^2,...,p^m`, and each has mass `p` by (SMP-6). Therefore

\[
p^m=P_pP_{p^2}\cdots P_{p^m}
\]

is exactly the prime-adic equal-generation mass law from the decimation-semigroup analysis.

So the two decompositions agree:

```text
prime-adic decimation generations
        =
primitive denominator p^a classes.
```

For `p=2`, the deepest primitive class `P_(2^m)=2` is exactly the odd-mode product of the dyadic chain.

## 6. Spectral primitive factors

The divisor relation also suggests an intrinsic polynomial factorization.

Let `Psi_d(u)` denote the normalized polynomial whose roots are precisely the primitive denominator-`d` modes. Then recursively

\[
H_d(u)
=
\prod_{\substack{e\mid d\\e>1}}\Psi_e(u).
\tag{SMP-9}
\]

The degree is

\[
\boxed{\deg\Psi_d=\varphi(d),}
\tag{SMP-10}
\]

because there are exactly `phi(d)` primitive residue classes modulo `d` in `1,...,d-1`.

The root product of `Psi_d` is exactly `P_d`, so

\[
\boxed{
\prod\operatorname{Roots}(\Psi_d)
=
\begin{cases}
p,&d=p^a,\\1,&\omega(d)\ge2.
\end{cases}
}
\tag{SMP-11}
\]

These `Psi_d` are finite spectral analogues of primitive/cyclotomic factors, but no polynomial identity with classical cyclotomic polynomials is asserted at the native layer.

## 7. Classical compatibility observation

The arithmetic value in (SMP-8) is the same famous prime-power dichotomy as

\[
\Phi_d(1)
=
\begin{cases}
p,&d=p^a,\\1,&\omega(d)\ge2,
\end{cases}
\]

for the classical cyclotomic polynomial.

Thus

\[
\boxed{P_d=\Phi_d(1)}
\]

as an arithmetic readout for `d>1`.

This numerical/arithmetic equality is a later compatibility observation. The spectral mass law above was derived from finite Dirichlet divisor decomposition and Möbius inversion, not by importing cyclotomic roots.

## 8. Research consequence

The finite Dirichlet spectrum carries its own divisor arithmetic:

```text
mode phase k/M
   -> reduced denominator d
   -> primitive spectral class Psi_d
   -> divisor product M = prod_(d|M,d>1) P_d
   -> Möbius inversion
   -> prime-power mass dichotomy
```

Freeze:

`DIVISOR_SELECTED_ROOT_PRODUCT = M/n` for `n|M`.

`PRIMITIVE_DENOMINATOR_MASS = MOBIUS_INVERSION_OF_LENGTH`.

`P_(p^a)=p`, `P_d=1` for `omega(d)>=2`.
