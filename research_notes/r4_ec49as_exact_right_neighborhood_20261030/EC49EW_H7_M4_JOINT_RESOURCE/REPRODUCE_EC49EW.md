# EC49EW reproducibility and sources

All paths below are within this research-note directory unless identified as immutable inherited links. Python 3.11+ and C++17 plus Node.js reproduce the primary integer and independent native-X6 checks; SciPy/HiGHS is used only for the independent MILP cross-check.

## Immutable predecessor implementation

For the frozen science model, retrieve `MODEL_EC49EU.py` from the predecessor `EC49EU_H7_M3_S4_EXACT/` evidence lineage at Git blob SHA `bcad085da0655d41753c166fd993cdb35e4d4815`, and `VERIFY_EC49EU_EXACT_DP.cpp` at Git blob SHA `d08c90554d205730ce6a36e89a59754e28f36902` (both in repository `awdawmip/enterprise-math`). The complete earlier EC49EU and EC49EV notes in Draft PR #1730 contain exact original context. They were used unchanged by this run; the two files are also embedded in the optional local full evidence bundle for offline reproducibility.

## Actual commands and expected results

```
python3 EC49EW_M4_S4_FULL.py
# full exhaustive result: H7=752 schedules; H6=389 exact prefixes;
# H7 screened 686; H7 exact-solved 66; global minimum E=92.

python3 EC49EW_M4_S6_T2T4_CASES.py
# exhaustive fixed-signature pattern: 72 cases; exact min E=72.

node VERIFY_EC49EW_INDEPENDENT.js
# PASS; returns independent finite populations and exact signed-X6
# witness E=92,M=4,S=4 and E=72,M=4,S=6.

python3 VERIFY_EC49EW_MILP.py
# HiGHS zero-gap witness-schedule objectives (92,72).

python3 VERIFY_EC49EW_CERTIFICATE.py
# Audit compressed full execution evidence, coverage, bounds and checks.
```

The exhaustive native-trie C++ DP is an integer OR-mask tree cover algorithm. It does not require floating arithmetic, approximate rank, logarithms or physical-time approximation. The rank checker is modular with a provable 9×9 determinant bound, not an assumption that modular rank is always rational rank.

**Actually executed local checks:** native integer C++17 DP in bounded resume segments, independent Node.js enumeration, and separate Python/SciPy HiGHS integer programming. Exact full report files are compressed using `gzip` then base64 and can be read back without loss. The raw `elapsed_seconds` field in one predecessor-style report measures only its last resumed segment.

**Git status:** This is an author-side portable research note pending native Research Activity/CLAIM/Result and independent Driver disposition; immutable Project P000 and science pins are unchanged. Full global M4,S<=6 classification remains future work.
