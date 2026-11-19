# Reproduce 52-reference R5 D14 exact plateau certificate

Frozen source: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Verify the full frozen `EXACT_R5_ALL_101_BUDGETS.json` SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; use frozen `stages_18.json` from the preceding R5 bundle. Do **not** fetch new scientific inputs from main.

From pinned `awdawmip/enterprise-math@c328562411f49bd9981d54b2eeb9b0220a66986c/research_notes/portable_direct/r5_fourteen_dominance_20261120/`, take `R5_FOURTEEN_F8_ONE.cpp` and `CENSUS_14_SIGNATURES.cpp` into a scratch directory with this file's `CERTIFY_52_REFS.cpp` and `ROOTS_NEW20.csv`. From the existing frozen R5 source reproduction bundle, use `make_adj.py` to create `window_adj.bin` (101×256×256 bytes).

Compile `g++ -O3 -std=c++17 R5_FOURTEEN_F8_ONE.cpp -o f8`, and run `./f8 window_adj.bin u v 20000000` for every CSV row; all twenty return exactly `F8=8335`. The standard predecessor 32 roots are already verified and remain pinned; they are not silently recalculated.

Compile and run `CENSUS_14_SIGNATURES.cpp` to create `R5_14_CLASS_REPS.csv`. It must contain 1,906 classes and 29,646 named pairs. Then compile and run `CERTIFY_52_REFS.cpp`. It must report `D14_52 CERTIFIED_CLASSES=1220 CERTIFIED_PAIRS=25896 UNRESOLVED_CLASSES=686 UNRESOLVED_PAIRS=3750`, and produce `CERTIFIED_52_CLASSES.csv` for an exact per-class audit.

Independent check: from the current frozen ZIP `R5_Fourteen_New6_Exact_20261120.zip` use `BUILD_ORACLE_14_ACTIONS.py 114 120` and `INDEPENDENT_ORACLE_FAST_14.cpp`. Compile `g++ -O3 -std=c++17 INDEPENDENT_ORACLE_FAST_14.cpp -o oracle`. Run `./oracle ORACLE_14_ACTIONS_U114_V120.txt`: observed `NIBBLE_F8 8335 STATES 2056586 ACTIONS 7`. Oracle action text SHA-256 `1cdd8285dc27a22e961167f9e980bb2433eb8df2e3ebdeef1f22a893c67ee5fd`.

All loops use exact integer observations, exact prices, full joint supports, finite capped counters and non-stalling minimax branches. The source-to-activity and independent mathematical review/admission boundaries remain separate.
