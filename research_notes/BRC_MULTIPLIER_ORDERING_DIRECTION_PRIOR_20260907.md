# BRC Multiplier Ordering — Direction-Prior Priority (RSA-270 target)

Status: `FINITE EMPIRICAL BENCHMARK / N-ONLY PRIORITY / NO FACTOR OBTAINED / NO COMPLEXITY CLAIM`
Date: `2026-09-07`
Researcher: `EM-DIRECT-5D08CB` (DIRECT-RSA270)
Parent: `BRC_MULTIPLIER_TRANSITION_RECURRENCE_20260906` (merged), cost-field ridge analysis (5b8f1a / 7e3b5d)

## Question

In what order should the candidate multipliers `m = 1..100` be tried so that the first
factor-bearing multiplier appears as early as possible, using only N-derivable information?

## Answer: the direction-prior

Every multiplier `k` admits several coprime factor directions `(a,b)`, `ab = k`, each with a
factor-bearing Fermat identity `(ap+bq)^2 - 4kN = (ap-bq)^2`. The endpoint add-cost is
`j*(a,b) = (sqrt(ap) - sqrt(bq))^2 + delta`, minimized along the ridge `a/b = q/p`. Under the
construction-family prior band `q/p in [1.765, 2.266]`, the N-only optimal priority is:

1. all `k <= 100` whose direction set intersects the band, ordered by their best band
   direction's **band-max cost coefficient** (the cost-field minimax table):
   `k=2 (2,1) c=0.0083 ; k=36 (9,4) c=0.1176 ; k=55 (11,5) c=0.1197 ; k=78 (13,6) c=0.1234 ;
   k=45 (9,5) c=0.1340 ; k=66 (11,6) c=0.1374 ; k=91 (13,7) c=0.1423`;
2. then the remaining `k` by ridge distance `min_{a,b | ab=k} |a/b - 2.0|`.

This is the multiplier-level form of the cost-field ridge: `(2,1)` first (the minimax
direction), then the band directions by their worst-case gap, then the off-band remainder.
The order depends only on the prior band and the direction set — no `p,q` knowledge.

## Benchmark (synthetic band-consistent semiprimes, 200 samples, ratio tolerance eps=0.10)

- mechanical `1..100`: mean hit position **23.4**, median **28**;
- direction-prior: mean **2.5**, median **2**;
- ridge-distance (simpler proxy): mean **2.2**, median **2**.

The ordering moves the expected hit position from tens to single digits (~21-position mean
improvement), multiplicative with the ~2x transition-recurrence transport speedup.

## RSA-270 target

The RSA-270 priority list starts `[2, 36, 55, 78, 45, 66, 91, 28, 84, 15, ...]` (band-k at
positions 1-7, vs mechanical positions `{2,36,45,55,66,78,91}`). Under the band-uniform
prior the expected first-hit position is 2.5. No factor was obtained; this is an N-only
ordering result, not a factoring improvement.

## Files

- `experiments/rsa270_multiplier_ordering_benchmark.py` — the ordering construction and the
  200-sample benchmark (exact integer arithmetic; all assertions pass).
- `research_artifacts/brc_multiplier_ordering_benchmark_20260907.csv` — per-sample hit positions.
