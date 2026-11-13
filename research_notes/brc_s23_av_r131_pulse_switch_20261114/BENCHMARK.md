# R131 exact benchmark — explicit event trace vs existential witness

Date: 2026-11-14 (Asia/Shanghai). Frozen input 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Execution uses local CPython Fraction; repeat count 3, in-process median milliseconds. Different requested outputs are compared: (a) full ordered trace enumeration with direct indicator evaluation and (b) two rational witnesses for the exactly two valid 16-bit words. This is not a matched-output performance ratio or a direct run of R130.

| B | Explicit trace positions | Trace construction (median ms) | Two certificates (median ms) |
|---:|---:|---:|---:|
| 64 | 251 | 1.169925 | 0.007541 |
| 256 | 1,019 | 5.558915 | 0.010145 |
| 1,024 | 4,091 | 25.376270 | 0.015714 |
| 4,096 | 16,379 | 100.042392 | 0.019689 |

Verification: 159 B values from 2 through 160, 50,721 exact partition representatives, 25,281 distinct cuts, 5,000 seeded random rational checks, 144 aligned scale/period cases with 12,912 exact probes, plus a 151-decimal-digit coefficient and exact positive/negative certificates. Full data: verification_r131.json. Result R131_PULSE_SWITCH_PASS.

Theorem R131.3 proves Omega(B) output records are needed for explicit ordered cuts of this family. Existential membership and witness computation requires only O(m) bit-pattern scans plus a fixed count of arithmetic operations on O(log B)-bit numbers. The full trace itself has a succinct pulse formula, and may be kept compressed. Exact rational arithmetic establishes all comparisons; timing fields depend on host load and Python version.

Reproduce: python check_r131.py > verification_r131.json. Numerical timing values may differ in a new environment; all mathematical test counts and Boolean checks are deterministic.
