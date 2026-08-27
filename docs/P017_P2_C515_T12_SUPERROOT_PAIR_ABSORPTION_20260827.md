# P017 — c=103/20 T1–T2 Super-Root Ordered-Pair Absorption — SUPERSEDED

Status: `SUPERSEDED BY LEAST-SHELL BUDGET CORRECTION / LOCAL SUPERROOT FACTS RETAINED / DO NOT USE ABSORPTION CONCLUSION`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Authoritative correction:

`docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`

## Retained facts

For the dangerous least-prime range

\[
\frac16\le u<\frac{73}{240},
\]

the original note correctly proved:

1. on the super-root pair sector `rp>W`,
   \[
   \kappa(u,t)=\frac12;
   \]
2. a basin state has at most two distinct larger divisor primes satisfying `rp>W`.

## Correction

The original pointwise absorption step used the entire base-minus-T3 numerator

\[
12u-1
\]

against the super-root pair penalty. This omitted the least-prime-shell T1–T2 cost introduced by the same second Buchstab decomposition.

The correct pair budget is

\[
C(u)=12u-1-\ell(u),
\]

where

\[
\ell(u)
=\frac12+6\left[\min\left(u,\frac{113}{240}-u\right)-\frac16\right]_+.
\]

At `u=1/6`, `C(u)=1/2`, so two super-root pair penalties of `1/2` cannot be uniformly absorbed from this budget alone.

Therefore the former full-absorption conclusion and the claim that all super-root pairs disappear from the analytic frontier are withdrawn. The retained kernel/count facts remain available inside the corrected residual analysis.

The correction note proves the valid replacement: least-prime shell plus one maximal ordered pair is always absorbed, and every remaining pair has a three-distinct-prime witness.

No finite P2 theorem or all-K claim is made here.
