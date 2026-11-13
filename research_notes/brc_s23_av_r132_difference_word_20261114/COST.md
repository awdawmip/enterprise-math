# R132: exact one-word feasibility versus full trace enumeration

Executed on 2026-11-14 Asia/Shanghai in one CPython standard-library Fraction process. Input family: x=0, A=B, d=E=1, m=12, theta in (0,1). The specified query word has only its last coordinate equal to 1. Median milliseconds of three independent in-process runs:

| B | Exact word decision and witness (ms) | Independent full atom/trace enumeration (ms) | Distinct attainable words |
|---:|---:|---:|---:|
| 64 | 0.105506 | 58.296449 | 224 |
| 256 | 0.113288 | 240.421373 | 224 |
| 1,024 | 0.129762 | 958.604351 | 224 |
| 4,096 | 0.164223 | 3728.850889 | 224 |

Both routes use exact rational arithmetic. The decision solver returns one witness for a specified pattern; the trace oracle generates and deduplicates all signatures across the parameter interval. These are different output contracts; the measured values are not an equal-output benchmark speedup claim or a direct rerun of R130.

Complete validation in verification_r132.json: B=2..18, m=1..8, 136 cases, 14,600 independently enumerated parameter positions, 8,670 all-pattern decisions (3,236 feasible), 5,000 seeded random words (790 positive), 151-decimal-digit B and m=64 with four rational witnesses. Exact result R132_ONEINTEGER_FEASIBILITY_PASS.

The structural theorem yields O(m²) inequalities in one integer q with O(log(B+m))-bit coefficients; exact witness extraction uses rational midpoints. Explicit full ordered trace output must report at least 2B-3 genuine changes of the first bit. Full input/output, preprocessing and arithmetic precision are included in the stated scope.

Reproduce the exact assertions: python check_r132.py > verification_r132.json. Wall-clock measurements depend on host load and interpreter; pass/fail and combinatorial counts are deterministic.
