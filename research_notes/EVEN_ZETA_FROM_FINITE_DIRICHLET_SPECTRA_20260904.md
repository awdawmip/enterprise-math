# Even zeta values from finite Dirichlet spectral moments

Status: `FREE_RESEARCH / INTERNAL COMPLETION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- exact finite reciprocal spectral moments;
- internal phase quantization `rho_(k,M) -> k tau`;
- intrinsic bound `rho_(k,M)>=2k`.

## 1. Finite spectral zeta moment

For integer `s>=1`, define

\[
Z_s(M)
:=
\sum_{k=1}^{M-1}u_{k,M}^{-s}.
\]

The Newton/central-factorial analysis proves exactly that

\[
Z_s(M)
=c_{s,0}+c_{s,1}M^2+\cdots+c_{s,s}M^{2s}
\]

with rational coefficients.

Let

\[
\boxed{\beta_s:=c_{s,s}.}
\]

Then immediately

\[
\boxed{
\lim_{M\to\infty}\frac{Z_s(M)}{M^{2s}}
=\beta_s.
}
\tag{EZF-1}
\]

## 2. The same scaled moment in normalized mode radii

Recall

\[
\rho_{k,M}:=M\sqrt{u_{k,M}}.
\]

Therefore

\[
\boxed{
\frac{Z_s(M)}{M^{2s}}
=
\sum_{k=1}^{M-1}\frac1{\rho_{k,M}^{2s}}.
}
\tag{EZF-2}
\]

The internal phase quantization theorem gives, for every fixed `k`,

\[
\rho_{k,M}
=2M S\left(\frac{k\tau}{2M}\right)
\longrightarrow k\tau.
\]

Hence each fixed summand tends to

\[
\frac1{k^{2s}\tau^{2s}}.
\]

## 3. Uniform spectral tail domination

The intrinsic chord bound gives

\[
\rho_{k,M}\ge2k.
\]

Consequently

\[
0<\frac1{\rho_{k,M}^{2s}}
\le
\frac1{(2k)^{2s}}.
\]

For every `s>=1`,

\[
\sum_{k=1}^{\infty}\frac1{(2k)^{2s}}
\]

converges.

Thus, for every cutoff `K`, uniformly in every `M>K`,

\[
\sum_{k=K+1}^{M-1}
\frac1{\rho_{k,M}^{2s}}
\le
2^{-2s}
\sum_{k=K+1}^{\infty}k^{-2s},
\]

and the right side tends to zero as `K->infinity`.

This finite-head/uniform-tail argument allows the limit to pass through the growing mode sum without any continuous spectral theorem.

Therefore

\[
\boxed{
\lim_{M\to\infty}
\frac{Z_s(M)}{M^{2s}}
=
\frac1{\tau^{2s}}
\sum_{k=1}^{\infty}\frac1{k^{2s}}.
}
\tag{EZF-3}
\]

## 4. Internal even-zeta identity

Define the ordinary arithmetic zeta value

\[
\zeta(2s):=\sum_{k=1}^{\infty}k^{-2s}.
\]

Comparing (EZF-1) and (EZF-3) gives

\[
\boxed{
\zeta(2s)=\beta_s\tau^{2s}.
}
\tag{EZF-4}
\]

This is obtained from finite Dirichlet spectra and the internal completion phase. No circle spectrum, Fourier basis, or prior value of classical `pi` is used.

## 5. Rational recursion for beta_s

The reciprocal elementary symmetric sums have leading coefficients

\[
E_j(M)
=\frac{M^{2j}}{(2j+1)!}+O(M^{2j-2}).
\]

Newton identities therefore give the leading-coefficient recursion

\[
\boxed{
\beta_s
=
\sum_{j=1}^{s-1}
(-1)^{j-1}
\frac{\beta_{s-j}}{(2j+1)!}
+
(-1)^{s-1}
\frac{s}{(2s+1)!}.
}
\tag{EZF-5}
\]

In particular,

\[
\beta_1=\frac16,
\qquad
\beta_2=\frac1{90},
\qquad
\beta_3=\frac1{945}.
\]

Thus

\[
\boxed{
\zeta(2)=\frac{\tau^2}{6},
\qquad
\zeta(4)=\frac{\tau^4}{90},
\qquad
\zeta(6)=\frac{\tau^6}{945}.
}
\tag{EZF-6}
\]

## 6. Generating function for beta_s

The leading reciprocal elementary coefficients are

\[
\frac1{(2j+1)!}.
\]

Newton identities are equivalently encoded by

\[
\boxed{
-\log\left(
\sum_{j=0}^{\infty}
\frac{(-1)^jz^j}{(2j+1)!}
\right)
=
\sum_{s=1}^{\infty}
\frac{\beta_s}{s}z^s.
}
\tag{EZF-7}
\]

The series inside the logarithm is the internally defined normalized completion `S(sqrt z)/sqrt z`, interpreted by its power series at zero.

## 7. Bernoulli identification

Using the algebraic Bernoulli-number generating function, the rational coefficients in (EZF-7) are

\[
\boxed{
\beta_s
=
(-1)^{s+1}
\frac{2^{2s-1}B_{2s}}{(2s)!}.
}
\tag{EZF-8}
\]

Therefore the full internal even-zeta formula is

\[
\boxed{
\zeta(2s)
=
(-1)^{s+1}
\frac{2^{2s-1}B_{2s}}{(2s)!}
\tau^{2s}.
}
\tag{EZF-9}
\]

After the separate classical compatibility `tau=pi`, this becomes Euler's classical formula. But the finite-spectrum derivation reaches (EZF-9) before classical `pi` is named.

## 8. Independence from the Euler-product proof route

The logic here does not require WSR-T04's infinite product identity.

It uses instead:

```text
finite root reciprocal moments
    -> exact polynomial in M^2
    -> leading rational coefficient beta_s

finite mode-radius quantization
    -> rho_(k,M) -> k tau
    -> uniform tail domination rho>=2k
    -> arithmetic zeta limit

compare the same finite scaled moment
    -> zeta(2s)=beta_s tau^(2s)
```

Thus the Euler product and the even-zeta formulas are two independent analytic completions of the same finite spectral carrier.

Their agreement is a nontrivial consistency check of the #1159 structure.

## 9. Primitive Jordan-totient refinement

The primitive denominator spectral moments satisfy

\[
Z_s^{\rm prim}(d)
=\sum_{r=1}^{s}c_{s,r}J_{2r}(d).
\]

The leading Jordan term is therefore

\[
\boxed{
\beta_s J_{2s}(d).
}
\]

So the same coefficient `beta_s` governs both:

1. the continuum even-zeta limit `zeta(2s)/tau^(2s)`;
2. the highest-order Jordan-totient component of every primitive finite spectral moment.

This gives a direct finite-arithmetic/completion bridge.

Freeze:

`EVEN_ZETA = LEADING_FINITE_SPECTRAL_MOMENT * TAU_POWER`.

`BETA_s = RATIONAL_NEWTON_COEFFICIENT = BERNOULLI_COEFFICIENT`.

`EULER_PRODUCT_PROOF_ROUTE` and `FINITE_ZETA_MOMENT_PROOF_ROUTE` are independent completions of the same native carrier.
