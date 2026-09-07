# BRC Square-Gap Table Cascade — Round 12

Status: `EXACT STAGED QR FILTER / ZERO FALSE NEGATIVES / FIXED 3.6KB BALANCED PROFILE / FINITE PIPELINE GAIN`
Date: `2026-09-07`
Parents: `t0.brc_square_gap_prefilter`, `t0.brc_linear_deep_tail`

## 1. Question

Round 11 reduced the long multiplier-root transport to the order-one linear law

`d=floor(2hJ/(4m+h))`

followed by at most two BRC corrections.  The user then asked whether the
previously built residue tables should be used rather than abandoned.

Yes.  The useful role of tables is not to replace the remaining integer division.
It is to make the *second* square-root test on the completion gap almost vanish.

## 2. Why a cascade instead of one large modulus

The checked-in mod-4032 bit table is only 504 bytes and has 192 quadratic-residue
classes, so a uniformly distributed integer survives with exact density

`192/4032 = 1/21 ~= 4.7619%`.

A larger single modulus rejects more values, but every candidate must pay that
larger modular reduction and touch the larger table.  A staged filter instead
keeps 4032 as the first gate and applies later moduli only to earlier survivors.

The BALANCED cascade is

`4032 -> 12155 -> 12673`,

where

`12155 = 5*11*13*17`,
`12673 = 19*23*29`.

The three moduli are pairwise coprime.

The existing 4032 table is reused directly.  The two secondary bitsets are small
enough to compile once per process from `x^2 mod M`, avoiding another large
checked-in base64 payload.

## 3. Exact table sizes and QR counts

| stage | modulus | raw bytes | QR classes | survival density |
|---:|---:|---:|---:|---:|
| 1 | 4032 | 504 | 192 | 1/21 ~= 4.7619% |
| 2 | 12155 | 1520 | 1134 | 1134/12155 ~= 9.3295% |
| 3 | 12673 | 1585 | 1800 | 1800/12673 ~= 14.2034% |

Profiles:

- `BASE`: 504 bytes;
- `COMPACT`: 2024 bytes;
- `BALANCED`: 3609 bytes.

## 4. Exact CRT survival law

A true integer square is a quadratic residue modulo every modulus, so every
stage is a necessary condition and the cascade has **zero false negatives**.

Because the stage moduli are pairwise coprime, the Chinese remainder theorem
makes the uniform joint density the exact product of the individual densities.

For COMPACT:

`(1/21)*(1134/12155) = 54/12155`

or approximately

`0.4442616%`.

For BALANCED:

`(1/21)*(1134/12155)*(1800/12673)`

`= 19440/30808063`

`~= 0.0006310036434`.

Thus only about

`0.0631004%`

of uniformly distributed gaps survive the three tables, corresponding to an
exact uniform rejection fraction of about

`99.9368996%`.

This is substantially stronger than the original single 4032 table while using
only 3.6KB of table memory.

## 5. Composition with the linear deep tail

For every retained multiplier state, Round 11 first obtains the exact BRC root
and remainder using the linear denominator predictor.  The completion gap is
then

`F = 0` if the remainder is zero, otherwise `2J+1-R`.

The cascade evaluates:

1. `F mod 4032`; stop immediately on rejection;
2. only survivors pay `F mod 12155`;
3. only those survivors pay `F mod 12673`;
4. only BALANCED survivors call exact `isqrt(F)`.

The cascade therefore attacks the remaining expensive squarehood test without
changing root-state semantics.

## 6. Reproducible finite benchmark

Committed benchmark parameters:

- deterministic odd N values;
- 16 samples per bit size;
- 700 retained mod-8 transitions per sample;
- same exact completion-gap semantics;
- direct baseline carries target by `hN` before each root and does not pay an
  artificial `m*N` multiplication;
- BASE and BALANCED use the same exact square witness check on survivors.

Committed finite results:

| N bits | BASE survivors | BALANCED survivors | no-table direct / linear BALANCED | linear BASE / linear BALANCED |
|---:|---:|---:|---:|---:|
| 1024 | 1161 | 35 | 1.86x | 1.04x |
| 2048 | 1271 | 23 | 2.02x | 1.04x |
| 4096 | 1162 | 27 | 2.32x | 1.09x |
| 8192 | 880 | 20 | 2.46x | 1.03x |

The incremental wall-clock benefit over the already optimized BASE pipeline is
modest because Round 11 moved the main bottleneck into root-state transport and
the remaining linear division.  The conceptual gain is larger: the expensive
second `isqrt` is nearly eliminated.

These are Python/environment finite timings, not an asymptotic machine-complexity
claim.

## 7. Other table uses tested and rejected for now

Two more aggressive ideas were probed before choosing the cascade:

1. **normalized reciprocal table for `1/(4m+h)`** followed by exact lower Newton
   refinement.  It is mathematically viable but substantially slower than
   Python big-integer division in the tested large-integer ranges;
2. **radix/BRC correction jump tables** before the certified order-one tail.
   They recover the exact root, but when the order-one predictor is still far
   away the correction quotient has too many bits and the Python digit walk is
   much slower than optimized `isqrt`.

Therefore the production decision is narrow:

`TABLES -> STAGED GAP REJECTION`,

not

`TABLES -> REPLACE LINEAR DENOMINATOR DIVISION`.

## 8. Boundary and next attack

- This is classical quadratic-residue filtering composed with BRC.
- It reduces only the second exact squarehood test; it does not reduce the
  multiplier search horizon.
- No RSA-practicality or asymptotic factorization-speedup claim is made.
- The 3.6KB BALANCED profile is the current default research tradeoff.

The next local target is the remaining order-one quotient

`floor(2hJ/(4m+h))`.

A future table-assisted division route should only be promoted if it beats the
native big-integer division after including table lookup, refinement and exact
correction costs.  Until then, retain native division and spend table budget on
staged square rejection.

## Artifacts

- `src/enterprise_math/brc_square_gap_cascade.py`
- `tests/test_brc_square_gap_cascade.py`
- `experiments/brc_square_gap_cascade_benchmark.py`
- `research_artifacts/brc_square_gap_cascade_benchmark_20260907.csv`
