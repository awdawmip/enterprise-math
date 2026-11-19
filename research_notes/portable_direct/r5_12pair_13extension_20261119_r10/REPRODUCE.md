# Reproduce R5 high-arity finite results

This directory accompanies the frozen-source research bundle `EnterpriseMath_R5_Twelve_Seed_Thirteen_F0_F3_20261119.zip` (41 included files, ZIP SHA-256 `2679dd36723dd6d930f57b752245fc2381ece19127e101474626bf5a2ecc5a0b`). The source JSON and complete CSV outputs are inside the bundle; this GitHub directory contains the full mathematical statement, compact certificate and source that independently regenerates its classifications.

The scientific input `EXACT_R5_ALL_101_BUDGETS.json` has SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The companion `stages_18.json` fixes the robust endpoint.

From the extracted bundle directory (or with the pinned input files next to this code):

```sh
python3 make_adj.py
g++ -O3 -std=c++17 R5_HIGH_ARITY_REPRO.cpp -o r5high
./r5high window_adj.bin census12 > pair12_f0_all30135.csv
./r5high window_adj.bin pair12 34 82 8 > pair12_34_82.csv
./r5high window_adj.bin census13 > third13_f0f3_all244.csv
python3 VERIFY_ENDPOINT_F0.py
```

Expected zero-error twelve-label output: `pairs=30135 signatures=2003; f0=733 count=30129; f0=734 count=3; f0=735 count=3`. Expected thirteen-label output: `classes=48` and all 244 rows carry `735,1685,2635,3585` for f0..f3. Expected (34,82) output: `V8=8335`.

Byte-checked complete census outputs in the local reproduction package:

* `pair12_f0_all30135.csv`: SHA-256 `be09f068a5b7432909b135cb4a198b3a9e113f4334a746b0b57e120a7a8ba688`
* `third13_f0f3_all244.csv`: SHA-256 `afc4a0e4939ff0625101683063a4403e2286484e4e9029ee4fc949095a911384`.

The corresponding separately compiled C++ routines were executed against the frozen input. The unified `R5_HIGH_ARITY_REPRO.cpp` was also compiled and its 30,135 and 244 rows compared exactly on all value columns. Its published Git blob SHA-1 is `6e5356a9637599b18ea1e4cab2822c900f07b2cf`. The independent doubled-left-endpoint verifier checked 66 twelve-label f0 instances including all six exceptional pairs. The second pre-existing four-bit Bellman oracle used independently generated seven-action masks for H12* and returned `V8=8335, states=2840397`.

The full 256-label eight-error interval remains `8335<=C8*<=8343`. No mathematical reviewer acceptance or native X6/Port preservation claim is implied. The four extra 13-label f8 certificates cover only t=2,3,8,96; f8 for all 244 extensions remains open.
