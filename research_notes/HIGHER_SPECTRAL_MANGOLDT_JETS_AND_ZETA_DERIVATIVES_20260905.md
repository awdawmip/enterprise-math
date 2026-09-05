# Higher spectral Mangoldt jets and zeta-derivative hierarchy

Status: `FREE_RESEARCH / ANALYTIC READOUT OF EXACT PULLBACK EIGENFAMILY / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- generalized Jordan pullback eigenfamily `J_z=mu*n^z`.

## 1. Higher jets at the zero eigencharacter

Define for integer `r>=1`

\[
\boxed{
\Lambda_r^{\rm spec}(n)
:=\left.\frac{d^r}{dz^r}J_z(n)\right|_{z=0}.
}
\tag{HMJ-1}

Since

\[
J_z(n)=\sum_{d\mid n}\mu(n/d)d^z,
\]

termwise finite differentiation gives

\[
\boxed{
\Lambda_r^{\rm spec}(n)
=\sum_{d\mid n}\mu(n/d)(\log d)^r.
}
\tag{HMJ-2}

The logarithms are derived analytic coordinates; the divisor/pullback algebra is finite before this readout.

## 2. First jet is ordinary von Mangoldt

For `r=1`,

\[
\boxed{
\Lambda_1^{\rm spec}(n)=\Lambda(n).
}
\tag{HMJ-3}

Thus the primitive endpoint prime-mass log and the first generalized-Jordan jet coincide.

## 3. Dirichlet-series transform

The generalized Jordan Dirichlet series is

\[
\sum_{n\ge1}\frac{J_z(n)}{n^s}
=\frac{\zeta(s-z)}{\zeta(s)}
\]

in the half-plane of absolute convergence.

Differentiate `r` times in `z` at zero:

\[
\boxed{
\sum_{n\ge1}
\frac{\Lambda_r^{\rm spec}(n)}{n^s}
=(-1)^r\frac{\zeta^{(r)}(s)}{\zeta(s)}.
}
\tag{HMJ-4}

For `r=1` this is the usual logarithmic derivative.

No claim about new analytic continuation, zero-free regions or RH follows merely from this representation.

## 4. Prime-support filtration

Write

\[
\omega(n)=|\{p:p\mid n\}|.
\]

The product form

\[
J_z(n)=n^z\prod_{p\mid n}(1-p^{-z})
\]

has a zero of exact order `omega(n)` at `z=0`.

Therefore

\[
\boxed{
\Lambda_r^{\rm spec}(n)=0
\quad\text{for }r<\omega(n).
}
\tag{HMJ-5

At the first visible order `t=omega(n)`,

\[
\boxed{
\Lambda_t^{\rm spec}(n)
=t!\prod_{p\mid n}\log p.
}
\tag{HMJ-6

This value is independent of the p-adic exponents of `n`; the first nonzero support jet sees the set of distinct prime directions, not their depth.

## 5. Higher jets distinguish mixed-prime support invisible to endpoint mass

If `n` is a prime power, `omega(n)=1`, so the first jet is already nonzero and equals `log p`.

If `n` has two distinct primes, then

\[
\Lambda_1^{\rm spec}(n)=0,
\]

but

\[
\Lambda_2^{\rm spec}(n)
=2\log p\log q
\]

for the two-prime support `{p,q}` at leading order.

For a denominator with `t` distinct primes, every jet below order `t` vanishes and the `t`-th becomes nonzero.

Thus

\[
\boxed{
\text{MINIMUM VISIBLE SPECTRAL-JET ORDER}
=\omega(n).
}
\tag{HMJ-7

## 6. Relation to mixed spectral join interactions

Pure mixed join factors have endpoint mass one because every mixed primitive denominator contains at least two distinct primes.  In the generalized-Jordan hierarchy this is exactly the statement that the first jet vanishes.

Higher join interactions generated from `t` genuinely new prime directions are naturally expected to first appear at jet order `t`; the precise mixed-factor decomposition decides which denominators occur, while (HMJ-5)--(HMJ-6) give the support-order visibility rule for each denominator.

So endpoint mass neutrality and higher mixed structure are compatible:

```text
first jet / Lambda:
    sees only one-prime support

higher jets:
    reveal higher-prime support interactions
```

## 7. Pullback transport of the jets

Differentiate the pullback eigenlaw

\[
\sum_{e\in\mathcal F_n(d)}J_z(e)=n^zJ_z(d)
\]

`r` times at zero:

\[
\boxed{
\sum_{e\in\mathcal F_n(d)}\Lambda_r^{\rm spec}(e)
=
\sum_{a=0}^{r}
\binom ra(\log n)^{r-a}\Lambda_a^{\rm spec}(d),
}
\tag{HMJ-8

where `Lambda_0^spec:=J_0`.

For `d>1`, `Lambda_0^spec(d)=0`, and at `r=1` this reduces to exact von-Mangoldt mass conservation.

Higher orders mix support complexity with scale-depth provenance triangularly.

## 8. Typing boundary

The hierarchy separates three kinds of data:

- distinct-prime support order `omega(n)`;
- p-adic depth in `n`;
- analytic log weights `log p`.

The first nonzero jet order records support count; its magnitude records the product of log-prime weights; deeper p-adic exponents enter only in higher terms beyond the leading support jet.

Therefore these coordinates must not be collapsed into one positive mass summary.

Freeze:

`SPECTRAL_MANGOLDT_JET_r = d^r/dz^r J_z | z=0`.

`DIRICHLET_SERIES = (-1)^r ZETA^(r)/ZETA`.

`FIRST_NONZERO_JET_ORDER = OMEGA(n)`.
