# T6 p13 one-valuation vertical order8 split (3,5) — full exact author exclusion

Date 2026-11-23, Asia/Hong_Kong. Mother goal `T6=2332` OPEN. Exact frozen scientific input `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md@d84bd940cfb093cdc60e569f15cad58772a51dca`, with 2331 cap **on each side**. No Native Task CLAIM/RUN or independent review claimed.

**Result:** No original exponent-shape configuration of maximal-prime-13, 13-valuation-one, vertical total order8 split `(3,5)` survives all six mixed 13-adic conditions and the original separate mass caps. This is the second new completed split after `(2,6)`. Remaining order8 split `(4,4)` and higher p13/lower prime layers remain OPEN.

The carrier is the same as the previously saved q8 `(2,6)` note. A named vertical atom `(q,r)`, with `1<=r<=12`, denotes denominator `13(13q+r)` and cost `169q+13r-1`. q0 signed coordinate `u_r` denotes denominator `13r`, cost `13r-1`. All exact observer equations yield six modular necessary conditions:

```
sum_r u_r / r^j + sum_(q,r)inPLUS 1/(13q+r)^j
  - sum_(q,r)inMINUS 1/(13q+r)^j == 0 (mod 13^j), j=1,...,6.
```

The saturated q0 lattice's index is `13^21`; its exact rational Gram-Schmidt minimum diagonal square strictly exceeds `2*2331^2`. Exhaustive two-nearest-integer recursion, exact rational comparisons, full named roster and opposite-side common-support cancellation were used. Recompute every relaxed leaf's signed q0 costs separately. The finite exclusion depends on the earlier high-valuation cancellation result and 12D lattice and is not independently admitted.

| First-side canonical range | Raw pairs | Common-support pairs | Evaluated primitive | Exact GS nodes | Relaxed leaves | Both-side valid |
|---|---:|---:|---:|---:|---:|---:|
| [0,20) | 218,160 | 100,080 | 118,080 | 276,615 | 0 | 0 |
| [20,120) | 1,090,800 | 536,990 | 553,810 | 1,261,024 | 0 | 0 |
| [120,160) | 436,320 | 220,040 | 216,280 | 487,159 | 0 | 0 |
| [160,260) | 1,090,800 | 496,935 | 593,865 | 1,340,092 | 4 | 0 |
| [260,330) | 763,560 | 351,355 | 412,205 | 916,037 | 2 | 0 |
| [330,400) | 763,560 | 319,225 | 444,335 | 986,972 | 0 | 0 |
| [400,465) | 709,020 | 246,910 | 462,110 | 1,020,736 | 1 | 0 |
| [465,520) | 599,940 | 137,225 | 462,715 | 1,044,744 | 1 | 0 |
| **Total** | **5,672,160** | **2,408,760** | **3,263,400** | **7,333,379** | **8** | **0** |

Complete first-side roster **520**, second-side roster **10,908**. Exactly 8 relaxed candidates pass the ball/modular check; each violates at least one actual mass cap. The minimum excess of the larger side mass above 2331 is 1036. There is no unvisited source-order range or inferred empty prefix.

Exact per-interval source-order SHA-256 (hash over lines `str((plus_roster,minus_roster))+'\\n'` in canonical sorted order):

```
[0,20)    58c351a82b72e8508ad30d0e8d03a00475e7da193b3080d2c1b21a005c58dbcc
[20,120)  cd3af95b522da29b687f43ed3c7c15bbf0f7e8d4f5d54f014ed0d29a16ccbb8b
[120,160) 9dd62fb5ef87f2b2b1289f10185d681129ff6df4744951011f1f1f2ef1b258ba
[160,260) e98b65d8592d8ff9e766cb928c0ee10518db8d6f02f42dcf36bfa8bbf691b136
[260,330) a41719df9ba36020a818a072b07467c2c02a1ed9ca916f0fdb37918eac863f62
[330,400) f3f98d2b94d373f3a69c8cfa22dfd66ab5ba5d3d52177b54a57e96ed12579460
[400,465) 50eb4c8001309c04d0e00f16c6e73bcf737ad180de132203c46d283efb11888e
[465,520) ac5848b30cf782c072be3ff647db43aa0fda848ee30c6b1a3c242fad6852b387
```

Reproduce with the already-published `research_checks/T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` using parameters `3 5 start end` for all eight slices. The actual computation used an author-local derivation of the q0 exact basis, and complete local witness JSON has SHA256 `1972fa2a0808fe0991277602c5d791f8dfe3c74ba366caa3cb18f10d31bf425c`. That standalone complete local JSON is **not yet a remote canonical artifact**. The published replay script was **not separately post-publication rerun**. Status: `AUTHOR_EXACT_FINITE_EXECUTED / GITHUB_AUTHOR_NOTE_PUBLISHED / UNREVIEWED / NOT_ADMITTED`.

Original Source conversation lane is distinct from maintenance; a pending Activity provenance mismatch remains, so no new event is assigned to the historical RA. Native semantic PROGRESS and Result remain absent. The Source continuation receipt `onhour-20261123-0627-own-t6-source-cont-ro-v1` has SUCCEEDED; this is not current execution authorization.

**Next:** p13 vertical order8 `(4,4)`, using canonical *unordered distinct* sides or ordered pairs with symmetry removed, exact named cancellation, q0 affine ball and two side budgets. Any genuine surviving modular/budget candidate needs lower-prime completion and original H0 scrutiny. Keep the overall T6 OPEN.
