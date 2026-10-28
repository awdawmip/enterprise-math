# D25 GH-19 — Exact binomial coefficient model and primality-sensitive obstruction

2026-10-28. Author-side auxiliary scalar research, independent of any native CLAIM; `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / SYNC_DEBT`. The remote write attempt for GH-17/18 was refused by the host; the only verified new GH-17–19 artifacts for this turn are local sandbox files. The Enterprise Math frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.

## Exact new reduction

Fix any integer `m>=0` and define the *rational* terminating polynomial

\[
F_m(z)=\sum_{r=0}^m \frac{(-m)_r^2}{(2m+2)_r r!}z^r.
\]

**Theorem GH-19a.** There is an identity over the integers and rational polynomials:

\[
\boxed{\binom{3m+1}{m}F_m(z)
=\sum_{r=0}^m\binom{3m+1}{m-r}\binom mr z^r
=[t^m](1+t)^{3m+1}(1+zt)^m.}
\]

For any prime `p=8m+3`, the binomial denominator is a unit in `F_p`, because `3m+1<p`. Hence the conjecture `F_m(9)=0 (mod p)` is *equivalent* to the pure integer coefficient certificate

\[
\boxed{p\mid B_m,\quad B_m=[t^m](1+t)^{3m+1}(1+9t)^m.}
\tag{GH-19}
\]

With `Q(t)=(1+t)^3(1+9t)` this becomes

\[
 B_m=[t^m](1+t)Q(t)^m,
\quad Q(t)=1+12t+30t^2+28t^3+9t^4.
\]

There is also the exact, over-\(\mathbb Z[t]\) algebraic decomposition

\[
\boxed{Q(t)=(1+6t-3t^2)^2+64t^3.}
\]

This is only an algebraic presentation; it is *not* by itself a CM identification, a characteristic-sum argument or proof of p-divisibility.

**Proof.** The coefficient identity follows term-by-term from

\[
\frac{(-m)_r^2}{(2m+2)_r r!}
=\frac{m!^2(2m+1)!}{r!(m-r)!^2(2m+1+r)!}
=\frac{\binom{3m+1}{m-r}\binom mr}{\binom{3m+1}{m}}.
\]

The right sum is exactly the coefficient convolution. No denominator of `binom(3m+1,m)` vanishes modulo prime `8m+3`, so the equivalence is valid. The quartic identity follows by direct expansion. QED.

## Primality-sensitive exact counterexample

The condition `m == 2 (mod 3)` alone does **not** imply the stronger integer divisibility `(8m+3) | B_m`. At `m=11`, `8m+3=91=7*13`, direct integer computation gives

\[
\boxed{B_{11}\bmod91=13\ne0.}
\]

Thus one cannot replace the prime quantifier with an arbitrary positive integer congruent to `19 (mod 24)`, even while keeping the same finite coefficient definition. This is a definitive negative certificate for the naive composite extension, not a counterexample for prime `p`.

## Finite exact checks, scope and next problem

Companion `gh19_binomial_check.py` executed local exact Python standard-library `math.comb` checks for all 43 primes `11<=p<1000`, `p mod 8=3`, comparing the original mod-p hypergeometric `F_m(9)` with the integer binomial `B_m / binom(3m+1,m)`; checked the quartic identity coefficientwise and the `m=11` composite counterexample. All passed. This does not establish `p | B_m` for *all* target primes.

BRC source fidelity: preserve `(p,m,r,z)` and the original GH-16 rank source, integral binomial observer, mod-p normalization, the `F/G` factor channels from GH-17, and original W/S/Hasse labels separately; the scalar polynomial does not supply an X6 native bridge or authorize an original S or LIFT claim. `B_m` here is a *binomial certificate*, not the separate original Hasse `B0` or GH-15 Laurent `B`.

**Next action:** derive a *prime-dependent* symmetry/character-sum or WZ certificate proving (or disproving) `p | [t^m](1+t)Q(t)^m` for all primes `p=8m+3 ≡19 (mod 24)`, equivalently `m≡2 (mod 3)` and `p` prime. The square-plus-cube identity suggests a candidate algebraic transformation but provides no proof by itself. Then combine with GH-17 and GH-18 to remove GH-16 double poles (while keeping GH-15's remaining simple Laurent term); do not conflate this with `T_p=0` or the native second-digit LIFT target. Remaining native H0/B0, `[X]U mod p²`, Frobenius η/κ, real p=373 experiment, and independent Driver review remain OPEN.
