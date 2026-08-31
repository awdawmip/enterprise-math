# Valley-band factoring cost model — frozen partial matrix

## Scope and classification

This model describes only the CPython 3.14.6 implementation and frozen
2026-08-23 corpus on the recorded i5-4690K execution node. It is a measured
partial model, not an asymptotic speed claim and not a comparison with an
optimized native quadratic sieve.

Classification: `INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`.

## Accounting model

For each completed run, let

- `P` be point candidates,
- `V` be band candidates,
- `R` be fully verified relations,
- `rho` be GF(2) rank,
- `D` be tested dependencies, and
- `W` be measured wall time.

The primary empirical quantities are

`relation_yield = R / (P + V)`,

`rank_yield = rho / (P + V)`, and

`rank_rate = rho / W`.

The instrumented decomposition is

`W = T_state + T_root + T_sieve + T_trial + T_recombine + T_LA + T_gcd + T_unattributed`.

`T_unattributed` is retained rather than forced into another stage. It includes
Python loop/allocation overhead, primality classification outside the timed
recombination block, `tracemalloc`, and timeout checks. Its size is a material
instrumentation limitation in the SLP/DLP runs.

## Point-only calibration at 96 bits

All rows below use factor-base bound 1200, multiplier 1, 60,000 candidates, and
three repeats. Relation and rank values were identical across repeats.

| Instance | CFRAC median s | Closed-point median s | closed/CFRAC | full relations | rank |
|---|---:|---:|---:|---:|---:|
| R96-00 | 2.6123214 | 4.3993874 | 1.6841 | 23 | 22 |
| R96-01 | 2.6175474 | 4.4890566 | 1.7150 | 29 | 29 |
| R96-02 | 2.5986081 | 4.3776894 | 1.6846 | 30 | 30 |

Across the nine runs per path, the median marginal cost was 43.538690
microseconds/candidate for reference CFRAC and 73.323123
microseconds/candidate for the independently implemented closed point path.
Their mathematical relation-stream and rank-trajectory digests agreed in all
nine paired runs. The observed slowdown is therefore implementation cost, not
evidence of a different relation stream.

## Frozen full-band threshold diagnostics

Each threshold was run once on R96-00 with SLP and retained as `TIMEOUT`.

| threshold | orbit steps | opened bands | band candidates | full | rank | wall s | peak bytes |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | 3,031 | 145 | 26,834 | 3 | 3 | 20.1101485 | 1,236,680 |
| 64 | 3,580 | 95 | 27,804 | 3 | 3 | 20.3438452 | 1,229,340 |
| 128 | 4,097 | 56 | 27,071 | 3 | 3 | 20.2078773 | 1,226,024 |
| 256 | 4,701 | 34 | 32,273 | 3 | 3 | 24.5933169 | 3,186,719 |
| 512 | 5,078 | 16 | 25,714 | 3 | 3 | 20.0004144 | 3,185,413 |

Every row is right-censored by the timeout. Threshold 256 exceeded the nominal
20-second limit by 4.593 seconds because the implementation checks the deadline
between orbit steps, not inside one band. Consequently these rows do not rank
threshold quality and cannot justify a best threshold.

## Large-prime ablation at threshold 256

The same R96-00 input, factor base, orbit and threshold were used. Each row is
one timeout-censored repeat.

| mode | total candidates | partials | DLP edges/cycles | full/rank | candidates/s | rank/s | wall s |
|---|---:|---:|---:|---:|---:|---:|---:|
| none | 439,847 | 0 | 0 / 0 | 30 / 30 | 21,474.46 | 1.4647 | 20.4823344 |
| SLP | 36,974 | 39 | 0 / 0 | 3 / 3 | 1,539.80 | 0.1249 | 24.0121686 |
| DLP | 36,974 | 223 | 223 / 0 | 3 / 3 | 1,487.40 | 0.1207 | 24.8582087 |

For this implementation, primality/cofactor classification dominates SLP/DLP
and is not completely captured by the stage timers. No DLP cycle completed.
The no-large-prime row processed about 14 times as many candidates per second
and about 12 times as much rank per second. One censored repeat is insufficient
for an algorithm-level claim; it is strong evidence of a local implementation
bottleneck and a reason not to report LP speedup.

## Multiplier and adaptive holdouts

Static quadratic-character scores selected candidates 13, 5, 17, 15, and 23.
Training-only 4,000-step pilots on R96-00/01/02 selected multiplier 13 with
aggregate rank 13. On holdout R96-06, multiplier 13 reached 29 verified
relations/rank 29 in 60,000 steps and 4.8284967 seconds; no dependency or factor
was found. The factor-base dimension for this run was 96.

The adaptive policy used only the threshold-256 training diagnostic. Its
Laplace posterior was 0.0001081783 relations/candidate and the frozen rule
opened no holdout bands. With SLP still enabled for point cofactors, the run
timed out at 33,426 points with 107 full relations, rank 102, five tested
dependencies, and no factor. The factor-base dimension was 108, below the
frozen rank target of 116. This is an adaptive-null result, not evidence for a
useful band policy.

## Exact-size checkpoints

Point-only CFRAC completed its fixed limits at 104, 112 and 128 bits:

| checkpoint | candidates | full/rank/dependencies | wall s | factor-base dimension | factor |
|---|---:|---:|---:|---:|---|
| F104 | 120,000 | 28 / 28 / 0 | 6.7010743 | 149 | null |
| F112 | 160,000 | 48 / 48 / 0 | 12.5682487 | 219 | null |
| F128 | 200,000 | 28 / 28 / 0 | 21.2349045 | 338 | null |

All are below `factor_base_dimension + 8`; none is a completed factorization.
Closed-point and band checkpoint rows were preserved as `NOT_RUN_BUDGET`.

## Memory and missing QS context

Maximum recorded Python allocation peak was 14,804,351 bytes in the no-LP
threshold-256 run. This is `tracemalloc` Python-allocation peak, not whole-process
resident set.

The pinned same-language `python_spqs_context` implementation is present and
hashed, but all four planned context rows were `NOT_RUN_BUDGET`. Therefore no
CFRAC/QS timing ratio exists. Language difference would have been `NONE`
(CPython versus CPython); no native-QS comparison was made.

## Model boundary

The frozen matrix has 31 completed rows, 9 timeouts, 49 budget-not-run rows,
zero errors, and zero factors. No extrapolation beyond this node, language,
corpus, factor-base grid or timeout regime is warranted. The full cost/yield
surface remains open.
