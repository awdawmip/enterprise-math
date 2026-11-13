# R130 exact benchmark — compressed event trace versus dense enumeration

Date: 2026-11-14 Asia/Shanghai. A reproducibility and algorithm-cost comparison for the S23 *auxiliary* observer, frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Scope and execution

`benchmark_r130.py` uses the same CPython `Fraction` environment, identical rational input `x=A=0,d=E=1,I=(0,1)`, and `m=16,32,64`. Each operation is separately executed three times, reporting median milliseconds (no fixed CPU clock or controlled thermal conditions). Dense mode independently constructs all event roots and evaluates every bit at every singleton/open-cell position; sparse mode constructs a lossless delta log; expansion converts that log to the **same full ordered word list**. The script asserted exact equality of all expanded and dense outputs, returning `R130_BENCHMARK_MATCH`.

| m | exact cuts | complete positions | dense ms | sparse ms | sparse-to-full expansion ms | dense bit evaluations | sparse bit evaluations |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 71 | 143 | 12.020 | 2.705 | 0.024 | 2288 | 408 |
| 32 | 307 | 615 | 88.791 | 11.747 | 0.151 | 19680 | 1832 |
| 64 | 1227 | 2455 | 707.716 | 55.080 | 1.541 | 157120 | 7752 |

For `m=64`, sparse construction plus full expansion took approximately 56.621 ms versus 707.716 ms for dense full-word calculation in this particular run, a ratio of approximately **12.5×**. The gain largely reflects fewer rational indicator evaluations; the comparison includes root generation in both modes. Full output still requires its own storage and materialization. These are measurements of the stated input family and local environment, not performance guarantees for arbitrary coefficients or languages.

## Mathematics and next experiment

R130.1 proves an exact evaluation bound `m+2 Σ_c |J(c)|`; R130.2 adds persistent point queries at logarithmic index cost. A useful next measurement is a controlled coefficient-bit-length matrix: fix m and interval precision, increase slope magnitudes while comparing event count, rational bit lengths, memory, total time, and the fixed-dimensional feasibility routes R126/R127. In particular the present quadratic event-sweep bound is coefficient-sensitive, whereas R126/R127 remain alternative representations for large slopes.

Data: `benchmark_r130.json`. Reproduction: `python benchmark_r130.py` after placing it beside `check_r130.py`. The proof and original verification data remain unchanged.
