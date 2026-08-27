# P017 — c=103/20 T1–T2 High-Pair Pointwise Absorption — SUPERSEDED

Status: `SUPERSEDED BY LEAST-SHELL BUDGET CORRECTION / LOCAL KERNEL FACTS RETAINED / DO NOT USE ABSORPTION CONCLUSION`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Authoritative correction:

`docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`

## Retained facts

For

\[
B=D^{31/40},\qquad \frac16\le u<\frac{73}{240},
\]

the following local statements from the original note remain correct:

1. if `rp>=B`, then
   \[
   \kappa(u,t)=\frac12;
   \]
2. four distinct high-pair larger primes are impossible;
3. three such primes require
   \[
   u>\frac{21}{80}.
   \]

## Correction

The original absorption step incorrectly spent the full base-minus-T3 numerator

\[
12u-1
\]

on high-pair penalties. After the second Buchstab decomposition the same state also carries the least-prime-shell T1–T2 penalty

\[
\ell(u)
=\frac12+6\left[\min\left(u,\frac{113}{240}-u\right)-\frac16\right]_+.
\]

Thus the pair budget is only

\[
C(u)=12u-1-\ell(u).
\]

At `u=1/6`,

\[
C(u)=\frac12,
\]

while two high-pair penalties would total `1`. Hence the claimed uniform absorption of the whole `rp>=B` sector does not follow.

The former conclusions `HP6` and `HP7` are withdrawn. Use the correction note, which proves instead that the least-prime shell plus **one maximal ordered pair** is always absorbed, leaving a corrected residual inner level at most `D^(1/2)`.

No finite P2 theorem or all-K claim is made here.
