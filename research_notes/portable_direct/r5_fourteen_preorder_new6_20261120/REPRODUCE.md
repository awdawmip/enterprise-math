# R5 14-label six new f8 references: reproduction

Frozen scientific source: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Put original `EXACT_R5_ALL_101_BUDGETS.json` (SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`) and matching `stages_18.json` beside these scripts. These fixed inputs are deliberately not copied into the branch.

Exact joint-support eight-error value and price-preorder:
```sh
python3 make_adj.py
g++ -O3 -std=c++17 R5_FOURTEEN_F8_ONE.cpp -o f8
for p in '21 114' '21 98' '81 88' '56 72' '8 120' '49 97'; do set -- $p; ./f8 window_adj.bin "$1" "$2" 24000000; done
g++ -O3 -std=c++17 CHECK_PREORDER_NEW6.cpp -o preorder
./preorder
```
Six values must match `NEW6_F8_EXACT.csv`. The preorder checker must confirm 1906 classes, 38127 edges, 1066 SCCs, 333 sink SCCs, original 22-reference coverage 836 classes/20159 pairs, and new 32-reference coverage 1008 classes/23828 pairs, otherwise exit nonzero.

Independent doubled-left-endpoint supports and 4-bit-per-counter C++ oracle (three completed verifications):
```sh
g++ -O3 -std=c++17 INDEPENDENT_ORACLE_EARLY_STALL.cpp -o oracle14
for p in '21 114' '21 98' '81 88'; do set -- $p; python3 BUILD_ORACLE_14_ACTIONS.py "$1" "$2"; ./oracle14 "ORACLE_14_ACTIONS_U${1}_V${2}.txt" 8; done
```
Independent checks actually completed only for these three classes, all at V8=8335. The other three new instances have a complete original exact DP but not a completed second implementation check. No full-256 optimum, mathematical review, formal CLAIM/RUN or native X6/BRC/Port equivalence is asserted.
