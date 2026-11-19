# Reproduction — R5 D14 six new roots

Frozen scientific input: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Do not re-pin. The prior 52-reference local reproduction bundle has this file, `stages_18.json`, `make_adj.py`, `SCAN_FRONTIER_MATRIX.cpp`, `SCAN_FRONTIER_NEW6.cpp`, `SOLVE_SELECTED_F8.cpp`, `CERTIFIED_52_CLASSES.csv`, `BUILD_ORACLE_14_ACTIONS.py` and `INDEPENDENT_ORACLE_FAST_14.cpp`. Its GitHub canonical research note is at https://github.com/awdawmip/enterprise-math/blob/9fd4c0449e731342e3343d8e634d9a98edd4cebf/research_notes/portable_direct/r5_d14_twenty_extra_references_20261120/RESEARCH.md . Those source bytes are unchanged; the present result builds on them.

With the predecessor tools plus new `VERIFY_NEW6_D14.py`, `ROOTS_NEW6.csv`, and `RESULT.json` in one working directory:

```sh
sha256sum EXACT_R5_ALL_101_BUDGETS.json
python3 make_adj.py
g++ -O3 -std=c++17 SCAN_FRONTIER_MATRIX.cpp -o matrix
./matrix window_adj.bin
cp SCAN_FRONTIER_NEW6.cpp SCAN_FRONTIER.cpp
g++ -O3 -std=c++17 SOLVE_SELECTED_F8.cpp -o solver14
for pair in '50 81' '50 96' '66 81' '49 65' '81 96' '96 97'; do
  ./solver14 window_adj.bin $pair 5000000
done
OPENBLAS_NUM_THREADS=1 python3 VERIFY_NEW6_D14.py
g++ -O3 -std=c++17 INDEPENDENT_ORACLE_FAST_14.cpp -o independent14
python3 BUILD_ORACLE_14_ACTIONS.py 50 81
./independent14 ORACLE_14_ACTIONS_U50_V81.txt
python3 BUILD_ORACLE_14_ACTIONS.py 96 97
./independent14 ORACLE_14_ACTIONS_U96_V97.txt
```

Expected full solver outputs: each V8=8335, with nonterminal counts 3904167 / 3027474 / 3408257 / 2778921 / 2455390 / 2103657 in listed order. Independent nibble checker: 8335, 3904167 states, 7 actions for (50,81); 8335, 2103657 states, 7 actions for (96,97). Coverage checker: PASS 1265 certified classes 26388 certified pairs 641 unresolved classes 3258 unresolved pairs.

All exact results are restricted to frozen integer interval model and f=8; this package neither establishes a new formal owner nor transfers the scalar theorem to native X6/BRC.
