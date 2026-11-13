# R128.4 — Exact published-formula crosscheck

Date: 2026-11-13 (Asia/Shanghai). **Prior-art verification**, not a new theorem. Source: A. E. Frid and D. Jamet, *The number of binary rotation words*, RAIRO Theoretical Informatics and Applications 48 (2014), 453–465, DOI: 10.1051/ita/2014019. [Published article](https://www.numdam.org/item/ITA_2014__48_4_453_0/), [preprint](https://arxiv.org/abs/1302.3722).

The paper's Theorem 1 gives an exact expression for the number f(n+1) of length-(n+1) binary rotation words, using Euler's totient function and the auxiliary sums f_1(n), f_2(n,l). The complete, **independently implemented** rational transcription of this published expression is in [check_r128_lit.py](check_r128_lit.py), separate from the cyclic-block construction [check_r128.py](check_r128.py).

The exact program was executed locally on 2026-11-13, returning:

```
R128_FRID_JAMET_FORMULA_CROSSCHECK_PASS 10 9
```

It compared independently generated rotation-word counts for every length m=4,...,13 (10 cases) against the paper's exact Theorem 1 formula, and checked nine counts against its published Table 1:

| m | Published / recomputed count |
|---:|---:|
| 6 | 64 |
| 7 | 112 |
| 10 | 504 |
| 15 | 2804 |
| 20 | 9442 |
| 30 | 51306 |
| 50 | 423814 |
| 75 | 2222984 |
| 100 | 7155096 |

The paper gives the sharp leading-order asymptotic `f(m) ~ 3*m^4/(4*pi^2)`. This confirms that `Theta(m^4)` belongs to established general rotation-word theory, so the previous generic complexity insight is not claimed novel.

**R128's exact S23 application** is the filter combining the polynomial free-rotation candidate enumeration with R126's three-integer feasibility encoding for correlated one-parameter signed S23 phases. It yields an upper bound `O(m^7)` on the *number of fixed-dimensional ILP calls for all signatures*; actual ILP bit costs and practical speed remain separately unmeasured.

Next scientific problem: analyze the correlated S23 family for parameter-sensitive improvements, rather than trying to beat `m^4` for the unrestricted free rotation words. The mathematical claim/admission status remains author-side, NOT_REVIEWED.
