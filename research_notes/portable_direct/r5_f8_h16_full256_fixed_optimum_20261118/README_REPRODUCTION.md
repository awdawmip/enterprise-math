# Reproduction

Place the exact frozen `EXACT_R5_ALL_101_BUDGETS.json` alongside these sources. Its SHA-256 must be `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The full table is retained in the accompanying 15-file ZIP and prior R5 scientific evidence. No scientific input repinning occurred.

Run:

```sh
python GENERATE_H16_ACTIONS.py
python VERIFY_FIXED_SCHEDULE_CERTIFICATE.py
python VERIFY_TRIPLE_PAIR_COVER.py
g++ -O3 -DNDEBUG -std=c++17 VERIFY_EXACT_16_MINIMAX.cpp -o verify16
./verify16 ACTIONS_H16_PLUS_5.txt 0
./verify16 ACTIONS_H16_PLUS_5.txt 1
./verify16 ACTIONS_H16_PLUS_5.txt 8
```

Expected root outputs: `f=0 V=735`, `f=1 V=1685`, `f=8 V=8335 states=23851087`. The f8 run can be memory/CPU intensive. Previous actual f8 run finished and printed the full root result; the original outer wrapper exit code was not recovered. All finite support tests use exact integers; no floating-point comparison affects the conclusions.

The nonadaptive all-f result has a direct mathematical proof using four pairs and a 735-cost dual, so its validity does not depend on a floating-point linear/integer programming solver. Independent numeric MILP and LP from the archived `OPTIMIZE_FIXED_CORRUPT_SCHEDULE.py` agreed at 12495 for f=8. Scope: derived 256-state scalar observer, not native X6 dynamics. Review: NOT_REVIEWED.
