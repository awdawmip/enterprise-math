# R37 actual local execution — 2026-11-10

Execution: `python VERIFY_R37.py` using Python arbitrary-precision integers, `fractions.Fraction`, `math.isqrt`, sorted historic phases, owner-labelled reverse scan, and separately implemented R36-style Euclidean Floor Sum per-arc rank/select. Six huge source windows plus direct finite enumerations executed. This is author-side evidence, not an independent proof acceptance record.

```text
SQRT2 16 mode CERTIFIED_SATURATED H/scan 22 oracle 496 bound 70
SQRT2 32 mode CERTIFIED_SATURATED H/scan 34 oracle 991 bound 169
SQRT2 128 mode CERTIFIED_SATURATED H/scan 133 oracle 3960 bound 408
SQRT2 257 mode CERTIFIED_SATURATED H/scan 471 oracle 7949 bound 985
S23 128 mode CERTIFIED_SATURATED H/scan 142 oracle 3960 bound 553
NEAR_THIRD 21 mode NEEDS_FLOOR_SUM_FALLBACK H/scan 2000 oracle 581 bound 4714045
PASS_R37_EXACT_SUFFIX_SATURATION_AND_FLOOR_SUM_REFERENCE PASS_SMALL_WINDOWS_BRUTE_AND_FLOOR_SUM
```

All five saturated rows: owner-labelled final sources exactly equal the independently computed whole-window Floor Sum select output (total comparisons: 16+32+128+257+128=561 labels); all scanned owner labels have whole-enclosure boundary-floor checks. Near-third scans 2,000 sources and reaches only 3 of 21 owners; its complete 21-label vector is determined by Floor Sum fallback at the rational midpoint. Small-window direct tests include 3 parameter/history configurations, 3 source endpoints and 7 requested lengths, with invalid negative windows skipped. Exact age vectors are preserved in `CERTIFICATE_R37_AGES.json`; `VERIFY_R37.py` regenerates the expanded rational certificate.

Local reference expanded-certificate SHA256 on the actual executed version: `767e05869595627da2675a52737b535cc35cce0527c9e0337a13dc619599ba72`. This byte digest includes diagnostic per-case wall-clock fields and is **not** a deterministic checksum of a fresh rerun. The exact age vectors, integer counts and rational convergent inequalities are stable mathematical contents.

Unchanged predecessor 298-run trillion-horizon dataset cross-check:
```text
R36  AFFINE_RUNS_R36.tsv   sha256=2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
R32  AFFINE_RUNS_R32.tsv   sha256=2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
```
These are verified earlier data files, not evidence that R37 recomputed the full 10^12-step output.

Validation scope: exact rational midpoint counts and whole-input interval-certified suffix owner labels; sufficient grid bounds use rational endpoint arithmetic; independent mathematical review and native P000 model transfer are pending.
