# T6 p13 v13=1 vertical order 8 split (4,4) — full exact author exclusion

2026-11-23 (Asia/Hong_Kong). Exact frozen model: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` at `d84bd940cfb093cdc60e569f15cad58772a51dca`; both original side exponent masses separately at most **2331**. This is **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

**Result:** The remaining cancellation-normalized p13 order-8 split **(4,4)** has no candidate satisfying the full six mixed 13-adic necessary congruences and both original budgets. Consequently, when combined with existing `(0,8),(1,7)` and newly saved `(2,6),(3,5)` exclusions, all five order-8 splits are author-level excluded. The mother goal `T6=2332` remains OPEN because higher p13 and lower prime layers remain.

## Exact carrier and symmetry

An atom `(q,r)` represents denominator `13(13q+r)`, cost `169q+13r-1`, with `1<=r<=12`. The q0 signed vector coordinate `u_r` represents denominator `13r` and cost `13r-1`. Six necessary constraints are

```
sum_r u_r*r^(-j) + sum_plus (13q+r)^(-j)
                    - sum_minus (13q+r)^(-j) == 0 (mod 13^j), j=1,...,6.
```

All arithmetic and Gram-Schmidt comparisons were exact (integer/Fraction), with the saturated 12D q0 lattice of index `13^21` and min Gram-Schmidt diagonal square greater than `2*2331^2`. For equal vertical orders we enumerate **unordered unequal canonical named rosters** only: a pair with opposite sign is its sign-reversed copy, so `pos<neg` is complete. Equal named rosters reduce to the previously closed q0-only case; any pair sharing a named atom reduces, by cancellation, to an already handled lower order, so the counted order-8 primitive support is disjoint.

There are 2,535 signed-side canonical order-4 named rosters. Hence exactly `choose(2535,2) = 3,211,845` unordered unequal pairs were covered. All exact q0 solutions inside the necessary budget ball were enumerated with at most the two nearest integer choices per coordinate (the justified radius is below the exact GS minimum diagonal square). Final original side masses are evaluated separately.

| First roster indices | Unordered unequal pairs | Common named support | Primitive pairs evaluated | GS recursion nodes | Relaxed candidates | Budget-valid |
|---|---:|---:|---:|---:|---:|---:|
| [0,200) | 486,900 | 237,442 | 249,458 | 566,781 | 0 | 0 |
| [200,600) | 853,800 | 352,103 | 501,697 | 1,121,134 | 0 | 0 |
| [600,1100) | 842,250 | 387,396 | 454,854 | 1,004,672 | 0 | 0 |
| [1100,1700) | 680,700 | 294,211 | 386,489 | 844,632 | 0 | 0 |
| [1700,2535) | 348,195 | 137,666 | 210,529 | 458,368 | 0 | 0 |
| **Total** | **3,211,845** | **1,408,818** | **1,803,027** | **3,995,587** | **0** | **0** |

All intervals finish and exactly cover [0,2535), without overlap. No relaxed affine-ball candidate survives the exact lattice search, stronger than an eventual budget-only exclusion. Per-interval source-order SHA256 over `str((pos,neg))+'\\n'`:

```
[0,200)       a75d8113b5e2baa461cf6187f50aa25129b250fab105f377791373e36ae337f5
[200,600)     688e88560cd811ce8d6e5f1273c94ce2ee3d74f0a4be877f4035d30b8fb90144
[600,1100)    89cd518f596a4980f70aa4833b7d92f0fe16f61bea8de5ca190fe47259769219
[1100,1700)   eb81272e58769aa886cc09ac952cf6de2256ecdb72612ab1a7dc4dc604c6e5df
[1700,2535)   ba4c50cad7a4d55d011467fa5806669d928bae5b619c2db5f40906a5502ccae9
```

The author-local finite JSON run summary has SHA256 `ba8568e5adca461ac75ebbc24d11fe7356d255861f6a5cf84248e222a6faff6d`. Source code reuses the already-published `research_checks/T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` roster and exact q0 algebra with `(4,4)` and a `pos<neg` symmetry restriction. A separate post-publication run of that existing checker and independent review have NOT been performed. The complete standalone local JSON is not claimed as GitHub-published.

**Evidence boundary:** the earlier p13 valuation>=2 cancellation and q0 saturation are dependencies; the finite proof is author-only. Existing Research Activity author attribution is unresolved across control subjects; no historical Researcher/RA event was fabricated. Source continuation and Task receipts are read-only without a winning CLAIM, Native PROGRESS or Result. Keep the older, separate q14 formal continuation intact.

**Next scientifically unfinished unit:** p13 vertical order **9** under the original frozen scope, first identify admissible side-order partitions by true mass and cancellation; perform exact mixed-congruence/affine tests as appropriate. Do not relabel the entire p13 or T6 problem solved.
