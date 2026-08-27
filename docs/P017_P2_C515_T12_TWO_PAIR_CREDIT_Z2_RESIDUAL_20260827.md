# P017 — c=103/20 T1–T2 Two-Pair Credit / z^2 Residual — SUPERSEDED

Status: `SUPERSEDED BY LEAST-SHELL BUDGET CORRECTION / z^2 CENSUS RETAINED AS CONDITIONAL DIAGNOSTIC ONLY`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Authoritative correction:

`docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`

## Correction

The original note used

\[
12u-1=2\left(6u-\frac12\right)
\]

to credit two ordered-pair penalties. This omitted the least-prime-shell T1–T2 penalty

\[
\ell(u)
=\frac12+6\left[\min\left(u,\frac{113}{240}-u\right)-\frac16\right]_+.
\]

The actual pair budget is

\[
C(u)=12u-1-\ell(u).
\]

At `u=1/6`,

\[
C(u)=\frac12,
\]

so only one maximal pair penalty `1/2` is uniformly free. Therefore the four-prime-witness / `D^(1/3)=z^2` residual ceiling does not follow.

The valid replacement is:

\[
\boxed{
\text{least-prime shell + one maximal ordered pair are absorbed pointwise},
}
\]

so any residual pair has a three-distinct-prime witness and conditioned inner level

\[
\boxed{Q_{\rm res}\le D^{1/2}=W^{5/9}.}
\]

At the Tier-A splice, after P(23) prestripping, the corrected worst-level beta-2 hard Rosser family has depth at most four and exactly

\[
\boxed{74025}
\]

states; see the correction note and its checker.

## Conditional diagnostic retained

The finite arithmetic census in the original note is still numerically correct **conditional on** a hypothetical `Q<=z^2` shell:

- P(23)-stripped hard support: 254 states, depth at most two;
- anchor-free odd support: 3141 states, depth at most five.

Those numbers must not be used as the actual T1–T2 residual support until an independent argument truly forces a `z^2` level.

No finite P2 theorem or all-K claim is made here.
