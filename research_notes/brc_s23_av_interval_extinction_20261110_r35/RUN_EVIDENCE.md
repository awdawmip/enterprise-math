# R35 actual local exact-computation evidence — 2026-11-10

Executed using Python integer and fractions.Fraction exact arithmetic; integer square-root rational enclosure for the second input. The production path contains **no per-positive-event list**.

Standalone R35:
```
S23 prefix [(129,164,(16,-61)), (165,292,(-43,164)), (293,328,(0,0)), (329,389,(-43,164))]
S23 final (-7551,28800)
S23 stages=3, extinction_queries=19, source_count_queries=4736, full_risk_queries=6
Independent S23 phase partition checks: 261

sqrt2_minus1 m=16 n<=96:
[(17,29,(5,-12)), (30,45,(-12,29)), (46,58,(0,0)), (59,70,(-12,29)), (71,74,(29,-70)), (75,87,(0,0)), (88,96,(29,-70))]
second final (106,-254)
second stages=5 extinction_queries=23 source_count_queries=848 full_risk_queries=10
Independent second-family phase partition checks: 80
PASS_R35_INTERVAL_EXTINCTION_EXACT_REGRESSION_TWO_FAMILIES
```

Compact independent invocation (using R34 pinned source file):
`python VERIFY_R35_COMPACT.py /path/to/VERIFY_R34_PREFIX.py`:
`PASS_R35_COMPACT_INTERVAL_CERT`.

Integration with *unmodified* R32 and R33:
```
PREFIX 4 no individual events, fibre-extinction queries 19
STAGES 78 Euclidean jump decisions 28
TAIL 148 direct bulk blocks, FINAL 298 runs
RESULT (-4017401528447, 15321634290944)
SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
PASS_R35_298_TRILLION_HORIZON_BYTE_IDENTICAL
```

Evidence scope: author-run exact computation and comparison to the earlier R32 frozen reference, not independent peer review.
