# Finite spectral Möbius sieve and the Euler product for even zeta values

Status: `FREE_RESEARCH / EXACT FINITE-SIEVE + ANALYTIC-COMPLETION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- full reciprocal spectral moment polynomial `Z_s(M)=P_s(M^2)`;
- divisor embedding of finite mode indices;
- internal mode-radius limit `rho_(k,M)->k tau` and lower bound `rho>=2k`.

## 1. Divisibility-restricted finite modes

Let

\[
Z_s(M):=\sum_{k=1}^{M-1}u_{k,M}^{-s}.
\]

If `d|M`, the modes with `d|k` are

\[
k=dr,\qquad 1\le r<M/d.
\]

Internal phase quantization gives exactly

\[
u_{dr,M}=u_{r,M/d}.
\]

Therefore

\[
\boxed{
\sum_{\substack{1\le k<M\\d\mid k}}u_{k,M}^{-s}
=Z_s(M/d).
}
\tag{FSM-1}

This is an exact finite spectral decimation identity, not an asymptotic statement.

## 2. Finite Möbius sieve

Let `P|M`.  Define the reciprocal moment of modes coprime to `P`:

\[
Z_s^{(P)}(M)
:=\sum_{\substack{1\le k<M\\(k,P)=1}}u_{k,M}^{-s}.
\]

Use the finite identity

\[
\mathbf 1_{(k,P)=1}
=\sum_{d\mid(k,P)}\mu(d).
\]

Exchange the finite sums and apply (FSM-1):

\[
\boxed{
Z_s^{(P)}(M)
=\sum_{d\mid P}\mu(d)Z_s(M/d).
}
\tag{FSM-2}

Thus ordinary Möbius sieving of integer indices is realized exactly by deletion/recombination of finite Dirichlet spectral subchains.

## 3. Jordan-coordinate closed form

Write the already derived full moment polynomial as

\[
Z_s(N)=P_s(N^2)
=a_{s,0}+\sum_{r=1}^{s}a_{s,r}N^{2r}.
\]

For `P>1`, the constant coefficient cancels because

\[
\sum_{d\mid P}\mu(d)=0.
\]

Therefore

\[
Z_s^{(P)}(M)
=\sum_{r=1}^{s}a_{s,r}M^{2r}
\sum_{d\mid P}\frac{\mu(d)}{d^{2r}}.
\]

Since

\[
\sum_{d\mid P}\mu(d)d^{-2r}
=\prod_{p\mid P}(1-p^{-2r})
=\frac{J_{2r}(P)}{P^{2r}},
\]

we get

\[
\boxed{
Z_s^{(P)}(M)
=
\sum_{r=1}^{s}a_{s,r}
\left(\frac MP\right)^{2r}J_{2r}(P).
}
\tag{FSM-3}

This is the exact finite spectral sieve formula.

## 4. Primitive spectrum is the maximally sieved spectrum

Set `P=M`.  Then `(k,M)=1` means exactly that the mode has reduced denominator `M`, so the left side is the primitive reciprocal moment:

\[
Z_s^{\rm prim}(M)
=Z_s^{(M)}(M).
\]

Equation (FSM-3) becomes

\[
\boxed{
Z_s^{\rm prim}(M)
=\sum_{r=1}^{s}a_{s,r}J_{2r}(M).
}
\tag{FSM-4}

Thus the previously discovered Jordan-totient primitive-moment law is exactly the endpoint `P=M` of the finite Möbius sieve.

Interpretation:

`PRIMITIVE_DENOMINATOR_SPECTRUM = FULL_SPECTRUM MOBIUS-SIEVED BY ITS OWN LENGTH`.

## 5. One-prime Euler-factor removal

For a prime `p|M`, (FSM-2) with `P=p` gives

\[
\boxed{
\sum_{\substack{1\le k<M\\p\nmid k}}u_{k,M}^{-s}
=Z_s(M)-Z_s(M/p).
}
\tag{FSM-5}

Scale by `M^{-2s}`.  Since the leading coefficient of `P_s` is `beta_s`,

\[
M^{-2s}[Z_s(M)-Z_s(M/p)]
\longrightarrow
\beta_s(1-p^{-2s}).
\]

On the mode-radius side,

\[
M^{-2s}u_{k,M}^{-s}=\rho_{k,M}^{-2s},
\]

and the internal limit/lower bound gives

\[
\rho_{k,M}^{-2s}	o(k\tau)^{-2s},
\qquad
\rho_{k,M}^{-2s}\le(2k)^{-2s}.
\]

Hence

\[
\boxed{
\beta_s(1-p^{-2s})
=
\frac1{\tau^{2s}}
\sum_{\substack{k\ge1\\p\nmid k}}k^{-2s}.
}
\tag{FSM-6}

This is the spectral removal of one Euler factor.

## 6. Finite prime set

Let

\[
P_y:=\prod_{p\le y}p
\]

be a finite primorial and choose lengths `M` divisible by `P_y`.  Then the exact sieve is

\[
Z_s^{(P_y)}(M)
=\sum_{d\mid P_y}\mu(d)Z_s(M/d).
\]

Scale and let `M->infinity` through multiples of `P_y`:

\[
\boxed{
\beta_s\prod_{p\le y}(1-p^{-2s})
=
\frac1{\tau^{2s}}
\sum_{\substack{k\ge1\\(k,P_y)=1}}k^{-2s}.
}
\tag{FSM-7}

The passage to the limit is dominated by `(2k)^(-2s)` and is valid for every integer `s>=1`.

## 7. Send the finite sieve through all primes

As `y->infinity`, for every fixed `k>1` some prime divisor of `k` eventually belongs to `P_y`; the only index which remains coprime to every finite primorial is `k=1`.

Dominated convergence therefore gives

\[
\sum_{(k,P_y)=1}k^{-2s}\longrightarrow1.
\]

Hence from (FSM-7),

\[
\boxed{
\beta_s\prod_p(1-p^{-2s})
=\tau^{-2s}.
}
\tag{FSM-8}

But the independently derived finite-spectrum moment limit is

\[
\boxed{
\zeta(2s)=\beta_s\tau^{2s}.
}
\tag{FSM-9}

Combining,

\[
\boxed{
\zeta(2s)
\prod_p(1-p^{-2s})=1,
}
\tag{FSM-10}

or equivalently

\[
\boxed{
\zeta(2s)=\prod_p(1-p^{-2s})^{-1}.
}
\tag{FSM-11}

## 8. Scope

No novelty is claimed for the classical Euler product of zeta.  The theorem-candidate strength is the derivation route:

```text
finite integer/rational Dirichlet spectrum
 -> exact divisor subchain identity
 -> finite Mobius spectral sieve
 -> Jordan-coordinate closed form
 -> internal mode-radius completion
 -> even-zeta Euler factors
```

No infinite Euler product over integers is used as an input to the finite sieve.

The result currently covers even positive integer arguments because the finite reciprocal spectral moments are powers `u^{-s}` whose scaling limit is `k^{-2s}`.

Freeze:

`FINITE_MOBIUS_SIEVE = EXACT_DIRICHLET_MODE_FILTER`.

`PRIMITIVE_JORDAN_MOMENTS = MAXIMAL_FINITE_SIEVE`.

`EVEN_ZETA_EULER_PRODUCT = FINITE_SPECTRAL_SIEVE_COMPLETION`.
