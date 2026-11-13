# R131 benchmark — dense full-word sweep vs exact cyclic gcd quotient

Date: 2026-11-14 (Asia/Shanghai); S23 auxiliary model at frozen pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Procedure

Exact common input for both methods: `x=1/7,A=3K,d=K,E=2K,m=7,I=(0,1)`, with K=1,2,4,8,16,32,64,128. The dense implementation independently constructs all R129 unquotiented exact affine integer-crossing cuts and evaluates complete 7-bit words at each cell/cut. The R131 implementation builds the normalized circular sparse trace once, filters singleton and open-cell states using exact integer-lift inequalities and returns the exact same set of attained full words. A direct `assert dense_set == quotient_set` was executed for every K.

Both variants use the same CPython standard-library `Fraction` arithmetic on one local machine. Each variant was executed separately three times; the figures below are observed median wall-clock milliseconds from the final recorded run, not controlled microbenchmark performance guarantees. Code: `benchmark_r131.py`; raw records: `benchmark_r131.json`. Reproduce beside the decoded `check_r131.py` using `python benchmark_r131.py`.

| K | Dense cuts | Quotient cuts | Distinct words | Dense ms | Quotient ms | Ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 44 | 44 | 36 | 2.702 | 1.751 | 1.54 |
| 2 | 89 | 44 | 36 | 5.258 | 1.736 | 3.03 |
| 4 | 179 | 44 | 36 | 10.454 | 1.800 | 5.81 |
| 8 | 359 | 44 | 36 | 18.416 | 1.819 | 10.12 |
| 16 | 719 | 44 | 36 | 42.941 | 2.097 | 20.47 |
| 32 | 1439 | 44 | 36 | 83.186 | 1.989 | 41.82 |
| 64 | 2879 | 44 | 36 | 160.131 | 1.715 | 93.40 |
| 128 | 5759 | 44 | 36 | 393.607 | 2.195 | 179.33 |

All eight exact set comparisons passed (`R131_BENCHMARK_EXACT_WORDSET_MATCH`). The reduction in *event counts* for this family follows rigorously from the gcd quotient, and the displayed runtime differences are measurements for a single interpreter/CPU environment. This benchmark does not compare R127/R126 integer programming solvers or the generation of every ordered repeated word in I. It measures construction of the **distinct attained word set**, not the full repeated parameter-time trace.

## Next

Test large coprime normalized coefficients and modular short relations to establish the crossover between R131 event enumeration and exact integer feasibility; record complete byte cost and memory, while preserving individual singleton-cut witnesses.
