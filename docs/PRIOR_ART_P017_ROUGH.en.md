# P017 Rough-Number / Buchstab Prior-Art Appendix

Status: `PRIOR-ART APPENDIX`  
Scope: rough-number counting, least-prime-factor recursion, and classical prime estimates used by the P017 cofactor-window line

## Rough numbers

Modern sieve literature uses functions such as `Phi(x,y)` to count integers up to `x` with no small prime divisor and studies them through Buchstab/de Bruijn theory. Steve Fan's explicit rough-number work is a current reference for this established framework. [SRC-FAN-2023-ROUGH-NUMBERS]

## Buchstab recursion

Least-prime-factor decomposition and Buchstab identities are established sieve tools. Runbo Li's work on variants of Buchstab's identity is a recent explicit reference that this recursion is mature prior mathematics rather than an Enterprise Math construction. [SRC-LI-2025-BUCHSTAB]

## Reciprocal-prime and prime-counting estimates

The asymptotic step after the exact L049 hit-state union uses classical prime-distribution estimates, not new project mathematics. Rosser and Schoenfeld give standard explicit estimates for prime-counting functions and for the reciprocal-prime sum, in the classical Mertens neighborhood. [SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]

In particular, P017 treats as prior art the facts that

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1)
\]

and that the number of primes up to `x` is `o(x)` (indeed much more precise estimates are classical). The project uses these only after it has already produced a finite exact interval of possible resource primes and an exact finite hit-count envelope.

P017 therefore does **not** claim as inventions:

- p-rough numbers;
- `Phi(x,y)`-type rough-number counts;
- partitioning a sifted set by its next least prime factor;
- Buchstab's identity or its iterated variants;
- Mertens' theorem for reciprocal primes;
- the prime number theorem, Rosser-Schoenfeld inequalities, or classical prime-counting estimates.

## Project-specific use under test

The P017 contribution being pressure-tested is narrower. Consecutive-square geometry gives each least-factor shell an **exact moving cofactor interval** with endpoints depending on the same cutoff `k` and least prime `p`. The raw interval length is itself an exact quotient-response / boundary-carry quantity. Applying established least-factor recursion to these special windows yields additional finite constraints, including a high-band contraction threshold `p^2 >= 2k` where each second-factor branch has at most one raw candidate and every shell state has at most three prime factors counted with multiplicity.

The later high-band route then builds exact pairwise resource separation, multiplicative capacity, and cross-shell hit-state unions before invoking any analytic prime-distribution theorem. The classical reciprocal-prime estimate is used only to turn the resulting finite resource interval

\[
\sqrt{2k}\le r\le\frac{k+2}{2}
\]

into an asymptotic envelope. The `log(2)` constant in that analytic corollary is therefore a specialization of classical Mertens behavior to the project-derived endpoints; it is not a new prime-distribution constant.

Historical novelty of the square-basin specialization remains `NOVELTY_UNVERIFIED`. Its value depends on whether the special moving windows and exact resource collisions yield a survivor bound unavailable from generic sieve density alone.
