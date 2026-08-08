# P017 Rough-Number / Buchstab Prior-Art Appendix

Status: `PRIOR-ART APPENDIX`  
Scope: rough-number counting and least-prime-factor recursion used by the P017 cofactor-window line

## Rough numbers

Modern sieve literature uses functions such as `Phi(x,y)` to count integers up to `x` with no small prime divisor and studies them through Buchstab/de Bruijn theory. Steve Fan's explicit rough-number work is a current reference for this established framework. [SRC-FAN-2023-ROUGH-NUMBERS]

## Buchstab recursion

Least-prime-factor decomposition and Buchstab identities are established sieve tools. Runbo Li's work on variants of Buchstab's identity is a recent explicit reference that this recursion is mature prior mathematics rather than an Enterprise Math construction. [SRC-LI-2025-BUCHSTAB]

P017 therefore does **not** claim as inventions:

- p-rough numbers;
- `Phi(x,y)`-type rough-number counts;
- partitioning a sifted set by its next least prime factor;
- Buchstab's identity or its iterated variants.

## Project-specific use under test

The P017 contribution being pressure-tested is narrower. Consecutive-square geometry gives each least-factor shell an **exact moving cofactor interval** with endpoints depending on the same cutoff `k` and least prime `p`. The raw interval length is itself an exact quotient-response / boundary-carry quantity. Applying established least-factor recursion to these special windows yields additional finite constraints, including a high-band contraction threshold `p^2 >= 2k` where each second-factor branch has at most one raw candidate and every shell state has at most three prime factors counted with multiplicity.

Historical novelty of this specialization remains `NOVELTY_UNVERIFIED`. Its value depends on whether the special moving windows yield a survivor bound unavailable from generic sieve density alone.
