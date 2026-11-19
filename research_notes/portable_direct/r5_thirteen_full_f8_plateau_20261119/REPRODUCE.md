# Reproduce the R5 thirteen-label all-244 eight-error plateau

The original frozen input is fixed by the 2026-11-19 research pin `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`, file `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The accompanying `stages_18.json` supplies `tau=int(U)-1`. The frozen input and old complete f0..f6 table are included in the conversation's portable ZIP, `EnterpriseMath_R5_Thirteen_F0_F8_Complete_20261119.zip`. Place them in this directory.

1. `python3 MAKE_ADJ.py`. This validates input SHA-256 and builds 6,619,136 exact ordered interval bits.
2. `g++ -O3 -std=c++17 R5_F7F8_CLASS_SOLVER.cpp -o solve13`.
3. For each of the 48 `representative_t` rows in `R5_F7F8_CLASSES.csv`, run `./solve13 window_adj.bin <t> 8 25000000` and compare both lines with the recorded f7/f8 values and memo-state counts. Each run returns 7385/8335, including the 9,426,228-state t144 case.
4. `python3 VERIFY_244_ENDPOINT_CLASSES.py` independently reconstructs all priced joint support families from **integer doubled left endpoints**, checks all 244 label memberships and 48 class statistics and outputs `R5_F7F8_244_LABEL_CLASSES.csv`.
5. For a separate implementation path, `python3 MAKE_INDEPENDENT_ACTIONS.py 2 130 144`, `g++ -O3 -std=c++17 INDEPENDENT_NIBBLE_ORACLE.cpp -o oracle13`, then `./oracle13 ACTIONS_T2.txt 8`, etc. Each yields 8335. This second program does not read the binary adjacency and encodes the entire error state as 4-bit digits rather than mixed radix.

The GitHub `RESULT.json` supplies all 48 representative outputs and coverage; the packaged original local logs, 244-row f0..f8 table, compiled validation outputs and hashes provide a complete recomputation capsule. The scientific conclusion is a fixed-tau scalar theorem; review state NOT_REVIEWED and formal CLAIM/RUN unchanged.
