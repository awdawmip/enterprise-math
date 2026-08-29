# Semiprime Square-Shell Midpoint Boundary — Driver Review

Status: `ACCEPTED / NEGATIVE_BOUNDARY / STATIC_SINGLE_SHELL_EXPANSION_CLOSED`

Driver-ID: `EM-DVR-P8H4Q2`
Driver authority: `DA-FADB5B44A384B8C3F3F5`

Task: `RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION`
Publication: `TP2-12778A2D48A1D5A57BA9`
Result: `RR-2A424E3B8EC11DC1278C`

## Verdict

`ACCEPTED` at `NEGATIVE_BOUNDARY / B+C` strength.

The result correctly separates exact shell/Fermat structure from factorization leverage. The adjacent-square-shell midpoint scan is exactly Fermat difference-of-squares in the declared coordinates; the discrete midpoint displacement obeys

`T = sqrt(N)(cosh(0.5 log(q/p)) - 1) - delta`, with `0 < delta < 1`,

so factor imbalance is the leading quantity and the local shell contribution is only the rounding-scale correction.

The tested adjacent-shell, local-neighbor-prime and raw finite multi-k feature family does not establish a factor-blind total-cost reduction. Neighbor-prime scanning reduces to trial-division ordering, while multi-k near-square residuals live inside multiplier-Fermat / Lehman / Hart structure.

The frozen counterexample `N=9171667=2851*3217`, `k=56`, is decisive against using raw nearest-square residual as a general productive-multiplier selector: the multiplier gives an exact difference-of-squares hit while ranking at the bottom of the tested residual ordering.

The exhaustive `N <= 10^7` census, held-out factor-ratio/bit-size tests, and deterministic checker supply an adequate adversarial boundary for this acceptance. No novelty, Working Truth, Foundation promotion, or asymptotic factorization advantage is accepted.

## Routing

Close further static single-shell/midpoint-correlation expansion. A continuation is justified only for a narrowly costed question that can still discriminate algorithmic value: `RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT`, with explicit total-cost accounting and kill conditions for no improvement, bit-size coverage collapse, or equivalence to standard Hart ordering plus modular sieving.

Lean formalization: `NOT_REQUIRED` at this structural/no-go checkpoint.

Independent replication: `NOT_REQUIRED` for this review authority; a second same-task return exists but its Result envelope is incomplete and must be repaired before it can enter parallel evidence synthesis.

External prior-art/duplication: `REQUIRED` for the exact residual-priority/Hart-equivalence boundary before any novelty-style interpretation.

Adversarial/ST: `SATISFIED_BY_REVIEWED_RESULT` through holdout, counterexamples and deterministic checker.

No canonical promotion is granted.
