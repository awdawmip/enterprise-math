# Hamming–Chebyshev synchronization Lean extraction plan

Status: `FREE_RESEARCH_FORMALIZATION_PLAN / REUSE_FIRST / NOT_FOUNDATION`
Date: `2026-09-04`

## Existing formal surfaces to consume

From the current #1159 branch:

- `hammingShellMode_zero`: shell-zero Krawtchouk amplitude is `Nat.choose m k`;
- `hammingShellMode_zero_ne`: physical shell-zero amplitudes are nonzero;
- the genuine finite Hamming/Krawtchouk operator and basis.

From pinned mathlib:

- `Nat.lcmUpto` and `Nat.factorization_lcmUpto`;
- `Chebyshev.psi_eq_log_lcmUpto`;
- `Chebyshev.choose_dvd_lcmUpto`;
- `Nat.sum_range_choose`;
- Kummer/Legendre factorization theorems for binomial coefficients.

Reuse resolution: `COMPOSE_APPLIED`. No new general LCM, primality, Chebyshev, or Kummer tool family is created.

## First Lean checkpoint

Define

`hammingRowClock m := (Finset.range (m + 1)).lcm (Nat.choose m)`.

Prove:

1. every physical shell-zero amplitude divides `hammingRowClock m`;
2. the row clock is nonzero/positive;
3. the row clock divides `Nat.lcmUpto m`;
4. `2^m <= (m+1) * hammingRowClock m` from the Hamming row sum;
5. the same statements rewritten through `hammingShellMode_zero`.

The exact Farhi identity

`(m+1) * hammingRowClock m = Nat.lcmUpto (m+1)`

is deferred to the next formal checkpoint because it requires the sharp lower factorization bound supplied by the explicit maximal-carry shell.

## Next formal checkpoint

Formalize PHC-T01:

`max_k v_p(choose (N-1) k) = log_p N - v_p(N)`

with explicit witness `k = p^(log_p N) - p^(v_p N)`, then obtain the exact clock equality prime-by-prime.
