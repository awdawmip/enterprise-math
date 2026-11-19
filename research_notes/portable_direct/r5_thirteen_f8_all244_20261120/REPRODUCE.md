# R5 f8 exact reproduction

Frozen science: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`, input `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The frozen input and `stages_18.json` are included in the companion ZIP, not duplicated as a GitHub rewrite. Place both alongside the scripts.

Python 3.9+ and g++ C++17:

```sh
python3 MAKE_WINDOW_ADJ.py
python3 VERIFY_R5_THIRTEEN_F8_ENDPOINT_CLASSES.py
g++ -O3 -std=c++17 SOLVE_R5_THIRTEEN_F7_F8.cpp -o solve13
./solve13 window_adj.bin 12000000 > reproduced_f7f8.csv 2> reproduced_48_classes.log
```

The C++ program reads 101 x 256 x 256 bytes, deduplicates all 244 names into exactly 48 full priced-support signatures, solves f7 and f8 once per class and outputs 244 name-specific rows. Compare its stderr class log to `CLASS_CERTIFICATE_F7_F8.csv` and its stdout prices to `ALL244_VALUES_F0_F8.csv`. The `state_cap` argument must be at least 9,426,228. For a fast smoke test, use `./solve13 window_adj.bin 12000000 1` for only the first signature class.

An alternative 4-bit-counter oracle is included in the companion ZIP, with center-derived independent actions and actual f8 output logs for t=2,21,144. It verifies selected classes, not the full 48-class high-budget census. All f0..6 values reuse the preceding published certificate; the new result here is complete f7/f8 coverage.

Scientific provenance, theorem scope, exact recurrence and review boundary are in RESEARCH.md. Source hash verification is a data-integrity requirement, not mathematical admission.
